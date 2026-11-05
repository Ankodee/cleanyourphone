package com.cleanphone.glasshome;

import android.app.Dialog;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.provider.Settings;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity implements AppAdapter.OnAppClickListener, DockAdapter.OnDockClickListener {

    private static final String PREFS_NAME = "glass_home_prefs";
    private static final String KEY_DOCK = "dock_packages";

    private RecyclerView recyclerApps;
    private RecyclerView recyclerDock;
    private EditText searchInput;
    private ImageView btnSettings;

    private AppAdapter appAdapter;
    private DockAdapter dockAdapter;

    private final List<AppModel> allInstalledApps = new ArrayList<>();
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private final Handler mainHandler = new Handler(Looper.getMainLooper());

    private BroadcastReceiver packageReceiver;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Allow live system wallpaper to be visible through translucent glass UI
        getWindow().setFlags(
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER,
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER
        );

        setContentView(R.layout.activity_main);

        initViews();
        setupPackageReceiver();
        loadInstalledApps();
    }

    private void initViews() {
        recyclerApps = findViewById(R.id.recycler_apps);
        recyclerDock = findViewById(R.id.recycler_dock);
        searchInput = findViewById(R.id.search_input);
        btnSettings = findViewById(R.id.btn_settings);

        // App library: 4-column fluid grid optimized for 120Hz lag-free performance
        recyclerApps.setLayoutManager(new GridLayoutManager(this, 4));
        recyclerApps.setHasFixedSize(true);
        recyclerApps.setItemViewCacheSize(40);
        appAdapter = new AppAdapter(this, this);
        recyclerApps.setAdapter(appAdapter);

        // Liquid Glass Dock: horizontal 4-5 apps
        LinearLayoutManager dockLayout = new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        recyclerDock.setLayoutManager(dockLayout);
        recyclerDock.setHasFixedSize(true);
        dockAdapter = new DockAdapter(this, this);
        recyclerDock.setAdapter(dockAdapter);

        // Real-time app search
        searchInput.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {}

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                appAdapter.filter(s != null ? s.toString() : "");
            }

            @Override
            public void afterTextChanged(Editable s) {}
        });

        btnSettings.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, SettingsActivity.class);
            startActivity(intent);
        });
    }

    private void setupPackageReceiver() {
        packageReceiver = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                // Auto reload when packages are debloated or installed
                loadInstalledApps();
            }
        };
        IntentFilter filter = new IntentFilter();
        filter.addAction(Intent.ACTION_PACKAGE_ADDED);
        filter.addAction(Intent.ACTION_PACKAGE_REMOVED);
        filter.addDataScheme("package");
        registerReceiver(packageReceiver, filter);
    }

    private void loadInstalledApps() {
        executor.execute(() -> {
            PackageManager pm = getPackageManager();
            Intent intent = new Intent(Intent.ACTION_MAIN, null);
            intent.addCategory(Intent.CATEGORY_LAUNCHER);

            List<ResolveInfo> activities = pm.queryIntentActivities(intent, 0);
            List<AppModel> apps = new ArrayList<>();
            String myPkg = getPackageName();

            for (ResolveInfo info : activities) {
                String pkg = info.activityInfo.packageName;
                if (pkg.equals(myPkg)) continue;

                String label = info.loadLabel(pm).toString();
                String activityName = info.activityInfo.name;
                apps.add(new AppModel(pkg, activityName, label, info.loadIcon(pm)));
            }

            Collections.sort(apps, (a, b) -> a.getLabel().compareToIgnoreCase(b.getLabel()));

            mainHandler.post(() -> {
                allInstalledApps.clear();
                allInstalledApps.addAll(apps);
                appAdapter.setApps(apps);
                updateDockApps();
            });
        });
    }

    private void updateDockApps() {
        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        Set<String> dockSet = prefs.getStringSet(KEY_DOCK, null);

        List<AppModel> dockList = new ArrayList<>();

        if (dockSet == null || dockSet.isEmpty()) {
            // Smart defaults for Apple-style dock: Dialer, Messaging, Browser, Camera
            for (AppModel app : allInstalledApps) {
                String pkg = app.getPackageName().toLowerCase();
                if (dockList.size() < 4) {
                    if (pkg.contains("dialer") || pkg.contains("phone") ||
                        pkg.contains("mms") || pkg.contains("message") ||
                        pkg.contains("chrome") || pkg.contains("browser") ||
                        pkg.contains("camera")) {
                        dockList.add(app);
                    }
                }
            }
            // If still empty, add first 4 apps
            if (dockList.isEmpty() && !allInstalledApps.isEmpty()) {
                int count = Math.min(4, allInstalledApps.size());
                dockList.addAll(allInstalledApps.subList(0, count));
            }
        } else {
            for (AppModel app : allInstalledApps) {
                if (dockSet.contains(app.getPackageName())) {
                    dockList.add(app);
                    if (dockList.size() >= 5) break;
                }
            }
        }

        dockAdapter.setDockApps(dockList);
    }

    @Override
    public void onAppClick(AppModel app) {
        launchApp(app);
    }

    @Override
    public void onAppLongClick(AppModel app, View anchor) {
        showAppOptionsDialog(app);
    }

    @Override
    public void onDockAppClick(AppModel app) {
        launchApp(app);
    }

    @Override
    public void onDockAppLongClick(AppModel app) {
        showAppOptionsDialog(app);
    }

    private void launchApp(AppModel app) {
        try {
            Intent intent = new Intent(Intent.ACTION_MAIN);
            intent.addCategory(Intent.CATEGORY_LAUNCHER);
            intent.setComponent(new ComponentName(app.getPackageName(), app.getActivityName()));
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
            // Snappy 0.5x instant launch transition
            startActivity(intent);
            overridePendingTransition(android.R.anim.fade_in, 0);
        } catch (Exception e) {
            Toast.makeText(this, "Could not launch " + app.getLabel(), Toast.LENGTH_SHORT).show();
        }
    }

    private void showAppOptionsDialog(AppModel app) {
        Dialog dialog = new Dialog(this);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setContentView(R.layout.dialog_app_options);

        if (dialog.getWindow() != null) {
            dialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));
        }

        ImageView icon = dialog.findViewById(R.id.dialog_app_icon);
        TextView title = dialog.findViewById(R.id.dialog_app_title);
        TextView pkgText = dialog.findViewById(R.id.dialog_app_package);
        Button btnToggleDock = dialog.findViewById(R.id.btn_toggle_dock);
        Button btnAppInfo = dialog.findViewById(R.id.btn_app_info);
        Button btnUninstall = dialog.findViewById(R.id.btn_uninstall);

        icon.setImageDrawable(app.getIcon());
        title.setText(app.getLabel());
        pkgText.setText(app.getPackageName());

        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        Set<String> dockSet = prefs.getStringSet(KEY_DOCK, new HashSet<>());
        boolean isPinned = dockSet.contains(app.getPackageName());
        btnToggleDock.setText(isPinned ? R.string.remove_from_dock : R.string.add_to_dock);

        btnToggleDock.setOnClickListener(v -> {
            Set<String> newSet = new HashSet<>(prefs.getStringSet(KEY_DOCK, new HashSet<>()));
            if (isPinned) {
                newSet.remove(app.getPackageName());
                Toast.makeText(this, "Removed from Dock", Toast.LENGTH_SHORT).show();
            } else {
                if (newSet.size() >= 5) {
                    Toast.makeText(this, "Dock is full (max 5 apps)", Toast.LENGTH_SHORT).show();
                    dialog.dismiss();
                    return;
                }
                newSet.add(app.getPackageName());
                Toast.makeText(this, "Pinned to Dock", Toast.LENGTH_SHORT).show();
            }
            prefs.edit().putStringSet(KEY_DOCK, newSet).apply();
            updateDockApps();
            dialog.dismiss();
        });

        btnAppInfo.setOnClickListener(v -> {
            Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS);
            intent.setData(Uri.parse("package:" + app.getPackageName()));
            startActivity(intent);
            dialog.dismiss();
        });

        btnUninstall.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_DELETE);
            intent.setData(Uri.parse("package:" + app.getPackageName()));
            startActivity(intent);
            dialog.dismiss();
        });

        dialog.show();
    }

    @Override
    public void onBackPressed() {
        if (searchInput != null && searchInput.getText().length() > 0) {
            searchInput.setText("");
        }
        // Do not call super so pressing back remains on Home screen
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (packageReceiver != null) {
            unregisterReceiver(packageReceiver);
        }
        executor.shutdown();
    }
}
