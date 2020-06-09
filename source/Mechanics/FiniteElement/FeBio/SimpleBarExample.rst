.. _FeBioSimpleBarExample:

==================
Simple Bar Example
==================
Purpose
'''''''
This tutorial demonstrates how to define the basic inputs for a FEBio simulation and execute that simulation with the command line.
A model of a bar in uniaxial tension will be used as a demonstration.

This tutorial shows how a human readable text file is used to define a finite element model. This tutorial does not focus on efficient ways to write that file. Users can use a simple text editor (such as *gedit* or *notepad*) to write these files for this tutorial, and other tutorials will demonstrate efficient ways of defining the file used to define the finite element model.

.. Note:: This tutorial uses a 3D structural analysis as an example, and the definitions are not exhaustive. Please refer to a finite element analysis textbook for more exhaustive definitions and examples.

Input File (.feb)
'''''''''''''''''
The input file (usually with a *.feb* extension) needs at least four sections to define a finite element model.

#) Nodes: The coordinates of the points that compose the geometry of the model. Each node is assigned an integer (*nodeId*) which is used to identify the specific node and its correspoinding coordinates.
#) Elements: Sets of nodeIds that define the geometry's surface and/or volume. Similar to nodes, each element is assigned an integer (*elementId*) which is used to identify specific elements.
#) Material: Each element is assigned a set of material properties.
#) Boundary conditions: A finite element analysis solves a set of partial differential equations, and boundary conditions are necessary inputs needed to solve those equations. In general, a boundary condition specifies a translation and/or rotation at a specific node.
#) Loads: Loads are not necessary for a finite element analysis, however loads are used to model specific conditions. For example, loads are not needed to model a cantilevered beam with a fixed displacement at one end, however loads are needed to model a cantilevered beam with a load at the end (*duh*). A finite element model with only boundary conditions may be called a *displacement controlled model*.

The following sections describe how to define each of these inputs to simulate a uniaxial tension.

Nodes
-----
Nodes specify the *x,y,z* coordinates of points that compose the finite element mesh. Each node is has four values associated with it. The first value is a *nodeId*, which is an integer that is used to identify the node. The other three values are the *x,y,z* coordinates.

This example uses two elements with 12 nodes, and those nodes are shown below.
In FEBio, the nodes need to have the following format (note that the *x,y,z* coordinates are not labeled. It is assumed that the coordinates follow the order of *x,y,z*):

.. code-block:: none

    <Nodes>
			<node id="1">0.0, 0.0, 0.0</node>
			<node id="2">1.0, 0.0, 0.0</node>
			<node id="3">1.0, 1.0, 0.0</node>
			<node id="4">0.0, 1.0, 0.0</node>
			<node id="5">0.0, 0.0, 1.0</node>
			<node id="6">1.0, 0.0, 1.0</node>
			<node id="7">1.0, 1.0, 1.0</node>
			<node id="8">0.0, 1.0, 1.0</node>
			<node id="9">0.0, 2.0, 0.0</node>
			<node id="10">1.0, 2.0, 0.0</node>
			<node id="11">1.0, 2.0, 1.0</node>
			<node id="12">0.0, 2.0, 1.0</node>
    </Nodes>

On a piece of paper, draw a 3D coordinate axes with twelve points that have the coordinates shown above. Label the coordinates with the nodeId shown (this will help with the element definition).

Elements
--------
Elements are also used to define the geometry used in the model. Apologies for the lack of a descriptive definition, the punch-line is a finite element model needs elements, and not just nodes.

Similar to nodes, each element is assigned a unique integer value (*elementId*). Additionally, an element is a set of nodeIds that compose the element. This example uses hexahedral elements that are composed of eight nodes, so each element needs to be defined with eight integers.

As a demonstration, draw a 3D coordinate axes with twelve points that have the coordinates shown above. Label the coordinates with the nodeId shown. Next, draw lines connecting adjacent nodes without diagonals (i.e. lines connecting nodes 1 and 2, nodes 2 and 3, nodes 3 and 4, etc. You will not draw a diagonal line connecting nodes 1 and 3). You will end up with two cubes, where one is on top of the other, and the two cubes share nodes 3, 4, 7 and 8. We can define each cube with the nodeIds:

* Element 1, [1, 2, 3, 4, 5, 6, 7, 8]
* Element 2, [4, 3 10, 9, 8, 7, 11, 12]

**Note** that the order of the nodeIds is not arbitrary, though the ordering of nodeIds is outside the scope of this tutorial.

In FEBio, element definitions need to have the following format:

.. code-block:: none

    <Elements mat="1" type="hex8">
			<elem id="1">1, 2, 3, 4, 5, 6, 7, 8</elem>
			<elem id="2">4, 3 10, 9, 8, 7, 11, 12</elem>
    </Elements>