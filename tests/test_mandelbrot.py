import subprocess
import sys

import pytest

from mandelbrot import render


def test_render_has_requested_dimensions():
    output = render(width=12, height=5)

    rows = output.splitlines()
    assert len(rows) == 5
    assert all(len(row) == 12 for row in rows)


def test_render_distinguishes_set_from_escaped_points():
    assert render(width=3, height=1, max_iterations=10) == "@@:"


@pytest.mark.parametrize(
    ("width", "height", "max_iterations"),
    [(0, 5, 10), (5, 0, 10), (5, 5, 0)],
)
def test_render_rejects_nonpositive_parameters(width, height, max_iterations):
    with pytest.raises(ValueError):
        render(width, height, max_iterations)


def test_module_cli_renders_requested_size():
    result = subprocess.run(
        [sys.executable, "-m", "mandelbrot", "--width", "8", "--height", "3"],
        check=True,
        capture_output=True,
        text=True,
    )

    rows = result.stdout.splitlines()
    assert len(rows) == 3
    assert all(len(row) == 8 for row in rows)