#!/usr/bin/env python3

import argparse
import random
import signal
import sys
import time
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
        (27, "Поиск мемов с котиками… Найдено: достаточно."),
        (42, "Ответ на жизнь, Вселенную и всё остальное: 42."),
        (69, "Синхронизация с Матрицей… Ложки не существует."),
        (88, "Калибруем флюкс-капаситор… почти готово."),
        (96, "Финальная полировка байтов до блеска ✨"),
    ]
    random.shuffle(pool)
    # Возьмём 3 случайных сообщения для разнообразия
    chosen = sorted(pool[:3], key=lambda x: x[0])
    # Вставим вступительное
    chosen.insert(0, (3, f"Начало этапа: {stage_name}"))
    # И заключительное
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
            # Печатаем подсказку на новой строке
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

    # Закрываем строку прогресса
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
        "--no-color",
        action="store_true",
        help="Отключить ANSI-цвета",
    )
    return parser.parse_args()


def maybe_disable_colors(no_color: bool) -> None:
    if not sys.stdout.isatty() or no_color:
        # Заменяем коды на пустые строки
        for attr in [a for a in dir(Ansi) if a.isupper()]:
            setattr(Ansi, attr, "")


def main() -> None:
    args = parse_args()
    maybe_disable_colors(args.no_color)

    print_banner()

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
    print(f"{Ansi.GREEN}{Ansi.BOLD}Миссия выполнена! Все байты счастливы, а вы — молодец!{Ansi.RESET}")
    print(f"{Ansi.GRAY}P.S. Это была пародия. Ни один файл не пострадал.\n{Ansi.RESET}")


if __name__ == "__main__":
    main()