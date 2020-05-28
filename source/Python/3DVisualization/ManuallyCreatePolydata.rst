.. _Python3DVisualizationManuallyCreatePolydata:

========================
Manually Create Polydata
========================
Purpose
'''''''
This tutorial demonstrates how to create polydata. For our purposes, polydata is the composition of two types of data (1) point coordinates (nodes) and (2) element definitions. Each node has three float values which are the (x,y,z) coordinates of the point, and each node is also associated with an integer, which is used to identify the node. Elements are variables that have *n* integer values, where the integers relate to the nodes that compose the element.

Polydata simple example
'''''''''''''''''''''''
The information that is needed to create polydata that is composed of two triangles is shown in the code-block below. The first three lines define three nodes, and the fourth line defines the triangle element. The node and element IDs occupy the first column. For the nodes, the x,y,z coordinates occupy the second, third and fourth columns, respectively. Similarly, the nodeIDs that compose the triangle element are defined in the second, third and fourth columns. The order if these integers has meaning, however that is not discussed here.

.. code-block:: none

    1, 1.0201, 0.0040, 0.0072
    2, 1.0305, 1.0057, 0.0099
    3, 1.3103, 1.0007, 1.0099
    4, -0.5000, 1.0000, 1.0099
    1, 1, 2, 3
    2, 1, 2, 4

.. image:: /Python/3DVisualization/img/ManuallyCreatePolydataSimple.png
   :width: 300px

The highlighted lines below show the filename variable definition, and operations that are used to manually create the polydata.

.. literalinclude:: /Python/3DVisualization/Scripts/ManuallyCreatePolydataSimple.py
    :language: python
    :emphasize-lines: 17-23, 25-32, 34-39, 41-43, 45-50