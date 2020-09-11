.. _FeBioLigamentInsertionDistanceFilter:

============================================
Ligament Insertion - Part 1: Distance Filter
============================================
Purpose
"""""""
The purpose of this tutorial is to demonstrate a method used to define insertion sites on ligaments/bones. This is a preliminary tutorial that demonstrates the concept, and other tutorials will use this concept.

Setup
"""""
See the :ref:`Python3DVisualizationPreliminary` tutorial for setup of Python.

This tutorial uses bone and ligament surfaces. You are free to use your favorite bone and ligament surface, however if those are not available, you can find the ones used in this tutorial in the OpenKnee(s) simtk repository (`https://simtk.org/svn/openknee/oks/oks003/Geometry/ <https://simtk.org/svn/openknee/oks/oks003/Geometry/>`_).

* Femur: `https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_FBB_AGS_LVTIT.stl <https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_FBB_AGS_LVTIT.stl>`_
* Tibia: `https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_MRC_TBB_EMK_01_LVTIT.stl <https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_MRC_TBB_EMK_01_LVTIT.stl>`_
* ACL: `https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_ACL_AGS_LVTIT.stl <https://simtk.org/svn/openknee/oks/oks003/Geometry/oks003_ACL_AGS_LVTIT.stl>`_

If you have been through the :ref:`FeBioModelAssembly` tutorial, then you should already have a project made (maybe called FebioTools). Use that same project, and add a directory called ``dat`` in the ``FebioTools`` directory. Download/move the femur, tibia, and ACL .stl files to that directory. This is not necessary, but it is useful to have some organization within a project. Also create a directory called ``sol`` in the ``FebioTools`` directory. This will mirror the folders used for the tutorials.

Ligament Insertion - Concept
""""""""""""""""""""""""""""
A knee model is normally composed of different geometries that can interact. For example, a simple knee model may have three geometries which are a femur, tibia, and a ligament (ACL, for example). These geometries won't interact with each other unless the modeler specifies some type of interaction.

One common interaction is to define that the ligament is rigidly attached to the femur and tibia. An basic and unuseful interaction may be that all of the ligament nodes are rigidly attached to the femur and tibia. This is unuseful because the rigid interaction means that the ligament will not deform and the model's behavior will not resemble a knee. To make the ligament interaction with the bones useful is to only define the nodes around the ligament's femoral insertion as being rigidly attached to the femur (and similarly for the tibia).

The distance between the ligament's nodes and the bone's geometry will be used to define whether the nodes are part of the ligament's insertion. The python script will loop over every node in the ligament's mesh and check the distance between the node and the bone's geometry. If the distance is less than some given value, then the nodeId will be stored in a list, and that list will later be used to define the ligament's ineraction in the finite element model. As mentioned before, this tutorial will demonstrate the conecpt, and other tutorials will demonstrate the implementation.

Distance Filter - Minimum working example
"""""""""""""""""""""""""""""""""""""""""
This example demonstrates the concept of finding the distance between a point and the bone's geometry. This example is relative straight-forward, so the comments in the code should explain the concept. Copy and paste the code below into the ``sol`` directory in your project (likely ``FebioTools/sol``).

.. literalinclude:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/Scrpits/FebioTools/sol/DistanceFilterExample.py
    :language: python
    :emphasize-lines: 7

One potential issue may be in the definition of the filename (``targetSurfaceFileName``) on the highlighted line. There are multiple ways to address this, but you may want to follow this fix because this will be necessary for later tutorials. The solution is to change the *working directory* for the script's configuration in *PyCharm* (assuming that you are using PyCharm).

To find the menu, click the dropdown for the *Edit Run/Debug configurations* dialog:

.. image:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/img/ChangeConfiguration1.png
   :width: 300px

Then select your script's configuration, and chance the *working directory* to the project's folder (for example: ``C:\Projects\FebioTools``, if this is your project's path), then click *Apply*, and exit the menu and run the script again.

.. image:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/img/ChangeConfiguration2.png
   :width: 300px

For an explanation of what is going on, lets assume that your project is located in ``C:\Projects\FebioTools``, and the .stl files you downloaded are located in ``C:\Projects\FebioTools\dat``, and the script you are running is located in ``C:\Projects\FebioTools\sol``. The variable in the script ``targetSurfaceFileName`` is a string that is a *relative path* to the desired file. There is nothing special about this variable, but when Python uses the string to open a file, it assumes that there are folders and filenames that match the string.

When you first tried to run the script, the default *working directory* was the same directory that the script is located in (i.e. ``C:\Projects\FebioTools\sol``). So when you defined ``targetSurfaceFileName`` in the script, the full path to the file is interpreted as ``C:\Projects\FebioTools\sol\dat\oks003_FMB_AGS_LVTIT.stl``. You had an error because there is no ``dat`` directory located inside the ``C:\Projects\FebioTools\sol`` folder.

By changing the *working directory* to ``C:\Projects\FebioTools`` in the *PyCharm* configuration, you are executing the script from the ``C:\Projects\FebioTools`` folder. The script works because when ``targetSurfaceFileName`` is used as a file path, there is "coincidentally" a directory inside ``C:\Projects\FebioTools`` called ``dat``, and inside the ``dat`` directory there is "coincidentally" a file named ``oks003_FMB_AGS_LVTIT.stl``.

Changing the *working directory* to the main project folder is generally good practice and it will be used in other tutorials.

Distance Filter - Ligament insertion example
""""""""""""""""""""""""""""""""""""""""""""
This example demonstrates the workflow for defining the nodeIds in a ligament insertion, then visualizes the nodes that were selected. Similar to the previous example, copy and paste the script below into the ``sol`` directory in the project (i.e. ``C:\Projects\FebioTools\sol``). You will likely have to change the *working directory* to ``C:\Projects\FebioTools\`` for the script, as explained in the previous example.

.. image:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/img/LigamentInsertionDistanceFilter.png
   :width: 300px

.. literalinclude:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/Scrpits/FebioTools/sol/LigamentInsertionDistanceFilter.py
    :language: python

Ligament insertion - Fiber direction example
""""""""""""""""""""""""""""""""""""""""""""
Aside from defining attachments for a finite element model, a similar workflow as the previous example could be used to define a vector between the center of insertion sites, and this vector could be used to define the ligament's fiber direction in a finite element model.

The example below calculates the center of the insertion area as the mean of all insertion point coordinates. The unit vector connecting the femur and tibia centers is printed. Please see the comments in the ``example`` function for more explanation.

Notice how the femur's insertion area isn't continuous. This is why visualizations are useful, because it shows how the insertion that the python script defined isn't complete. In practice, the script may also overestimate the insertion area. To fix this particular problem, the modeler may want to redefine the ACL segmentation around the area of the femoral insertion.

.. image:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/img/FiberDirection1.png
   :width: 300px

.. literalinclude:: /Mechanics/FiniteElement/FeBio/ModelCreationTutorials/Scrpits/FebioTools/sol/FiberDirectionLigamentInsertion.py
    :language: python
