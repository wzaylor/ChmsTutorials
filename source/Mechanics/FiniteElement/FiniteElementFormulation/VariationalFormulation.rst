.. _FiniteElementFormulationVariationalFormulation:

Variational Formulation
"""""""""""""""""""""""
First, defining the strong form of the problem. This tutorial uses deformation of a 3D solid as an example.

.. math::
    \begin{split}
       \frac{\partial \sigma_{ij}}{\partial x_j} + B_i &= 0 \\
       \text{Subject to } \sigma_{ij}n_j &= t_i \text{ on } \Gamma_f \\
       u_i &= g_i \text{ on } \Gamma_u
    \end{split}
    :label: eq:strongForm


.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/Potato.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    A 2D representation of a body showing the (red) essential boundary conditions (:math:`\Gamma_u`) and (greed) the essential boundary conditions (:math:`\Gamma_f`).

Recognizing that :eq:`eq:strongForm` is an expression for force, we can
define a functional :math:`W` by multiplying every point in
:eq:`eq:strongForm` by an arbitrary set of displacements :math:`\eta_i`
(taking :math:`F_i = \frac{\partial \sigma_{ij}}{\partial x_j} + B_i`).

.. math::
    \begin{split}
        W(\eta) &= F_i\eta_i \\
        &= \frac{\partial \sigma_{ij}}{\partial x_j}\eta_i + B_i\eta_i
    \end{split}
   :label: eq:strongToWeak1


By doing this, we have used a first order tensor value
(:eq:`eq:strongForm`) in a scalar functional (:eq:`eq:strongToWeak1`). In the
context of this problem, :math:`W` can be thought of as an expression
for work (a force multiplied by a displacement).

Similarly, we can define another functional :math:`I(\eta)` by
integrating :math:`W(\eta)` over the volume of the body.

.. math::
    \begin{split}
        I(\eta) &= \int_V \eta_iF_i dV \\
        &= \int_V \eta_i\Big[\frac{\partial \sigma_{ij}}{\partial x_j} + B_i \Big] dV \\
        &= \int_V \Big[\frac{\partial \sigma_{ij}}{\partial x_j}\eta_i + B_i\eta_i \Big] dV \\
    \end{split}
   :label: eq:strongToWeak2

This is an expression of the work done over the volume due to an
arbitrary set of displacements :math:`\eta`. We can take the :ref:`variation<FiniteElementFormulationVirtualWork>`
of :math:`I(\eta)` to minimize the amount of work done by the forces
(:math:`F_i`, :eq:`eq:strongForm`).

Before moving forward, we need to restrict the arbitrary set of
displacements :math:`\eta` to be admissable. This means that
:math:`\eta_i` satisfies the boundary conditions specified in
:eq:`eq:strongForm` (:math:`u_i = g_i` on :math:`\Gamma_u`).

.. math::
    \begin{split}
        \eta_i &= u_i + \alpha v_i \\
        \text{subject to } v_i &= 0 \text{ on }\Gamma_u
    \end{split}
   :label: eq:displacementVariationDefinition

Taking variation of :eq:`eq:strongToWeak2`, recalling
:eq:`eq:displacementVariationDefinition`.

.. math::
   \begin{split}
           \delta I(\eta) &= \alpha \Big[\frac{d I(\eta)}{d \alpha} \Big] \\
           &= \alpha \int_V \Big[\frac{d}{d\alpha}\big(\frac{\partial \sigma_{ij}}{\partial x_j}\eta_i \big) + \frac{d}{d\alpha}\big(B_i\eta_i \big) \Big]dV \\
           &= \alpha \int_V \Big[\big(\frac{d}{d\alpha} \frac{\partial \sigma_{ij}}{\partial x_j}\big) \eta_i + \frac{\partial \sigma_{ij}}{\partial x_j} \frac{d\eta_i}{d\alpha} + \frac{d B_i}{d\alpha}\eta_i + B_i\frac{d\eta_i}{d \alpha} \Big] dV \\
           &= \alpha \int_V \Big[\frac{\partial \sigma_{ij}}{\partial x_j} \frac{d\eta_i}{d\alpha} + B_i\frac{d\eta_i}{d \alpha} \Big] dV \\
           &= \alpha \int_V \Big[\frac{\partial \sigma_{ij}}{\partial x_j} \frac{d (u_i + \alpha v_i)}{d\alpha} + B_i\frac{d(u_i + \alpha v_i)}{d \alpha} \Big] dV \\
           &= \alpha \int_V \Big[\frac{\partial \sigma_{ij}}{\partial x_j}v_i + B_iv_i \Big] dV \\
       \end{split}

Similar to :eq:`eq:asideVariationDisplacement`, the variation of the
displacement :math:`\eta` can be written as
:math:`\delta \eta_i = \alpha v_i`. Substituting this into the above
equation.

.. math::
    \delta I(\eta) = \int_V \Big[\frac{\partial \sigma_{ij}}{\partial x_j}\delta \eta_i + B_i \delta \eta_i \Big] dV
   :label: eq:strongToWeak3


We can expand the first term in :eq:`eq:strongToWeak3` by integrating by
parts (:math:`\int_a^b fg'dx=fg|_a^b-\int_a^bf'gdx`).

.. math:: \int_V \frac{\partial \sigma_{ij}}{\partial x_j}\delta \eta_i dV = \delta \eta_i\int_V \frac{\partial \sigma_{ij}}{\partial x_j}dV - \int_V\sigma_{ij}\frac{\partial \eta_i}{\partial x_j} dV

Recalling the Gauss divergence theorem
(:math:`\int_V \frac{\partial F_{ij}}{\partial x_j}dV =\oint_S F_{ij}n_jdS`),
the above equation can be rewritten.

.. math:: \int_V \frac{\partial \sigma_{ij}}{\partial x_j}\delta \eta_i dV = \delta \eta_i\int_\Gamma \sigma_{ij}n_jd\Gamma - \int_V\sigma_{ij}\frac{\partial \delta\eta_i}{\partial x_j} dV

Where :math:`\Gamma` is the surface of the volume. Substituting the
above equation into :eq:`eq:strongToWeak3`.

.. math:: \delta I(\eta) = -\int_V\sigma_{ij}\frac{\partial \delta\eta_i}{\partial x_j} dV + \int_\Gamma \sigma_{ij}n_j \delta \eta_i d\Gamma + \int_V B_i \delta \eta_i dV

.. NOTE::
    Non-zero surface tractions (:math:`t_i=\sigma_{ij}n_j`) that are specified in :eq:`eq:strongForm` are defined along the regions :math:`\Gamma_f`. Everywhere else on the surface of the body, the surface tractions are defined to be zero (i.e. :math:`t_i=\sigma_{ij}n_j=0`). This means that the integral over parts of the surface that are not :math:`\Gamma_f` are zero. Therefore, we can change the
    second term in the above equation to only include the non-zero surface
    integrals, which only fall in the region :math:`\Gamma_f`.

.. math::
    \delta I(\eta) = -\int_V\sigma_{ij}\frac{\partial \delta\eta_i}{\partial x_j} dV + \int_{\Gamma_f}\sigma_{ij}n_j \delta \eta_i d\Gamma_f + \int_V B_i \delta \eta_i dV
    :label: eq:weakFormulation

The expression in :eq:`eq:weakFormulation` is referred to as the variational (or
or weak) formulation of :eq:`eq:strongForm`.