package com.cleanphone.glasshome;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.graphics.Color;
import android.os.Build;
import android.view.View;
import android.view.Window;

public class ThemeManager {

    private static final String PREFS_NAME = "glass_home_prefs";
    private static final String KEY_THEME = "theme_mode";

    public static final String MODE_DARK = "dark";
    public static final String MODE_LIGHT = "light";
    public static final String MODE_SYSTEM = "system";

    public static String getThemeMode(Context context) {
        SharedPreferences prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        return prefs.getString(KEY_THEME, MODE_DARK);
    }

    public static void setThemeMode(Context context, String mode) {
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
                .edit()
                .putString(KEY_THEME, mode)
                .apply();
    }

    public static boolean isDarkTheme(Context context) {
        String mode = getThemeMode(context);
        if (MODE_LIGHT.equals(mode)) {
            return false;
        } else if (MODE_DARK.equals(mode)) {
            return true;
        } else {
            int nightMode = context.getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK;
            return nightMode != Configuration.UI_MODE_NIGHT_NO;
        }
    }

    public static int getTextPrimary(boolean isDark) {
        return isDark ? Color.parseColor("#E6EDF3") : Color.parseColor("#1F2328");
    }

    public static int getTextSecondary(boolean isDark) {
        return isDark ? Color.parseColor("#8B949E") : Color.parseColor("#57606A");
    }

    public static int getTextMuted(boolean isDark) {
        return isDark ? Color.parseColor("#57606A") : Color.parseColor("#8C959F");
    }

    public static int getSearchPillBg(boolean isDark) {
        return isDark ? Color.parseColor("#20FFFFFF") : Color.parseColor("#14000000");
    }

    public static int getSearchPillStroke(boolean isDark) {
        return isDark ? Color.parseColor("#26FFFFFF") : Color.parseColor("#18000000");
    }

    public static int getDockFill(boolean isDark) {
        return isDark ? Color.parseColor("#2212161E") : Color.parseColor("#38FFFFFF");
    }

    public static int getDockStroke(boolean isDark) {
        return isDark ? Color.parseColor("#22FFFFFF") : Color.parseColor("#18000000");
    }

    public static int getOverlayBg(boolean isDark) {
        return isDark ? Color.parseColor("#E60D1117") : Color.parseColor("#F0F6F8FA");
    }

    public static int getSearchInputBg(boolean isDark) {
        return isDark ? Color.parseColor("#2E1E2430") : Color.parseColor("#40E2E5E9");
    }

    public static void applySystemBars(Activity activity, boolean isDark) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            Window window = activity.getWindow();
            int flags = window.getDecorView().getSystemUiVisibility();

            flags |= View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                     View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN |
                     View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION;

            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                if (isDark) {
                    flags &= ~View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR;
                } else {
                    flags |= View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR;
                }
            }

            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                if (isDark) {
                    flags &= ~View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR;
                } else {
                    flags |= View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR;
                }
            }

            window.getDecorView().setSystemUiVisibility(flags);
            window.setStatusBarColor(Color.TRANSPARENT);
            window.setNavigationBarColor(Color.TRANSPARENT);
        }
    }
}
