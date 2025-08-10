param(
  [Parameter(Mandatory=$true)]
  [string]$ExePath,
  [string]$ShortcutName = "Nedohacker Lite"
)

# Пример: ./install_autostart.ps1 -ExePath "C:\\Path\\To\\NedoClub.Wpf.exe"

$startup = [Environment]::GetFolderPath('Startup')
if (-not (Test-Path $ExePath)) {
  Write-Error "ExePath не найден: $ExePath"
  exit 1
}

$lnk = Join-Path $startup ("{0}.lnk" -f $ShortcutName)

$wsh = New-Object -ComObject WScript.Shell
$shortcut = $wsh.CreateShortcut($lnk)
$shortcut.TargetPath = $ExePath
$shortcut.WorkingDirectory = [System.IO.Path]::GetDirectoryName($ExePath)
$shortcut.Description = "Запуск Nedohacker Lite на старте Windows"
$shortcut.Save()

Write-Host "Создан ярлык автозагрузки: $lnk"