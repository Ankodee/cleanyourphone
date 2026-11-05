package com.cleanphone.glasshome;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;

public class AppAdapter extends RecyclerView.Adapter<AppAdapter.ViewHolder> {

    public interface OnAppClickListener {
        void onAppClick(AppModel app);
        void onAppLongClick(AppModel app, View anchor);
    }

    private final Context context;
    private final List<AppModel> fullList = new ArrayList<>();
    private final List<AppModel> displayedList = new ArrayList<>();
    private final OnAppClickListener listener;

    public AppAdapter(Context context, OnAppClickListener listener) {
        this.context = context;
        this.listener = listener;
    }

    public void setApps(List<AppModel> apps) {
        fullList.clear();
        fullList.addAll(apps);
        displayedList.clear();
        displayedList.addAll(apps);
        notifyDataSetChanged();
    }

    public void filter(String query) {
        displayedList.clear();
        if (query == null || query.trim().isEmpty()) {
            displayedList.addAll(fullList);
        } else {
            String lower = query.toLowerCase().trim();
            for (AppModel app : fullList) {
                if (app.getLabel().toLowerCase().contains(lower) ||
                    app.getPackageName().toLowerCase().contains(lower)) {
                    displayedList.add(app);
                }
            }
        }
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.item_app, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        AppModel app = displayedList.get(position);
        holder.icon.setImageDrawable(app.getIcon());
        holder.label.setText(app.getLabel());

        // 0.5x Ultra-snappy lag-free touch response (50ms down, 80ms rebound)
        holder.itemView.setOnTouchListener((v, event) -> {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    v.animate()
                            .scaleX(0.92f)
                            .scaleY(0.92f)
                            .setDuration(50)
                            .setInterpolator(new android.view.animation.DecelerateInterpolator(2.0f))
                            .start();
                    break;
                case MotionEvent.ACTION_UP:
                case MotionEvent.ACTION_CANCEL:
                    v.animate()
                            .scaleX(1.0f)
                            .scaleY(1.0f)
                            .setDuration(80)
                            .setInterpolator(new android.view.animation.OvershootInterpolator(1.2f))
                            .start();
                    break;
            }
            return false;
        });

        holder.itemView.setOnClickListener(v -> {
            if (listener != null) {
                listener.onAppClick(app);
            }
        });

        holder.itemView.setOnLongClickListener(v -> {
            if (listener != null) {
                listener.onAppLongClick(app, v);
                return true;
            }
            return false;
        });
    }

    @Override
    public int getItemCount() {
        return displayedList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView icon;
        TextView label;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            icon = itemView.findViewById(R.id.app_icon);
            label = itemView.findViewById(R.id.app_label);
        }
    }
}
