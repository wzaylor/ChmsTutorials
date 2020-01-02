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

The body :math:`B` is discretized with with :math:`n_e` elements (:math:`\Omega_e`). Notice in the figure above how this discretization approximates the actual geometry of the body.

.. math::
    B \approx B^h = \bigcup^{n_e}_{e=1} \Omega_e

Where the assembly of the elements is described further in the :ref:`FiniteElementFormulationDiscretizationAssembly` section.

The primary field variable (which is displacements in these tutorials) is approximated using interpolation functions. This interpolation is done across each element.

.. math::
    \bar{u}_i(X) \approx \hat{u}_i(X) = \sum_{I=1}^{n_n} N^I(X) u^I_i

Where :math:`\bar{u}_i` is the exact solution, :math:`\hat{u}_i` is the approximate solution, and :math:`u^I_i` is displacement for the :math:`I` node in the element. The values for :math:`u^I_i` are the unknown quantities in the finite element formulation. The shape functions (:math:`N^I`) are defined in the element (:math:`\Omega_e`). Notice how :math:`N^I(X)` is a function of the coordinates with respect to the reference coordinate system (:math:`X`). If we used this definition for the shape functions (:math:`N^I`), then we would need to define a unique set of shape functions for every element, and this would be cumbersome. To avoid this issue, we can map the elements in the :math:`X` domain (:math:`\Omega_e`) to a single reference element (:math:`\Omega_{\Box}`) using isoparametric mapping.

.. _FiniteElementFormulationDiscretizationIsoparametricElement:

Isoparametric Element
'''''''''''''''''''''
An isoparametric element is defined for every element type. The shape functions (:math:`N^I`) are defined with respect to the coordinate system in the isoparametric element's space. This allows for multiple mesh elements to use the same set of shape functions. These tutorials will only demonstrate eight noded hexahedral element, therefore, :math:`n_e=8` and :math:`I=1,2,\ldots,8`. 

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
    X_i = \sum_{I=1}^{n_e} N^I(\theta)X^I_i

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
        X_i = \sum_{I=1}^{n_e} N^I(\theta)X^I_i

    For this example, we can define :math:`\bar{X}_i^I = N^I(\theta)X^I_i`.

    .. math::
        \begin{split}
        X_i &= \sum_{I=1}^{n_e} N^I(\theta)X^I_i \\
        &= \sum_{I=1}^{n_e} \bar{X}_i^I
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

Isoparametric Element - Kineamtics
''''''''''''''''''''''''''''''''''
All of the kineamtic and geometric variables are interpolated by the shape functions (:math:`N^I`). We are using an :ref:`isoparametric element<FiniteElementFormulationDiscretizationIsoparametricElement>` and shape functions defined with respect to that element's coordinate system (:math:`\theta = (\xi,\eta,\zeta)`) to avoid defining unique shape functions for every element in the mesh. Therefore, we need a way to map between each element's known reference configuration (defined with respect to the reference coordinate system :math:`X_A`), and the element's deformed configuration (defined with respect to the deformed coordinate system :math:`x_i`).

For a given point in the The coordinates of a point in the isoparametric element's space (:math:`\theta_i`) can be determined using the shape functions :math:`N^I`.
