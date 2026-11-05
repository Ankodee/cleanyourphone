package com.cleanphone.glasshome;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;

public class SearchResultsAdapter extends RecyclerView.Adapter<SearchResultsAdapter.SearchViewHolder> {

    private final Context context;
    private final List<AppModel> results = new ArrayList<>();
    private final AppGridAdapter.OnAppClickListener listener;

    public SearchResultsAdapter(Context context, AppGridAdapter.OnAppClickListener listener) {
        this.context = context;
        this.listener = listener;
    }

    public void setResults(List<AppModel> newResults) {
        results.clear();
        if (newResults != null) {
            results.addAll(newResults);
        }
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public SearchViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.item_search_result, parent, false);
        return new SearchViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull SearchViewHolder holder, int position) {
        AppModel app = results.get(position);
        holder.icon.setImageDrawable(app.getIcon());
        holder.title.setText(app.getLabel());
        holder.subtitle.setText(app.getPackageName() + " • " + app.getCategory());

        holder.itemView.setOnClickListener(v -> {
            if (listener != null) listener.onAppClick(app);
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
        return results.size();
    }

    static class SearchViewHolder extends RecyclerView.ViewHolder {
        ImageView icon;
        TextView title;
        TextView subtitle;

        SearchViewHolder(@NonNull View itemView) {
            super(itemView);
            icon = itemView.findViewById(R.id.search_item_icon);
            title = itemView.findViewById(R.id.search_item_title);
            subtitle = itemView.findViewById(R.id.search_item_subtitle);
        }
    }
}
