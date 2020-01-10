import numpy as np


def example():
    # The nodes defined in the reference coordinate system.
    # Note that the row index is used to indicate the node number. i.e. the coordinates of node_0 is elementNodes[0]
    elementNodes = np.array([[0., 0.04, 0.06],[1.1, 0.05, 0], [1.05, 1.15, 0.08], [0.06, 1.02, 0.09],
                            [0.03, 0.014, 1.125], [1.05, 0.04, 1.07], [1.01, 1.05, 1.12], [0.17, 1.049, 1.1]])

    # node0 displaces 0.5 units in the x0 direction
    nodeDisplacements = np.array([[0.5, 0., 0.], [0., 0., 0.], [0., 0., 0.], [0., 0., 0.],
                                  [0., 0., 0.], [0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])

    # A point in the isoparametric coordinate system. Note that this should be inside the isoparametric element.
    isoparametricCoordinate = np.array([0.95, 0.84, -0.62])

    displacementGradient = getDeformationGradient(elementNodes, nodeDisplacements, isoparametricCoordinate)

    return

def getDeformationGradient(elementNodes, elementNodeDisp, isoparaCoord):
    """
    Calculate the displacement gradient with respect to the same coordinate system that ``elementNodes`` is defined in.
    This gradient is taken at the point P.
    The given isoparametric point (``isoparaCoord``) maps to point P.

    The point P referenced above is defined with respect to the same coordinate system that ``elementNodes`` is defined in.
    This is usally the reference body's coordinate system, or the deformed body's coordinate system.

    ..NOTE:: This function assumes that an eight noded hexahedral element is being used with known basis functions.

    :param elementNodes: array 8x3, The coordinates of the element's nodes in the reference or deformed coordinate system. The order of these points should relate to the the isoparametric element's numbering of [node0, node1, ..., node7].
    :param elementNodeDisp: array 8x3, The displacements of the element's nodes in the reference or deformed coordinate system. The order should relate to the order of ``elementNodes``.
    :param isoparaCoord: array 1x3, The coordinates of a point in the isoparametric coordinate system.
    :return: array 3x3, The deformation gradient at the point in the point (p) that corresponds to the given isoparametric coordinate (``isoparaCoord``).
    """
    # Get the gradient of the 8 shape functions.
    dNI_dXA = getShapeFunctionGradient(elementNodes, isoparaCoord)

    displacementGradient = np.zeros((3,3))
    for i in range(8): # Iterate over the 8 shape functions
        u_i = np.array([[elementNodeDisp[i,0]], [elementNodeDisp[i,1]], [elementNodeDisp[i,2]]]) # Rearrange the displacement of node_i into a 3x1 array.
        dNI_dXA_i = np.reshape(dNI_dXA[i], (1,3)) # Get the gradient of the ith shape function and rearranged it into a 3x1 array.

        displacementGradient_i = u_i@dNI_dXA_i # du_dx = [[u_1*dNI_dX1, u_1*dNI_dX2, u_1*dNI_dX3],[u_2*dNI_dX1, u_2*dNI_dX2, u_2*dNI_dX3],[u_3*dNI_dX1, u_3*dNI_dX2, u_3*dNI_dX3]]
        displacementGradient = displacementGradient + displacementGradient_i

    return displacementGradient

def getShapeFunctionGradient(elementNodes, isoparaCoord):
    """
    Calculate the gradient of the 8 shape functions with respect to the same coordinate system that ``elementNodes`` is defined in.
    These gradients are the gradients at the point P.
    The given isoparametric point (``isoparaCoord``) maps to point P.

    The point p referenced above is defined with respect to the same coordinate system that ``elementNodes`` is defined in.
    This is usally the reference body's coordinate system, or the deformed body's coordinate system.

    ..NOTE:: This function assumes that an eight noded hexahedral element is being used with known basis functions.

    :param elementNodes: array 8x3, The coordinates of the element's nodes in the reference or deformed coordinate system. The order of these points should relate to the the isoparametric element's numbering of [node0, node1, ..., node7].
    :param isoparaCoord: array 1x3, The coordinates of a point in the isoparametric coordinate system.
    :return: array 8x3, The gradient of the 8 shape functions at the point in the point (p) that corresponds to the given isoparametric coordinate (``isoparaCoord``).
    """
    # Calculate the derivative of the shape functions with respect to the isoparametric coordinate system (theta0, theta1, theta2)
    # Note that the shape functions are already known, and the form of the derivatives is already known, so the values of isoparametric point's coordinates are substituted into the values.
    # The structure of these values is as such:
    # dNa_dtheta0[0] = partial derivative if shape function 1 (N^1) with respect to theta0
    # dNa_dtheta0[1] = partial derivative if shape function 2 (N^2) with respect to theta0
    # ...
    # dNa_dtheta0[7] = partial derivative if shape function 8 (N^8) with respect to theta0
    dNI_dtheta0, dNI_dtheta1, dNI_dtheta2 = getShapeFunctionDerivative(isoparaCoord)

    # Calculate the Jacobian of the mapping from the given isoparametric coordinate (``isoparaCoord``) to the element's coordinate system.
    jacobian = getIsoparametricJacobian(elementNodes, isoparaCoord)
    # Calculate the inverse of the Jacobian that was just calculated
    inverseJacobian = np.linalg.inv(jacobian)

    # Pg 63 and 64 in Kim, Introduction to Nonlinear Finite Element Analysis
    dNI_dXA = np.zeros((8, 3)) # Initialize the gradient of the 8 shape functions
    for I in range(8):  # Iterate over the 8 shape functions
        dNjdr = np.array([dNI_dtheta0[I], dNI_dtheta1[I], dNI_dtheta2[I]]).reshape((1, 3))  # The partial derivative of the Ith shape function wrt. the isoparametric coordinates.
        dNI_dXA[I] = dNjdr@inverseJacobian
    return dNI_dXA


def getIsoparametricJacobian(elementNodes, isoparaCoord):
    """
    This function defines the Jacobian of the mapping from the isoparametric space to the space that the given nodes are defined with respect to.

    ..NOTE:: This function assumes that an eight noded hexahedral element is being used with known basis functions.

    :param elementNodes: array 8x3, The coordinates of the element's nodes in the reference or deformed coordinate system. The order of these points should relate to the the isoparametric element's numbering of [node0, node1, ..., node7].
    :param isoparaCoord: array 1x3, The coordinates of a point in the isoparametric coordinate system.
    :return: array 3x3, The Jacobian of the mapping from the point in isoparametric space to corresponding point in the space that the given nodes are defined with respect to.
    """
    # Calculate the derivative of the shape functions with respect to the isoparametric coordinate system (theta0, theta1, theta2)
    # Note that the shape functions are already known, and the form of the derivatives is already known, so the values of isoparametric point's coordinates are substituted into the values.
    # The structure of these values is as such:
    # dNa_dtheta0[0] = partial derivative if shape function 1 (N^1) with respect to theta0
    # dNa_dtheta0[1] = partial derivative if shape function 2 (N^2) with respect to theta0
    # ...
    # dNa_dtheta0[7] = partial derivative if shape function 8 (N^8) with respect to theta0
    dNI_dtheta0, dNI_dtheta1, dNI_dtheta2 = getShapeFunctionDerivative(isoparaCoord)

    jacobian = np.zeros((3, 3)) # Initialize the desired Jacobian before we start the summation.
    for i in range(8): # Iterate over the eight points and shape functions
        jacobian_i = np.zeros((3, 3))  # Initialize an array for the ith iteration.
        jacobian_i[0,0] = dNI_dtheta0[i]*elementNodes[i,0]
        jacobian_i[0,1] = dNI_dtheta1[i]*elementNodes[i,0]
        jacobian_i[0,2] = dNI_dtheta2[i]*elementNodes[i,0]

        jacobian_i[1,0] = dNI_dtheta0[i]*elementNodes[i,1]
        jacobian_i[1,1] = dNI_dtheta1[i]*elementNodes[i,1]
        jacobian_i[1,2] = dNI_dtheta2[i]*elementNodes[i,1]

        jacobian_i[2,0] = dNI_dtheta0[i]*elementNodes[i,2]
        jacobian_i[2,1] = dNI_dtheta1[i]*elementNodes[i,2]
        jacobian_i[2,2] = dNI_dtheta2[i]*elementNodes[i,2]

        jacobian = jacobian + jacobian_i
    return jacobian


def getShapeFunctionDerivative(isoparaCoord):
    """
    Calculate the derivative of the shape functions with respect to the isoparametric coordinate system (theta0, theta1, theta2)
    Note that the shape functions are already known, and the form of the derivatives is already known, so the values of isoparametric point's coordinates are substituted into the values.

    ..NOTE:: This function assumes that an eight noded hexahedral element is being used with known basis functions.
    Because the basis functions are known, the derivative of the basis functions is hard-coded into this function.

    The structure of these values is as such:
        dNa_dtheta0[0] = partial derivative if shape function 1 (N^1) with respect to theta0
        dNa_dtheta0[1] = partial derivative if shape function 2 (N^2) with respect to theta0
        ...
        dNa_dtheta0[7] = partial derivative if shape function 8 (N^8) with respect to theta0
        dNa_dtheta1[0] = partial derivative if shape function 1 (N^1) with respect to theta1
        dNa_dtheta1[1] = partial derivative if shape function 2 (N^2) with respect to theta1
        ...
        dNa_dtheta1[7] = partial derivative if shape function 8 (N^8) with respect to theta1
        dNa_dtheta2[0] = partial derivative if shape function 1 (N^1) with respect to theta2
        dNa_dtheta2[1] = partial derivative if shape function 2 (N^2) with respect to theta2
        ...
        dNa_dtheta2[7] = partial derivative if shape function 8 (N^8) with respect to theta2

    :param isoparaCoord: array 1x3, The coordinates of a point in the isoparametric coordinate system.
    :return: [array 1x8, array 1x8, array 1x8], The partial derivative of 8 shape functions with respect to theta0, theta1, theta2 [dNI_dtheta0, dNI_dtheta1, dNI_dtheta2].
    """
    dNI_dtheta0 = np.array([-1*(1 - isoparaCoord[1])*(1 - isoparaCoord[2]), 1*(1 - isoparaCoord[1])*(1 - isoparaCoord[2]), 1*(1 + isoparaCoord[1])*(1 - isoparaCoord[2]), -1*(1 + isoparaCoord[1])*(1 - isoparaCoord[2]),
                            -1*(1 - isoparaCoord[1])*(1 + isoparaCoord[2]), 1*(1 - isoparaCoord[1])*(1 + isoparaCoord[2]), 1*(1 + isoparaCoord[1])*(1 + isoparaCoord[2]), -1*(1 + isoparaCoord[1])*(1 + isoparaCoord[2])])*0.125

    dNI_dtheta1 = np.array([-1*(1 - isoparaCoord[0])*(1 - isoparaCoord[2]), -1*(1 + isoparaCoord[0])*(1 - isoparaCoord[2]), 1*(1 + isoparaCoord[0])*(1 - isoparaCoord[2]), 1*(1 - isoparaCoord[0])*(1 - isoparaCoord[2]),
                            -1*(1 - isoparaCoord[0])*(1 + isoparaCoord[2]), -1*(1 + isoparaCoord[0])*(1 + isoparaCoord[2]), 1*(1 + isoparaCoord[0])*(1 + isoparaCoord[2]), 1*(1 - isoparaCoord[0])*(1 + isoparaCoord[2])])*0.125

    dNI_dtheta2 = np.array([-1*(1 - isoparaCoord[0])*(1 - isoparaCoord[1]), -1*(1 + isoparaCoord[0])*(1 - isoparaCoord[1]), -1*(1 + isoparaCoord[0])*(1 + isoparaCoord[1]), -1*(1 - isoparaCoord[0])*(1 + isoparaCoord[1]),
                            1*(1 - isoparaCoord[0])*(1 - isoparaCoord[1]), 1*(1 + isoparaCoord[0])*(1 - isoparaCoord[1]), 1*(1 + isoparaCoord[0])*(1 + isoparaCoord[1]), 1*(1 - isoparaCoord[0])*(1 + isoparaCoord[1])])*0.125

    return dNI_dtheta0, dNI_dtheta1, dNI_dtheta2

if __name__ == '__main__':
    example()
    