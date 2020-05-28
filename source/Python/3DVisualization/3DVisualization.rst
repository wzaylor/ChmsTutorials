.. _Python3DVisualization:

=================================
Python 3D Visualization Tutorials
=================================
This set of tutorials describes how to create 3D visualizations and use the same visualization tools to assist in model generation.

These tutorials will start with simple examples, then build upon those examples to demonstrate practical uses of the visualization tools. The code is written in a way to demonstrate the operations that are used. Users are encouraged to use the examples to develop functions and classes that fit their needs.

.. image:: /Python/3DVisualization/img/KneeModelLigament_GUI.png
   :width: 300px


The tutorials below show the basics of creating a visualization. The :ref:`Python3DVisualizationPreliminary` tutorial describes what software needs to be installed before proceeding. The :ref:`Python3DVisualizationRenderWindow` tutorial shows the basic code that will be used in every visualization tutorial, and the :ref:`Python3DVisualizationCoordinateAxes` tutorial demonstrates a basic visualization workflow.

.. toctree::
    :maxdepth: 1
    :caption: Basic tutorials:

    /Python/3DVisualization/Preliminary.rst
    /Python/3DVisualization/RenderWindow.rst
    /Python/3DVisualization/CoordinateAxes.rst
    /Python/3DVisualization/Sphere.rst

The tutorials below show how to work with geometry that you may use for biomechanics work. This geometry includes surfaces and finite element meshes for bones, ligaments, cartilage, etc. For these tutorials, we will use surfaces and finite element meshes that are available. The geometry will come from the `OpenKnee(s) <https://simtk.org/projects/openknee>`_ project.

.. toctree::
    :maxdepth: 1
    :caption: Load geometry tutorials:

    /Python/3DVisualization/LoadStlSurface.rst
    /Python/3DVisualization/ManuallyCreatePolydata.rst