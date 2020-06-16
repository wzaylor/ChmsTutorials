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

The purpose of this tutorial is to generate files, so we will start by demonstrating how to write XML data. Once we understand how to write XML data, we will realize that the "trick" to generating FEBio files is making sure the data is used appropriately so FEBio can read the file that we generate. A useful resource for the formatting information is the FEBio user documentation (`https://help.febio.org/FEBio/FEBio_um_2_9/index.html <https://help.febio.org/FEBio/FEBio_um_2_9/index.html>`_, section 3 *Free Format Input*).

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

.. _FeBioSimpleBarScriptedGeometryNodesData:

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

.. _FeBioSimpleBarScriptedGeometryElementsData:

Generating Elements Data
------------------------
This section of the tutorial describes how to generate the XML-element needed to produce the *Elements* section of the *.feb* file that is the same as shown in a :ref:`Previous tutorial<FeBioSimpleBarExampleElements>`. The workflow is similar to that used to define the *Nodes* XML-element(s) (:ref:`FeBioSimpleBarScriptedGeometryNodesData`).

We will start with a basic example of how to generate the *Elements* XML data, then modify that example to make a more useful python script. To begin, below is a basic example of a python script that generates the *Elements* section shown in a :ref:`Previous tutorial<FeBioSimpleBarExampleElements>`.

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

    fooElementsData = {'mat':'1', 'type':'hex8'} # Define the XML-attributes that will be used for the 'Elements' XML-element
    fooElements = ET.Element('Elements', fooElementsData)

    # Define the XML-element for element1 in the finite element model
    barElement1Data = {'id':'1'} # Define the XML-attributes that will be used for the 'elem' XML-element that relates to element1
    barElement1 = ET.Element('elem', barElement1Data) # Define the XML-element for element1
    barElement1.text = '1, 2, 3, 4, 5, 6, 7, 8' # Specify the text for 'barElement1'
    fooElements.append(barElement1) # Add 'barElement1' as a child of 'fooElements`

    # Define the XML-element for element2 in the finite element model
    # **NOTE** This uses a different approach from 'element1'. The two approaches are equivalent!!!
    barElement2 = ET.Element('elem', {'id':'2'}) # Notice how we just define the dictionary in place of a variable. Compare this to lines 26 and 27.
    barElement2.text = '4, 3, 10, 9, 8, 7, 11, 12' # This is the same approach as for 'element1' (see line 28)
    fooElements.append(barElement2) # This is the same approach as for 'element1' (see line 29)

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.

    xmlElementWriter(fooElements, fizzBuzzFileName)

Next, we will modify the above script to use a function to create the *elem* XML-elements. **Note** numpy arrays are used to define the elements. Numpy arrays are not necessary for this script, however numpy arrays will be used in other tutorials.

.. code-block:: python
    :emphasize-lines: 22-44, 50, 53, 57

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

    def getElemXmlElement(elementId, elementDefinition):
        """
        Create a 'elem' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <elem id="1">4, 3, 10, 9, 8, 7, 11, 12</elem>

        .. NOTE:: This function assumes that the element is composed of 8 nodes.

        :param elementId: int, The integer that is assigned to the xml-attribute "id=elementId"
        :param elementDefinition: array 1x8, An array of integers. These integers are used as the 'elem' xml-element's text, which is a comma separated list.
        :return: xml.etree.ElementTree.Element instance, An xml-element that is populated with the given data.
        """
        # Two operations are happening in this line in the following order:
        #   1) str(elementId)   elementId is converted to a string.
        #       Notice how the results of this operation are not used to define a variable, rather they are used as the input for the next operation.
        #   2) {'id':str(elementId)}    A dictionary with one entry is generated. We are giving that entry a key of 'id'.
        #       Notice how the results of the previous operation are supplying the value for the entry.
        elementData = {'id':str(elementId)}
        xmlElement = ET.Element('elem', elementData) # Define the xml-element.
        # Specify the text for 'xmlElement'
        xmlElement.text = f'{elementDefinition[0]}, {elementDefinition[1]}, {elementDefinition[2]}, {elementDefinition[3]}, {elementDefinition[4]}, {elementDefinition[5]}, {elementDefinition[6]}, {elementDefinition[7]}'
        return xmlElement

    fooElementsData = {'mat':'1', 'type':'hex8'} # Define the XML-attributes that will be used for the 'Elements' XML-element
    fooElements = ET.Element('Elements', fooElementsData)

    # Define an array for the element definitions. Specify that they are integers.
    elementsDef = np.array([[1, 2, 3, 4, 5, 6, 7, 8],[4, 3, 10, 9, 8, 7, 11, 12]], dtype=int)

    # Define the XML-element for element1 in the finite element model
    barElement1 = getElemXmlElement(1, elementsDef[0])
    fooElements.append(barElement1) # Add 'barElement1' as a child of 'fooElements`

    # Define the XML-element for element2 in the finite element model
    barElement2 = getElemXmlElement(2, elementsDef[1])
    fooElements.append(barElement2) # This is the same approach as for 'element1' (see line 29)

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.

    xmlElementWriter(fooElements, fizzBuzzFileName)

