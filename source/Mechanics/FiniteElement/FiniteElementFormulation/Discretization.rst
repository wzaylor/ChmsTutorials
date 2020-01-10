.. _FiniteElementFormulationDiscretization:

Discretization
""""""""""""""
We first need to discretize the :ref:`variational form<FiniteElementFormulationVariationalFormulation>` (:eq:`fea:weakFormulation`) before we can solve for the field variable (in this case displacements) that satisfy the :ref:`variational form<FiniteElementFormulationVariationalFormulation>`.

.. _FiniteElementFormulationDiscretizationBodyDiscretization:

.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/PotatoDiscretization.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    A 2D representation showing the discretization of a body. Note that some of the elements in this mesh are not ideal.

The body :math:`B` is discretized with with :math:`n_n` elements (:math:`\Omega_e`). Notice in the figure above how this discretization approximates the actual geometry of the body.

.. math::
    B \approx B^h = \bigcup^{n_e}_{e=1} \Omega_e

Where the assembly of the elements is described further in the :ref:`FiniteElementFormulationDiscretizationAssembly` section.

The primary field variable (which is displacements in these tutorials) is approximated using interpolation functions. This interpolation is done across each element.

.. math::
    \bar{u}_A(X) \approx \hat{u}_A(X) = \sum_{I=1}^{n_n} N^I(X) u^I_A
    :label: fea:displacementApproximation

Where :math:`\bar{u}_A` is the exact solution, :math:`\hat{u}_A` is the approximate solution, and :math:`u^I_A` is displacement for the :math:`I` node in the element. The values for :math:`u^I_A` are the unknown quantities in the finite element formulation. The shape functions (:math:`N^I`) are defined in the element (:math:`\Omega_e`). 

Recall from :ref:`FiniteElementFormulationKinematics` that the strain is a function of displacements where the gradient of the displacenent is taken with respect to the reference configuration. Therefore, we need to define :math:`\frac{\partial u_A}{\partial X_B}`. Substituting :eq:`fea:displacementApproximation` into the partial derivative (and noticing how :math:`u_A` is not a function of :math:`X`)

.. math::
    \begin{split}
    \frac{\partial \hat{u}_A}{\partial X_B} &= \frac{\partial}{\partial X_B}\Big[\sum_{I=1}^{n_n} N^I(X) u^I_A \Big] \\
    &= \sum_{I=1}^{n_n} u^I_A \frac{\partial N^I(X)}{\partial X_B}
    \end{split}
    :label: fea:displacementGradientApproximation1

Before we solve for :math:`\frac{\partial N^I}{\partial X_B}`, we should notice that :math:`N^I(X)` is a function of the coordinates with respect to the reference coordinate system (:math:`X`). *If we used this definition for the shape functions* (:math:`N^I`), *then we would need to define a unique set of shape functions for every element, and this would be cumbersome.* To avoid this issue, we can map the elements in the :math:`X` domain (:math:`\Omega_e`) to a single reference element (:math:`\Omega_{\Box}`) using isoparametric mapping.

.. _FiniteElementFormulationDiscretizationIsoparametricElement:

