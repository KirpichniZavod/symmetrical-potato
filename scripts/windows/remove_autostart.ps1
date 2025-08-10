param(
  [string]$ShortcutName = "Nedohacker Lite"
)

$startup = [Environment]::GetFolderPath('Startup')
$lnk = Join-Path $startup ("{0}.lnk" -f $ShortcutName)

if (Test-Path $lnk) {
  Remove-Item $lnk -Force
  Write-Host "Удалён ярлык автозагрузки: $lnk"
} else {
  Write-Host "Ярлык не найден: $lnк"
}