package com.cleanphone.glasshome;

import android.app.WallpaperManager;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.LinearGradient;
import android.graphics.Paint;
import android.graphics.RadialGradient;
import android.graphics.Shader;
import android.util.DisplayMetrics;

/**
 * Generates and applies bespoke minimalist wallpapers:
 * - Premium Abstract Blue: Flowing midnight navy, cobalt, royal blue, and steel-blue organic ribbon curves.
 * - Warm Charcoal, Warm Linen, Minimal Slate.
 */
public class WallpaperHelper {

    public static final int PRESET_PREMIUM_BLUE = 0;
    public static final int PRESET_DARK_NAVY = 1;
    public static final int PRESET_CHARCOAL = 2;
    public static final int PRESET_WARM_LINEN = 3;
    public static final int PRESET_MINIMAL_SLATE = 4;

    public static Bitmap createWallpaperBitmap(Context context, int preset, int width, int height) {
        if (preset == PRESET_PREMIUM_BLUE) {
            try {
                Bitmap bmp = BitmapFactory.decodeResource(context.getResources(), R.drawable.wallpaper_premium_blue);
                if (bmp != null) {
                    if (bmp.getWidth() == width && bmp.getHeight() == height) {
                        return bmp;
                    }
                    return Bitmap.createScaledBitmap(bmp, width, height, true);
                }
            } catch (Throwable ignored) {}
        }

        Bitmap bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG | Paint.DITHER_FLAG);

        int cTop, cMid, cBot;
        switch (preset) {
            case PRESET_CHARCOAL:
                cTop = Color.parseColor("#101318");
                cMid = Color.parseColor("#181E27");
                cBot = Color.parseColor("#222A36");
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
                cTop = Color.parseColor("#080D1A");
                cMid = Color.parseColor("#111D35");
                cBot = Color.parseColor("#1B2A4A");
                break;
        }

        Shader linear = new LinearGradient(
                0, 0, 0, height,
                new int[]{cTop, cMid, cBot},
                new float[]{0f, 0.45f, 1f},
                Shader.TileMode.CLAMP
        );
        paint.setShader(linear);
        canvas.drawRect(0, 0, width, height, paint);

        int glowColor = (preset == PRESET_WARM_LINEN || preset == PRESET_MINIMAL_SLATE)
                ? Color.argb(35, 255, 255, 255)
                : Color.argb(45, 60, 130, 230);
        Shader radial = new RadialGradient(
                width * 0.5f, height * 0.32f, width * 0.70f,
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
            Bitmap wallpaper = createWallpaperBitmap(context, preset, width, height);

            WallpaperManager wm = WallpaperManager.getInstance(context);
            wm.setBitmap(wallpaper);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
