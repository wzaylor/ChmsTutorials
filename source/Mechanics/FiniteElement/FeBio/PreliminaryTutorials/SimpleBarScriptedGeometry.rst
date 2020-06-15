.. _FeBioSimpleBarScriptedGeometry:

=================================================
Scripted Geometry Generation - Simple Bar Example
=================================================
Purpose
'''''''
In the :ref:`Simple Bar Example<FeBioSimpleBarExample>` we saw that a finite element model definition is composed individual sections. It can be useful to setup a workflow where specific parts of that file are automatically generated. One area that this is particularly useful is in the *Geometry* section.

This tutorial introduces an approach to generate human readable text file that defines the *Geometry* section from the :ref:`Simple Bar Example<FeBioSimpleBarExample>`. This is a preliminary tutorial, so the example scripts are written to demonstrate concepts (not demonstrate code efficiency).

Workflow
''''''''
The workflow that is demonstrated

#) Node and element definition - manually define node coordinates and element definitions in the script.
#) Generate XML data - *.feb* files are written in an XML format, and Python has a module that implements that formatting. The bulk of this tutorial demonstrates how that is done.
#) Write the XML data - Use the XML data that was generated to write a human readable file.

The purpose of this tutorial is to generate files, so we will start by demonstrating how to write XML data.

.. _FeBioSimpleBarScriptedGeometryGeneratingAndWriting:

XML data - Generating and Writing
---------------------------------
There are a multitude of tutorials online that discuss the syntax and structure of XML files. This section does not focus on XML syntax, but rather starts with a basic example XML data structure, then increases complexity. It expected that interested readers will copy-and-paste code sections and run the Python scripts as they read along.

First, we will create an XML-element (it is hyphenated to delineate from elements in a finite element model). XML-elements are the structures that contain the desired data that is being stored, and each XML-element can be a *parent* to *child* XML-elements. Each XML-element is required to have a tag, which is a string value. For example, the code block in the :ref:`Nodes<FeBioSimpleBarExampleNodes>` section of a previous tutorial shows a *parent* XML-element with a tag of *Nodes*. The *Nodes* XML-element has 12 *child* XML-elements, each of which have a tag of *node*.

Below is a Python script that defines an XML-element with a tag of 'HelloWorld'. Note that this element isn't being written to a file, so the script doesn't really do anything (yet).

.. code-block:: python

    import xml.etree.ElementTree as ET
    foo = ET.Element("HelloWorld")

Now we will modify the script to write the XML-element to a file called "TestFile.xml". This file will be written to whatever working-directory you are using to run your Python script. For example, if your Python script is located in ``C:\Projects\FunWithFEBio``, then the file will likely be written to that same directory.

.. code-block:: python

    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    foo = ET.Element("HelloWorld")

    fooText = ET.tostring(foo) # Convert the XML-element 'foo' to a string variable
    xmlText = xml.dom.minidom.parseString(fooText)  # Get the text that composes the xml-element.
    xmlString = xmlText.toprettyxml(encoding='ISO-8859-1')  # Make the text pretty by adding line breaks and indentations
    # Write the xml file.
    with open('TestFile.xml', mode='wb') as fl: # Open a new file called 'TestFile.xml'
        fl.write(xmlString) # Write 'xmlString' to the file

We are going to reuse the above operation for writing an XML-file throughout this tutorial (and later tutorials), so we will create a function in the Python script that writes any given XML-element to a file with the given filename.

