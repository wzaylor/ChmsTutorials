import numpy as np

class Part(object):
    def __init__(self, name):
        """
        Define a "part".
        A "part" stores information about a given geometry/mesh.
        The data from this class is used to populate the "Geometry" part of a FeBio input file (.feb file).

        .. NOTE:: The nodeIds and elementIds stored in this class are relative to the part.
        This means that the first element and node ID is zero.

        :param name: string, The string that is assigned to the part.
        """
        self.name = name #: string, The name that is assigned to the part.
        self.nodes = None #: array nx3: The (x,y,z) coordinates for n nodes. The node numbers (nodeIds) correspond to the row number in the array.
        self.elements = None #: array mx8: The element definitions that compose the part's mesh. It is assumed that these are 8 noded hexahedral elements. The element numbers (elementIds) correspond to the row number in the array.
        self.materialId = None #: int: The integer that is associated with the part's material properties. It is assumed that all of the part's elements have the same material properties.
        self.nodeSets = {} #: dictionary: The nodesets for the part. Each key in the dictionary is the name of the nodeset, and the value for each entry is a 1xr array, where the values in the list are the nodeIds that compose the element set.

    def setNodes(self, nodes):
        """
        Populate the self.nodes attribute.

        :param nodes: array nx3, The (x,y,z) node coordinates. The row number corresponds to the nodeId.
        :return:
        """
        self.nodes = nodes
        return

    def setElements(self, elements):
        """
        Populate the self.elements attribute.

        .. NOTE:: This method assumes that only hexahedral elements are defined.

        :param elements: array nx8, The element definitions that compose the part's mesh.  The element numbers (elementIds) correspond to the row number in the array.
        :return:
        """
        self.elements = np.asarray(elements, dtype=int) # Populate self.elements, and make sure the value is an array of integers.
        return

    def setMaterialId(self, materialId):
        """
        Populate the self.materialId attribute.

        .. NOTE:: It is assumed that all of the elements in this part have the same material properties, therefore the same materialId.

        :param materialId: int, The materialId that is associated with the part's material properties in the FeBio .feb file.
        :return:
        """
        self.materialId = materialId
        return

    def addNodeSet(self, nodeSet, setName):
        """
        Add a nodeset to self.nodeSets.
        :param nodeSet: array 1xn, The nodeIds that compose the nodeSet.
        :param setName: string, The key that is assigned to the nodeSet in self.nodeSets.
        :return:
        """
        # Code protection. Avoid overwriting existing nodeSets
        if setName in self.nodeSets.keys():
            raise ValueError(f"A nodeSet with the name {setName} already exists in self.nodeSets. Please check your inputs.")

        self.nodeSets[setName] = np.asarray(nodeSet, dtype=int) # Populate self.nodeSets[setName], and make sure the set of an array of integers.
        return