Recognize that a finite element model may use different element types. so we want to make ``getElemXmlElement`` more flexible. The current function cannot be used for other element types because it requires ``elementDefintion`` to have 8 values.

The line ``xmlElement.text = f'{elementDefinition[0]}, {elementDefinition[1]}...`` is the only part of the ``getElemXmlElement`` function that requires ``elementDefinition`` to have at least 8 values. Experienced users will note that strings in Python can be appended with the addition operation (i.e. ``"hello world" = "hello" + " world"``.

Below you can see a brief Python script that iterates over an array and appends text from that array to a string.

.. code-block:: python

    elements = [1, 4, 3, 749] # This is defined as a list for demonstration. For this application, 1D arrays and lists are interchangeable.

    txt = "" # Create string that has no text (i.e. an empty string).
    for i in range(len(elements)): # Notice how 'len()' is a function that yields an integer, and 'range()` is a separate function that takes an integer as an input.
            # Notice how we are inserting a comma and space after the value that is being inserted.
            # The value that is being inserted is inside the braces {}, and the value takes the place of the braces in the resulting string.
            txt = txt + f'{elements[i]}, '
    print(txt)
    # We want to remove the trailing comma and space
    newTxt = txt.rstrip(', ')
    print(newTxt)

We will use the above example to modify ``getElemXmlElement``.

.. code-block:: python
    :emphasize-lines: 21-25

    def getElemXmlElement(elementId, elementDefinition):
        """
        Create a 'elem' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <elem id="1">4, 3, 10, 9, 8, 7, 11, 12</elem>

        :param elementId: int, The integer that is assigned to the xml-attribute "id=elementId"
        :param elementDefinition: array 1xn, An array of 'n' integers. These integers are used as the 'elem' xml-element's text, which is a comma separated list.
        :return: xml.etree.ElementTree.Element instance, An xml-element that is populated with the given data.
        """
        # Two operations are happening in this line in the following order:
        #   1) str(elementId)   elementId is converted to a string.
        #       Notice how the results of this operation are not used to define a variable, rather they are used as the input for the next operation.
        #   2) {'id':str(elementId)}    A dictionary with one entry is generated. We are giving that entry a key of 'id'.
        #       Notice how the results of the previous operation are supplying the value for the entry.
        elementData = {'id':str(elementId)}
        xmlElement = ET.Element('elem', elementData) # Define the xml-element.

        # Specify the text for 'xmlElement'
        txt = '' # Initialize an empty string
        for i in range(len(elementDefinition)):
            txt = txt + f'{elementDefinition[i]}, '
        txt = txt.rstrip(', ')
        xmlElement.text = txt
        return xmlElement

Finally, we will modify the previous example. Instead of assigning the elementId, we will used the row in the ``elementsDef`` array to specify the elementId.

