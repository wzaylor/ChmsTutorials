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

XML data - Generating and Writing
---------------------------------
There are a multitude of tutorials online that discuss the syntax and structure of XML files. This section does not focus on XML syntax, but rather starts with a basic example XML data structure, then increases complexity. It expected that interested readers will copy-and-paste code sections and run the Python scripts as they read along.

First, we will create a XML-element (it is hyphenated to delineate from elements in a finite element model). XML-elements are the structures that contain the desired data that is being stored, and each XML-element can be a *parent* to *child* XML-elements. Each XML-element is required to have a tag, which is a string value. For example, the code block in the :ref:`Nodes<FeBioSimpleBarExampleNodes>` section of a previous tutorial shows a *parent* XML-element with a tag of *Nodes*. The *Nodes* XML-element has 12 *child* XML-elements, each of which have a tag of *node*.

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