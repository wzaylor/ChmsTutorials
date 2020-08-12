import numpy as np
import xml.etree.ElementTree as ET

# Custom modules/functions
import FebioPart
import FebioModelAssembly
import FebioFileWriter

def example():
    # Manually define the node coordinates
    part0Coordinates = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0]])
    part1Coordinates = np.array([[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0], [0.0, 2.0, 0.0], [1.0, 2.0, 0.0], [1.0, 2.0, 1.0], [0.0, 2.0, 1.0]])
    # Manually define the elements.
    part0Elements = np.array([[0, 1, 2, 3, 4, 5, 6, 7]], dtype=int)
    part1Elements = np.array([[0, 1, 2, 3, 4, 5, 6, 7]], dtype=int)
    # Manually define the nodeSets
    part0NodeSet = [3,2,7,6]
    part1NodeSet = [0,1,4,5]

    # Define part0
    part0 = FebioPart.Part('part0')
    part0.setNodes(part0Coordinates)
    part0.setElements(part0Elements)
    part0.setMaterialId(1)
    part0.addNodeSet(part0NodeSet, 'part0NodeSet')

    # Define part1
    part1 = FebioPart.Part('part1')
    part1.setNodes(part1Coordinates)
    part1.setElements(part1Elements)
    part1.setMaterialId(1)
    part1.addNodeSet(part1NodeSet, 'part1NodeSet')

    modelAssembly = FebioModelAssembly.ModelAssembly()
    modelAssembly.addPart(part0)
    modelAssembly.addPart(part1)

    geometryXmlElement = FebioFileWriter.getGeometryElement(modelAssembly)

    # Define an xml-element that is necessary for FEBio.
    rootElement = ET.Element('febio_spec',{'version': '2.5'})  # Create the element that will contain the 'Geometry' xml-element.
    rootElement.append(geometryXmlElement)

    FebioFileWriter.xmlElementWriter(rootElement, 'test.xml')

    return


if __name__ == '__main__':
    example()