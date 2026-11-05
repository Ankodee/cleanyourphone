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
    private final RectF boundsF = new RectF();
    private float cornerRadius = 60f;

    public LiquidGlassDrawable(float cornerRadius) {
        this.cornerRadius = cornerRadius;
        strokePaint.setStyle(Paint.Style.STROKE);
        strokePaint.setStrokeWidth(2.5f);
        strokePaint.setColor(0x66FFFFFF); // 40% translucent specular white
    }

    @Override
    protected void onBoundsChange(@NonNull Rect bounds) {
        super.onBoundsChange(bounds);
        boundsF.set(bounds);
        if (bounds.height() > 0) {
            // Liquid frosted glass vertical gradient
            Shader fillShader = new LinearGradient(
                    0, bounds.top, 0, bounds.bottom,
                    new int[]{0x45FFFFFF, 0x22FFFFFF, 0x30FFFFFF},
                    new float[]{0f, 0.5f, 1f},
                    Shader.TileMode.CLAMP
            );
            fillPaint.setShader(fillShader);

            // Specular border gradient (lighter at top edge like light hitting glass)
            Shader strokeShader = new LinearGradient(
                    0, bounds.top, 0, bounds.bottom,
                    new int[]{0x80FFFFFF, 0x33FFFFFF},
                    null,
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
