package com.cleanphone.glasshome;

import android.app.WallpaperManager;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.LinearGradient;
import android.graphics.Paint;
import android.graphics.RadialGradient;
import android.graphics.Shader;
import android.util.DisplayMetrics;

/**
 * Generates and applies sophisticated minimalist wallpapers:
 * Muted colours, soft gradients, deep navy, charcoal, warm grey.
 * Zero distracting patterns, optimal contrast for icon clarity.
 */
public class WallpaperHelper {

    public static final int PRESET_DARK_NAVY = 0;
    public static final int PRESET_CHARCOAL = 1;
    public static final int PRESET_WARM_LINEN = 2;
    public static final int PRESET_MINIMAL_SLATE = 3;

    public static Bitmap createWallpaperBitmap(int preset, int width, int height) {
        Bitmap bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG | Paint.DITHER_FLAG);

        int cTop, cMid, cBot;
        switch (preset) {
            case PRESET_CHARCOAL:
                cTop = Color.parseColor("#0F1115");
                cMid = Color.parseColor("#15181F");
                cBot = Color.parseColor("#1C2028");
                break;
            case PRESET_WARM_LINEN:
                cTop = Color.parseColor("#F5F6F8");
                cMid = Color.parseColor("#E9EBF0");
                cBot = Color.parseColor("#DFE2E8");
                break;
            case PRESET_MINIMAL_SLATE:
                cTop = Color.parseColor("#ECEFF2");
                cMid = Color.parseColor("#DFE4E8");
                cBot = Color.parseColor("#D4DAE0");
                break;
            case PRESET_DARK_NAVY:
            default:
                cTop = Color.parseColor("#0B0E14");
                cMid = Color.parseColor("#111823");
                cBot = Color.parseColor("#17202D");
                break;
        }

        // 1. Base smooth linear vertical gradient
        Shader linear = new LinearGradient(
                0, 0, 0, height,
                new int[]{cTop, cMid, cBot},
                new float[]{0f, 0.45f, 1f},
                Shader.TileMode.CLAMP
        );
        paint.setShader(linear);
        canvas.drawRect(0, 0, width, height, paint);

        // 2. Subtle radial ambient glow in the upper-center to gently highlight the clock widget
        int glowColor = (preset == PRESET_WARM_LINEN || preset == PRESET_MINIMAL_SLATE)
                ? Color.argb(35, 255, 255, 255)
                : Color.argb(22, 120, 160, 220);
        Shader radial = new RadialGradient(
                width * 0.5f, height * 0.28f, width * 0.65f,
                glowColor, Color.TRANSPARENT,
                Shader.TileMode.CLAMP
        );
        Paint glowPaint = new Paint(Paint.ANTI_ALIAS_FLAG | Paint.DITHER_FLAG);
        glowPaint.setShader(radial);
        canvas.drawRect(0, 0, width, height, glowPaint);

        return bitmap;
    }

    public static boolean applyPreset(Context context, int preset) {
        try {
            DisplayMetrics dm = context.getResources().getDisplayMetrics();
            int width = Math.max(720, dm.widthPixels);
            int height = Math.max(1280, dm.heightPixels);
            Bitmap wallpaper = createWallpaperBitmap(preset, width, height);

            WallpaperManager wm = WallpaperManager.getInstance(context);
            wm.setBitmap(wallpaper);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
