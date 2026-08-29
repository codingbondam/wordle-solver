#!/usr/bin/env python3
"""Print the Fibonacci series."""

import sys


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(", ".join(str(n) for n in fibonacci(count)))


if __name__ == "__main__":
    main()
