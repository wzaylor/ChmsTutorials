.. _FeBioModelAssembly:

==============
Model Assembly
==============
Purpose
'''''''
This tutorial outlines a way to manage the data that composes a finite element model. This data is managed to create/assembly a finite element model. This is important because data management is the foundation of a model development workflow. A scripted model development workflow is useful for ensuring that consistent methods are used to develop finite element models for multiple subjects/specimens.

This tutorial focuses on how to manage the model's geometry and the corresponding nodesets and elementsets.

Preliminary Notes
'''''''''''''''''
.. This tutorial creates Python code that will used and modified in other tutorials. It is strongly encouraged that readers create one Python file, then modify that file as needed. This tutorial shows the entire file at the bottom, and that code can be copy-and-pasted into a new file. Unexperienced users should create a new project in PyCharm (or use an existing project), add a directory called ``src`` to that project, and save the code as ``FeBioModelAssembly.py`` (note there is nothing special about the folder name ``src``, it is just the organization that these tutorials will use).

Users unfamiliar with Python classes should go through the :ref:`PythonGeneralPythonClass` before proceeding.

Model Assembly - Code Architecture
''''''''''''''''''''''''''''''''''
Before we start, we should consider how we want to use the code. Knee models are generally an "assembly" of different discrete "parts", each with their own unique material properties and other attributes (quotations are used because "assembly" and "parts" are not terms that are associated with FEBio or the finite element method). For example, the future workflow we setup will define an individual *femur* part, an *ACL* part and a *tibia* part. These parts will then be "assembled" and written to a *.feb* file. The *.feb* file defines the finite element model in a format that can be read by FEBio, and the model is then solved by FEBio.

One challenge that we face with using FEBio is that it does not use "local" node or element numbers. This is a challenge because the geometry is individually defined with node/element numbers that start at 1 (or 0). For example, if I have a femur with node numbers 1 to 10500, then I need to redefine my tibia node numbering to start at 10501. This is trivial to implement, however the implementation requires us to define a structure/architecture.

We will define three primary steps to creating a finite element model with the Python scripts:
    #) **Part definition**: Define the individual parts (i.e. define a variable that store's the part's data)
    #) **Model assembly**: Assembly the parts (i.e. adjust node and element numbering)
    #) **Model writing**: Write the assembled model to a .feb file.

Part Definition
---------------
First, create an empty file named ``FebioPart.py`` in your PyCharm project in the ``src`` directory. For example, if your project is named ``FebioTools``, the file you create should be located in ``C:\Projects\FebioTools\src\FebioPart.py``.

The primary purpose of the *part* in the model definition is to store node and element data. A Python class will be used to define *part* objects in the code (see the :ref:`PythonGeneralPythonClass` tutorial if you are unfamiliar). This tutorial defines a basic *part* class for clarity. Later tutorials will make improvements on that class (it is intended that interested users will modify the existing *part* class instead of creating multiple variations of the same class).

The *part* class will have the following attributes:
    * nodes, array nx3: The (x,y,z) coordinates for n nodes. The node numbers (nodeIds) correspond to the row number in the array.
    * elements, array mx8: The element definitions that compose the part's mesh. It is assumed that these are 8 noded hexahedral elements. The element numbers (elementIds) correspond to the row number in the array.
    * materialId, int: The integer that is associated with the part's material properties. It is assumed that all of the part's elements have the same material properties.
    * nodeSets, dictionary: The nodesets for the part. Each key in the dictionary is the name of the nodeset, and the value for each entry is a 1xr array, where the values in the list are the nodeIds that compose the element set.

In practice, there are multiple ways to define the attributes for the *part*. Knowing that the *part* class will likely be modified in the future, we will create individual methods to assign values to the part's attributes. The names of these methods will not be creative, they will simply be *setNodes* to define the part's nodes attribute, etc.

.. literalinclude:: /Mechanics/FiniteElement/FeBio/PreliminaryTutorials/Scripts/FebioTools/src/FebioPart.py
   :language: python
   :emphasize-lines: 1
   :linenos:

