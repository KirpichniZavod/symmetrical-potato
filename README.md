# Nedohacker Lite — безопасная пародия

Демо-проект для конкурса: безвредная имитация «вируса» с визуальными эффектами.

## Python (терминал, кроссплатформенно)

Запуск: 
```bash
python3 /workspace/prank_virus.py --gta6-installer --mode demo
```
Полезные флаги:
- `--auto-continue` — без ожиданий
- `--bsod-seconds 6` — длительность BSOD
- `--login-user Anubis --login-pass Nedohacker` — ожидаемые данные логина

## Windows WPF (красивый визуал)

Папка: `csharp/NedoClub.Wpf`

- Проект: `NedoClub.Wpf.csproj` (TargetFramework: net8.0-windows)
- Особенности:
  - Полноэкранный оверлей, окно без рамок, TopMost
  - «Инсталлер GTA6» → «Вирус» → фейковый BSOD
  - Блокировка попыток закрытия во время шоу (Alt+F4/ESC игнор)
  - Секретный выход: Ctrl+Alt+Shift+Q
  - Логин: Anubis / Пароль: Nedohacker

Сборка:
1. Установите .NET 8 SDK и Windows SDK
2. Откройте проект в Visual Studio (Windows) и запустите

Важно: проект НЕ вносит изменений в систему, автозапуск и т.п. — только визуал.