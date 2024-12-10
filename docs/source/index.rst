.. MyCProject documentation master file, created by
   sphinx-quickstart on Fri Dec  6 19:42:32 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MyCProject's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

C API Documentation
===================
.. autodoxygenindex::
   :project: MyCProject

.. doxygenfile:: main.c
   :project: MyCProject

.. doxygenfile:: math_operations.c
   :project: MyCProject