Isoparametric Element
'''''''''''''''''''''
An isoparametric element is defined for every element type. The shape functions (:math:`N^I`) are defined with respect to the coordinate system in the isoparametric element's space. This allows for multiple mesh elements to use the same set of shape functions. These tutorials will only demonstrate eight noded hexahedral element, therefore, :math:`n_n=8` and :math:`I=1,2,\ldots,8`. 

The isoparametric element's nodal coordinates (:math:`\theta^I = (\xi^I,\eta^I,\zeta^I)`) are defined as shown in :numref:`fig:feaIsoparametricElement` and :numref:`tab:feaIsoparametricNodeCoordinates`.

.. _fig:feaIsoparametricElement:
.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/IsoparametricElement.png
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    An example of an eight node hexahedral element and its corresponding isoparametric element. Note that the mesh element's node numbers are not sequential. Also note that the coordinates at the nodes are given superscripts to indicate their node number.

.. _tab:feaIsoparametricNodeCoordinates:
.. csv-table:: Isoparametric hexahedral element nodal coordiantes. 

   Node number (:math:`\theta^I`), :math:`\xi^I`,:math:`\eta^I`,:math:`\zeta^I`
   :math:`\theta^1`, -1, -1, -1
   :math:`\theta^2`, 1, -1, -1
   :math:`\theta^3`, 1, 1, -1
   :math:`\theta^4`, -1, 1, -1
   :math:`\theta^5`, -1, -1, 1
   :math:`\theta^6`, 1, -1, 1
   :math:`\theta^7`, 1, 1, 1
   :math:`\theta^8`, -1, 1, 1


These tutorials will only demonstrate eight noded hexahedral element, therefore there are eight shape functions. Referring to the coordinates shown for the element nodes (:math:`\theta^I`) in :numref:`fig:feaIsoparametricElement` and :numref:`tab:feaIsoparametricNodeCoordinates`, the shape functions are:

.. math::
    \begin{split}
        N^1(\theta) &= \frac{1}{8}(1 - \xi)(1 - \eta)(1 - \zeta) \\
        N^2(\theta) &= \frac{1}{8}(1 + \xi)(1 - \eta)(1 - \zeta) \\
        N^3(\theta) &= \frac{1}{8}(1 + \xi)(1 + \eta)(1 - \zeta) \\
        N^4(\theta) &= \frac{1}{8}(1 - \xi)(1 + \eta)(1 - \zeta) \\
        N^5(\theta) &= \frac{1}{8}(1 - \xi)(1 - \eta)(1 + \zeta) \\
        N^6(\theta) &= \frac{1}{8}(1 + \xi)(1 - \eta)(1 + \zeta) \\
        N^7(\theta) &= \frac{1}{8}(1 + \xi)(1 + \eta)(1 + \zeta) \\
        N^8(\theta) &= \frac{1}{8}(1 - \xi)(1 + \eta)(1 + \zeta)
    \end{split}
    :label: fea:shapeFunctions

We can use this mapping to define the coordinates of a point inside the isoparametric element to the corresponding coordinates inside the mesh element.

.. math::
    X_i = \sum_{I=1}^{n_n} N^I(\theta)X^I_A

.. seealso::
    **Example**:
    Consider an element with the following coordinates (the node numbers correspond to those in :numref:`fig:feaIsoparametricElement`. Calculate the coordinates of the point :math:`\theta = (0.5, 0, 0)` (which exists in :math:`\Omega_{\Box}`) in the mesh element's coordinate system (:math:`X`).:

        .. csv-table:: The nodal coordinates of the given element.

            Element node number (:math:`I`), Mesh node number,  :math:`X_1`,:math:`X_2`,:math:`X_3`
            1, 12, 10., -100., 1.
            2, 47, 11., -90., 0.
            3, 109, 8.5, -91.5, 0.5
            4, 77, 8.75, -101., 0.25
            5, 13, 10.25, -105., 6.
            6, 88, 10.75, -95.5, 5.5
            7, 5, 8., -104., 5.25
            8, 184, 9., -100.5, 6.5

    Solution:
        The coordinates of the point is defined with the following equation.

    .. math::
        X_i = \sum_{I=1}^{n_n} N^I(\theta)X^I_A

    For this example, we can define :math:`\bar{X}_A^I = N^I(\theta)X^I_A`.

    .. math::
        \begin{split}
        X_A &= \sum_{I=1}^{n_n} N^I(\theta)X^I_A \\
        &= \sum_{I=1}^{n_n} \bar{X}_A^I
        \end{split}

    For :math:`I=1`, we want to substitute :math:`\theta = (\xi^I,\eta^I,\zeta^I) = (0.5, 0, 0)` into :math:`N^1` from :eq:`fea:shapeFunctions` and the coordinates of the node that relates to the element node number 1, which is :math:`(X_1, X_2, X_3) = (10., -100., 1.)`.

    .. math::
        \begin{split}
            \bar{X}_A^1 &= \frac{1}{8}(1 - \xi)(1 - \eta)(1 - \zeta)X_A^1 \\
            &= \frac{1}{8}(1 - 0.5)(1 - 0.)(1 - 0.)X_i^1 \\
            &= 0.0625X_A^1 \\
            &= 0.0625\begin{bmatrix}10.\\ -100. \\ 1.\end{bmatrix} \\
            &= \begin{bmatrix}0.625\\ -6.252 \\ 0.0625\end{bmatrix}
        \end{split}

    Similarly for :math:`I=2`, we can define :math:`\bar{X}^2_A` by substituting :math:`\theta = (0.5, 0, 0)` into :math:`N^2` from :eq:`fea:shapeFunctions` and the coordinates of the node that relates to the element node number 2, which is :math:`(X_1, X_2, X_3) = (11., -90., 0.)`.

    .. math::
        \begin{split}
            \bar{X}_A^2 &= \frac{1}{8}(1 + \xi)(1 - \eta)(1 - \zeta)X_A^1 \\
            &= \frac{1}{8}(1 + 0.5)(1 - 0.)(1 - 0.)X_A^1 \\
            &= 0.1875X_i^2 \\
            &= 0.1875\begin{bmatrix}11.\\ -90. \\ 0.\end{bmatrix} \\
            &= \begin{bmatrix}2.0625\\ -16.875 \\ 0.\end{bmatrix}
        \end{split}

    Repeating this process for :math:`I=3,4,\ldots,8`, and sum :math:`\bar{X}_A^I` to determine :math:`X_A`. 


.. _FiniteElementFormulationDiscretizationIsoparametricElementMapping:

Isoparametric Element - Mapping
'''''''''''''''''''''''''''''''
The derivative of the mapping from the isoparametric element coordiante system (:math:`\theta_\alpha`) to the reference coordinate system (:math:`X_A`) is denoted as :math:`J^\Box_{A\alpha}`.

.. sidebar:: A note on notation

    In :math:`J^\Box_{A\alpha}`, the superscript :math:`\Box` is used to differentiate this value from other Jacobian values that arise later. The subscript :math:`A` is capitolized to indicate the reference configuration (rather than the deformed configuration). Finally, the greek subscript :math:`\alpha` is used to indicate the isoparametric element's coordinate system.
.. math::
    J^\Box_{A\alpha} = \frac{\partial X_A}{\partial \theta_\alpha}


.. _fig:feaIsoparametricElementJacobianMappingReference:
.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/IsoparametricElementReferenceMapping.png
    :width: 250px
    :align: center
    :alt: alternate text
    :figclass: align-center

    The mapping from the isoparametric element coordinate system to the reference coordinate system.

Recall from the :ref:`FiniteElementFormulationDiscretizationIsoparametricElement` section that :math:`X_A` can be expressed as :math:`X_i = \sum_{I=1}^{n_n} N^I(\theta)X^I_A`. Substituting this into the definition of :math:`J^\Box_{A\alpha}` (noting that the element's coordinates (:math:`X^I_A` are fixed values).

.. math::
    \begin{split}
    J^\Box_{A\alpha} &= \frac{\partial X_A}{\partial \theta_\alpha} \\
    &= \frac{\partial }{\partial \theta_\alpha} \Big[\sum_{I=1}^{n_n} N^I(\theta)X^I_A \Big] \\
    &= \sum_{I=1}^{n_n}X^I_A\frac{\partial N^I(\theta)}{\partial \theta_\alpha}
    \end{split}
    :label: fea:isoparametricMappingReferenceConfiguration

The mapping :math:`J^\Box_{A\alpha}` is fully defined because the element's coordiantes (:math:`X^I_A`) are already defined through discretization of the body (:numref:`FiniteElementFormulationDiscretizationBodyDiscretization`), and the shape functions for the isoparametric element are already defined (for example, :eq:`fea:shapeFunctions`). With these known values, we can define the components of the tensor :math:`J^\Box_{A\alpha}`.

.. _FiniteElementFormulationDiscretizationIsoparametricElementDisplacementGradient:

Isoparametric Element - Displacement Gradient
'''''''''''''''''''''''''''''''''''''''''''''
Recall that the displacement gradient was approximated in :eq:`fea:displacementGradientApproximation1`, and notice the partial derivative is defined with respect to the element's coordiantes (:math:`X_B`) and not isoparametric coordinates (:math:`\theta_\alpha)`. We want to express :math:`\frac{\partial N^I(X)}{\partial X_B}` in terms of isoparametric coordinates (:math:`\theta`).

