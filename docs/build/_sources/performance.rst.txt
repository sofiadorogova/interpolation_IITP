Performance Metrics
===================

This page compares the execution time of interpolation methods as the number of data points increases.

.. image:: images/performance_metrics.png
    :alt: Performance comparison of interpolation methods
    :width: 700px

**Analysis of results**:

- **Linear interpolation** demonstrates very fast performance even for large data sizes (linear complexity).
- **Nearest neighbor interpolation** shows moderate performance.
- **Lagrange interpolation** exhibits significant growth in execution time as the data size increases, making it computationally expensive for large data sets.

Thus, choose interpolation methods carefully depending on your dataset size and accuracy requirements.