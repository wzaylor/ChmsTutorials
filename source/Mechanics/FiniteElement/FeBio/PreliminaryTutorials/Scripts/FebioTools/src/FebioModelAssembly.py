
class ModelAssembly(object):

    def __init__(self):
        self.parts = {}  #: dictionary, A dictionary of instances of the FebioTools.FebioPart.Part class instance. The keys are the names that are assigned to the parts.
        self.nodeSetNames = []  #: list, A list that stores the names of the nodesets that are defined in ``self.parts``. This variable is generally used for convenience, so the names do not need to be references from ``self.parts``.

        self.nodeIdOffset = 1 #: int, The offset in the node numbering that is used to modify the part's nodeIds. This starts at 1 because Febio starts node numbering at 1 and not 0.
        self.elementIdOffset = 1 #: int, The offset in the element numbering that is used to modify the part's elementIds. This starts at 1 because Febio starts element numbering at 1 and not 0.

        self.nodeIds = {} #: dictionary, A dictionary of lists. The keys are the part's name and the list is the nodeIds that correspond to the part's nodes.
        self.elementIds = {} #: dictionary, A dictionary of lists. The keys are the part's name and the list is the elementIds that correspond to the part's elements.

    def addPart(self, part):
        """
        This method populates ``self.parts``, and also checks that there are no duplicate nodeSet names between parts.
        Error checking is used for nodeSet names because those names are used to identify the nodeset.
        If there are duplicate names, then there will likely be an error in FeBio.

        :param part: FeBioTools.FeBioPart.Part instance, The part that is being added to the geometry.
        :return:
        """
        # First, check if the part's name has already been used.
        if part.name in self.parts.keys():
            raise KeyError(f"The part name: '{part.name}' already exists in self.parts")

        # Perform error checking for duplicate nodeset names
        for partNodeSetName in part.nodeSets.keys():  # Iterate over nodeSet names. If there are none, then this loop is passed over.
            for partName in self.parts.keys():  # Iterate over the parts that have already been added. This allows for a more descriptive error to be thrown if there is a duplicate nodeset name.
                if partNodeSetName in self.nodeSetNames:
                    raise KeyError(f"The nodeSet name: '{partNodeSetName}' is already defined in the part named '{partName}'")

        self.parts[part.name] = part # Add the part to the self.parts dictionary
        self.nodeSetNames += list(part.nodeSets.keys())  # Populate self.nodeSetNames

        partNodeNum = len(self.parts[part.name].nodes) # The number of nodes in the part.
        partElementNum = len(self.parts[part.name].elements) # The number of elements in the part.

        # Assign the nodeIds and elementIds for the part in self.nodeIds and self.elementIds, respectively.
        self.nodeIds[part.name] = list(range(self.nodeIdOffset, self.nodeIdOffset + partNodeNum)) #
        self.elementIds[part.name] = list(range(self.elementIdOffset, self.elementIdOffset + partElementNum))

        # Adjust the nodeIds in self.parts[part.name].nodeSets by self.nodeIdOffset
        _updateNodeIds(self.parts[part.name], self.nodeIdOffset)

        # Now that we have added a part, update self.nodeIdOffset and self.elementIdOffset for the next part that may be added
        self.nodeIdOffset = self.nodeIdOffset + partNodeNum
        self.elementIdOffset = self.elementIdOffset + partElementNum
        return

def _updateNodeIds(part, nodeIdOffset):
    """
    Change the nodeIds in part.elements and part.nodeSets.

    ..NOTE:: This function updates the attributes in ``part`` by reference.

    :param part: FeBioTools.FeBioPart.Part instance, The part that being updated.
    :param nodeIdOffset: int, The amount that is being added to the nodeIds
    :return:
    """
    part.elements = part.elements + nodeIdOffset # Increase the values in part.elements by 'nodeIdOffset'
    for setName in part.nodeSets.keys():
        part.nodeSets[setName] = part.nodeSets[setName] + nodeIdOffset # Increase the values in part.nodeSets[setName] by 'nodeIdOffset'
    return