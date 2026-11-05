package com.cleanphone.glasshome;

import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.BatteryManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Horizontal SpringBoard Pager Adapter.
 * Enables authentic left-to-right paginated app browsing like iOS 17/18.
 * Page 0: iOS Frosted Glass Widget + Home App Grid (16 apps)
 * Pages 1 .. N-1: Standard 4x5 App Pages (20 apps per page)
 * Page N: iOS App Library with 2x2 Frosted Category Folders
 */
public class SpringBoardPagerAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    public interface OnSearchTriggerListener {
        void onSearchTriggered();
    }

    private static final int VIEW_TYPE_HOME = 0;
    private static final int VIEW_TYPE_APPS = 1;
    private static final int VIEW_TYPE_LIBRARY = 2;

    private static final int HOME_APPS_COUNT = 16;
    private static final int SUBSEQUENT_APPS_COUNT = 20;

    private final Context context;
    private final List<AppModel> allApps = new ArrayList<>();
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
        pagedApps.clear();
        libraryCategories.clear();

        if (apps != null && !apps.isEmpty()) {
            allApps.addAll(apps);

            // Slicing for Page 0 (Home Page: max 16 apps)
            int firstPageEnd = Math.min(HOME_APPS_COUNT, allApps.size());
            pagedApps.add(new ArrayList<>(allApps.subList(0, firstPageEnd)));

            // Slicing for subsequent pages (20 apps per page)
            int cursor = firstPageEnd;
            while (cursor < allApps.size()) {
                int nextEnd = Math.min(cursor + SUBSEQUENT_APPS_COUNT, allApps.size());
                pagedApps.add(new ArrayList<>(allApps.subList(cursor, nextEnd)));
                cursor = nextEnd;
            }

            // Build App Library categories
            buildLibraryCategories();
        }

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
        if (holder instanceof HomeViewHolder) {
            HomeViewHolder h = (HomeViewHolder) holder;
            // Update live battery level in iOS widget
            int battery = getBatteryLevel();
            h.batteryText.setText(battery > 0 ? battery + "%" : "100%");

            // Bind Page 0 App Grid
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
        // Number of app pages + 1 App Library page
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
        TextView batteryText;
        RecyclerView appGrid;

        HomeViewHolder(@NonNull View itemView) {
            super(itemView);
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
