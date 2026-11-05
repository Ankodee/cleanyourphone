package com.cleanphone.glasshome;

import android.app.Dialog;
import android.app.KeyguardManager;
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
import android.view.animation.DecelerateInterpolator;
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
 * CleanPhone Premium Minimalist Home Screen.
 * Design Philosophy:
 * - Extremely clean, uncluttered, balanced hierarchy with generous breathing room.
 * - Minimal architectural digital clock, date and battery header.
 * - Zero duplicate apps between the main home grid and the dock.
 * - Subtle translucent dock with soft wallpaper pass-through and minimal hairline stroke.
 * - Minimalist compact search interface with instant Spotlight search overlay.
 * - Full Dark Mode and Light Mode support with curated muted gradient wallpapers.
 * - Respects system status bar and navigation bar insets.
 */
public class MainActivity extends AppCompatActivity implements
        AppGridAdapter.OnAppClickListener,
        DockAdapter.OnDockClickListener,
        SpringBoardPagerAdapter.OnSearchTriggerListener {

    private static final String PREFS_NAME = "glass_home_prefs";
    private static final String KEY_DOCK = "dock_packages";

    private View rootLayout;
    private RecyclerView horizontalPager;
    private LinearLayoutManager pagerLayoutManager;
    private PagerSnapHelper snapHelper;
    private SpringBoardPagerAdapter pagerAdapter;

    private LinearLayout dotsContainer;
    private View btnSearchPill;
    private ImageView searchIconView;
    private TextView searchHintText;

    private FrameLayout dockContainer;
    private View glassDock;
    private RecyclerView recyclerDock;
    private DockAdapter dockAdapter;
    private LiquidGlassDrawable dockGlassDrawable;

    private RelativeLayout spotlightOverlay;
    private EditText spotlightSearchInput;
    private TextView btnCancelSearch;
    private RecyclerView recyclerSearchResults;
    private SearchResultsAdapter searchResultsAdapter;

    private final List<AppModel> allInstalledApps = new ArrayList<>();
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private final Handler mainHandler = new Handler(Looper.getMainLooper());

    private BroadcastReceiver packageReceiver;
    private BroadcastReceiver screenStateReceiver;
    private ImageView unlockBlurOverlay;
    private volatile Bitmap blurredWallpaperBitmap;
    private boolean isLockScreenActive = false;
    private int currentPageIndex = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Edge-to-edge transparent system wallpaper rendering
        Window window = getWindow();
        window.setFlags(
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER,
                WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER
        );

        boolean isDark = ThemeManager.isDarkTheme(this);
        ThemeManager.applySystemBars(this, isDark);

        setContentView(R.layout.activity_main);

        initViews();
        setupWindowInsets();
        setupSpringBoardPager();
        setupSpotlightSearch();
        setupWallpaperGlassBlur();
        setupPackageReceiver();
        setupScreenStateReceiver();
        handleIntent(getIntent());
        loadInstalledApps();
    }

    private void initViews() {
        rootLayout = findViewById(R.id.root_layout);
        unlockBlurOverlay = findViewById(R.id.unlock_blur_overlay);
        horizontalPager = findViewById(R.id.horizontal_pager);
        dotsContainer = findViewById(R.id.dots_container);

        btnSearchPill = findViewById(R.id.btn_search_pill);
        searchIconView = findViewById(R.id.search_icon_view);
        searchHintText = findViewById(R.id.search_hint_text);

        dockContainer = findViewById(R.id.dock_container);
        glassDock = findViewById(R.id.glass_dock);
        recyclerDock = findViewById(R.id.recycler_dock);

        spotlightOverlay = findViewById(R.id.spotlight_overlay);
        spotlightSearchInput = findViewById(R.id.spotlight_search_input);
        btnCancelSearch = findViewById(R.id.btn_cancel_search);
        recyclerSearchResults = findViewById(R.id.recycler_search_results);

        // Bottom Minimal Floating Dock
        LinearLayoutManager dockLayout = new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        recyclerDock.setLayoutManager(dockLayout);
        recyclerDock.setHasFixedSize(true);
        dockAdapter = new DockAdapter(this, this);
        recyclerDock.setAdapter(dockAdapter);

        // Spotlight search trigger
        btnSearchPill.setOnClickListener(v -> openSpotlightSearch());

        // Long-press search bar to open Home Screen Theme & Wallpaper Menu
        btnSearchPill.setOnLongClickListener(v -> {
            showHomeScreenMenu();
            return true;
        });
    }

    /**
     * Dynamically adjusts status bar and navigation bar insets
     * so widgets and the dock never collide with 3-button or gesture bars.
     */
    private void setupWindowInsets() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT_WATCH && rootLayout != null) {
            rootLayout.setOnApplyWindowInsetsListener((v, insets) -> {
                int topInset = insets.getSystemWindowInsetTop();
                int bottomInset = insets.getSystemWindowInsetBottom();
                float density = getResources().getDisplayMetrics().density;

                if (horizontalPager != null) {
                    horizontalPager.setPadding(
                            horizontalPager.getPaddingLeft(),
                            topInset,
                            horizontalPager.getPaddingRight(),
                            (int) (130 * density) + bottomInset
                    );
                }

                if (dockContainer != null) {
                    dockContainer.setPadding(
                            dockContainer.getPaddingLeft(),
                            dockContainer.getPaddingTop(),
                            dockContainer.getPaddingRight(),
                            (int) (10 * density) + bottomInset
                    );
                }

                return insets;
            });
        }
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        handleIntent(intent);
    }

    private void handleIntent(Intent intent) {
        if (intent == null) return;
        String themeExtra = intent.getStringExtra("theme");
        if ("light".equalsIgnoreCase(themeExtra)) {
            ThemeManager.setThemeMode(this, ThemeManager.MODE_LIGHT);
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_WARM_LINEN);
            applyTheme(false);
            mainHandler.postDelayed(this::setupWallpaperGlassBlur, 300);
        } else if ("dark".equalsIgnoreCase(themeExtra)) {
            ThemeManager.setThemeMode(this, ThemeManager.MODE_DARK);
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_DARK_NAVY);
            applyTheme(true);
            mainHandler.postDelayed(this::setupWallpaperGlassBlur, 300);
        }

        String action = intent.getStringExtra("action");
        if ("set_wallpaper".equals(action)) {
            String presetStr = intent.getStringExtra("preset");
            int preset = WallpaperHelper.PRESET_DARK_NAVY;
            if ("charcoal".equalsIgnoreCase(presetStr)) {
                preset = WallpaperHelper.PRESET_CHARCOAL;
            } else if ("warm_linen".equalsIgnoreCase(presetStr) || "light".equalsIgnoreCase(presetStr)) {
                preset = WallpaperHelper.PRESET_WARM_LINEN;
            } else if ("slate".equalsIgnoreCase(presetStr)) {
                preset = WallpaperHelper.PRESET_MINIMAL_SLATE;
            }
            WallpaperHelper.applyPreset(this, preset);
            mainHandler.postDelayed(this::setupWallpaperGlassBlur, 300);
        }
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
        spotlightOverlay.setOnClickListener(v -> closeSpotlightSearch());
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
        boolean isDark = ThemeManager.isDarkTheme(this);
        spotlightOverlay.setBackgroundColor(ThemeManager.getOverlayBg(isDark));
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

    private void setupWallpaperGlassBlur() {
        boolean isDark = ThemeManager.isDarkTheme(this);

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
                        int scaledW = Math.max(16, srcBitmap.getWidth() / 5);
                        int scaledH = Math.max(16, srcBitmap.getHeight() / 5);
                        Bitmap downscaled = Bitmap.createScaledBitmap(srcBitmap, scaledW, scaledH, true);
                        Bitmap blurred = FastBlur.blur(downscaled, 18, true);

                        blurredWallpaperBitmap = blurred;

                        mainHandler.post(() -> {
                            if (blurred != null) {
                                if (dockGlassDrawable == null) {
                                    dockGlassDrawable = new LiquidGlassDrawable(
                                            getResources().getDimension(R.dimen.dock_radius)
                                    );
                                }
                                dockGlassDrawable.setTheme(isDark);
                                dockGlassDrawable.setBlurredWallpaper(blurred);
                                glassDock.setBackground(dockGlassDrawable);

                                if (isLockScreenActive && unlockBlurOverlay != null) {
                                    unlockBlurOverlay.setImageBitmap(blurred);
                                }
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

        int dotH = (int) (4 * getResources().getDisplayMetrics().density);
        int dotActiveW = (int) (12 * getResources().getDisplayMetrics().density);
        int margin = (int) (3 * getResources().getDisplayMetrics().density);

        for (int i = 0; i < totalPages; i++) {
            View dot = new View(this);
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                    i == currentPageIndex ? dotActiveW : dotH,
                    dotH
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

    private void setupScreenStateReceiver() {
        screenStateReceiver = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                if (intent == null || intent.getAction() == null) return;
                String action = intent.getAction();
                if (Intent.ACTION_SCREEN_OFF.equals(action)) {
                    prepareGlassLockOverlay();
                } else if (Intent.ACTION_SCREEN_ON.equals(action)) {
                    KeyguardManager km = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
                    if (km != null && km.isKeyguardLocked()) {
                        prepareGlassLockOverlay();
                    }
                } else if (Intent.ACTION_USER_PRESENT.equals(action)) {
                    triggerGlassUnlockTransition();
                }
            }
        };
        IntentFilter filter = new IntentFilter();
        filter.addAction(Intent.ACTION_SCREEN_OFF);
        filter.addAction(Intent.ACTION_SCREEN_ON);
        filter.addAction(Intent.ACTION_USER_PRESENT);
        registerReceiver(screenStateReceiver, filter);
    }

    private void prepareGlassLockOverlay() {
        isLockScreenActive = true;
        mainHandler.post(() -> {
            if (unlockBlurOverlay != null) {
                if (blurredWallpaperBitmap != null) {
                    unlockBlurOverlay.setImageBitmap(blurredWallpaperBitmap);
                }
                unlockBlurOverlay.setAlpha(1.0f);
                unlockBlurOverlay.setScaleX(1.06f);
                unlockBlurOverlay.setScaleY(1.06f);
                unlockBlurOverlay.setVisibility(View.VISIBLE);
            }
        });
    }

    private void triggerGlassUnlockTransition() {
        if (unlockBlurOverlay == null) return;
        mainHandler.post(() -> {
            if (!isLockScreenActive && unlockBlurOverlay.getVisibility() != View.VISIBLE) {
                return;
            }
            isLockScreenActive = false;
            if (blurredWallpaperBitmap != null && unlockBlurOverlay.getDrawable() == null) {
                unlockBlurOverlay.setImageBitmap(blurredWallpaperBitmap);
            }
            unlockBlurOverlay.setVisibility(View.VISIBLE);
            unlockBlurOverlay.animate().cancel();
            unlockBlurOverlay.animate()
                    .alpha(0f)
                    .scaleX(1.0f)
                    .scaleY(1.0f)
                    .setDuration(450)
                    .setInterpolator(new DecelerateInterpolator(1.8f))
                    .withEndAction(() -> unlockBlurOverlay.setVisibility(View.GONE))
                    .start();
        });
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
                updateDockApps();
                updatePageDots();
            });
        });
    }

    private void updateDockApps() {
        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        Set<String> dockSet = prefs.getStringSet(KEY_DOCK, null);
        List<AppModel> dockList = new ArrayList<>();
        Set<String> dockPackages = new HashSet<>();

        if (dockSet == null || dockSet.isEmpty()) {
            AppModel phoneApp = null;
            AppModel msgApp = null;
            AppModel browserApp = null;
            AppModel cameraApp = null;

            for (AppModel app : allInstalledApps) {
                String pkg = app.getPackageName().toLowerCase();
                String label = app.getLabel().toLowerCase();
                if (phoneApp == null && (pkg.contains("dialer") || pkg.contains("phone") || pkg.contains("contact") || label.contains("phone") || label.contains("dialer"))) {
                    phoneApp = app;
                } else if (msgApp == null && (pkg.contains("mms") || pkg.contains("message") || label.contains("message"))) {
                    msgApp = app;
                } else if (browserApp == null && (pkg.contains("chrome") || pkg.contains("browser") || label.contains("chrome") || label.contains("browser"))) {
                    browserApp = app;
                } else if (cameraApp == null && (pkg.contains("camera") || label.contains("camera"))) {
                    cameraApp = app;
                }
            }

            if (phoneApp != null) { dockList.add(phoneApp); dockPackages.add(phoneApp.getPackageName()); }
            if (msgApp != null) { dockList.add(msgApp); dockPackages.add(msgApp.getPackageName()); }
            if (browserApp != null) { dockList.add(browserApp); dockPackages.add(browserApp.getPackageName()); }
            if (cameraApp != null) { dockList.add(cameraApp); dockPackages.add(cameraApp.getPackageName()); }

            if (dockList.size() < 4) {
                for (AppModel app : allInstalledApps) {
                    if (!dockPackages.contains(app.getPackageName())) {
                        dockList.add(app);
                        dockPackages.add(app.getPackageName());
                        if (dockList.size() >= 4) break;
                    }
                }
            }
        } else {
            for (AppModel app : allInstalledApps) {
                if (dockSet.contains(app.getPackageName())) {
                    dockList.add(app);
                    dockPackages.add(app.getPackageName());
                    if (dockList.size() >= 4) break;
                }
            }
        }

        dockAdapter.setDockApps(dockList);

        // De-duplicate: Exclude dock apps from home page grid!
        pagerAdapter.setDockPackages(dockPackages);
        pagerAdapter.setApps(allInstalledApps);
    }

    private void showHomeScreenMenu() {
        Dialog dialog = new Dialog(this);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setContentView(R.layout.dialog_app_options);

        if (dialog.getWindow() != null) {
            dialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));
        }

        ImageView icon = dialog.findViewById(R.id.dialog_app_icon);
        TextView title = dialog.findViewById(R.id.dialog_app_title);
        TextView pkgText = dialog.findViewById(R.id.dialog_app_package);
        Button btnTheme = dialog.findViewById(R.id.btn_toggle_dock);
        Button btnWallpaper = dialog.findViewById(R.id.btn_app_info);
        Button btnSettings = dialog.findViewById(R.id.btn_uninstall);

        icon.setImageResource(R.drawable.ic_settings);
        title.setText("Home Screen Design");
        pkgText.setText("Minimalist Visual System");

        boolean isDark = ThemeManager.isDarkTheme(this);
        btnTheme.setText(isDark ? "Switch to Light Theme" : "Switch to Dark Theme");
        btnTheme.setOnClickListener(v -> {
            boolean newDark = !isDark;
            ThemeManager.setThemeMode(this, newDark ? ThemeManager.MODE_DARK : ThemeManager.MODE_LIGHT);
            applyTheme(newDark);
            dialog.dismiss();
            Toast.makeText(this, newDark ? "Dark theme activated" : "Light theme activated", Toast.LENGTH_SHORT).show();
        });

        btnWallpaper.setText("Apply Minimalist Wallpaper");
        btnWallpaper.setOnClickListener(v -> {
            boolean currentDark = ThemeManager.isDarkTheme(this);
            WallpaperHelper.applyPreset(this, currentDark ? WallpaperHelper.PRESET_DARK_NAVY : WallpaperHelper.PRESET_WARM_LINEN);
            mainHandler.postDelayed(this::setupWallpaperGlassBlur, 300);
            Toast.makeText(this, "Minimalist Wallpaper Applied", Toast.LENGTH_SHORT).show();
            dialog.dismiss();
        });

        btnSettings.setText("Launcher Settings");
        btnSettings.setOnClickListener(v -> {
            startActivity(new Intent(this, SettingsActivity.class));
            dialog.dismiss();
        });

        dialog.show();
    }

    private void applyTheme(boolean isDark) {
        ThemeManager.applySystemBars(this, isDark);

        if (dockGlassDrawable != null) {
            dockGlassDrawable.setTheme(isDark);
        }
        if (searchIconView != null) {
            searchIconView.setColorFilter(ThemeManager.getTextMuted(isDark));
        }
        if (searchHintText != null) {
            searchHintText.setTextColor(ThemeManager.getTextMuted(isDark));
        }
        if (btnSearchPill != null) {
            android.graphics.drawable.GradientDrawable pillBg = new android.graphics.drawable.GradientDrawable();
            pillBg.setShape(android.graphics.drawable.GradientDrawable.RECTANGLE);
            pillBg.setCornerRadius(getResources().getDimension(R.dimen.search_pill_radius));
            pillBg.setColor(ThemeManager.getSearchPillBg(isDark));
            pillBg.setStroke((int)(0.75f * getResources().getDisplayMetrics().density), ThemeManager.getSearchPillStroke(isDark));
            btnSearchPill.setBackground(pillBg);
        }
        if (spotlightOverlay != null) {
            spotlightOverlay.setBackgroundColor(ThemeManager.getOverlayBg(isDark));
        }
        if (pagerAdapter != null) {
            pagerAdapter.notifyDataSetChanged();
        }
        updatePageDots();
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
    }

    @Override
    protected void onResume() {
        super.onResume();
        KeyguardManager km = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
        if (km != null && !km.isKeyguardLocked()) {
            if (isLockScreenActive) {
                triggerGlassUnlockTransition();
            }
        }
        // Sync system bars and theme on resume
        boolean isDark = ThemeManager.isDarkTheme(this);
        ThemeManager.applySystemBars(this, isDark);
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            KeyguardManager km = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
            if (km != null && !km.isKeyguardLocked()) {
                if (isLockScreenActive) {
                    triggerGlassUnlockTransition();
                }
            }
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        KeyguardManager km = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
        if (km != null && km.isKeyguardLocked()) {
            prepareGlassLockOverlay();
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (packageReceiver != null) {
            try {
                unregisterReceiver(packageReceiver);
            } catch (Exception ignored) {}
            packageReceiver = null;
        }
        if (screenStateReceiver != null) {
            try {
                unregisterReceiver(screenStateReceiver);
            } catch (Exception ignored) {}
            screenStateReceiver = null;
        }
        executor.shutdown();
    }
}
