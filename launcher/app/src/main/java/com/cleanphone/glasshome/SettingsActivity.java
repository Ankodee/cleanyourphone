package com.cleanphone.glasshome;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.Settings;
import android.widget.Button;
import android.widget.Toast;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class SettingsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Simple programmatic settings UI
        android.widget.LinearLayout layout = new android.widget.LinearLayout(this);
        layout.setOrientation(android.widget.LinearLayout.VERTICAL);
        layout.setPadding(48, 64, 48, 48);

        android.widget.TextView title = new android.widget.TextView(this);
        title.setText("Liquid Glass Home");
        title.setTextSize(24f);
        title.setTextColor(0xFFFFFFFF);
        title.setPadding(0, 0, 0, 32);
        layout.addView(title);

        Button btnDefaultHome = new Button(this);
        btnDefaultHome.setText("Set as Default Home Screen");
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

        Button btnWallpaper = new Button(this);
        btnWallpaper.setText("Change Wallpaper");
        btnWallpaper.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_SET_WALLPAPER);
            startActivity(Intent.createChooser(intent, "Choose Wallpaper"));
        });
        layout.addView(btnWallpaper);

        Button btnResetDock = new Button(this);
        btnResetDock.setText("Reset Dock Apps to Default");
        btnResetDock.setOnClickListener(v -> {
            getSharedPreferences("glass_home_prefs", MODE_PRIVATE)
                    .edit()
                    .remove("dock_packages")
                    .apply();
            Toast.makeText(this, "Dock reset. Return to home to see changes.", Toast.LENGTH_SHORT).show();
            finish();
        });
        layout.addView(btnResetDock);

        setContentView(layout);
    }
}