Using the chain rule, we can express :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}` as a function of :math:`\frac{\partial N^I(X)}{\partial X_B}` (recalling the definition of :math:`J^\Box_{A\alpha}` in :eq:`fea:isoparametricMappingReferenceConfiguration`).

.. math::
    \begin{split}
    \frac{\partial N^I(\theta)}{\partial \theta_\alpha} &= \frac{\partial N^I(X)}{\partial X_B} \frac{\partial X_B}{\partial \theta_\alpha} \\
    &= \frac{\partial N^I(X)}{\partial X_B}\Big[ \sum_{I=1}^{n_n}X^I_B\frac{\partial N^I(\theta)}{\partial \theta_\alpha} \Big] \\
    &= \frac{\partial N^I(X)}{\partial X_B} J^\Box_{B\alpha}
    \end{split}

We can rearrange the above equation to solve for :math:`\frac{\partial N^I(X)}{\partial X_B}`.

.. math::
    \begin{split}
    \frac{\partial N^I(X)}{\partial X_B} &= (J^\Box)^{-1}_{\alpha B}\frac{\partial N^I(\theta)}{\partial \theta_\alpha}
    \end{split}

Recognize that we can already define the tensor :math:`J^\Box_{B\alpha}` (:eq:`fea:isoparametricMappingReferenceConfiguration`), so we can also determine its inverse :math:`(J^\Box)^{-1}_{\alpha B}`. Substituting the above equation into :eq:`fea:displacementGradientApproximation1`.

.. math::
    \frac{\partial \hat{u}_A}{\partial X_B} = \sum_{I=1}^{n_n} u^I_A (J^\Box)^{-1}_{\alpha B}\frac{\partial N^I(\theta)}{\partial \theta_\alpha}
    :label: fea:displacementGradientApproximation2

Example Code
''''''''''''
This example code shows how the formulation above can be implemented, and each part of that implementation is shown separately with an explanation of how the code relates to the equations above. The purpose of the code is to clearly demonstrate the application of the formulation, and not code efficiency. You can find the :ref:`complete script<FiniteElementFormulationDiscretizationExample>` at the end of this section.

    In this example we are given:
        * Nodal coordinates (``elementNodes`` in the example code) of an element defined in the reference configuration (:math:`X_A`). This is done to remain consistent with the equations defined earlier in this section, however the code is the same if the nodal coordinates are defined with respect to the deformed configuration (:math:`x_i`).  We are also given a set
        * Nodal displacements (``nodeDisplacements`` in the example code) of the element's nodes.
        * The coordinates of a point defined with respect to the isoparametric element's coordinate system (``isoparametricCoordinate`` in the example code, and :math:`P_\alpha` in :numref:`fig:feaIsoparametricElementJacobianMappingPointP`). This point should lie inside the isoparametric element. This point has one corresponding point that is defined inside the element defined by ``elementNodes``, and we will call this point :math:`P_A` (:numref:`fig:feaIsoparametricElementJacobianMappingPointP`).

    We are looking to define:
        * The displacement gradient (:math:`\frac{\partial \hat{u}_A}{\partial X_B}`) at point :math:`P` (``displacementGradient`` in the example code). This is the value defined by :eq:`fea:displacementGradientApproximation2`.

    This example assumes:
        * The shape functions defined in :eq:`fea:shapeFunctions` are used in this formulation. These functions (specifically, their partial derivatives) are hard-coded into this example.

.. _fig:feaIsoparametricElementJacobianMappingPointP:
.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/IsoparametricElementJacobianPointP.png
    :width: 250px
    :align: center
    :alt: alternate text
    :figclass: align-center

    The gradient of the mapping (:math:`J^\Box_{A\alpha}`) of a point :math:`P_\alpha` from the isoparametric element coordinate system to the corresponding point in the element's coordinate system (:math:`P_A`).

**We will start** by defining the partial derivatives of the shape functions (:math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}`). Notice how this value is expressed in both :eq:`fea:displacementGradientApproximation2` and :eq:`fea:isoparametricMappingReferenceConfiguration`. Given that this is used in two places, a function was used to determine these values.

