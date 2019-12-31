.. _FiniteElementFormulationDiscretization:

Discretization
""""""""""""""
We first need to discretize the :ref:`variational form<FiniteElementFormulationVariationalFormulation>` (:eq:`fea:weakFormulation`) before we can solve for the field variable (in this case displacements) that satisfy the :ref:`variational form<FiniteElementFormulationVariationalFormulation>`.

.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/PotatoDiscretization.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    A 2D representation showing the discretization of a body.

The body :math:`B` is discretized with with :math:`n_e` elements (:math:`\Omega_e`). Notice in the figure above how this discretization approximates the actual geometry of the body.

.. math::
    B \approx B^h = \bigcup^{n_e}_{e=1} \Omega_e

Where the assembly of the elements is described further in the :ref:`FiniteElementFormulationDiscretizationAssembly` section.

The primary field variable (which is displacements in these tutorials) is approximated using interpolation functions. This interpolation is done across each element.

.. math::
    \bar{u}_i(X) \approx \hat{u}_i(X) = \sum_{I=1}^{n_n} N^I u^I_i

Where :math:`\bar{u}_i` is the exact solution, :math:`\hat{u}_i` is the approximate solution, and :math:`u^I_i` is displacement for the :math:`I` node in the element. The values for :math:`u^I_i` are the unknown quantities in the finite element formulation. The shape functions (:math:`N^I`) are defined in the element (:math:`\Omega_e`). Notice how :math:`N^I(X)` is a function of the coordinates with respect to the reference coordinate system (:math:`X`). If we used this definition for the shape functions (:math:`N^I`), then we would need to define a unique set of shape functions for every element. This would be cumbersome. To avoid this issue, we can map the elements in the :math:`X` domain (:math:`\Omega_e`) to a single reference element (:math:`\Omega_{\Box}`).

Isoparametric Element
'''''''''''''''''''''
words