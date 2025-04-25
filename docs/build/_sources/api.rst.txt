API Reference
=============

.. currentmodule:: interpolation_package.interpolation_methods

This section provides an overview of the core components within the ``interpolation_package`` module, including its primary functions used for different types of interpolations.

-------------------------------

*Overview of Functions*

Below are brief introductions to each function provided by the module:

- **linear_interpolation**: Performs linear interpolation between known data points.
- **nearest_neighbor_interpolation**: Uses the closest neighboring point to estimate values.
- **lagrange_interpolation**: Applies polynomial-based interpolation via Lagrange polynomials.

---------------------------------

*Detailed Descriptions*

Each function will be described in detail below, along with examples illustrating their typical uses.

---

*1. Function: linear_interpolation*

**Purpose:**  
Provides linear interpolation between two given points based on input coordinates and corresponding values.

**Arguments:**  

- **x**: An array of nodes where the function is defined.

- **y**: Corresponding function values at those nodes.

- **x_new**: New coordinate(s) where we want to interpolate.

**Returns:**  
Interpolated value(s) at specified coordinates.

**Example Use Case:**  

.. code-block:: python

    from interpolation_package.interpolation_methods import linear_interpolation
    import numpy as np

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = linear_interpolation(x, y, x_new)
    print(result)  # Output: Approximate sine value at x=3

---

*2. Function: nearest_neighbor_interpolation*

**Purpose:**  
Selects the nearest neighbor node to determine interpolated values.

**Arguments:**  

- **x**: Array of nodes representing the grid points.

- **y**: Function values at these nodes.

- **x_new**: Coordinates for which we need interpolated values.

**Returns:**  
Value(s) obtained through selecting the nearest neighbors.

**Example Use Case:**  

.. code-block:: python from interpolation_package.interpolation_methods import nearest_neighbor_interpolation
    import numpy as np

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = nearest_neighbor_interpolation(x, y, x_new)
    print(result)  # Output: Value from the nearest point to x_new

---

*3. Function: lagrange_interpolation*

**Purpose:**  
Applies Lagrange polynomial interpolation over multiple data points.

**Arguments:**  

- **x**: Grid points where the function is evaluated.

- **y**: Values of the function at these grid points.

- **x_new**: Points where we seek interpolated values.

**Returns:**  
Values computed using Lagrange polynomials.

**Example Use Case:**  

.. code-block:: python

    from interpolation_package.interpolation_methods import lagrange_interpolation
    import numpy as np

    x = np.array([0, 2, 4, 6, 8, 10])
    y = np.sin(x)
    x_new = 3
    result = lagrange_interpolation(x, y, x_new)
    print(result)  # Output: Interpolated value using Lagrange polynomials

---

*Comparison Table*

+-------------------------+------------------+----------------------------------------+
| Method                  | Complexity       | Advantages                             |
+=========================+==================+========================================+
| Linear Interpolation    | Low              | Fast computation                       |
+-------------------------+------------------+----------------------------------------+
| Nearest Neighbor        | Medium           | Simple implementation                   |
+-------------------------+------------------+----------------------------------------+
| Lagrange Polynomial     | High             | More accurate results when needed       |
+-------------------------+------------------+----------------------------------------+

---

*Conclusion*

This API reference covers the essential details required to effectively utilize the various interpolation techniques offered by the ``interpolation_package``. Users should choose the appropriate technique depending on desired accuracy and computational efficiency.