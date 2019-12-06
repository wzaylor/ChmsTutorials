.. _Python3DVisualizationSphere:

======
Sphere
======
Purpose
'''''''
This tutorial demonstrates one way to create general shapes using *VTK*. General shapes can be generated using a *VTK* class that generates a specific type of geometry (generally called a *source*). This class can be used to generate *polydata* which is a general 3D object.

This example will keep the coordinate axes from the :ref:`coordinate axes example<Python3DVisualizationCoordinateAxes>`, but it will also add a sphere with a radius of ``1.2``, and place it at the coordinates ``[1, 4, 6]``. The ``vtkSphereSource`` class is used to generate *polydata*, and the polydata is added to the visualization.

**Polydata is the geometry that is used in visualizations. You will almost always be working with polydata or something similar when using VTK.**

Polydata is similar to a finite element mesh. It contains points which are analogous to nodes, and cells which are analogous to elements. The cells can be 2D or 3D.

This example will also demonstrate a routine that you will often use ``Define polydata, Define mapper, Define Actor .. Add polydata to the mapper .. Add the mapper to the actor .. Add the actor to the renderer``. This routine requires three variables
    #) Polydata - The geometry
    #) Mapper - Mapps polydata to graphics primitives
    #) Actor - Represents an object (geometry & properties) in a rendered scene

.. image:: /Python/3DVisualization/img/Sphere.png
   :width: 300px

The lines that are highlighted below show the code that was added to the :ref:`Python3DVisualizationCoordinateAxes` tutorial.

.. literalinclude:: /Python/3DVisualization/Scripts/Sphere.py
    :language: python
    :emphasize-lines: 17-26, 28-31, 33-38