.. code-block:: python
    :emphasize-lines: 55-57

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

    def getElemXmlElement(elementId, elementDefinition):
        """
        Create a 'elem' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <elem id="1">4, 3, 10, 9, 8, 7, 11, 12</elem>

        :param elementId: int, The integer that is assigned to the xml-attribute "id=elementId"
        :param elementDefinition: array 1xn, An array of 'n' integers. These integers are used as the 'elem' xml-element's text, which is a comma separated list.
        :return: xml.etree.ElementTree.Element instance, An xml-element that is populated with the given data.
        """
        # Two operations are happening in this line in the following order:
        #   1) str(elementId)   elementId is converted to a string.
        #       Notice how the results of this operation are not used to define a variable, rather they are used as the input for the next operation.
        #   2) {'id':str(elementId)}    A dictionary with one entry is generated. We are giving that entry a key of 'id'.
        #       Notice how the results of the previous operation are supplying the value for the entry.
        elementData = {'id':str(elementId)}
        xmlElement = ET.Element('elem', elementData) # Define the xml-element.

        # Specify the text for 'xmlElement'
        txt = '' # Initialize an empty string
        for i in range(len(elementDefinition)):
            txt = txt + f'{elementDefinition[i]}, '
        txt = txt.rstrip(', ')
        xmlElement.text = txt
        return xmlElement

    fooElementsData = {'mat':'1', 'type':'hex8'} # Define the XML-attributes that will be used for the 'Elements' XML-element
    fooElements = ET.Element('Elements', fooElementsData)

    # Define an array for the element definitions. Specify that they are integers.
    elementsDef = np.array([[1, 2, 3, 4, 5, 6, 7, 8],[4, 3, 10, 9, 8, 7, 11, 12]], dtype=int)

    for i in range(len(elementsDef)):
        elemXmlElement = getElemXmlElement(i + 1, elementsDef[i])
        fooElements.append(elemXmlElement)

    fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.

    xmlElementWriter(fooElements, fizzBuzzFileName)

.. _FeBioSimpleBarScriptedGeometryPuttingTogether:

Putting it Together
-------------------
We will combine the workflows from :ref:`FeBioSimpleBarScriptedGeometryNodesData` and :ref:`FeBioSimpleBarScriptedGeometryElementsData` to produce one xml file.

First, we will just combine the two examples to produce one xml file. **Note** A function called ``example`` was used in the example below. This is generally good practice because it helps avoid variables accidentally being overwritten (and other reasons not described in this tutorial).

