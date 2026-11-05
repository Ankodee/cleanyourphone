package com.cleanphone.glasshome;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.GridLayout;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CategoryFolderAdapter extends RecyclerView.Adapter<CategoryFolderAdapter.FolderViewHolder> {

    public static class CategoryGroup {
        String title;
        List<AppModel> apps;

        public CategoryGroup(String title, List<AppModel> apps) {
            this.title = title;
            this.apps = apps;
        }
    }

    private final Context context;
    private final List<CategoryGroup> groups = new ArrayList<>();
    private final AppGridAdapter.OnAppClickListener listener;

    public CategoryFolderAdapter(Context context, AppGridAdapter.OnAppClickListener listener) {
        this.context = context;
        this.listener = listener;
    }

    public void setGroups(List<CategoryGroup> newGroups) {
        groups.clear();
        if (newGroups != null) {
            groups.addAll(newGroups);
        }
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public FolderViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.item_category_folder, parent, false);
        return new FolderViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull FolderViewHolder holder, int position) {
        CategoryGroup group = groups.get(position);
        holder.title.setText(group.title);
        holder.grid.removeAllViews();

        int maxApps = Math.min(4, group.apps.size());
        int iconPx = (int) (48 * context.getResources().getDisplayMetrics().density);

        for (int i = 0; i < maxApps; i++) {
            AppModel app = group.apps.get(i);
            ImageView iv = new ImageView(context);
            GridLayout.LayoutParams params = new GridLayout.LayoutParams();
            params.width = iconPx;
            params.height = iconPx;
            params.setMargins(8, 8, 8, 8);
            iv.setLayoutParams(params);
            iv.setImageDrawable(app.getIcon());
            iv.setScaleType(ImageView.ScaleType.FIT_CENTER);

            iv.setOnClickListener(v -> {
                if (listener != null) listener.onAppClick(app);
            });
            iv.setOnLongClickListener(v -> {
                if (listener != null) listener.onAppLongClick(app, v);
                return true;
            });

            holder.grid.addView(iv);
        }
    }

    @Override
    public int getItemCount() {
        return groups.size();
    }

    static class FolderViewHolder extends RecyclerView.ViewHolder {
        GridLayout grid;
        TextView title;

        FolderViewHolder(@NonNull View itemView) {
            super(itemView);
            grid = itemView.findViewById(R.id.folder_grid);
            title = itemView.findViewById(R.id.folder_title);
        }
    }
}
