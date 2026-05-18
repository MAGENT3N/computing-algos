# Computing / Algorithms

A collection of implementations in scientific computing,
signal processing, and numerical methods.

---

## Implementations

| File | Topic | Description |
|------|-------|-------------|
| `dft_slow.py` | Signal Processing | Naive O(n²) DFT implementation |
| `grapher.py` | Utility | Plotting helper — used across projects |
| `fast_fib.py` | Algorithms | Fast Fibonacci implementation |
| `gradient_descent.py` | Optimization | Gradient descent from scratch |
| `monte_carlo_integration.py` | Numerical Methods | Monte Carlo integration |
| `rk4.py` | Numerical Methods | Runge-Kutta 4th order ODE solver |
| `naive_peak_finder.py` | Algorithms | Naive peak finding algorithm |
| `fraction_class.py` | Data Structures | Fraction class implementation |

---

## DFT (Discrete Fourier Transform)

**File:** `dft_slow.py`  
**Concepts:** Signal Processing, Frequency Domain Analysis  
**What it does:** Naive O(n²) implementation of the Discrete Fourier Transform.
Computes the inner product of the signal x(n) with sinusoids at each frequency
k = 0, 1, ..., N-1:
Equation - X(k) = sum of x(n) * e^(-j2πkn/N) for n = 0 to N-1

**Note:** Intentionally naive — FFT implementation coming soon for direct speed comparison.

---

## Grapher Utility

**File:** `grapher.py`  
**What it does:** Wraps matplotlib to simplify plotting. Provides a
`plot_multiple_graphs()` function to plot multiple graphs cleanly in one call.  
**Used by:** All projects in this repo that require visualization.

---

## Coming Soon
- FFT implementation and benchmarking against naive DFT

---

*Each implementation is standalone. `grapher.py` is a shared utility.*
