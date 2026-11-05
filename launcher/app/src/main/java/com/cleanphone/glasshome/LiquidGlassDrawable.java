package com.cleanphone.glasshome;

import android.graphics.Canvas;
import android.graphics.ColorFilter;
import android.graphics.LinearGradient;
import android.graphics.Paint;
import android.graphics.PixelFormat;
import android.graphics.Rect;
import android.graphics.RectF;
import android.graphics.Shader;
import android.graphics.drawable.Drawable;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class LiquidGlassDrawable extends Drawable {
    private final Paint fillPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint strokePaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint highlightPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final RectF boundsF = new RectF();
    private float cornerRadius = 48f;

    public LiquidGlassDrawable(float cornerRadius) {
        this.cornerRadius = cornerRadius;
        strokePaint.setStyle(Paint.Style.STROKE);
        strokePaint.setStrokeWidth(1.8f);

        highlightPaint.setStyle(Paint.Style.STROKE);
        highlightPaint.setStrokeWidth(1.0f);
        highlightPaint.setColor(0x55FFFFFF);
    }

    @Override
    protected void onBoundsChange(@NonNull Rect bounds) {
        super.onBoundsChange(bounds);
        boundsF.set(bounds);
        if (bounds.height() > 0 && bounds.width() > 0) {
            // Refined Liquid Glass Refraction Gradient (Translucent, deep ambient frost)
            Shader fillShader = new LinearGradient(
                    0, bounds.top, 0, bounds.bottom,
                    new int[]{0x38FFFFFF, 0x1AFFFFFF, 0x28FFFFFF},
                    new float[]{0f, 0.45f, 1f},
                    Shader.TileMode.CLAMP
            );
            fillPaint.setShader(fillShader);

            // Specular border reflection (gleaming top edge, soft bottom dispersion)
            Shader strokeShader = new LinearGradient(
                    0, bounds.top, bounds.width() * 0.3f, bounds.bottom,
                    new int[]{0x99FFFFFF, 0x33FFFFFF, 0x44FFFFFF},
                    new float[]{0f, 0.6f, 1f},
                    Shader.TileMode.CLAMP
            );
            strokePaint.setShader(strokeShader);
        }
    }

    @Override
    public void draw(@NonNull Canvas canvas) {
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, fillPaint);
        canvas.drawRoundRect(boundsF, cornerRadius, cornerRadius, strokePaint);
    }

    @Override
    public void setAlpha(int alpha) {
        fillPaint.setAlpha(alpha);
        invalidateSelf();
    }

    @Override
    public void setColorFilter(@Nullable ColorFilter colorFilter) {
        fillPaint.setColorFilter(colorFilter);
        invalidateSelf();
    }

    @Override
    public int getOpacity() {
        return PixelFormat.TRANSLUCENT;
    }
}
