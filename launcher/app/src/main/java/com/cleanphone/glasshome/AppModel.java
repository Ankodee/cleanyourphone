package com.cleanphone.glasshome;

import android.graphics.drawable.Drawable;

public class AppModel {
    private final String packageName;
    private final String activityName;
    private final String label;
    private final Drawable icon;

    public AppModel(String packageName, String activityName, String label, Drawable icon) {
        this.packageName = packageName;
        this.activityName = activityName;
        this.label = label;
        this.icon = icon;
    }

    public String getPackageName() {
        return packageName;
    }

    public String getActivityName() {
        return activityName;
    }

    public String getLabel() {
        return label;
    }

    public Drawable getIcon() {
        return icon;
    }
}
