Installation
============

There are several ways to install the Interpolation-IITP library. We recommend installing via **Poetry**, but other options are also supported.

Using Poetry
------------

If you have **Poetry** already installed, simply clone the repository and navigate to the root folder:

.. code-block:: console

    git clone https://github.com/your_username/interpolation_iitp.git
    cd interpolation_iitp

Then install the package directly:

.. code-block:: console

    poetry install

Alternative Methods
-------------------

Alternatively, you may install the library manually using **pip**:

.. code-block:: console

    pip install interpolation-iitp

However, note that manual installations might require additional configuration for dependency management.

Verifying Installation
----------------------

Once installed, verify everything works correctly by running:

.. code-block:: python

    >>> import interpolation_package
    >>> print(interpolation_package.__version__)