.. code-block:: python

    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    def xmlElementWriter(xmlElement, fileName):
        """
        Write the given XML-element to a file that has the given fileName

        :param xmlElement: xml.etree.ElementTree.Element instance, The XML-element that contains all of the data that is being written, including desired child XML-elements.
        :param fileName: string, The name of the file that is being generated. Note that if this fileName already exists, then that file will be overwritten without warning.
        :return:
        """
        xmlElementText = ET.tostring(xmlElement)  # Convert the XML-element 'xmlElement' to a string variable
        xmlText = xml.dom.minidom.parseString(xmlElementText)  # Get the text that composes the xml-element.
        xmlString = xmlText.toprettyxml(encoding='ISO-8859-1')  # Make the text pretty by adding line breaks and indentations
        # Write the xml file.
        with open(fileName, mode='wb') as fl:  # Open/create a new file that uses the 'fileName' variable to define the file's name.
            fl.write(xmlString)  # Write 'xmlString' to the file

        return

    foo = ET.Element("HelloWorld")
    xmlElementWriter(foo, 'TestFile.xml')

Generating Nodes Data
---------------------
This section of the tutorial describes how to generate the XML-element needed to produce the *Nodes* section of the *.feb* file that is the same as shown in a :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>`. Notice how the *Nodes* XML-element has 12 child XML-elements, and the child XML-elements are composed of three distinct parts:

#) A tag of *node*.
#) An attribute called *id* which is assigned a unique value.
#) Text in the element that has a comma separated list of coordinates.

This section will demonstrate how to create the *Nodes* structure shown in a :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>` with a series of examples. These examples use one node entry, and the final example demonstrates how to create the entire structure shown in the :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>`.

First, we will create a *Nodes* XML-element that has one child XML-element with a tag of *node*. Note that this also uses the ``xmlElementWriter`` function from :ref:`FeBioSimpleBarScriptedGeometryGeneratingAndWriting`.

.. code-block:: python

    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    def xmlElementWriter(xmlElement, fileName):
        """
        Write the given XML-element to a file that has the given fileName

        :param xmlElement: xml.etree.ElementTree.Element instance, The XML-element that contains all of the data that is being written, including desired child XML-elements.
        :param fileName: string, The name of the file that is being generated. Note that if this fileName already exists, then that file will be overwritten without warning.
        :return:
        """
        xmlElementText = ET.tostring(xmlElement)  # Convert the XML-element 'xmlElement' to a string variable
        xmlText = xml.dom.minidom.parseString(xmlElementText)  # Get the text that composes the xml-element.
        xmlString = xmlText.toprettyxml(encoding='ISO-8859-1')  # Make the text pretty by adding line breaks and indentations
        # Write the xml file.
        with open(fileName, mode='wb') as fl:  # Open/create a new file that uses the 'fileName' variable to define the file's name.
            fl.write(xmlString)  # Write 'xmlString' to the file

        return

    fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.
    barNodesChild = ET.SubElement(fooNodes, 'node') # Create a child element with the variable 'fooNodes' as the parent.
    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.
    xmlElementWriter(fooNodes, fizzBuzzFileName) # Write the xml file.

After running the above example, the contents of the file named ``TestFile.xml`` are:

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <Nodes>
        <node/>
    </Nodes>

Notice how ``node`` xml-element does not have the attribute ``id`` that present in a :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>`. Next we will add that attribute. We will use a python variable type called a *dictionary*. Think of a dictionary as list, but instead of using an integer to access values, *keys* are used to access values (where *keys* are usually strings). See `https://www.w3schools.com/python/python_dictionaries.asp <https://www.w3schools.com/python/python_dictionaries.asp>`_ for more information on *dictionaries*. The *keys* for the dictionary values are the name of the XML-element's attributes, and the corresponding value in the dictionary is the value for the XML-element's attribute.

Modify the original example with the code-block shown below.

.. code-block:: python
    :emphasize-lines: 3,6

    fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.

    nodeAttributeData = {'id':'1'} # Define a dictionary with a key called 'id' and set the value for that key as a string '1'
    # Create a child element with the variable 'fooNodes' as the parent.
    # Specify the xml-element's attributes as being defined in the 'nodeAttributeData' variable
    barNodesChild = ET.SubElement(fooNodes, 'node', nodeAttributeData)

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.
    xmlElementWriter(fooNodes, fizzBuzzFileName) # Write the xml file.

