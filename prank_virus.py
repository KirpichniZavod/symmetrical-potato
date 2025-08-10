#!/usr/bin/env python3

import argparse
import random
import signal
import sys
import time
import shutil
from typing import List, Tuple


class Ansi:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"


def fullscreen_splash(text: str, wait_for_enter: bool) -> None:
    # Очистить экран и вывести текст примерно по центру
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    cols, rows = shutil.get_terminal_size(fallback=(80, 24))
    lines = text.splitlines()
    centered = []
    for line in lines:
        visible = line
        if len(visible) > cols:
            visible = visible[:cols]
        pad = max(0, (cols - len(visible)) // 2)
        centered.append(" " * pad + visible)
    top_pad = max(0, (rows - len(centered)) // 2)
    print("\n" * top_pad + "\n".join(centered))
    if wait_for_enter and sys.stdin.isatty():
        print()
        try:
            input(f"{Ansi.DIM}Нажмите Enter, чтобы продолжить…{Ansi.RESET}")
        except EOFError:
            # Если нет TTY — просто продолжаем
            pass


def print_banner() -> None:
    lines = [
        f"{Ansi.MAGENTA}{Ansi.BOLD}╔══════════════════════════════════════════════╗{Ansi.RESET}",
        f"{Ansi.MAGENTA}{Ansi.BOLD}║     ДРУЖЕЛЮБНЫЙ ПАРОДИЙНЫЙ 'ВИРУС' :)       ║{Ansi.RESET}",
        f"{Ansi.MAGENTA}{Ansi.BOLD}╠══════════════════════════════════════════════╣{Ansi.RESET}",
        f"{Ansi.YELLOW} Это безвредная шутка. Никаких файлов не трогаем,{Ansi.RESET}",
        f"{Ansi.YELLOW} ничего не шифруем, ничего никуда не отправляем.{Ansi.RESET}",
        f"{Ansi.GRAY} Только текст, прогресс-бары и позитив!{Ansi.RESET}",
        f"{Ansi.MAGENTA}{Ansi.BOLD}╚══════════════════════════════════════════════╝{Ansi.RESET}",
    ]
    for line in lines:
        print(line)
    print()


def handle_interrupt(signum, frame):
    print(f"\n{Ansi.GREEN}{Ansi.BOLD}Супергерой нажал Ctrl+C — зло повержено!{Ansi.RESET}")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


def spinner_frames() -> List[str]:
    return ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


def format_progress_bar(percent: int, width: int = 28) -> str:
    filled = int(width * percent / 100)
    return f"[{'#' * filled}{'.' * (width - filled)}] {percent:3d}%"


def stage_messages(stage_name: str) -> List[Tuple[int, str]]:
    pool = [
        (7, "Обнаружен кот в коробке Шрёдингера. Оставляем в покое."),
        (13, "Оптимизируем добро. Зло не прошло проверку качества."),
        (19, "Антиобход активирован: Alt+F4 детектед — шутка!"),
        (23, "Ваня, что ты сделал?"),
        (27, "Поиск мемов с котиками… Найдено: достаточно."),
        (33, "Костян, не замазывай по братски."),
        (42, "Ответ на жизнь, Вселенную и всё остальное: 42."),
        (54, "Добавление в автозапуск… да шучу я! Ничего не добавляем."),
        (69, "Синхронизация с Матрицей… Ложки не существует."),
        (88, "Калибруем флюкс-капаситор… почти готово."),
        (96, "Финальная полировка байтов до блеска ✨"),
    ]
    random.shuffle(pool)
    chosen = sorted(pool[:4], key=lambda x: x[0])
    chosen.insert(0, (3, f"Начало этапа: {stage_name}"))
    chosen.append((97, f"Этап '{stage_name}' успешно завершён"))
    return chosen


def run_stage(stage_name: str, duration_seconds: float) -> None:
    frames = spinner_frames()
    tips = stage_messages(stage_name)
    tip_index = 0

    start_time = time.time()
    end_time = start_time + max(duration_seconds, 0.1)

    last_percent_shown = -1
    frame_index = 0
    while True:
        now = time.time()
        remaining = end_time - now
        if remaining <= 0:
            percent = 100
        else:
            elapsed = now - start_time
            percent = int(max(0.0, min(100.0, (elapsed / (end_time - start_time)) * 100)))

        if tip_index < len(tips) and percent >= tips[tip_index][0]:
            print(f"\n{Ansi.CYAN}{tips[tip_index][1]}{Ansi.RESET}")
            tip_index += 1

        if percent != last_percent_shown:
            bar = format_progress_bar(percent)
            spin = frames[frame_index % len(frames)]
            sys.stdout.write(f"\r {Ansi.BLUE}{spin}{Ansi.RESET} {bar}  {Ansi.DIM}{stage_name}{Ansi.RESET}")
            sys.stdout.flush()
            last_percent_shown = percent

        if percent >= 100:
            break

        frame_index += 1
        time.sleep(0.05)

    sys.stdout.write("\n")
    sys.stdout.flush()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Безвредная пародия на 'вирус': анимации и шутки без действий с системой",
    )
    parser.add_argument(
        "--mode",
        choices=["demo", "medium", "epic"],
        default="demo",
        help="Скорость и длительность шоу: demo (коротко), medium, epic (подлиннее)",
    )
    parser.add_argument(
        "--gta6-installer",
        action="store_true",
        help="Включить режим фальшивого инсталлятора GTA6 (чисто визуально)",
    )
    parser.add_argument(
        "--password",
        type=str,
        default=None,
        help="Попросить ввести пароль перед запуском (для шутки). Если неверный — всё равно продолжим.",
    )
    parser.add_argument(
        "--auto-continue",
        action="store_true",
        help="Автоматически пройти заставку без ожидания Enter (удобно для демо/скриптов)",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Отключить ANSI-цвета",
    )
    return parser.parse_args()


def maybe_disable_colors(no_color: bool) -> None:
    if not sys.stdout.isatty() or no_color:
        for attr in [a for a in dir(Ansi) if a.isupper()]:
            setattr(Ansi, attr, "")


def prompt_password_if_needed(expected: str | None) -> None:
    if not expected:
        return
    if not sys.stdin.isatty():
        print(f"{Ansi.DIM}(Нет TTY) Пропускаем ввод пароля. Это же шутка!{Ansi.RESET}")
        return
    attempts_left = 3
    while attempts_left > 0:
        try:
            user = input(f"Введите пароль для продолжения: ")
        except EOFError:
            print(f"{Ansi.DIM}Не удалось прочитать ввод. Продолжаем ради шоу.{Ansi.RESET}")
            return
        if user == expected:
            print(f"{Ansi.GREEN}Верно! Добро пожаловать в безопасную пародию.{Ansi.RESET}")
            return
        attempts_left -= 1
        if attempts_left == 2:
            print(f"{Ansi.YELLOW}Ваня, что ты сделал? Пароль не подходит.{Ansi.RESET}")
        elif attempts_left == 1:
            print(f"{Ansi.YELLOW}Костян, не замазывай по братски — снова мимо.{Ansi.RESET}")
        else:
            print(f"{Ansi.MAGENTA}Ладно, в честь конкурса пустим без пароля :) {Ansi.RESET}")
            return


def main() -> None:
    args = parse_args()
    maybe_disable_colors(args.no_color)

    warning_text = (
        f"{Ansi.RED}{Ansi.BOLD}ЭТА ПРОГРАММА МОЖЕТ ПРИНЕСТИ ВРЕД ИЛИ УСЛОЖНИТЬ ИСПОЛЬЗОВАНИЕ ПК!{Ansi.RESET}\n"
        f"{Ansi.YELLOW}{Ansi.BOLD}СТРОГО ДЛЯ КАНАЛА Nedohacker lite.{Ansi.RESET}\n"
        f"{Ansi.BOLD}Я вас предупрдил!{Ansi.RESET}\n\n"
        f"{Ansi.GRAY}(На самом деле это безопасная пародия: ничего не меняем в системе){Ansi.RESET}"
    )

    fullscreen_splash(warning_text, wait_for_enter=not args.auto_continue)
    print_banner()

    prompt_password_if_needed(args.password)

    if args.gta6_installer:
        stages = [
            ("Запуск установщика GTA6", 1.6 if args.mode == "demo" else 2.2 if args.mode == "medium" else 3.0),
            ("Проверка лицензии Rockstar", 1.4 if args.mode == "demo" else 2.0 if args.mode == "medium" else 2.6),
            ("Распаковка архивов", 1.6 if args.mode == "demo" else 2.2 if args.mode == "medium" else 3.0),
            ("Установка компонентов DirectX", 1.5 if args.mode == "demo" else 2.1 if args.mode == "medium" else 2.8),
            ("Оптимизация под RTX", 1.4 if args.mode == "demo" else 2.0 if args.mode == "medium" else 2.6),
            ("Создание ярлыка на рабочем столе", 1.2 if args.mode == "demo" else 1.8 if args.mode == "medium" else 2.4),
            ("Добавление в автозапуск (шутка!)", 1.0 if args.mode == "demo" else 1.4 if args.mode == "medium" else 2.0),
            ("Финальная проверка", 1.0 if args.mode == "demo" else 1.4 if args.mode == "medium" else 2.0),
        ]
    else:
        modes = {
            "demo": [
                ("Сканирование улыбок", 1.2),
                ("Квантовое добрение байтов", 1.4),
                ("Шифрование позитива", 1.3),
                ("Надёжное восстановление хорошего настроения", 1.2),
            ],
            "medium": [
                ("Сканирование улыбок", 2.0),
                ("Квантовое добрение байтов", 2.5),
                ("Шифрование позитива", 2.2),
                ("Надёжное восстановление хорошего настроения", 2.0),
            ],
            "epic": [
                ("Сканирование улыбок", 3.0),
                ("Квантовое добрение байтов", 3.5),
                ("Шифрование позитива", 3.2),
                ("Надёжное восстановление хорошего настроения", 3.0),
            ],
        }
        stages = modes.get(args.mode, modes["demo"])

    print(f"{Ansi.BOLD}{Ansi.GREEN}Инициализация системы дружелюбия…{Ansi.RESET}")
    time.sleep(0.4)
    print(f"{Ansi.DIM}Совет: Нажмите Ctrl+C, чтобы героически спасти мир в любой момент.{Ansi.RESET}\n")

    for stage_name, duration in stages:
        run_stage(stage_name, duration)

    print()
    if args.gta6_installer:
        print(f"{Ansi.GREEN}{Ansi.BOLD}Установка завершена! Запуск GTA6… шутка ;) {Ansi.RESET}")
    else:
        print(f"{Ansi.GREEN}{Ansi.BOLD}Миссия выполнена! Все байты счастливы, а вы — молодец!{Ansi.RESET}")
    print(f"{Ansi.GRAY}P.S. Это была пародия. Ни один файл не пострадал.\n{Ansi.RESET}")


if __name__ == "__main__":
    main()