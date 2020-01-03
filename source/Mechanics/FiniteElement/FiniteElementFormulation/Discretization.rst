.. _FiniteElementFormulationDiscretization:

Discretization
""""""""""""""
We first need to discretize the :ref:`variational form<FiniteElementFormulationVariationalFormulation>` (:eq:`fea:weakFormulation`) before we can solve for the field variable (in this case displacements) that satisfy the :ref:`variational form<FiniteElementFormulationVariationalFormulation>`.

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
    \bar{u}_i(X) \approx \hat{u}_i(X) = \sum_{I=1}^{n_n} N^I(X) u^I_i
    :label: fea:displacementApproximation

Where :math:`\bar{u}_i` is the exact solution, :math:`\hat{u}_i` is the approximate solution, and :math:`u^I_i` is displacement for the :math:`I` node in the element. The values for :math:`u^I_i` are the unknown quantities in the finite element formulation. The shape functions (:math:`N^I`) are defined in the element (:math:`\Omega_e`). Notice how :math:`N^I(X)` is a function of the coordinates with respect to the reference coordinate system (:math:`X`). If we used this definition for the shape functions (:math:`N^I`), then we would need to define a unique set of shape functions for every element, and this would be cumbersome. To avoid this issue, we can map the elements in the :math:`X` domain (:math:`\Omega_e`) to a single reference element (:math:`\Omega_{\Box}`) using isoparametric mapping.

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
    X_i = \sum_{I=1}^{n_n} N^I(\theta)X^I_i

