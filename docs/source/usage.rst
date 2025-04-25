Usage
=====

This section demonstrates how to use the Interpolation-IITP library effectively. We'll cover each of the interpolation methods included in the package.

--------------------------

### Importing the Library

Firstly, let's import the necessary modules:

.. code-block:: python

    from interpolation_package.interpolation_methods import (
        linear_interpolation,
        nearest_neighbor_interpolation,
        lagrange_interpolation
    )
    import numpy as np

--------------------------

### Example 1: Linear Interpolation

Linear interpolation estimates values between two known points linearly.

.. code-block:: python

    # Define sample data
    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)

    # Point where we want to interpolate
    x_new = 3

    # Perform linear interpolation
    result = linear_interpolation(x, y, x_new)
    print(result)  # Output: Approximation of sin(3)

--------------------------

### Example 2: Nearest Neighbor Interpolation

Nearest neighbor interpolation selects the value of the nearest point to the target location.

.. code-block:: python

    # Same data as before
    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)

    # Another point for interpolation
    x_new = 5.5

    # Perform nearest neighbor interpolation
    result = nearest_neighbor_interpolation(x, y, x_new)
    print(result)  # Output: The exact value of the nearest point

--------------------------

### Example 3: Lagrange Interpolation

Lagrange interpolation fits a polynomial curve passing through all data points.

.. code-block:: python

    # Larger dataset
    x_large = np.arange(0, 10, 0.5)
    y_large = np.sin(x_large)

    # Point for interpolation
    x_query = 3.75

    # Perform Lagrange interpolation
    result = lagrange_interpolation(x_large, y_large, x_query)
    print(result)  # Output: Estimated value at x=3.75

--------------------------

### Tips for Better Results

- Ensure that your input data is well-ordered and free of inconsistencies.
- Choose the right interpolation method according to your problem domain.
- Consider preprocessing noisy data sets before applying interpolation.
