package com.cleanphone.glasshome;

import android.graphics.Bitmap;
import android.graphics.BitmapShader;
import android.graphics.Canvas;
import android.graphics.ColorFilter;
import android.graphics.LinearGradient;
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
 * Custom Liquid Glass Drawable that emulates Apple iOS 17/18 frosted glass
 * with wallpaper light dispersion, specular edge highlights, and subtle chromatic sheen.
 */
public class LiquidGlassDrawable extends Drawable {

    private final Paint blurPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint frostPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint strokePaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint specularPaint = new Paint(Paint.ANTI_ALIAS_FLAG);

    private final RectF boundsF = new RectF();
    private final Matrix shaderMatrix = new Matrix();

    private float cornerRadius;
    private Bitmap blurredWallpaperBitmap;
    private BitmapShader wallpaperShader;

    public LiquidGlassDrawable(float cornerRadius) {
        this.cornerRadius = cornerRadius;

        strokePaint.setStyle(Paint.Style.STROKE);
        strokePaint.setStrokeWidth(1.6f);

        specularPaint.setStyle(Paint.Style.STROKE);
        specularPaint.setStrokeWidth(0.9f);
        specularPaint.setColor(0x60FFFFFF);
    }

    /**
     * Pass the blurred system wallpaper to enable true optical frosted glass refraction!
     */
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
            // iOS Liquid Glass Refraction Gradient (frosted milky-translucent layer)
            Shader frostShader = new LinearGradient(
                    0, bounds.top, 0, bounds.bottom,
                    new int[]{0x40FFFFFF, 0x1EFFFFFF, 0x2AFFFFFF},
                    new float[]{0f, 0.5f, 1f},
                    Shader.TileMode.CLAMP
            );
            frostPaint.setShader(frostShader);

            // Specular border reflection (gleaming top edge highlight down to subtle refraction)
            Shader strokeShader = new LinearGradient(
                    0, bounds.top, bounds.width() * 0.25f, bounds.bottom,
                    new int[]{0xAAFFFFFF, 0x30FFFFFF, 0x48FFFFFF},
                    new float[]{0f, 0.65f, 1f},
                    Shader.TileMode.CLAMP
            );
            strokePaint.setShader(strokeShader);

            // Scale wallpaper shader to screen coordinates
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

        // 2. Draw frosted translucent glass fill
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, frostPaint);

        // 3. Draw specular outer stroke (Apple frosted edge)
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, strokePaint);

        // 4. Subtle inset highlight arc on top border
        if (boundsF.height() > 20) {
            RectF inset = new RectF(boundsF.left + 1f, boundsF.top + 1f, boundsF.right - 1f, boundsF.top + 3f);
            canvas.drawRoundRect(inset, cornerRadius, cornerRadius, specularPaint);
        }
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