.. seealso::
    **Example**:
    Consider an element with the following coordinates (the node numbers correspond to those in :numref:`fig:feaIsoparametricElement`. Calculate the coordinates of the point :math:`\theta = (0.5, 0, 0)` (which exists in :math:`\Omega_{\Box}`) in the mesh element's coordinate system (:math:`x`).:

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
        X_i = \sum_{I=1}^{n_n} N^I(\theta)X^I_i

    For this example, we can define :math:`\bar{X}_i^I = N^I(\theta)X^I_i`.

    .. math::
        \begin{split}
        X_i &= \sum_{I=1}^{n_n} N^I(\theta)X^I_i \\
        &= \sum_{I=1}^{n_n} \bar{X}_i^I
        \end{split}

    For :math:`I=1`, we want to substitute :math:`\theta = (\xi^I,\eta^I,\zeta^I) = (0.5, 0, 0)` into :math:`N^1` from :eq:`fea:shapeFunctions` and the coordinates of the node that relates to the element node number 1, which is :math:`(X_1, X_2, X_3) = (10., -100., 1.)`.

    .. math::
        \begin{split}
            \bar{X}_i^1 &= \frac{1}{8}(1 - \xi)(1 - \eta)(1 - \zeta)X_i^1 \\
            &= \frac{1}{8}(1 - 0.5)(1 - 0.)(1 - 0.)X_i^1 \\
            &= 0.0625X_i^1 \\
            &= 0.0625\begin{bmatrix}10.\\ -100. \\ 1.\end{bmatrix} \\
            &= \begin{bmatrix}0.625\\ -6.252 \\ 0.0625\end{bmatrix}
        \end{split}

    Similarly for :math:`I=2`, we can define :math:`\bar{X}^2_i` by substituting :math:`\theta = (0.5, 0, 0)` into :math:`N^2` from :eq:`fea:shapeFunctions` and the coordinates of the node that relates to the element node number 2, which is :math:`(X_1, X_2, X_3) = (11., -90., 0.)`.

    .. math::
        \begin{split}
            \bar{X}_i^2 &= \frac{1}{8}(1 + \xi)(1 - \eta)(1 - \zeta)X_i^1 \\
            &= \frac{1}{8}(1 + 0.5)(1 - 0.)(1 - 0.)X_i^1 \\
            &= 0.1875X_i^2 \\
            &= 0.1875\begin{bmatrix}11.\\ -90. \\ 0.\end{bmatrix} \\
            &= \begin{bmatrix}2.0625\\ -16.875 \\ 0.\end{bmatrix}
        \end{split}

    Repeating this process for :math:`I=3,4,\ldots,8`, and sum :math:`\bar{X}_i^I` to determine :math:`X_i`. 


.. _FiniteElementFormulationDiscretizationIsoparametricElementDisplacementGradient:

Isoparametric Element - Displacement Gradient
'''''''''''''''''''''''''''''''''''''''''''''
Recall that the displacement was approximated using :eq:`fea:displacementApproximation`. Also recall from :ref:`FiniteElementFormulationKinematics` that the strain is a function of displacements where the gradient of the displacenent is taken with respect to the reference configuration. Therefore, we need to define :math:`\frac{\partial u}{\partial X_A

From the example at the end of the :ref:`FiniteElementFormulationDiscretizationIsoparametricElement` section, we showed that we can define the coordinates of a point within a mesh element (point :math:`X_A` defined in :math:`\Omega_e`) given the mesh element's nodal coordinates and the coordinates of a point within the isoparametric element (point :math:`\theta_i` defined in :math:`\Omega_\Box`). How would the coordinates of a point defined in :math:`\Omega_e` change as we change the coordinates of the corresponding point in :math:`\Omega_\Box`? Put another way, what is the gradient of point :math:`X_A` with respect to the isoparametric element's coordinate system? We will call this gradient :math:`J^\Box_{A\alpha}`.

.. math::
    J^\Box_{A\alpha} = \frac{\partial X_A}{\partial \theta_\alpha}

.. Note::
    **A note on notation**.
    In :math:`J^\Box_{A\alpha}`, the superscript :math:`\Box` is used to differentiate this value from other Jacobian values that arise later. The subscript :math:`A` is capitolized to indicate the reference configuration (rather than the deformed configuration). Finally, the greek subscript :math:`\alpha` is used to indicate the isoparametric element's coordinate system.

Recalling that :math:`X_A = \sum_{I=1}^{n_n} N^I(\theta)X^I_A`, the above equation can be rewritten.

.. math::
    \begin{split}
    J^\Box_{A\alpha} &= \frac{\partial X_A}{\partial \theta_\alpha} \\
    &= \frac{\partial}{\partial \theta_\alpha}\big[\sum_{I=1}^{n_n} N^I(\theta)X^I_A\big] \\
    &= \sum_{I=1}^{n_n}X^I_A \Big(\frac{\partial N^I(\theta)}{\partial \theta_\alpha}\Big)
    \end{split}

For an eight noded quadrilateral element, there are eight shape functions (:eq:`fea:shapeFunctions`). For each shape function, :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}` is a first order tensor value. This first order tensor is multiplied by the element node coordinates :math:`X_A` which yields a second order tensor (note that there are two free indices, one for :math:`X_A`, and one for :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha}`). Note that :math:`\frac{\partial N^I(\theta)}{\partial \theta_\alpha} = \Big[\frac{\partial N^I}{\partial \xi}, \frac{\partial N^I}{\partial \eta}, \frac{\partial N^I}{\partial \zeta}\Big]^T`.

Recognizing that the element mesh is a required input for finite element analysis, :math:`X_A` is already defined for the element. Similarly the shape functions are also an attribute of the elements, so the shape functions :math:`N^I(\theta)` are already defined. With these known values, we can explicitly defined :math:`J^\Box_{A\alpha}`.

**Similar** to what was shown above, if we known the deformed configuration of an element, we can define the mapping between the gradient of point :math:`x_i` with respect to the isoparametric element's coordinate system (where :math:`x_i` is defined with respect to the deformed element's coordinate system). We will call this gradient :math:`j^\Box_{i\alpha}`.

.. math::
    \begin{split}
    j^\Box_{i\alpha} &= \frac{\partial x_i}{\partial \theta_\alpha} \\
    &= \frac{\partial}{\partial \theta_\alpha}\big[\sum_{I=1}^{n_n} N^I(\theta)x^I_i\big] \\
    &= \sum_{I=1}^{n_n}x^I_i \Big(\frac{\partial N^I(\theta)}{\partial \theta_\alpha}\Big)
    \end{split}


.. _fig:feaIsoparametricElementDeformatino:
.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/IsoparametricElementDeformation.png
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    An example of an eight node hexahedral