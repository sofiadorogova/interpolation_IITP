API Reference
=============

.. currentmodule:: interpolation_package.interpolation_methods

This section provides an overview of the core functions within the ``interpolation_package`` module.

Overview of Functions
---------------------

Below are brief descriptions of each function:

- **linear_interpolation**: Performs linear interpolation between known data points.
- **nearest_neighbor_interpolation**: Estimates values by choosing the nearest known data point.
- **lagrange_interpolation**: Applies polynomial interpolation via Lagrange polynomials.

Detailed Descriptions
---------------------

Each function is described in detail below, along with examples.

Linear Interpolation
~~~~~~~~~~~~~~~~~~~~

**Purpose:**  
Performs linear interpolation between two known data points.

**Arguments:**

- **x**: Array of nodes where the function is defined.
- **y**: Corresponding function values at these nodes.
- **x_new**: New coordinate(s) where interpolation is required.

**Returns:**  
Interpolated value(s) at the specified coordinates.

**Example:**

.. code-block:: python

    import numpy as np
    from interpolation_package.interpolation_methods import linear_interpolation

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = linear_interpolation(x, y, x_new)
    print(result)  # Approximate sine value at x=3

Nearest Neighbor Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:**  
Determines interpolated values based on the nearest neighbor.

**Arguments:**

- **x**: Array of grid points.
- **y**: Function values at these points.
- **x_new**: Coordinate(s) for interpolation.

**Returns:**  
Value(s) from the nearest neighbor points.

**Example:**

.. code-block:: python

    import numpy as np
    from interpolation_package.interpolation_methods import nearest_neighbor_interpolation

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = nearest_neighbor_interpolation(x, y, x_new)
    print(result)  # Value from nearest point to x_new

Lagrange Interpolation
~~~~~~~~~~~~~~~~~~~~~~

**Purpose:**  
Applies polynomial interpolation using Lagrange polynomials.

**Arguments:**

- **x**: Grid points.
- **y**: Values of the function at these points.
- **x_new**: Coordinates where interpolation is required.

**Returns:**  
Interpolated values computed using Lagrange polynomials.

**Example:**

.. code-block:: python

    import numpy as np
    from interpolation_package.interpolation_methods import lagrange_interpolation

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = lagrange_interpolation(x, y, x_new)
    print(result)  # Interpolated value at x=3

Comparison Table
----------------

+-------------------------+------------------+-----------------------------------------+
| Method                  | Complexity       | Advantages                              |
+=========================+==================+=========================================+
| Linear Interpolation    | Low              | Fast computation                        |
+-------------------------+------------------+-----------------------------------------+
| Nearest Neighbor        | Medium           | Simple and intuitive                    |
+-------------------------+------------------+-----------------------------------------+
| Lagrange Polynomial     | High             | Accurate interpolation for small data   |
+-------------------------+------------------+-----------------------------------------+

Conclusion
----------

This API reference provides details to effectively use the interpolation methods provided by ``interpolation_package``. Choose a method according to your requirements on accuracy and performance.