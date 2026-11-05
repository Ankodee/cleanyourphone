package com.cleanphone.glasshome;

import android.app.Dialog;
import android.app.WallpaperManager;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.RenderEffect;
import android.graphics.Shader;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.provider.Settings;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.PagerSnapHelper;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * CleanYourPhone Liquid Glass Home - Authentic iOS 17/18 Launcher Clone.
 * Features:
 * - Left-to-right horizontal paginated SpringBoard with smooth snapping.
 * - Real optical liquid glass blur effect over the live background wallpaper.
 * - iOS Smart Stack widget (Clock, Date, Battery status).
 * - Floating frosted glass dock with dynamic wallpaper pass-through.
 * - Floating iOS Spotlight search pill and live search overlay.
 * - iOS App Library on the final page with 2x2 frosted category folders.
 * - 0.5x lag-free snappy touch response with hardware acceleration.
 */
public class MainActivity extends AppCompatActivity implements
        AppGridAdapter.OnAppClickListener,
        DockAdapter.OnDockClickListener,
        SpringBoardPagerAdapter.OnSearchTriggerListener {

    private static final String PREFS_NAME = "glass_home_prefs";
    private static final String KEY_DOCK = "dock_packages";

    private RecyclerView horizontalPager;
    private LinearLayoutManager pagerLayoutManager;
    private PagerSnapHelper snapHelper;
    private SpringBoardPagerAdapter pagerAdapter;

    private LinearLayout dotsContainer;
    private View btnSearchPill;

    private FrameLayout dockContainer;
    private View glassDock;
    private RecyclerView recyclerDock;
    private DockAdapter dockAdapter;

    private RelativeLayout spotlightOverlay;
    private EditText spotlightSearchInput;
    private TextView btnCancelSearch;
    private RecyclerView recyclerSearchResults;
    private SearchResultsAdapter searchResultsAdapter;

    private final List<AppModel> allInstalledApps = new ArrayList<>();
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private final Handler mainHandler = new Handler(Looper.getMainLooper());

    private BroadcastReceiver packageReceiver;
    private int currentPageIndex = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Enable edge-to-edge system wallpaper rendering
        Window window = getWindow();
        window.setFlags(
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER,
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER
        );

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            window.getDecorView().setSystemUiVisibility(
                    View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                    View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN |
                    View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            );
            window.setStatusBarColor(Color.TRANSPARENT);
            window.setNavigationBarColor(Color.TRANSPARENT);
        }

        setContentView(R.layout.activity_main);

        initViews();
        setupSpringBoardPager();
        setupSpotlightSearch();
        setupWallpaperGlassBlur();
        setupPackageReceiver();
        loadInstalledApps();
    }

    private void initViews() {
        horizontalPager = findViewById(R.id.horizontal_pager);
        dotsContainer = findViewById(R.id.dots_container);
        btnSearchPill = findViewById(R.id.btn_search_pill);

        glassDock = findViewById(R.id.glass_dock);
        recyclerDock = findViewById(R.id.recycler_dock);

        spotlightOverlay = findViewById(R.id.spotlight_overlay);
        spotlightSearchInput = findViewById(R.id.spotlight_search_input);
        btnCancelSearch = findViewById(R.id.btn_cancel_search);
        recyclerSearchResults = findViewById(R.id.recycler_search_results);

        // Bottom Liquid Glass Dock
        LinearLayoutManager dockLayout = new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        recyclerDock.setLayoutManager(dockLayout);
        recyclerDock.setHasFixedSize(true);
        dockAdapter = new DockAdapter(this, this);
        recyclerDock.setAdapter(dockAdapter);

        // Spotlight trigger button
        btnSearchPill.setOnClickListener(v -> openSpotlightSearch());
    }

    private void setupSpringBoardPager() {
        pagerLayoutManager = new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        horizontalPager.setLayoutManager(pagerLayoutManager);
        horizontalPager.setHasFixedSize(true);
        horizontalPager.setItemViewCacheSize(10);

        snapHelper = new PagerSnapHelper();
        snapHelper.attachToRecyclerView(horizontalPager);

        pagerAdapter = new SpringBoardPagerAdapter(this, this, this);
        horizontalPager.setAdapter(pagerAdapter);

        horizontalPager.addOnScrollListener(new RecyclerView.OnScrollListener() {
            @Override
            public void onScrollStateChanged(@NonNull RecyclerView recyclerView, int newState) {
                if (newState == RecyclerView.SCROLL_STATE_IDLE) {
                    View centerView = snapHelper.findSnapView(pagerLayoutManager);
                    if (centerView != null) {
                        int pos = pagerLayoutManager.getPosition(centerView);
                        if (pos != currentPageIndex) {
                            currentPageIndex = pos;
                            updatePageDots();
                        }
                    }
                }
            }
        });
    }

    private void setupSpotlightSearch() {
        recyclerSearchResults.setLayoutManager(new LinearLayoutManager(this));
        searchResultsAdapter = new SearchResultsAdapter(this, this);
        recyclerSearchResults.setAdapter(searchResultsAdapter);

        spotlightSearchInput.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {}

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                filterSearchResults(s != null ? s.toString() : "");
            }

            @Override
            public void afterTextChanged(Editable s) {}
        });

        btnCancelSearch.setOnClickListener(v -> closeSpotlightSearch());

        spotlightOverlay.setOnClickListener(v -> {
            // Tapping empty region closes spotlight
            closeSpotlightSearch();
        });
    }

    private void filterSearchResults(String query) {
        if (query.trim().isEmpty()) {
            searchResultsAdapter.setResults(allInstalledApps);
            return;
        }

        String q = query.toLowerCase().trim();
        List<AppModel> filtered = new ArrayList<>();
        for (AppModel app : allInstalledApps) {
            if (app.getLabel().toLowerCase().contains(q) ||
                app.getPackageName().toLowerCase().contains(q) ||
                app.getCategory().toLowerCase().contains(q)) {
                filtered.add(app);
            }
        }
        searchResultsAdapter.setResults(filtered);
    }

    private void openSpotlightSearch() {
        spotlightOverlay.setVisibility(View.VISIBLE);
        spotlightOverlay.setAlpha(0f);
        spotlightOverlay.animate().alpha(1f).setDuration(120).start();

        spotlightSearchInput.setText("");
        spotlightSearchInput.requestFocus();
        filterSearchResults("");

        InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
        if (imm != null) {
            imm.showSoftInput(spotlightSearchInput, InputMethodManager.SHOW_IMPLICIT);
        }
    }

    private void closeSpotlightSearch() {
        InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
        if (imm != null) {
            imm.hideSoftInputFromWindow(spotlightSearchInput.getWindowToken(), 0);
        }

        spotlightOverlay.animate().alpha(0f).setDuration(100).withEndAction(() -> {
            spotlightOverlay.setVisibility(View.GONE);
            spotlightSearchInput.setText("");
        }).start();
    }

    /**
     * Samples the system wallpaper and applies high-speed stack blur
     * to provide the true optical Liquid Glass effect on the dock and cards!
     */
    private void setupWallpaperGlassBlur() {
        // Modern Android 12+ (API 31+) native hardware blur effect
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            try {
                glassDock.setRenderEffect(RenderEffect.createBlurEffect(28f, 28f, Shader.TileMode.CLAMP));
            } catch (Exception ignored) {}
        }

        // Fast StackBlur wallpaper sampler for universal glass refraction (API 21+)
        executor.execute(() -> {
            try {
                WallpaperManager wm = WallpaperManager.getInstance(MainActivity.this);
                Drawable wp = wm.getDrawable();
                if (wp != null) {
                    Bitmap srcBitmap;
                    if (wp instanceof BitmapDrawable) {
                        srcBitmap = ((BitmapDrawable) wp).getBitmap();
                    } else {
                        srcBitmap = Bitmap.createBitmap(
                                Math.max(1, wp.getIntrinsicWidth()),
                                Math.max(1, wp.getIntrinsicHeight()),
                                Bitmap.Config.ARGB_8888
                        );
                        Canvas c = new Canvas(srcBitmap);
                        wp.setBounds(0, 0, c.getWidth(), c.getHeight());
                        wp.draw(c);
                    }

                    if (srcBitmap != null && srcBitmap.getWidth() > 0 && srcBitmap.getHeight() > 0) {
                        // Downsample 5x for instant zero-lag blur computation
                        int scaledW = Math.max(16, srcBitmap.getWidth() / 5);
                        int scaledH = Math.max(16, srcBitmap.getHeight() / 5);
                        Bitmap downscaled = Bitmap.createScaledBitmap(srcBitmap, scaledW, scaledH, true);
                        Bitmap blurred = FastBlur.blur(downscaled, 18, true);

                        mainHandler.post(() -> {
                            if (blurred != null) {
                                LiquidGlassDrawable glassDrawable = new LiquidGlassDrawable(
                                        getResources().getDimension(R.dimen.dock_radius)
                                );
                                glassDrawable.setBlurredWallpaper(blurred);
                                glassDock.setBackground(glassDrawable);
                            }
                        });
                    }
                }
            } catch (Exception ignored) {}
        });
    }

    private void updatePageDots() {
        int totalPages = pagerAdapter.getItemCount();
        dotsContainer.removeAllViews();

        int dotSize = (int) (6 * getResources().getDisplayMetrics().density);
        int dotActiveW = (int) (16 * getResources().getDisplayMetrics().density);
        int margin = (int) (4 * getResources().getDisplayMetrics().density);

        for (int i = 0; i < totalPages; i++) {
            View dot = new View(this);
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                    i == currentPageIndex ? dotActiveW : dotSize,
                    dotSize
            );
            params.setMargins(margin, 0, margin, 0);
            dot.setLayoutParams(params);
            dot.setBackgroundResource(i == currentPageIndex ? R.drawable.glass_dot_active : R.drawable.glass_dot_inactive);
            dotsContainer.addView(dot);
        }
    }

    private void setupPackageReceiver() {
        packageReceiver = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
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
                pagerAdapter.setApps(apps);
                updatePageDots();
                updateDockApps();
            });
        });
    }

    private void updateDockApps() {
        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        Set<String> dockSet = prefs.getStringSet(KEY_DOCK, null);
        List<AppModel> dockList = new ArrayList<>();

        if (dockSet == null || dockSet.isEmpty()) {
            // Default 4 iconic iOS dock apps: Phone, Messages, Browser, Camera
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
            if (dockList.isEmpty() && !allInstalledApps.isEmpty()) {
                int count = Math.min(4, allInstalledApps.size());
                dockList.addAll(allInstalledApps.subList(0, count));
            }
        } else {
            for (AppModel app : allInstalledApps) {
                if (dockSet.contains(app.getPackageName())) {
                    dockList.add(app);
                    if (dockList.size() >= 4) break;
                }
            }
        }

        dockAdapter.setDockApps(dockList);
    }

    @Override
    public void onAppClick(AppModel app) {
        if (spotlightOverlay.getVisibility() == View.VISIBLE) {
            closeSpotlightSearch();
        }
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

    @Override
    public void onSearchTriggered() {
        openSpotlightSearch();
    }

    private void launchApp(AppModel app) {
        try {
            Intent intent = new Intent(Intent.ACTION_MAIN);
            intent.addCategory(Intent.CATEGORY_LAUNCHER);
            intent.setComponent(new ComponentName(app.getPackageName(), app.getActivityName()));
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
            startActivity(intent);
            // 0.5x Snappy iOS Launch Transition (150ms half-duration zoom & fade)
            overridePendingTransition(R.anim.app_launch_enter, R.anim.app_launch_exit);
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
        btnToggleDock.setText(isPinned ? "Remove from Dock" : "Pin to Dock");

        btnToggleDock.setOnClickListener(v -> {
            Set<String> newSet = new HashSet<>(prefs.getStringSet(KEY_DOCK, new HashSet<>()));
            if (isPinned) {
                newSet.remove(app.getPackageName());
                Toast.makeText(this, "Removed from Dock", Toast.LENGTH_SHORT).show();
            } else {
                if (newSet.size() >= 4) {
                    Toast.makeText(this, "Dock is full (max 4 apps)", Toast.LENGTH_SHORT).show();
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
        if (spotlightOverlay.getVisibility() == View.VISIBLE) {
            closeSpotlightSearch();
            return;
        }
        if (currentPageIndex != 0) {
            horizontalPager.smoothScrollToPosition(0);
            return;
        }
        // Keep user on Home Screen
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
