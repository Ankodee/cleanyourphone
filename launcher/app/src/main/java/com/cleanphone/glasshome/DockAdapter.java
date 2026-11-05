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

public class DockAdapter extends RecyclerView.Adapter<DockAdapter.ViewHolder> {

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
        dockApps.addAll(apps);
        notifyDataSetChanged();
    }

    public List<AppModel> getDockApps() {
        return dockApps;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.item_dock_app, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        AppModel app = dockApps.get(position);
        holder.icon.setImageDrawable(app.getIcon());

        // 0.5x Ultra-snappy dock touch response (50ms down, 80ms rebound)
        holder.itemView.setOnTouchListener((v, event) -> {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    v.animate()
                            .scaleX(0.88f)
                            .scaleY(0.88f)
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

    public static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView icon;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            icon = itemView.findViewById(R.id.dock_app_icon);
        }
    }
}
