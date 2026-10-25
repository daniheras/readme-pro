#!/usr/bin/env python3
"""pomo — a tiny terminal pomodoro timer with no dependencies."""

import argparse
import time


def run_cycle(label: str, minutes: int) -> None:
    total = minutes * 60
    print(f"\n--- {label}: {minutes} min ---")
    while total:
        m, s = divmod(total, 60)
        print(f"\r{m:02d}:{s:02d} remaining ({label})", end="", flush=True)
        time.sleep(1)
        total -= 1
    print(f"\r{label} done!" + " " * 12, flush=True)


def main() -> int:
    p = argparse.ArgumentParser(description="Terminal pomodoro timer.")
    p.add_argument("--work", type=int, default=25, help="work block length in minutes (default 25)")
    p.add_argument("--break-min", type=int, default=5, help="break length in minutes (default 5)")
    p.add_argument("--cycles", type=int, default=4, help="work/break cycles before stopping (default 4)")
    args = p.parse_args()

    print(f"pomo: {args.cycles} cycles of {args.work}m work / {args.break_min}m break. Ctrl-C to stop.")
    try:
        for cycle in range(1, args.cycles + 1):
            run_cycle(f"cycle {cycle}/{args.cycles} work", args.work)
            if cycle < args.cycles:
                run_cycle(f"cycle {cycle}/{args.cycles} break", args.break_min)
    except KeyboardInterrupt:
        print("\nstopped.")
        return 130
    print("all cycles complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
