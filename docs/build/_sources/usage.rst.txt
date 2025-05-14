Usage
=====

This section demonstrates how to use the Interpolation-IITP library effectively. We'll cover each of the interpolation methods included in the package, along with their mathematical formulations.

Importing the Library
----------------------

Firstly, let's import the necessary modules:

.. code-block:: python

    from interpolation_package.interpolation_methods import (
        linear_interpolation,
        nearest_neighbor_interpolation,
        lagrange_interpolation
    )
    import numpy as np

Interpolation CLI Usage
-----------------------

The Interpolation-IITP library provides command-line interface (CLI) tools for convenience.

.. click:: interpolation_package.cli_interpolation:main
   :prog: interp-demo

Linear Interpolation
--------------------

Linear interpolation estimates values between two known points linearly. The interpolation formula is:

.. math::

    y = y_i + \frac{(x - x_i)}{(x_{i+1} - x_i)} \cdot (y_{i+1} - y_i)

**Example:**

.. code-block:: python

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3

    result = linear_interpolation(x, y, x_new)
    print(result)  # Approximation of sin(3)

Nearest Neighbor Interpolation
------------------------------

Nearest neighbor interpolation selects the value of the nearest known data point. Formally, it can be defined as:

.. math::

    y = y_i,\quad \text{where}\quad |x - x_i| = \min_j |x - x_j|

**Example:**

.. code-block:: python

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 5.5

    result = nearest_neighbor_interpolation(x, y, x_new)
    print(result)  # The exact value of the nearest point

Lagrange Interpolation
----------------------

Lagrange interpolation fits a polynomial curve passing through all data points. The general formula is:

.. math::

    L(x) = \sum_{j=0}^{n-1} y_j \cdot \ell_j(x),\quad\text{where}\quad
    \ell_j(x) = \prod_{\substack{0 \le m \le n-1 \\ m \neq j}} 
    \frac{x - x_m}{x_j - x_m}

**Example:**

.. code-block:: python

    x_large = np.arange(0, 10, 0.5)
    y_large = np.sin(x_large)
    x_query = 3.75

    result = lagrange_interpolation(x_large, y_large, x_query)
    print(result)  # Estimated value at x=3.75

Comparison of Interpolation Methods
-----------------------------------

The following image demonstrates a visual comparison of linear, nearest neighbor, and Lagrange interpolation methods applied to the sine function:

.. image:: /images/interpolation_comparison.png
    :alt: Comparison of interpolation methods
    :width: 700px

- **Linear Interpolation:** Quick, piecewise-linear approximation.
- **Nearest Neighbor Interpolation:** Stepwise, simple, efficient for discrete data.
- **Lagrange Interpolation:** Smooth polynomial approximation, accurate but may oscillate significantly between points.