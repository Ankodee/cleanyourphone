package com.cleanphone.glasshome;

import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.BatteryManager;
import android.provider.AlarmClock;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextClock;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Minimalist Horizontal SpringBoard Pager Adapter.
 * Clean, balanced hierarchy:
 * Page 0: Minimal Clock & Date + Battery header + Curated App Grid (Zero dock duplicates)
 * Pages 1 .. N-1: Remaining installed applications (16 apps per page)
 * Page N: Organized App Library with categories
 */
public class SpringBoardPagerAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    public interface OnSearchTriggerListener {
        void onSearchTriggered();
    }

    private static final int VIEW_TYPE_HOME = 0;
    private static final int VIEW_TYPE_APPS = 1;
    private static final int VIEW_TYPE_LIBRARY = 2;

    private static final int HOME_APPS_COUNT = 8;
    private static final int SUBSEQUENT_APPS_COUNT = 16;

    private final Context context;
    private final List<AppModel> allApps = new ArrayList<>();
    private final Set<String> dockPackages = new HashSet<>();
    private final AppGridAdapter.OnAppClickListener appClickListener;
    private final OnSearchTriggerListener searchTriggerListener;

    private final List<List<AppModel>> pagedApps = new ArrayList<>();
    private final List<CategoryFolderAdapter.CategoryGroup> libraryCategories = new ArrayList<>();

    public SpringBoardPagerAdapter(Context context,
                                   AppGridAdapter.OnAppClickListener appClickListener,
                                   OnSearchTriggerListener searchTriggerListener) {
        this.context = context;
        this.appClickListener = appClickListener;
        this.searchTriggerListener = searchTriggerListener;
    }

    public void setApps(List<AppModel> apps) {
        allApps.clear();
        if (apps != null) {
            allApps.addAll(apps);
        }
        rebuildPages();
    }

    public void setDockPackages(Set<String> packages) {
        dockPackages.clear();
        if (packages != null) {
            dockPackages.addAll(packages);
        }
        rebuildPages();
    }

    private void rebuildPages() {
        pagedApps.clear();
        libraryCategories.clear();

        if (allApps.isEmpty()) {
            notifyDataSetChanged();
            return;
        }

        // De-duplicate: Never duplicate apps between the main grid and the bottom dock
        List<AppModel> nonDockApps = new ArrayList<>();
        for (AppModel app : allApps) {
            if (!dockPackages.contains(app.getPackageName())) {
                nonDockApps.add(app);
            }
        }

        // Slicing for Page 0 (Home Page: clean minimalist top 8 apps)
        int homeCount = Math.min(HOME_APPS_COUNT, nonDockApps.size());
        pagedApps.add(new ArrayList<>(nonDockApps.subList(0, homeCount)));

        // Slicing for subsequent pages (16 apps per page)
        int cursor = homeCount;
        while (cursor < nonDockApps.size()) {
            int nextEnd = Math.min(cursor + SUBSEQUENT_APPS_COUNT, nonDockApps.size());
            pagedApps.add(new ArrayList<>(nonDockApps.subList(cursor, nextEnd)));
            cursor = nextEnd;
        }

        // Build App Library categories
        buildLibraryCategories();
        notifyDataSetChanged();
    }

    private void buildLibraryCategories() {
        Map<String, List<AppModel>> catMap = new HashMap<>();
        for (AppModel app : allApps) {
            String cat = app.getCategory();
            if (!catMap.containsKey(cat)) {
                catMap.put(cat, new ArrayList<>());
            }
            catMap.get(cat).add(app);
        }

        // Suggestions (Top 4 apps)
        if (allApps.size() >= 4) {
            libraryCategories.add(new CategoryFolderAdapter.CategoryGroup("Suggestions",
                    new ArrayList<>(allApps.subList(0, Math.min(8, allApps.size())))));
        }

        for (Map.Entry<String, List<AppModel>> entry : catMap.entrySet()) {
            libraryCategories.add(new CategoryFolderAdapter.CategoryGroup(entry.getKey(), entry.getValue()));
        }
    }

    @Override
    public int getItemViewType(int position) {
        if (position == 0) {
            return VIEW_TYPE_HOME;
        } else if (position <= pagedApps.size() - 1) {
            return VIEW_TYPE_APPS;
        } else {
            return VIEW_TYPE_LIBRARY;
        }
    }

    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(context);
        if (viewType == VIEW_TYPE_HOME) {
            View v = inflater.inflate(R.layout.page_home, parent, false);
            return new HomeViewHolder(v);
        } else if (viewType == VIEW_TYPE_APPS) {
            View v = inflater.inflate(R.layout.page_apps, parent, false);
            return new AppsViewHolder(v);
        } else {
            View v = inflater.inflate(R.layout.page_app_library, parent, false);
            return new LibraryViewHolder(v);
        }
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
        boolean isDark = ThemeManager.isDarkTheme(context);

        if (holder instanceof HomeViewHolder) {
            HomeViewHolder h = (HomeViewHolder) holder;

            // Update live battery level in widget
            int battery = getBatteryLevel();
            h.batteryText.setText(battery > 0 ? battery + "%" : "100%");

            // Apply dynamic theme colors to widget
            h.clockWidget.setTextColor(ThemeManager.getTextPrimary(isDark));
            h.dateWidget.setTextColor(ThemeManager.getTextSecondary(isDark));
            h.batteryText.setTextColor(ThemeManager.getTextSecondary(isDark));
            h.dividerDot.setTextColor(ThemeManager.getTextMuted(isDark));
            h.batteryIcon.setColorFilter(ThemeManager.getTextSecondary(isDark));

            // Tap Clock to open Alarms/Clock
            h.clockWidget.setOnClickListener(v -> {
                try {
                    Intent intent = new Intent(AlarmClock.ACTION_SHOW_ALARMS);
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                    context.startActivity(intent);
                } catch (Exception ignored) {}
            });

            // Tap Date to open Calendar
            h.dateWidget.setOnClickListener(v -> {
                try {
                    Intent intent = new Intent(Intent.ACTION_MAIN);
                    intent.addCategory(Intent.CATEGORY_APP_CALENDAR);
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                    context.startActivity(intent);
                } catch (Exception ignored) {}
            });

            // Bind Page 0 App Grid (Max 8 apps, plenty of breathing space)
            List<AppModel> pageApps = !pagedApps.isEmpty() ? pagedApps.get(0) : new ArrayList<>();
            AppGridAdapter adapter = new AppGridAdapter(context, appClickListener);
            h.appGrid.setLayoutManager(new GridLayoutManager(context, 4));
            h.appGrid.setHasFixedSize(true);
            h.appGrid.setAdapter(adapter);
            adapter.setApps(pageApps);

        } else if (holder instanceof AppsViewHolder) {
            AppsViewHolder h = (AppsViewHolder) holder;
            List<AppModel> pageApps = position < pagedApps.size() ? pagedApps.get(position) : new ArrayList<>();
            AppGridAdapter adapter = new AppGridAdapter(context, appClickListener);
            h.appGrid.setLayoutManager(new GridLayoutManager(context, 4));
            h.appGrid.setHasFixedSize(true);
            h.appGrid.setAdapter(adapter);
            adapter.setApps(pageApps);

        } else if (holder instanceof LibraryViewHolder) {
            LibraryViewHolder h = (LibraryViewHolder) holder;
            h.searchTrigger.setOnClickListener(v -> {
                if (searchTriggerListener != null) {
                    searchTriggerListener.onSearchTriggered();
                }
            });

            CategoryFolderAdapter adapter = new CategoryFolderAdapter(context, appClickListener);
            h.categoryRecycler.setLayoutManager(new GridLayoutManager(context, 2));
            h.categoryRecycler.setHasFixedSize(true);
            h.categoryRecycler.setAdapter(adapter);
            adapter.setGroups(libraryCategories);
        }
    }

    @Override
    public int getItemCount() {
        int count = pagedApps.size();
        return count > 0 ? count + 1 : 1;
    }

    private int getBatteryLevel() {
        try {
            Intent intent = context.registerReceiver(null, new IntentFilter(Intent.ACTION_BATTERY_CHANGED));
            if (intent != null) {
                int level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
                int scale = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1);
                if (level >= 0 && scale > 0) {
                    return (int) ((level / (float) scale) * 100);
                }
            }
        } catch (Exception ignored) {}
        return 85;
    }

    static class HomeViewHolder extends RecyclerView.ViewHolder {
        TextClock clockWidget;
        TextClock dateWidget;
        TextView dividerDot;
        ImageView batteryIcon;
        TextView batteryText;
        RecyclerView appGrid;

        HomeViewHolder(@NonNull View itemView) {
            super(itemView);
            clockWidget = itemView.findViewById(R.id.widget_clock);
            dateWidget = itemView.findViewById(R.id.widget_date);
            dividerDot = itemView.findViewById(R.id.widget_divider_dot);
            batteryIcon = itemView.findViewById(R.id.widget_battery_icon);
            batteryText = itemView.findViewById(R.id.text_battery_level);
            appGrid = itemView.findViewById(R.id.page_app_grid);
        }
    }

    static class AppsViewHolder extends RecyclerView.ViewHolder {
        RecyclerView appGrid;

        AppsViewHolder(@NonNull View itemView) {
            super(itemView);
            appGrid = itemView.findViewById(R.id.page_app_grid);
        }
    }

    static class LibraryViewHolder extends RecyclerView.ViewHolder {
        View searchTrigger;
        RecyclerView categoryRecycler;

        LibraryViewHolder(@NonNull View itemView) {
            super(itemView);
            searchTrigger = itemView.findViewById(R.id.library_search_trigger);
            categoryRecycler = itemView.findViewById(R.id.recycler_app_library);
        }
    }
}
