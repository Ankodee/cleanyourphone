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

    public String getCategory() {
        String p = packageName.toLowerCase();
        String l = label.toLowerCase();

        if (p.contains("dialer") || p.contains("phone") || p.contains("contact") ||
            p.contains("message") || p.contains("mms") || p.contains("mail") ||
            p.contains("whatsapp") || p.contains("telegram") || p.contains("chat")) {
            return "Communication";
        }
        if (p.contains("camera") || p.contains("photo") || p.contains("gallery") ||
            p.contains("music") || p.contains("audio") || p.contains("video") ||
            p.contains("recorder") || p.contains("media")) {
            return "Creativity & Media";
        }
        if (p.contains("settings") || p.contains("clock") || p.contains("calculator") ||
            p.contains("calendar") || p.contains("file") || p.contains("tool") ||
            p.contains("download") || p.contains("manager")) {
            return "Utilities";
        }
        if (p.contains("chrome") || p.contains("browser") || p.contains("search") ||
            p.contains("map") || p.contains("weather") || p.contains("note")) {
            return "Information";
        }
        return "Other";
    }
}
