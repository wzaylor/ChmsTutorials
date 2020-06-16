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

The following sections describe how to define each of these inputs to simulate a uniaxial tension. One end of the bar will be fixed, and loads will be applied to the other end.

Material
--------
Every deformable element in the finite element model needs to have material properties assigned. The assigned materials are important to defining the system that is being modeled. For this example, we will use a Neo-Hookean material. We will specify a Young's modulus of 500 and a Poisson's ratio of 0.3

.. code-block:: xml

    <Material>
        <material id="1" name="SomeName" type="neo-Hookean">
            <density>1</density>
            <E>500</E>
            <v>0.3</v>
        </material>
    </Material>

.. NOTE:: Units are not explicitly defined in the finite element model. It is up to the user to manage units. We will take Young's modulus to have units of MPa. The node coordinates and applied loads should be consistent with Young's modulus units. Note that Poisson's ratio does not have any units.

.. _FeBioSimpleBarExampleNodes:

Nodes
-----
Nodes specify the *x,y,z* coordinates of points that compose the finite element mesh. Each node is has four values associated with it. The first value is a *nodeId*, which is an integer that is used to identify the node. The other three values are the *x,y,z* coordinates.

This example uses two elements with 12 nodes, and those nodes are shown below.
In FEBio, the nodes need to have the following format (note that the *x,y,z* coordinates are not labeled. It is assumed that the coordinates follow the order of *x,y,z*):

.. code-block:: xml

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

.. NOTE:: Units are not explicitly defined in the finite element model. It is up to the user to manage units. We will take the node coordinates to have units of mm.

.. _FeBioSimpleBarExampleElements:

Elements
--------
Elements are also used to define the geometry used in the model. Apologies for the lack of a descriptive definition, the punch-line is a finite element model needs elements, and not just nodes.

Similar to nodes, each element is assigned a unique integer value (*elementId*). Additionally, an element is a set of nodeIds that compose the element. This example uses hexahedral elements that are composed of eight nodes, so each element needs to be defined with eight integers.

As a demonstration, draw a 3D coordinate axes with twelve points that have the coordinates shown above. Label the coordinates with the nodeId shown. Next, draw lines connecting adjacent nodes without diagonals (i.e. lines connecting nodes 1 and 2, nodes 2 and 3, nodes 3 and 4, etc. You will not draw a diagonal line connecting nodes 1 and 3). You will end up with two cubes, where one is on top of the other, and the two cubes share nodes 3, 4, 7 and 8. We can define each cube with the nodeIds:

* Element 1, [1, 2, 3, 4, 5, 6, 7, 8]
* Element 2, [4, 3 10, 9, 8, 7, 11, 12]

**Note** that the order of the nodeIds is not arbitrary, though the ordering of nodeIds is outside the scope of this tutorial.

In FEBio, element definitions need to have the following format:

.. code-block:: xml

    <Elements mat="1" type="hex8">
        <elem id="1">1, 2, 3, 4, 5, 6, 7, 8</elem>
        <elem id="2">4, 3, 10, 9, 8, 7, 11, 12</elem>
    </Elements>

Sets
----
Node and element IDs can be grouped into sets. A nodeset is a list of nodeIds, and similarly an elementset is a list of elementIds. Node and element sets are not necessary for the finite element method, however FEBio uses nodesets to apply boundary conditions.

A nodeset (and elementset) consists of two values. The first value is the set's name, which is used to identify the nodeset in other parts of the model definition. The second value is a list of nodeIds.

In this example, we want to apply boundary conditions to one end of the bar and loads to the other end. Referring to the :ref:`FeBioSimpleBarExampleNodes` section and the simple drawing of the geometry, we will select the nodes that have coordinates ``y=0`` as the fixed end (nodes 1, 2, 5, 6), and nodes that have coordinates ``y=2`` as the loaded end (nodes 9, 10, 11, 12). We will add these two sets after our ``Nodes`` definition, as shown below.

.. code-block:: xml

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
    <NodeSet name="fixed">
        <node id="1"/>
        <node id="2"/>
        <node id="5"/>
        <node id="6"/>
    </NodeSet>
    <NodeSet name="loaded">
        <node id="9"/>
        <node id="10"/>
        <node id="11"/>
        <node id="12"/>
    </NodeSet>

Boundary Conditions
-------------------
Boundary conditions specify known displacements (and rotations) at specific nodes in the model. There needs to be at least one boundary condition for every nodal degree of freedom in the model. In this example, the nodes only have translational degrees of freedom, so we need to specify at least one displacement in the x, y, and z directions. We are defining the a boundary condition by specifying these displacements.

