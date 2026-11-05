package com.cleanphone.glasshome;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.provider.Settings;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

/**
 * Minimalist Settings Screen.
 * Control themes, curated wallpaper presets, and default launcher status.
 */
public class SettingsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        boolean isDark = ThemeManager.isDarkTheme(this);
        ThemeManager.applySystemBars(this, isDark);

        ScrollView scrollView = new ScrollView(this);
        scrollView.setBackgroundColor(isDark ? 0xFF0E1116 : 0xFFF5F6F8);

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        int pad = (int) (20 * getResources().getDisplayMetrics().density);
        layout.setPadding(pad, pad + 16, pad, pad + 32);

        // Header Title
        TextView title = new TextView(this);
        title.setText("Minimalist Home");
        title.setTextSize(24f);
        title.setTextColor(isDark ? 0xFFE6EDF3 : 0xFF1F2328);
        title.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
        layout.addView(title);

        TextView subtitle = new TextView(this);
        subtitle.setText("Visual Design & Theme Configuration");
        subtitle.setTextSize(13f);
        subtitle.setTextColor(isDark ? 0xFF8B949E : 0xFF57606A);
        subtitle.setPadding(0, 4, 0, 24);
        layout.addView(subtitle);

        // Section: Themes
        addSectionHeader(layout, "THEMES", isDark);

        Button btnDark = createStyledButton("Dark Mode", isDark);
        btnDark.setOnClickListener(v -> {
            ThemeManager.setThemeMode(this, ThemeManager.MODE_DARK);
            Toast.makeText(this, "Dark theme selected", Toast.LENGTH_SHORT).show();
            recreate();
        });
        layout.addView(btnDark);

        Button btnLight = createStyledButton("Light Mode", isDark);
        btnLight.setOnClickListener(v -> {
            ThemeManager.setThemeMode(this, ThemeManager.MODE_LIGHT);
            Toast.makeText(this, "Light theme selected", Toast.LENGTH_SHORT).show();
            recreate();
        });
        layout.addView(btnLight);

        Button btnSystem = createStyledButton("Follow System Theme", isDark);
        btnSystem.setOnClickListener(v -> {
            ThemeManager.setThemeMode(this, ThemeManager.MODE_SYSTEM);
            Toast.makeText(this, "System theme selected", Toast.LENGTH_SHORT).show();
            recreate();
        });
        layout.addView(btnSystem);

        // Section: Wallpapers
        addSectionHeader(layout, "CURATED WALLPAPERS", isDark);

        Button btnWpBlue = createStyledButton("Apply Abstract Blue (Flagship)", isDark);
        btnWpBlue.setOnClickListener(v -> {
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_PREMIUM_BLUE);
            Toast.makeText(this, "Abstract Blue wallpaper applied", Toast.LENGTH_SHORT).show();
        });
        layout.addView(btnWpBlue);

        Button btnWpNavy = createStyledButton("Apply Obsidian Navy (Dark)", isDark);
        btnWpNavy.setOnClickListener(v -> {
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_DARK_NAVY);
            Toast.makeText(this, "Obsidian Navy wallpaper applied", Toast.LENGTH_SHORT).show();
        });
        layout.addView(btnWpNavy);

        Button btnWpCharcoal = createStyledButton("Apply Warm Graphite (Dark)", isDark);
        btnWpCharcoal.setOnClickListener(v -> {
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_CHARCOAL);
            Toast.makeText(this, "Warm Graphite wallpaper applied", Toast.LENGTH_SHORT).show();
        });
        layout.addView(btnWpCharcoal);

        Button btnWpLinen = createStyledButton("Apply Warm Linen (Light)", isDark);
        btnWpLinen.setOnClickListener(v -> {
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_WARM_LINEN);
            Toast.makeText(this, "Warm Linen wallpaper applied", Toast.LENGTH_SHORT).show();
        });
        layout.addView(btnWpLinen);

        Button btnWpSlate = createStyledButton("Apply Minimal Slate (Light)", isDark);
        btnWpSlate.setOnClickListener(v -> {
            WallpaperHelper.applyPreset(this, WallpaperHelper.PRESET_MINIMAL_SLATE);
            Toast.makeText(this, "Minimal Slate wallpaper applied", Toast.LENGTH_SHORT).show();
        });
        layout.addView(btnWpSlate);

        // Section: System & Defaults
        addSectionHeader(layout, "SYSTEM & DEFAULTS", isDark);

        Button btnDefaultHome = createStyledButton("Set as Default Home Screen", isDark);
        btnDefaultHome.setOnClickListener(v -> {
            try {
                Intent intent = new Intent(Settings.ACTION_MANAGE_DEFAULT_APPS_SETTINGS);
                startActivity(intent);
            } catch (Exception e) {
                Intent intent = new Intent(Settings.ACTION_SETTINGS);
                startActivity(intent);
            }
        });
        layout.addView(btnDefaultHome);

        Button btnResetDock = createStyledButton("Reset Dock Apps to Default", isDark);
        btnResetDock.setOnClickListener(v -> {
            getSharedPreferences("glass_home_prefs", MODE_PRIVATE)
                    .edit()
                    .remove("dock_packages")
                    .apply();
            Toast.makeText(this, "Dock reset to defaults", Toast.LENGTH_SHORT).show();
            finish();
        });
        layout.addView(btnResetDock);

        scrollView.addView(layout);
        setContentView(scrollView);
    }

    private void addSectionHeader(LinearLayout layout, String title, boolean isDark) {
        TextView header = new TextView(this);
        header.setText(title);
        header.setTextSize(11f);
        header.setTextColor(isDark ? 0xFF58A6FF : 0xFF0969DA);
        header.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
        header.setLetterSpacing(0.08f);
        header.setPadding(4, 20, 0, 8);
        layout.addView(header);
    }

    private Button createStyledButton(String text, boolean isDark) {
        Button btn = new Button(this);
        btn.setText(text);
        btn.setTextSize(13.5f);
        btn.setAllCaps(false);
        btn.setTextColor(isDark ? 0xFFE6EDF3 : 0xFF1F2328);
        btn.setBackgroundColor(isDark ? 0xFF1C2128 : 0xFFE8ECEF);

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );
        params.setMargins(0, 4, 0, 4);
        btn.setLayoutParams(params);
        return btn;
    }
}
