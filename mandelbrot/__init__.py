"""Render the Mandelbrot set as ASCII art."""

__version__ = "0.1.0"

_SHADES = " .:-=+*#%@"


def render(width: int = 80, height: int = 24, max_iterations: int = 100) -> str:
	"""Return an ASCII rendering of the Mandelbrot set."""
	if width < 1 or height < 1:
		raise ValueError("width and height must be positive")
	if max_iterations < 1:
		raise ValueError("max_iterations must be positive")

	x_min, x_max = -2.0, 1.0
	y_span = (x_max - x_min) * height * 2 / width
	y_min, y_max = -y_span / 2, y_span / 2
	rows = []

	for row in range(height):
		imaginary = (
			0.0
			if height == 1
			else y_max - row * (y_max - y_min) / (height - 1)
		)
		line = []
		for column in range(width):
			real = (
				(x_min + x_max) / 2
				if width == 1
				else x_min + column * (x_max - x_min) / (width - 1)
			)
			z = 0j
			point = complex(real, imaginary)
			for iteration in range(max_iterations):
				z = z * z + point
				if z.real * z.real + z.imag * z.imag > 4:
					break
			else:
				iteration = max_iterations - 1

			shade_index = iteration * (len(_SHADES) - 1) // max(max_iterations - 1, 1)
			line.append(_SHADES[shade_index])
		rows.append("".join(line))

	return "\n".join(rows)


__all__ = ["render"]
