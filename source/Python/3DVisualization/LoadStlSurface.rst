.. _Python3DVisualizationLoadStlSurface:

=================
Load .stl Surface
=================
Purpose
'''''''
This tutorial demonstrates how to load a surface from a .stl file into the visualization. This process is similar to the :ref:`Sphere tutorial<Python3DVisualizationSphere>`, however the source of the polydata comes from the .stl file.

You will need a .stl file for this tutorial. You can use your favorite .stl file, or if that is not available, you can download one from the OpenKnee(s) repository. Here is a link to specimen oks003: `http://simtk.org/svn/openknee/oks/oks003/Geometry/ <http://simtk.org/svn/openknee/oks/oks003/Geometry/>`_.

You will need to change the ``stlSurfaceFileName`` variable to be the specific filename for the .stl file you are using. The filename's variable is a string:

.. code-block:: python

    stlSurfaceFileName = r'/home/will/Projects/ChmsTutorials/source/Python/3DVisualization/dat/oks003_FMB_AGS_LVTIT.stl'

This is the complete path to the .stl file. If you are using a Windows computer, this variable may look like this:

.. code-block:: python

    stlSurfaceFileName = r'C:\Projects\InterestingSurfaces\oks003_FMB_AGS_LVTIT.stl'

Notice how ``r`` is placed before the definition of the string. This prefix makes the string a *raw string*. This is not exactly necessary, however it avoids issues where your filename may have contain special characters, such as ``\n`` or ``\t``. More experienced users can explore using relative paths for the filenames, however that is not discussed here.

.. image:: /Python/3DVisualization/img/LoadStlSurface.png
   :width: 300px

.. literalinclude:: /Python/3DVisualization/Scripts/LoadStlSurface.py
    :language: python
    :emphasize-lines: 17-18, 20-27