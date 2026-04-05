$folder = 'E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE\PICTURE FOLDER\DEFECTS'

# Rename F-DEFECT*.JPG -> E-DEFECT*.JPG
Get-ChildItem -Path $folder -Filter 'F-DEFECT*.JPG' | ForEach-Object {
    $newName = $_.Name -replace '^F-DEFECT', 'E-DEFECT'
    Rename-Item -Path $_.FullName -NewName $newName
    Write-Host "Renamed: $($_.Name) -> $newName"
}
Write-Host "Done."
