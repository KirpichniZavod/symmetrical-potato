using System;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Threading;

namespace NedoClub.Wpf;

public partial class MainWindow : Window
{
    private bool _lockdownEnabled;
    private readonly Random _random = new();

    public MainWindow()
    {
        InitializeComponent();
        BtnStartInstall.Click += async (_, __) => await RunInstallerAsync();
        BtnExit.Click += (_, __) => TryExit();
        BtnToBsod.Click += async (_, __) => await RunVirusAndBsodAsync();
        BtnLogin.Click += (_, __) => HandleLogin();
        this.PreviewKeyDown += MainWindow_PreviewKeyDown;
        this.Closing += (s, e) =>
        {
            if (_lockdownEnabled)
            {
                e.Cancel = true; // игнорируем закрытие
            }
        };
        InstallerStage.Text = "Готов к установке";
        InstallerSub.Text = "Nedohacker Social Ultra+";
    }

    private void MainWindow_PreviewKeyDown(object sender, KeyEventArgs e)
    {
        // Секретный выход: Ctrl+Alt+Shift+Q
        if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) &&
            (Keyboard.IsKeyDown(Key.LeftAlt) || Keyboard.IsKeyDown(Key.RightAlt)) &&
            (Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) &&
            e.Key == Key.Q)
        {
            _lockdownEnabled = false;
            TryExit();
            return;
        }

        if (_lockdownEnabled)
        {
            e.Handled = true; // блокируем Alt+F4, Esc и т.п.
        }
    }

    private void TryExit()
    {
        if (_lockdownEnabled)
        {
            InstallerSub.Text = "Режим защиты активен — выход заблокирован";
            return;
        }
        Application.Current.Shutdown();
    }

    private async Task RunInstallerAsync()
    {
        RootTabs.SelectedItem = TabInstaller;
        BtnStartInstall.IsEnabled = false;
        InstallerSub.Text = "Запуск установщика GTA6…";

        string[] stages =
        {
            "Проверка лицензии Rockstar",
            "Распаковка архивов",
            "Установка компонентов DirectX",
            "Оптимизация под RTX",
            "Создание ярлыка на рабочем столе",
            "Добавление в автозапуск (шутка!)",
            "Финальная проверка"
        };

        for (int i = 0; i < stages.Length; i++)
        {
            InstallerStage.Text = stages[i];
            await AnimateProgressBar(InstallerProgress, i * 100 / stages.Length, (i + 1) * 100 / stages.Length, 900);
            InstallerSub.Text = RandomJoke();
        }

        InstallerStage.Text = "Установка завершена!";
        InstallerSub.Text = "Запуск GTA6… шутка ;)";
        await Task.Delay(600);
        await RunVirusAndBsodAsync();
    }

    private async Task RunVirusAndBsodAsync()
    {
        RootTabs.SelectedItem = TabVirus;
        _lockdownEnabled = true;
        InstallerSub.Text = "Режим защиты активирован";

        await AnimateProgressBar(VirusProgress, 0, 100, 1600);
        await Task.Delay(300);
        RootTabs.SelectedItem = TabBsod;
        await AnimateProgressBar(BsodBar, 0, 100, 2500);
        await Task.Delay(800);
        _lockdownEnabled = false; // после шоу снимаем блок
    }

    private async Task AnimateProgressBar(ProgressBar bar, int from, int to, int durationMs)
    {
        var sw = System.Diagnostics.Stopwatch.StartNew();
        while (sw.ElapsedMilliseconds < durationMs)
        {
            double t = sw.ElapsedMilliseconds / (double)durationMs;
            int val = (int)(from + (to - from) * EaseOutCubic(t));
            bar.Dispatcher.Invoke(() => bar.Value = val, DispatcherPriority.Background);
            await Task.Delay(15);
        }
        bar.Dispatcher.Invoke(() => bar.Value = to, DispatcherPriority.Background);
    }

    private static double EaseOutCubic(double t)
    {
        t = Math.Clamp(t, 0, 1);
        return 1 - Math.Pow(1 - t, 3);
    }

    private string RandomJoke()
    {
        string[] jokes =
        {
            "Ваня, что ты сделал?",
            "Костян, не замазывай по братски.",
            "Антиобход активирован: Alt+F4 детектед — шутка!",
            "Добавление в автозапуск… да шучу я! Ничего не добавляем.",
            "Калибруем флюкс-капаситор… почти готово.",
            "Синхронизация с Матрицей… Ложки не существует.",
        };
        return jokes[_random.Next(jokes.Length)];
    }

    private void HandleLogin()
    {
        var user = TxtUser.Text.Trim();
        var pass = PwdPass.Password;
        if (user.Equals("Anubis", StringComparison.OrdinalIgnoreCase) && pass == "Nedohacker")
        {
            LoginOverlay.Visibility = Visibility.Collapsed;
            return;
        }
        LoginHint.Visibility = Visibility.Visible;
        LoginHint.Text = _random.Next(2) == 0 ? "Ваня, что ты сделал?" : "Костян, не замазывай по братски.";
    }
}