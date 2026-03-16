Add-Type -AssemblyName System.Drawing

# Load the SVG as a bitmap by rendering it via WebBrowser (use System.Drawing directly for a circle)
# We'll draw a simple 32x32 red circle favicon to match Zealet's red circle brand mark

$sizes = @(32, 192, 512)

foreach ($size in $sizes) {
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $g   = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.Clear([System.Drawing.Color]::Transparent)

    # Red filled circle
    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 190, 19, 25))
    $g.FillEllipse($brush, 0, 0, $size, $size)

    # White "Z" text
    $font  = New-Object System.Drawing.Font("Arial", ($size * 0.5), [System.Drawing.FontStyle]::Bold)
    $white = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $fmt   = New-Object System.Drawing.StringFormat
    $fmt.Alignment = [System.Drawing.StringAlignment]::Center
    $fmt.LineAlignment = [System.Drawing.StringAlignment]::Center
    $rect  = New-Object System.Drawing.RectangleF(0, 0, $size, $size)
    $g.DrawString("Z", $font, $white, $rect, $fmt)

    $g.Dispose()

    $outPath = "E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE\assets\img\favicon-$size.png"
    $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    Write-Host "Created: favicon-$size.png"
}

# Copy 32px as the default favicon.png
Copy-Item "E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE\assets\img\favicon-32.png" `
          "E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE\assets\img\favicon.png" -Force
Write-Host "Done."
