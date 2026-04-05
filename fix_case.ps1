$folder = 'E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE\PICTURE FOLDER\DEFECTS'

Get-ChildItem -Path $folder -Filter '*.jpg' | ForEach-Object {
    $newName = [System.IO.Path]::GetFileNameWithoutExtension($_.Name) + '.JPG'
    $dest = Join-Path $folder $newName
    # Use a temp name to avoid case-insensitive clash on Windows
    $tmp = Join-Path $folder ($_.BaseName + '_tmp.JPG')
    Rename-Item -Path $_.FullName -NewName $tmp
    Rename-Item -Path $tmp -NewName $newName
    Write-Host "Renamed: $($_.Name) -> $newName"
}
Write-Host "Done."