Recognize that each shape function (:math:`N^I(\theta)`) is a scalar function (i.e. given coordinates :math:`\theta_\alpha = [\xi, \eta, \zeta]^T` the function :math:`N^1(\theta)` yields a scalar). Therefore, the gradient of the shape functions is a first order tensor (i.e. three components, like a vector). In this example code, those components are split into three different variables [``dNI_dtheta0``, ``dNI_dtheta1``, ``dNI_dtheta2``]. Those variables for each shape function are then organized in an array:

    ``dNI_dtheta0`` = [:math:`\frac{\partial N^1}{\partial \theta_0}, \frac{\partial N^2}{\partial \theta_0}, \ldots, \frac{\partial N^8}{\partial \theta_0}`]

    ``dNI_dtheta1`` = [:math:`\frac{\partial N^1}{\partial \theta_1}, \frac{\partial N^2}{\partial \theta_1}, \ldots, \frac{\partial N^8}{\partial \theta_1}`]

    ``dNI_dtheta2`` = [:math:`\frac{\partial N^1}{\partial \theta_2}, \frac{\partial N^2}{\partial \theta_2}, \ldots, \frac{\partial N^8}{\partial \theta_2}`]

Using :eq:`fea:shapeFunctions`, we can solve for the values in ``dNI_dtheta0``.

