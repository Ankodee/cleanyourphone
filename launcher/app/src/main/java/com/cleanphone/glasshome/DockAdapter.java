package com.cleanphone.glasshome;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;

public class DockAdapter extends RecyclerView.Adapter<DockAdapter.DockViewHolder> {

    public interface OnDockClickListener {
        void onDockAppClick(AppModel app);
        void onDockAppLongClick(AppModel app);
    }

    private final Context context;
    private final List<AppModel> dockApps = new ArrayList<>();
    private final OnDockClickListener listener;

    public DockAdapter(Context context, OnDockClickListener listener) {
        this.context = context;
        this.listener = listener;
    }

    public void setDockApps(List<AppModel> apps) {
        dockApps.clear();
        if (apps != null) {
            dockApps.addAll(apps);
        }
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public DockViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.item_dock_app, parent, false);
        return new DockViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull DockViewHolder holder, int position) {
        AppModel app = dockApps.get(position);
        holder.icon.setImageDrawable(app.getIcon());

        // Snappy iOS press touch effect
        holder.itemView.setOnTouchListener((v, event) -> {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    v.animate().scaleX(0.90f).scaleY(0.90f).setDuration(80).start();
                    break;
                case MotionEvent.ACTION_UP:
                case MotionEvent.ACTION_CANCEL:
                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(120).start();
                    break;
            }
            return false;
        });

        holder.itemView.setOnClickListener(v -> {
            if (listener != null) {
                listener.onDockAppClick(app);
            }
        });

        holder.itemView.setOnLongClickListener(v -> {
            if (listener != null) {
                listener.onDockAppLongClick(app);
                return true;
            }
            return false;
        });
    }

    @Override
    public int getItemCount() {
        return dockApps.size();
    }

    static class DockViewHolder extends RecyclerView.ViewHolder {
        ImageView icon;

        DockViewHolder(@NonNull View itemView) {
            super(itemView);
            icon = itemView.findViewById(R.id.dock_app_icon);
        }
    }
}