After running the above example, the contents of the file named ``TestFile.xml`` are:

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <Nodes>
        <node id="1"/>
    </Nodes>

Next we will add the coordinate data to the *node* element. If we look at the example in a :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>`, we'll notice how the node coordinate data is outside of the braces ``<node id="1">0.0, 0.0, 0.0</node>``. This is the *text* part of the XML-element. The example below demonstrates how to add *text* to the XML-element.

Modify the original example with the code-block shown below.

.. code-block:: python
    :emphasize-lines: 7

    fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.

    nodeAttributeData = {'id':'1'} # Define a dictionary with a key called 'id' and set the value for that key as a string '1'
    # Create a child element with the variable 'fooNodes' as the parent.
    # Specify the xml-element's attributes as being defined in the 'nodeAttributeData' variable
    barNodesChild = ET.SubElement(fooNodes, 'node', nodeAttributeData)
    barNodesChild.text = '0., 0., 0.' # Define the text value for the 'barNodesChild' xml-element.

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.
    xmlElementWriter(fooNodes, fizzBuzzFileName) # Write the xml file.

After running the above example, the contents of the file named ``TestFile.xml`` are:

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <Nodes>
        <node id="1">0., 0., 0.</node>
    </Nodes>

Next we will turn the previous example into a function that creates the *node* xml-elements. This function is called ``getNodeXmlElement(nodeId, nodeCoordinates)``. We will need a *nodeId* and *nodeCoordinates* as inputs. Both of these inputs are normally numbers, so the function will convert them into strings while defining the element.

.. code-block:: python
    :emphasize-lines: 3, 5-20, 46-47, 49-50

    import xml.etree.ElementTree as ET
    import xml.dom.minidom
    import numpy as np # This is needed to define the node's coordinates

    def xmlElementWriter(xmlElement, fileName):
        """
        Write the given XML-element to a file that has the given fileName

        :param xmlElement: xml.etree.ElementTree.Element instance, The XML-element that contains all of the data that is being written, including desired child XML-elements.
        :param fileName: string, The name of the file that is being generated. Note that if this fileName already exists, then that file will be overwritten without warning.
        :return:
        """
        xmlElementText = ET.tostring(xmlElement)  # Convert the XML-element 'xmlElement' to a string variable
        xmlText = xml.dom.minidom.parseString(xmlElementText)  # Get the text that composes the xml-element.
        xmlString = xmlText.toprettyxml(encoding='ISO-8859-1')  # Make the text pretty by adding line breaks and indentations
        # Write the xml file.
        with open(fileName, mode='wb') as fl:  # Open/create a new file that uses the 'fileName' variable to define the file's name.
            fl.write(xmlString)  # Write 'xmlString' to the file

        return

    def getNodeXmlElement(nodeId, nodeCoordinates):
        """
        Create a 'node' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <node id="1">0., 0., 0.</node>

        :param nodeId: int, The integer that is used to identify the node in the finite element mesh.
        :param nodeCoordinates: array 1x3, The coordinates of the node in the finite element mesh.
        :return:
        """
        # Convert 'nodeId' to a string value.
        # Notice how overwriting the original value in 'nodeId' with a string value.
        nodeId = str(nodeId)
        # Define a dictionary with a key called 'id'.
        attributeData = {'id': nodeId}
        element = ET.Element('node', attributeData) # Create an xml-element with a tag of 'node' and attributes defines with the 'attributeData' dictionary.
        # Notice here how the values in braces {} are converted into strings automatically.
        # The values outside the braces remain part of the string.
        element.text = f'{nodeCoordinates[0]}, {nodeCoordinates[1]}, {nodeCoordinates[2]}' # Define the text value for the 'barNodesChild' xml-element.
        return element

    fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.

    barNodeId = 1 # Define a variable for the nodeId
    barNodeCoordinate = np.array([0., 0., 0.]) # Define the node's coordinate.

    barNodesChild = getNodeXmlElement(barNodeId, barNodeCoordinate) # Create the xml-element for the node
    fooNodes.append(barNodesChild) # Add 'barNodesChild' as a child element to the 'fooNodes' element.

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.
    xmlElementWriter(fooNodes, fizzBuzzFileName) # Write the xml file.

Finally, we will modify the above example to write all of the node data from a :ref:`Previous tutorial<FeBioSimpleBarExampleNodes>`. We will manually enter the node coordinates, and take the *row-index* of the coordinates to correspond to the nodeId.

.. code-block:: python
    :emphasize-lines: 46-57, 59-62

    import xml.etree.ElementTree as ET
    import xml.dom.minidom
    import numpy as np

    def xmlElementWriter(xmlElement, fileName):
        """
        Write the given XML-element to a file that has the given fileName

        :param xmlElement: xml.etree.ElementTree.Element instance, The XML-element that contains all of the data that is being written, including desired child XML-elements.
        :param fileName: string, The name of the file that is being generated. Note that if this fileName already exists, then that file will be overwritten without warning.
        :return:
        """
        xmlElementText = ET.tostring(xmlElement)  # Convert the XML-element 'xmlElement' to a string variable
        xmlText = xml.dom.minidom.parseString(xmlElementText)  # Get the text that composes the xml-element.
        xmlString = xmlText.toprettyxml(encoding='ISO-8859-1')  # Make the text pretty by adding line breaks and indentations
        # Write the xml file.
        with open(fileName, mode='wb') as fl:  # Open/create a new file that uses the 'fileName' variable to define the file's name.
            fl.write(xmlString)  # Write 'xmlString' to the file

        return

    def getNodeXmlElement(nodeId, nodeCoordinates):
        """
        Create a 'node' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <node id="1">0., 0., 0.</node>

        :param nodeId: int, The integer that is used to identify the node in the finite element mesh.
        :param nodeCoordinates: array 1x3, The coordinates of the node in the finite element mesh.
        :return:
        """
        # Convert 'nodeId' to a string value.
        # Notice how overwriting the original value in 'nodeId' with a string value.
        nodeId = str(nodeId)
        # Define a dictionary with a key called 'id'.
        attributeData = {'id': nodeId}
        element = ET.Element('node', attributeData) # Create an xml-element with a tag of 'node' and attributes defines with the 'attributeData' dictionary.
        # Notice here how the values in braces {} are converted into strings automatically.
        # The values outside the braces remain part of the string.
        element.text = f'{nodeCoordinates[0]}, {nodeCoordinates[1]}, {nodeCoordinates[2]}' # Define the text value for the 'barNodesChild' xml-element.
        return element

    fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.

    barCoordinates = np.array([[0.0, 0.0, 0.0], # Manually define the node coordinates
                               [1.0, 0.0, 0.0],
                               [1.0, 1.0, 0.0],
                               [0.0, 1.0, 0.0],
                               [0.0, 0.0, 1.0],
                               [1.0, 0.0, 1.0],
                               [1.0, 1.0, 1.0],
                               [0.0, 1.0, 1.0],
                               [0.0, 2.0, 0.0],
                               [1.0, 2.0, 0.0],
                               [1.0, 2.0, 1.0],
                               [0.0, 2.0, 1.0]])

    for i in range(len(barCoordinates)): # Iterate for i=0 to i= length of 'barCoordinates' minus one.
        barNodeId = i + 1 # Add 1 to i because FEBio starts counting at 1 and not zero.
        barNodesChild = getNodeXmlElement(barNodeId, barCoordinates[i]) # Create the xml-element for the node
        fooNodes.append(barNodesChild) # Add 'barNodesChild' as a child element to the 'fooNodes' element.

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.
    xmlElementWriter(fooNodes, fizzBuzzFileName) # Write the xml file.