.. math::
    \begin{split}
    \frac{\partial N^1}{\partial \theta_0} &= \frac{\partial N^1}{\partial \xi} = -\frac18 (1 - \eta)(1 - \zeta) \\
    \frac{\partial N^2}{\partial \theta_0} &= \frac{\partial N^1}{\partial \xi} = \frac18 (1 - \eta)(1 - \zeta) \\
    \ldots & \\
    \frac{\partial N^8}{\partial \theta_0} &= \frac{\partial N^1}{\partial \xi} = -\frac18 (1 + \eta)(1 + \zeta) \\
    \end{split}

Similarly, we can solve for the values in ``dNI_dtheta1`` and ``dNI_dtheta2``. **Notice** how these equations need values for :math:`\xi`, :math:`\eta`, and :math:`\zeta` to be defined. This is why we need to input the *given/known* isoparametric coordinate into the function shown below. **Notice** how :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}` is fully defined when we know the isoparametric coordinate, *which is a given value in this example!!!*

.. code-block:: python

    def getShapeFunctionDerivative(isoparaCoord):
        dNI_dtheta0 = np.array([-1*(1 - isoparaCoord[1])*(1 - isoparaCoord[2]), 1*(1 - isoparaCoord[1])*(1 - isoparaCoord[2]), 1*(1 + isoparaCoord[1])*(1 - isoparaCoord[2]), -1*(1 + isoparaCoord[1])*(1 - isoparaCoord[2]),
                            -1*(1 - isoparaCoord[1])*(1 + isoparaCoord[2]), 1*(1 - isoparaCoord[1])*(1 + isoparaCoord[2]), 1*(1 + isoparaCoord[1])*(1 + isoparaCoord[2]), -1*(1 + isoparaCoord[1])*(1 + isoparaCoord[2])])*0.125

        dNI_dtheta1 = np.array([-1*(1 - isoparaCoord[0])*(1 - isoparaCoord[2]), -1*(1 + isoparaCoord[0])*(1 - isoparaCoord[2]), 1*(1 + isoparaCoord[0])*(1 - isoparaCoord[2]), 1*(1 - isoparaCoord[0])*(1 - isoparaCoord[2]),
                            -1*(1 - isoparaCoord[0])*(1 + isoparaCoord[2]), -1*(1 + isoparaCoord[0])*(1 + isoparaCoord[2]), 1*(1 + isoparaCoord[0])*(1 + isoparaCoord[2]), 1*(1 - isoparaCoord[0])*(1 + isoparaCoord[2])])*0.125

        dNI_dtheta2 = np.array([-1*(1 - isoparaCoord[0])*(1 - isoparaCoord[1]), -1*(1 + isoparaCoord[0])*(1 - isoparaCoord[1]), -1*(1 + isoparaCoord[0])*(1 + isoparaCoord[1]), -1*(1 - isoparaCoord[0])*(1 + isoparaCoord[1]),
                            1*(1 - isoparaCoord[0])*(1 - isoparaCoord[1]), 1*(1 + isoparaCoord[0])*(1 - isoparaCoord[1]), 1*(1 + isoparaCoord[0])*(1 + isoparaCoord[1]), 1*(1 - isoparaCoord[0])*(1 + isoparaCoord[1])])*0.125

        return dNI_dtheta0, dNI_dtheta1, dNI_dtheta2

**Next**, now that we have defined :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}`, we can define :math:`J^\Box_{A\alpha}` using :eq:`fea:isoparametricMappingReferenceConfiguration`. The purpose of the ``getIsoparametricJacobian`` function is to calculate :math:`J^\Box_{A\alpha}`, and express its components in a 3x3 array. Notice how :eq:`fea:isoparametricMappingReferenceConfiguration` sums over :math:`X^I_A\frac{\partial N^I(\theta)}{\partial \theta_\alpha}`, which is a second order tensor (as indicated by the two free indices, :math:`A` and :math:`\alpha`). The function below iterates over :math:`I`, and uses the expanded index notation to calculate :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}`.

Notice that the element's nodal coordinates (``elementNodes``) and the coordinates of the isoparametric point (``isoparaCoord``) are input into this function. These two variables are *known/given*.

.. code-block:: python

    def getIsoparametricJacobian(elementNodes, isoparaCoord):
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

.. _FiniteElementFormulationDiscretizationExample:

.. literalinclude:: /Mechanics/FiniteElement/FiniteElementFormulation/Scripts/Discretization.py
    :language: python
