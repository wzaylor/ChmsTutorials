.. _Python3DVisualizationCoordinateAxes:

==============
CoordinateAxes
==============
Purpose
'''''''
This tutorial demonstrates a common routine that is used when creating visualizations: 

``Define actor > Add actor to renderer``

This is a simplified version of that routine because the class *vtk.vtkAxesActor* automatically constructs the geometry. Later tutorials will demonstrate how to construct geometry and add it to the renderer.

This example also changes the default interactor style (which is better suited for a joystick) to a different interactor style (which is better suited for a mouse). Both styles allow the user can use the mouse buttons to rotate, pan, and zoom. Comment out the line with ``iren.SetInteractorStyle(trackBallStyle)`` to demonstrate the difference between the default and track-ball interactor styles. This also demonstrates that defining a variable is not enough to have an effect, the variable must also be set appropriately.


.. image:: /Python/3DVisualization/img/CoordinateAxes.png
   :width: 300px

The lines that are highlighted below show the code that was added to the :ref:`Python3DVisualizationRenderWindow` tutorial.

.. literalinclude:: /Python/3DVisualization/Scripts/CoordinateAxes.py
    :language: python
    :emphasize-lines: 17-20, 22-26