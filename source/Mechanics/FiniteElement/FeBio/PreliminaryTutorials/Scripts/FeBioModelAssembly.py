import numpy as np

class Part(object):
    def __init__(self, name):
        """
        Define a "part".
        A "part" stores information about a given geometry/mesh.
        The data from this class is used to populate the "Geometry" part of a FeBio input file (.feb file).

        .. NOTE:: The nodeIds and elementIds stored in this class are relative to the part.
        This means that the first element and node ID is zero.

        :param name: string, The name that is assigned to the part
        """
        self.name = name #: The name that is assigned to the part.
        self.nodes = None #: array nx3, The coordinates of n nodes in the mesh. The row index is taken as the node's number (i.e. nodeId).
        self.elements = {} #: dictionary, A dictionary with keys 'elements': array lxm, An array of the elements, 'elementIds': array 1xn, The integer that is assigned to each element, and 'materialId': int, The number that identifies the element's material.
        # self.elementType = None #: string, The string that identifies the element type. It is assumed that all of the elements are of the same type.
        # self.elementMaterialId = None #: int, The value that relates the material to the elements. It is assumed that the same material properties are assigned to the all the elements.
        # self.elementIds = None #: array 1xm, The element numbers that are assigned to the elements.
        self.nodeIds = None #: array 1xn, The node numbers that are assigned to the nodes.
        self.nodeNum = 0 #: int, The number of nodes in the mesh.
        self.elementNum = 0 #: int, The number of elements in the mesh.
        self.elementSets = {} #: dictionary, A dictionary of the element sets. The keys to the dictionary are strings. The value for each entry is a 1xt array of integers. The value for each index is an integer that relates to the elementId.
        self.nodeSets = {} #: dictionary, A dictionary of the node sets. The keys to the dictionary are strings. The value for each entry is a 1xk array of integers. The value for each index is an integer that relates to the nodeId.
        self.surfaces = {} #: dictionary, A dictionary of the surfaces associated with the part. The keys are strings. The value for each entry is a rxs array of integers. The surface is composed of 'r' faces, each of which contain 's' nodes. The values are integers that relates to the nodeId.
        self.surfaceTypes = {} #: dictionary, A dictionary of the surface types associated with the part. The keys are strings that relate to ``self.surfaces``. The value for each entry is a string that defines the face type.
