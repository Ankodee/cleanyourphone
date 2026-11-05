package com.cleanphone.glasshome;

import android.graphics.Bitmap;
import android.graphics.BitmapShader;
import android.graphics.Canvas;
import android.graphics.ColorFilter;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.PixelFormat;
import android.graphics.Rect;
import android.graphics.RectF;
import android.graphics.Shader;
import android.graphics.drawable.Drawable;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

/**
 * Premium Minimalist Translucent Dock Drawable.
 * Emulates soft optical wallpaper pass-through with subtle hairline stroke,
 * eliminating harsh specular reflections and heavy outlines.
 */
public class LiquidGlassDrawable extends Drawable {

    private final Paint blurPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint frostPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint strokePaint = new Paint(Paint.ANTI_ALIAS_FLAG);

    private final RectF boundsF = new RectF();
    private final Matrix shaderMatrix = new Matrix();

    private float cornerRadius;
    private Bitmap blurredWallpaperBitmap;
    private BitmapShader wallpaperShader;
    private boolean isDark = true;

    public LiquidGlassDrawable(float cornerRadius) {
        this.cornerRadius = cornerRadius;

        strokePaint.setStyle(Paint.Style.STROKE);
        strokePaint.setStrokeWidth(1.2f);
        updateColors();
    }

    public void setTheme(boolean isDark) {
        this.isDark = isDark;
        updateColors();
        invalidateSelf();
    }

    private void updateColors() {
        frostPaint.setColor(ThemeManager.getDockFill(isDark));
        strokePaint.setColor(ThemeManager.getDockStroke(isDark));
    }

    public void setBlurredWallpaper(Bitmap bitmap) {
        this.blurredWallpaperBitmap = bitmap;
        if (bitmap != null) {
            this.wallpaperShader = new BitmapShader(bitmap, Shader.TileMode.CLAMP, Shader.TileMode.CLAMP);
            blurPaint.setShader(wallpaperShader);
        } else {
            this.wallpaperShader = null;
            blurPaint.setShader(null);
        }
        invalidateSelf();
    }

    public void setCornerRadius(float cornerRadius) {
        this.cornerRadius = cornerRadius;
        invalidateSelf();
    }

    @Override
    protected void onBoundsChange(@NonNull Rect bounds) {
        super.onBoundsChange(bounds);
        boundsF.set(bounds);

        if (bounds.width() > 0 && bounds.height() > 0) {
            if (wallpaperShader != null && blurredWallpaperBitmap != null) {
                shaderMatrix.reset();
                float scaleX = (float) bounds.width() / (float) blurredWallpaperBitmap.getWidth();
                float scaleY = (float) bounds.height() / (float) blurredWallpaperBitmap.getHeight();
                shaderMatrix.setScale(scaleX, scaleY);
                wallpaperShader.setLocalMatrix(shaderMatrix);
            }
        }
    }

    @Override
    public void draw(@NonNull Canvas canvas) {
        // 1. Draw blurred wallpaper base if available (optical background distortion)
        if (wallpaperShader != null) {
            canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, blurPaint);
        }

        // 2. Draw frosted translucent surface
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, frostPaint);

        // 3. Draw minimal hairline stroke
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, strokePaint);
    }

    @Override
    public void setAlpha(int alpha) {
        frostPaint.setAlpha(alpha);
        blurPaint.setAlpha(alpha);
        invalidateSelf();
    }

    @Override
    public void setColorFilter(@Nullable ColorFilter colorFilter) {
        frostPaint.setColorFilter(colorFilter);
        blurPaint.setColorFilter(colorFilter);
        invalidateSelf();
    }

    @Override
    public int getOpacity() {
        return PixelFormat.TRANSLUCENT;
    }
}
