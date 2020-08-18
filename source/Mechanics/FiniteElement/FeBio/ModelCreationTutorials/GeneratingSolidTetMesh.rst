.. _FeBioGeneratingSolidTetMesh:

===================================
Generating a Solid Tetrahedral Mesh
===================================
Purpose
'''''''
The purpose of this tutorial is to demonstrate one way that a solid mesh can be generated from a surface mesh.

Surface meshes are commonly created from segmentations of MR or CT images. This tutorial will demonstrate meshing a surface mesh of an ACL, however other anatomy/geometry can be substituted. Users are encouraged to use their favorite ACL surface mesh, however if that is not available, the mesh used in this tutorial can be found in the OpenKnee(s) project (file name: oks003_ACL_AGS_LVTIT.stl, `https://simtk.org/svn/openknee/oks/oks003/Geometry <https://simtk.org/svn/openknee/oks/oks003/Geometry>`_)

Setup
'''''
This tutorial uses a Python module called *tetgen* (`https://pypi.org/project/tetgen/ <https://pypi.org/project/tetgen/>`_). To install this module, open a command window (or terminal in Linux), and enter this command: ``pip install tetgen``

This tutorial also uses the module *VTK*. Refer to the following section for information on installing *VTK*: :ref:`VTK setup<Python3DVisualizationPreliminary>`.

Minimal Working Example
'''''''''''''''''''''''
Here is a minimal working example, where a solid tetrahedral mesh is generated from a surface file, and nothing is actually done with the mesh. The mesh is lost to the ether when the script is finished running.

Notice the following things about the example:
    #) The variable ``surfaceMeshFileName`` has ``r`` before the quotation marks. **This is important for Windows users**. The ``r`` defines the string as a *raw string*. This is important because a string can accidentally have special characters, such as ``\n`` which specifies a new line (i.e. ``foo = 'C:\Projects\nibbler\oks003_ACL_AGS_LVTIT.stl'`` has a new line character in the file name).
    #) The variable ``switches`` defines the options that are specified for mesh generation. This example has ``-a1.0 -V``, where ``-a1.0`` specifies the target maximum element volume. This is useful for controlling the number of elements in the mesh. The input ``-V`` specifies a *verbose* output. This means the mesh statistics are printed to the output window. These statistics are useful metrics for reporting/recording mesh quality. For example, methods for a journal article may read: "All meshes were generated with an aspect ratio less than 30". The inputs can be found in the *tetgen* documentation (`http://wias-berlin.de/software/index.jsp?id=TetGen&lang=1 <http://wias-berlin.de/software/index.jsp?id=TetGen&lang=1>`_, and `http://wias-berlin.de/software/tetgen/1.5/doc/manual/manual005.html#sec36 <http://wias-berlin.de/software/tetgen/1.5/doc/manual/manual005.html#sec36>`_)

.. literalinclude:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/Scrpits/TetMeshMinimalExample.py
    :language: python

Saving the Tetrahedral Mesh
'''''''''''''''''''''''''''

