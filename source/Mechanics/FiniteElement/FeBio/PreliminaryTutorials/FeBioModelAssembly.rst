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
This tutorial creates Python code that will used and modified in other tutorials. It is strongly encouraged that readers create one Python file, then modify that file as needed. This tutorial shows the entire file at the bottom, and that code can be copy-and-pasted into a new file. Unexperienced users should create a new project in PyCharm (or use an existing project), add a directory called ``src`` to that project, and save the code as ``FeBioModelAssembly.py`` (note there is nothing special about the folder name ``src``, it is just the organization that these tutorials will use).

Users unfamiliar with Python classes should go through the :ref:`PythonGeneralPythonClass` before proceeding.

Model Assembly - Code Architecture
''''''''''''''''''''''''''''''''''
Before we start to create ``FeBioModelAssembly.py``, we should consider how we want to use the code. Knee models are generally an "assembly" of different discrete "parts", each with their own unique material properties and other attributes (quotations are used because "assembly" and "parts" are not terms that are associated with FEBio or the finite element method). For example, the future workflow we setup will define an individual *femur* part, an *ACL* part and a *tibia* part. These parts will then be "assembled" and written to a *.feb* file. The *.feb* file defines the finite element model in a format that can be read by FEBio, and the model is then solved by FEBio.

One challenge that we face with using FEBio is that it does not use "local" node or element numbers. This is a challenge because the geometry is individually defined with node/element numbers that start at 1. For example, if I have a femur with node numbers 1 to 10500, then I need to redefine my tibia node numbering to start at 10501. This is trivial to implement, however the implementation requires us to define a structure/architecture.

We will define three primary steps to creating a finite element model with the Python scripts:
    #) Define the individual parts
    #) Assembly the parts (i.e. adjust node and element numbering)
    #) Write the parts to a .feb file.