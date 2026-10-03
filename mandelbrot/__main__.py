"""Command-line interface for the ASCII Mandelbrot renderer."""

import argparse

from mandelbrot import render


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the Mandelbrot set as ASCII art.")
    parser.add_argument("--width", type=int, default=80, help="output width in characters")
    parser.add_argument("--height", type=int, default=24, help="output height in rows")
    parser.add_argument("--iterations", type=int, default=100, help="maximum iterations per point")
    args = parser.parse_args()

    try:
        print(render(args.width, args.height, args.iterations))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()