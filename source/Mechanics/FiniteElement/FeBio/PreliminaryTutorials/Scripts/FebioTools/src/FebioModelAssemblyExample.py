import numpy as np
import xml.etree.ElementTree as ET

# Custom modules/functions
import FebioPart
import FebioModelAssembly
import FebioFileWriter

def example():
    # Manually define the node coordinates
    part0Coordinates = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0]])
    part1Coordinates = np.array([[0.0, 1.1, 0.0], [1.0, 1.1, 0.0], [1.0, 2.0, 0.0], [0.0, 2.0, 0.0], [0.0, 1.1, 1.0], [1.0, 1.1, 1.0], [1.0, 2.0, 1.0], [0.0, 2.0, 1.0]])
    # Manually define the elements.
    part0Elements = np.array([[0, 1, 2, 3, 4, 5, 6, 7]], dtype=int)
    part1Elements = np.array([[0, 1, 2, 3, 4, 5, 6, 7]], dtype=int)
    # Manually define the nodeSets
    part0FixedNodeSet = [0,1,4,5] # The nodes that are fixed
    part0TiedNodeSet = [3,2,7,6] # The nodes that are nearest part1
    part1LoadedNodeSet = [2,3,6,7]

    # Define part0
    part0 = FebioPart.Part('part0')
    part0.setNodes(part0Coordinates)
    part0.setElements(part0Elements)
    part0.setMaterialId(1)
    part0.addNodeSet(part0FixedNodeSet, 'part0FixedNodeSet')
    part0.addNodeSet(part0TiedNodeSet, 'part0TiedNodeSet')

    # Define part1
    part1 = FebioPart.Part('part1')
    part1.setNodes(part1Coordinates)
    part1.setElements(part1Elements)
    part1.setMaterialId(2)
    part1.addNodeSet(part1LoadedNodeSet, 'part1LoadedNodeSet')

    # Create an instance of the model assembly object
    modelAssembly = FebioModelAssembly.ModelAssembly()
    modelAssembly.addPart(part0) # Use the 'addPart' method with part0
    modelAssembly.addPart(part1) # Use the 'addPart' method with part0

    # Create the xml-element that is used to define the geometry for part0 and part1 in the .feb file
    geometryXmlElement = FebioFileWriter.getGeometryElement(modelAssembly)

    # Define an xml-element that is necessary for FEBio.
    rootElement = ET.Element('febio_spec',{'version': '2.5'})  # Create the element that will contain the 'Geometry' xml-element.
    rootElement.append(geometryXmlElement) # Add the geometry xml-element to the rootElement

    # Write the .feb file that defines the part's geometry
    FebioFileWriter.xmlElementWriter(rootElement, 'BoxGeometry.xml')
    return


if __name__ == '__main__':
    example()