# ASCII Mandelbrot

Render the Mandelbrot set in your terminal using only the Python standard library.

```sh
python -m mandelbrot
```

Set the output size and iteration limit with options:

```sh
python -m mandelbrot --width 100 --height 30 --iterations 150
```

Install the pytest test dependency and run the test suite with:

```sh
python -m pip install -e '.[test]'
python -m pytest
```

The renderer is also available as `mandelbrot.render(width, height, max_iterations)`.