Boundary conditions are important to defining the system that is being modeled. There can be much more discussion about the use of boundary conditions, however that is beyond the scope of this example. For this example, we will model one end of the bar as being rigidly fixed, therefore the nodes at one end of the bar will be constrained to have zero displacement in the x, y, z directions.

.. code-block:: xml

    <Boundary>
        <fix bc="x,y,z" node_set="fixed"/>
    </Boundary>


Loads
-----
Similar to boundary conditions, loads are important to defining the system that is being modeled. There can be much more discussion about the use of loads, however that is beyond the scope of this example.

In this example, we are applying a 10 N load to each node at one of the bar. Notice how there are four nodes at the end of the bar, so we are simulating a 40 N load being applied.

.. code-block:: xml

    <Loads>
        <nodal_load bc="y" node_set="loaded">
            <scale lc="1">1.0</scale>
        </nodal_load>
    </Loads>
    <LoadData>
        <loadcurve id="1" type="smooth">
            <point>0.,0.</point>
            <point>1.,10.</point>
        </loadcurve>
    </LoadData>

Notice how the load has a ``scale`` of 1, and the load definition refers to a load curve which coincidentally has an ID of 1. In this example we are using the load curve to control the magnitude of the load, where at 0 seconds, there is no load being applied, and at 1 second a load of 10 is being applied. While it is trivial for this example, load curves are useful for more complex loading conditions.

.. NOTE:: Units are not explicitly defined in the finite element model. It is up to the user to manage units. We will take the loads to have units of N.

.. _SimpleBarExampleRunningModel:

Running the Model
-----------------
We can assemble all of the above pieces into the model shown below. Copy and paste the text below into a file, and save that file to a specific directory (such as ``C:\Projects\BarExample\BarExample.feb``). Note that the file should be saved with a ``.feb`` extension.

We will execute this command from a ``command prompt`` on Windows (or a ``terminal`` on Linux). If you are using Windows, you will have to modify your computer's path (see section 2.1: `https://help.febio.org/FEBio/FEBio_um_2_9/index.html <https://help.febio.org/FEBio/FEBio_um_2_9/index.html>`_). The path you would add may be similar to this: ``C:\Program Files\FEBio2.9.1\bin``

From the command prompt (or terminal) navigate to the directory where you saved the .feb file (for example, ``C:\Projects\BarExample``. Enter the command
``febio3 BarExample.feb``. This will run the simulation and the results should be saved to a file called ``BarExample.xplt``.

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <febio_spec version="2.5">
        <Module type="solid"/>
        <Control>
            <time_steps>10</time_steps>
            <step_size>0.1</step_size>
            <max_refs>15</max_refs>
            <max_ups>10</max_ups>
            <diverge_reform>1</diverge_reform>
            <reform_each_time_step>1</reform_each_time_step>
            <dtol>0.001</dtol>
            <etol>0.01</etol>
            <rtol>0</rtol>
            <lstol>0.9</lstol>
            <min_residual>1e-20</min_residual>
            <qnmethod>0</qnmethod>
            <rhoi>0</rhoi>
            <time_stepper>
                <dtmin>0.01</dtmin>
                <dtmax>0.1</dtmax>
                <max_retries>5</max_retries>
                <opt_iter>10</opt_iter>
            </time_stepper>
            <analysis type="static"/>
        </Control>
        <Material>
            <material id="1" name="NeoHookean" type="neo-Hookean">
                <density>1</density>
                <E>500</E>
                <v>0.3</v>
            </material>
        </Material>
        <Geometry>
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
            <NodeSet name="fixed">
                <node id="1"/>
                <node id="2"/>
                <node id="5"/>
                <node id="6"/>
            </NodeSet>
            <NodeSet name="loaded">
                <node id="9"/>
                <node id="10"/>
                <node id="11"/>
                <node id="12"/>
            </NodeSet>
            <Elements mat="1" type="hex8">
                <elem id="1">1, 2, 3, 4, 5, 6, 7, 8</elem>
                <elem id="2">4, 3, 10, 9, 8, 7, 11, 12</elem>
            </Elements>
        </Geometry>
        <Boundary>
            <fix bc="x,y,z" node_set="fixed"/>
        </Boundary>
        <Loads>
            <nodal_load bc="y" node_set="loaded">
                <scale lc="1">1.0</scale>
            </nodal_load>
        </Loads>
        <LoadData>
            <loadcurve id="1" type="smooth">
                <point>0.,0.</point>
                <point>1.,10.</point>
            </loadcurve>
        </LoadData>
    </febio_spec>