.. code-block:: python
    :emphasize-lines: 79-84, 102-103, 107

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
        :return: xml.etree.ElementTree.Element instance, An xml-element that is populated with the given data.
        """
        # Convert 'nodeId' to a string value.
        # Notice how overwriting the original value in 'nodeId' with a string value.
        nodeId = str(nodeId)
        # Define a dictionary with a key called 'id'.
        attributeData = {'id': nodeId}
        element = ET.Element('node',
                             attributeData)  # Create an xml-element with a tag of 'node' and attributes defines with the 'attributeData' dictionary.
        # Notice here how the values in braces {} are converted into strings automatically.
        # The values outside the braces remain part of the string.
        element.text = f'{nodeCoordinates[0]}, {nodeCoordinates[1]}, {nodeCoordinates[2]}'  # Define the text value for the 'barNodesChild' xml-element.
        return element

    def getElemXmlElement(elementId, elementDefinition):
        """
        Create a 'elem' xml-element that is populated with the given data.

        The xml-element that is returned is something similar to this:
            <elem id="1">4, 3, 10, 9, 8, 7, 11, 12</elem>

        :param elementId: int, The integer that is assigned to the xml-attribute "id=elementId"
        :param elementDefinition: array 1xn, An array of 'n' integers. These integers are used as the 'elem' xml-element's text, which is a comma separated list.
        :return: xml.etree.ElementTree.Element instance, An xml-element that is populated with the given data.
        """
        # Two operations are happening in this line in the following order:
        #   1) str(elementId)   elementId is converted to a string.
        #       Notice how the results of this operation are not used to define a variable, rather they are used as the input for the next operation.
        #   2) {'id':str(elementId)}    A dictionary with one entry is generated. We are giving that entry a key of 'id'.
        #       Notice how the results of the previous operation are supplying the value for the entry.
        elementData = {'id':str(elementId)}
        xmlElement = ET.Element('elem', elementData) # Define the xml-element.

        # Specify the text for 'xmlElement'
        txt = '' # Initialize an empty string
        for i in range(len(elementDefinition)):
            txt = txt + f'{elementDefinition[i]}, '
        txt = txt.rstrip(', ')
        xmlElement.text = txt
        return xmlElement

    def example():
        # Manually define the node coordinates
        barCoordinates = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0], [0.0, 2.0, 0.0], [1.0, 2.0, 0.0], [1.0, 2.0, 1.0], [0.0, 2.0, 1.0]])
        # Manually define the elements.
        elementsDef = np.array([[1, 2, 3, 4, 5, 6, 7, 8],[4, 3, 10, 9, 8, 7, 11, 12]], dtype=int)
        # Manually define the data needed for the 'Elements' xml-element
        fooElementsData = {'mat': '1', 'type': 'hex8'}  # Define the XML-attributes that will be used for the 'Elements' XML-element

        # Define an xml-element that will be used as the parent to the 'Nodes' and 'Elements' xml-elements.
        geometryElement = ET.Element('Geometry')

        # Create the 'Nodes' xml-element
        fooNodes = ET.Element('Nodes') # Create an element with 'Nodes' as the tag.

        for i in range(len(barCoordinates)):  # Iterate for i=0 to i= length of 'barCoordinates' minus one.
            barNodeId = i + 1  # Add 1 to i because FEBio starts counting at 1 and not zero.
            barNodesChild = getNodeXmlElement(barNodeId, barCoordinates[i])  # Create the xml-element for the node
            fooNodes.append(barNodesChild)  # Add 'barNodesChild' as a child element to the 'fooNodes' element.

        fooElements = ET.Element('Elements', fooElementsData)

        # Define an array for the element definitions. Specify that they are integers.

        for i in range(len(elementsDef)):
            elemXmlElement = getElemXmlElement(i + 1, elementsDef[i])
            fooElements.append(elemXmlElement)

        # Add the xml-elements 'fooNodes' and 'fooElements' as children to the 'geometryElement' xml-element.
        geometryElement.append(fooNodes)
        geometryElement.append(fooElements)

        fizzBuzzFileName = 'TestFile.xml'  # Define the filename of the xml file that is being written.

        xmlElementWriter(geometryElement, fizzBuzzFileName)

    if __name__ == '__main__':
        example()

Simple Bar Example - Multiple Input Files
'''''''''''''''''''''''''''''''''''''''''
The purpose of this tutorial is that we want to define a finite element model with two input files. One file defines the node and element data for the model, and the other contains the remaining data.

After running the last example in the :ref:`FeBioSimpleBarScriptedGeometryPuttingTogether` section, we have created a file called ``TestFile.xml``. We will copy that file to whatever directory we want to use for a FEBio simulation (for example: ``C:\Projects\BarExample\Example2``). In the same directory that contains ``TestFile.xml``, we will create ``BarExample2.feb``, and copy-and-paste the code-block shown below to ``BarExample2.feb``. Compare this code-block to the one shown in a :ref:`previous tutorial<SimpleBarExampleRunningModel>`. Notice how the *Nodes* and *Elements* parts are replaced with the ``<Include>TestFile.xml</Include>`` statement.

Run the ``BarExample2.feb`` (see :ref:`SimpleBarExampleRunningModel` to show how to run a .feb file in *command prompt* or a *terminal*).

.. code-block:: xml
    :emphasize-lines: 33

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
        <Include>TestFile.xml</Include>
        <Geometry>
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