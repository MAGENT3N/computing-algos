# Computing / Algorithms

A collection of implementations in scientific computing, 
signal processing, and numerical methods.

---

## DFT (Discrete Fourier Transform)

**File:** `dft_slow.py`  
**What it does:** Naive O(n²) implementation of the Discrete Fourier Transform. Basicall
**Concepts** Computing the sum -$$X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-j2\pi kn/N}$$
**Note:** Intentionally slow/naive — FFT implementation coming soon for comparison.

---

## Grapher Utility

**File:** `grapher.py`  
**What it does:** Helper functions for plotting — wraps matplotlib,plot multiple graphs
with the help of a custom plot_multiple_graphs function
to make generating graphs quicker and cleaner.  
**Used by:** DFT and future projects in this repo.

---

## Notes
Each implementation is standalone
