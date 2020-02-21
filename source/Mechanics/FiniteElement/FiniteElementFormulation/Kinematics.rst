.. _FiniteElementFormulationKinematics:

Kinematics
""""""""""
We will start the discussion of kinematics by first defining strain. Note that this **does not** assume small strains.

These derivations parallel those in Thomas B. Bahder's article *Transformation Properties of the Lagrangian and Eularian Strain Tensors*. (`<https://arxiv.org/pdf/physics/0211003.pdf>`_)

.. _FiniteElementFormulationKinematicsDistanceBetweenPoints:

Distance Between Points
'''''''''''''''''''''''
We will start by considering two points that are part of a larger body. These points have positions :math:`P^1` and :math:`P^2` at time :math:`t_0=0` (:numref:`FiniteElementFormulationKinematicsDistance`). These two points are close together, but they are separated by a distance :math:`\Delta S^0`. At a later time (:math:`t>t_0`), the body undergoes some deformation, and these two points move to new positions (:math:`Q^1`, :math:`Q^2`), and these new points are separated by a distance :math:`\Delta S^t`.

.. _FiniteElementFormulationKinematicsDistance:

.. figure:: /Mechanics/FiniteElement/FiniteElementFormulation/img/DeformationLengthChange.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    The position of two points before and after some deformation at time :math:`t`. The red line shows the path of the particles, and the dashed lines show the displacement between points.

.. sidebar:: A note on coordinate systems

    The points :math:`P^1` and :math:`P^2` are defined with respect to the **reference configuration**, where the points have coordinates denoted with capitol letters and indicies. The points have coordinates defined with respect to the reference (:math:`X_A`) coordinate system, :math:`P^1 = X_A^1` and :math:`P^2=X_A^2`.

    Similarly, the points :math:`Q^1` and :math:`Q^2` are defined with respect to the **deformed configuration**, where the points have coordinates denoted with lower case letters and indicies. The points have coordinates defined with respect to the deformed (:math:`x_i`) coordinate system :math:`Q^1 = x_i^1` and :math:`Q^2=x_i^2`.

The distance between the points :math:`P^1` and :math:`P^2` is defined as

.. math::
    \Delta S^0 = \delta_{AB} \Delta X_A \Delta X_B

And similarly the distance between the points :math:`Q^1` and :math:`Q^2` is defined as

.. math::
    \Delta S^t = \delta_{ij} \Delta x_i \Delta x_j

We will define a measure of strain (:math:`\psi`) as the difference in the squared distance between points at time :math:`t` and time :math:`t_0` (:eq:`fea:kinematicsStrainDistance0`).

.. math::
    \psi = (\Delta S^t)^2 - (\Delta S^0)^2
    :label: fea:kinematicsStrainDistance0

The distance between points :math:`Q^1` and :math:`Q^2` (:numref:`FiniteElementFormulationKinematicsDistance`) can be expressed as :math:`\Delta S^t = \sqrt{\delta_{ij}\Delta x_i \Delta x_j}`. Similarly, the distance between points :math:`P^1` and :math:`P^2` can be expressed as :math:`\Delta S^0 = \sqrt{\delta_{AB}\Delta X_A \Delta X_B}`. In Cartesian coordinates, :math:`\Delta x_i = x^2_i - x^1_i`. Similarly :math:`\Delta X_A = X^2_A - X^1_A`. Substituting these expressions into :eq:`fea:kinematicsStrainDistance0`.

.. math::
    \begin{split}
    \psi &= (\Delta S^t)^2 - (\Delta S^0)^2 \\
    &= \big(\sqrt{\delta_{ij}\Delta x^1_i \Delta x^2_j}\big)^2 - \big(\sqrt{\delta_{AB}\Delta X^1_A \Delta X^2_B}\big)^2\\
    &= \delta_{ij}\Delta x_i \Delta x_j - \delta_{AB}\Delta X_A \Delta X_B \\
    &= \delta_{ij}(x^2_i - x^1_i)(x^2_j - x^1_j) - \delta_{AB}(X^2_A - X^1_A)(X^2_B - X^1_B)\\
    \end{split}
    :label: fea:kinematicsStrainDistance1

Notice that this is a scalar value, which is invariant, meaning that it is the same value no matter what coordinate system it is defined with respect to. However the values that are used to define :math:`\psi` in :eq:`fea:kinematicsStrainDistance1` are defined with respect to the reference (:math:`X_i`) or the deformed (:math:`x_i`) configuration. The following sections will defined this strain metric with respect to either the reference configuration (:ref:`Lagrangian strain<FiniteElementFormulationKinematicsLagrangianStrain>`), or the deformed configuration (:ref:`Eularian strain<FiniteElementFormulationKinematicsEularianStrain>`).

.. _FiniteElementFormulationKinematicsLagrangianStrain:

Lagrangian Strain
'''''''''''''''''
Earlier we defined strain as the difference in distance between two points at time :math:`t` and time :math:`t=t_0=0` (:eq:`fea:kinematicsStrainDistance1`). If we relate our coordinates to the reference configuration (the configuration at :math:`t=t_0=0`), then the coordinates of the points (:math:`Q^1`, :math:`Q^2` :numref:`FiniteElementFormulationKinematicsDistance`) at time :math:`t\geq 0` are functions of the coordinates of the reference configuration.

.. math::
    x_i = x_i(X_A, t)

We can input the coordinates of points :math:`P^1` and :math:`P^2` into the above equation to define the coordinates of those points at different times (i.e. at different deformations). For example we can use :math:`X_A=P^1_A` at :math:`t>0`, then :math:`x_i(P^1_A, t) = x^1_i` (and similarly for :math:`P^2`). If we do the same at :math:`t=0`, then :math:`x_i(P^1_A, t=0) = P^1_A`.

Now, **we will make two assumptions**
    #) The points :math:`P^1` and :math:`P^2` are infinitesimally separated
    #) Assume continuity in the body as it deforms

As a result of these assumptions :math:`Q^1` and :math:`Q^2` are also infinitesimally separated. Note that the distance between points :math:`P^M` and :math:`Q^m` are not necessarily infinitesimal.

Consider one point :math:`x^2_i=x_i(X^2_A,t)`, and use a Taylor series expansion about the position of the point :math:`x^1_i(X^1_A,t)` (recall that as a result of the previously mentioned assumptions, the points :math:`Q^1 =x^1_i(X^1_A,t)` and :math:`Q^2 =x^2_i(X^2_A,t)` are infinitesimally close).

.. math::
    \begin{split}
    x^2_i &= x_i(X^1_A,t) + \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)dX_A + \ldots \\
    &= x_i(X^1_A,t) + \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)(X^2_A - X^1_A) + \ldots \\
    \end{split}

Recall from a :ref:`previous section<FiniteElementFormulationKinematicsDistanceBetweenPoints>` that :math:`\Delta x_i = x^2_i - x^1_i`. Substituting the above equation in the the expression for :math:`\Delta x_i`. Also neglecting the higher order terms because :math:`P^1` and :math:`P^2` are infinitesimally close, and noting that :math:`x^1_i=x_i(X^1_A,t)`.

.. math::
    \begin{split}
    \Delta x_i &= x^2_i - x^1_i \\
    &= x_i(X^1_A,t) + \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)(X^2_A - X^1_A) - x^1_i \\
    &= \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)(X^2_A - X^1_A)
    \end{split}

Noting that :math:`\Delta X_A = X^2_A - X^1_A`, the above equation can be rewritten.

.. math::
    \begin{split}
    \Delta x_i &= \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)(X^2_A - X^1_A) \\
    &= \Big(\frac{\partial x_i(X_A,t)}{\partial X_A}|_{X_A=X^1_A}\Big)\Delta X_A
    \end{split}

Substituting the above equation into :eq:`fea:kinematicsStrainDistance1`.

.. math::
    \begin{split}
    \psi &= \delta_{ij}\Delta x_i \Delta x_j - \delta_{AB}\Delta X_A \Delta X_B \\
    &= \delta_{ij}\Big(\frac{\partial x_i(X^1_A,t)}{\partial X_A}\Delta X_A\Big) \Delta x_j - \delta_{AB}\Delta X_A \Delta X_B \\
    &= \delta_{ij}\Big(\frac{\partial x_i(X^1_A,t)}{\partial X_A}\Delta X_A\Big) \Big(\frac{\partial x_j(X^1_B,t)}{\partial X_B}\Delta X_B\Big) - \delta_{AB}\Delta X_A \Delta X_B \\
    &= \Big[\delta_{ij}\Big(\frac{\partial x_i(X^1_A,t)}{\partial X_A}\Big) \Big(\frac{\partial x_j(X^1_B,t)}{\partial X_B}\Big) - \delta_{AB}\Big]\Delta X_A \Delta X_B \\
    \end{split}
    :label: fea:kinematicsStrainLagrangian

The term inside the brackets in :eq:`fea:kinematicsStrainLagrangian` is *similar* to the Lagrangian strain tensor (:math:`E_{AB}`). We multiply the expression by :math:`\frac 12` to define Lagrangian strain. *Note that if strain happens to be infinitesimally small, then the definition of Lagrange strain is the same as engineering strain. The two definitions diverge as strain increases.*

.. math::
    \boxed{
    E_{AB} = \frac{1}{2}\Big[\delta_{ij}\Big(\frac{\partial x_i(X_A,t)}{\partial X_A}\Big) \Big(\frac{\partial x_j(X_B,t)}{\partial X_B}\Big) - \delta_{AB}\Big]}
    :label: fea:kinematicsLagrangeStrain

Substutituing :eq:`fea:kinematicsLagrangeStrain` into :eq:`fea:kinematicsStrainLagrangian`.

.. math::
    \psi = 2E_{AB}\Delta X_A \Delta X_B

**Notice** that all of the terms in :eq:`fea:kinematicsLagrangeStrain` and :eq:`fea:kinematicsStrainLagrangian` are defined with respect to coordinates in the reference coordinate system (:math:`X_A`).

.. _FiniteElementFormulationKinematicsEularianStrain:

Eularian Strain
'''''''''''''''
Earlier we defined strain as the difference in distance between two points at time :math:`t` and time :math:`t=t_0=0` (:eq:`fea:kinematicsStrainDistance1`). If we relate our coordinates to the deformed configuration (the configuration at :math:`t>0`), then the coordinates of the points (:math:`P^1`, :math:`P^2` :numref:`FiniteElementFormulationKinematicsDistance`) at time :math:`t=0` are functions of the coordinates of the deformed configuration.

.. math::
    X_A = X_A(x_i, t)

We can input the coordinates of points :math:`Q^1` and :math:`Q^2` into the above equation to define the coordinates of those points at different times (i.e. at different deformations). For example we can use :math:`x_i=Q^1_i` at :math:`t>0`, then :math:`X_A(Q^1_i, t) = X^1_A` (and similarly for :math:`Q^2`). If we do the same at :math:`t=0`, then :math:`X_A(Q^1_i, t=0) = P^1_A`.

Now, **we will make two assumptions**
    #) The points :math:`Q^1` and :math:`Q^2` are infinitesimally separated
    #) Assume continuity in the body as it deforms

As a result of these assumptions :math:`P^1` and :math:`P^2` are also infinitesimally separated. Note that the distance between points :math:`P^M` and :math:`Q^m` are not necessarily infinitesimal.

Consider one point :math:`X^2_A=X_A(x^2_i,t)`, and use a Taylor series expansion about the position of the point :math:`X^1_A(x^1_i,t)` (recall that as a result of the previously mentioned assumptions, the points :math:`P^1 =X^1_A(x^1_i,t_0)` and :math:`P^2 =X^2_A(x^2_i,t_0)` are infinitesimally close).

.. math::
    \begin{split}
    X^2_A &= X_A(x^1_i,t) + \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)dx_i + \ldots \\
    &= X_A(x^1_i,t) + \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)(x^2_i - x^1_i) + \ldots \\
    \end{split}

Recall from a :ref:`previous section<FiniteElementFormulationKinematicsDistanceBetweenPoints>` that :math:`\Delta X_A = X^2_A - X^1_A`. Substituting the above equation in the the expression for :math:`\Delta X_A`. Also neglecting the higher order terms because :math:`Q^1` and :math:`Q^2` are infinitesimally close, and noting that :math:`X^1_A=X_A(x^1_i,t)`.

.. math::
    \begin{split}
    \Delta X_A &= X^2_A - X^1_A \\
    &= X_A(x^1_i,t) + \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)(x^2_i - x^1_i) - X^1_A \\
    &= \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)(x^2_i - x^1_i)
    \end{split}

Noting that :math:`\Delta x_i = x^2_i - x^1_i`, the above equation can be rewritten.

.. math::
    \begin{split}
    \Delta X_A &= \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)(x^2_i - x^1_i) \\
    &= \Big(\frac{\partial X_A(x_i,t)}{\partial x_i}|_{x_i=x^1_i}\Big)\Delta x_i
    \end{split}

Substituting the above equation into :eq:`fea:kinematicsStrainDistance1`.

.. math::
    \begin{split}
    \psi &= \delta_{ij}\Delta x_i \Delta x_j - \delta_{AB}\Delta X_A \Delta X_B \\
    &= \delta_{ij}\Delta x_i \Delta x_j - \delta_{AB}\Big(\frac{\partial X_A(x^1_i,t)}{\partial x_i}\Delta x_i\Big) \Delta X_B \\
    &= \delta_{ij}\Delta x_i \Delta x_j - \delta_{AB}\Big(\frac{\partial X_A(x^1_i,t)}{\partial x_i}\Delta x_i\Big) \Big(\frac{\partial X_B(x^1_j,t)}{\partial x_j}\Delta x_j\Big)\\
    &= \Big[\delta_{ij} - \delta_{AB}\Big(\frac{\partial X_A(x^1_i,t)}{\partial x_i}\Big) \Big(\frac{\partial X_B(x^1_j,t)}{\partial x_j}\Big) \Big]\Delta x_i \Delta x_j
    \end{split}
    :label: fea:kinematicsStrainEularian

The term inside the brackets in :eq:`fea:kinematicsStrainEularian` is *similar* to the Eularian strain tensor (:math:`e_{ij}`). We multiply the expression by :math:`\frac 12` to define Eularian strain. *Note that if strain happens to be infinitesimally small, then the definition of Eularian strain is the same as engineering strain. The two definitions diverge as strain increases.*

.. math::
    \boxed{
    e_{ij} = \frac{1}{2}\Big[\delta_{ij} - \delta_{AB}\Big(\frac{\partial X_A(x^1_i,t)}{\partial x_i}\Big) \Big(\frac{\partial X_B(x^1_j,t)}{\partial x_j}\Big)\Big]}
    :label: fea:kinematicsEularianeStrain

Substutituing :eq:`fea:kinematicsEularianeStrain` into :eq:`fea:kinematicsStrainEularian`.

.. math::
    \psi = 2e_{ij}\Delta x_i \Delta x_j

**Notice** that all of the terms in :eq:`fea:kinematicsEularianeStrain` and :eq:`fea:kinematicsStrainEularian` are defined with respect to coordinates in the deformed coordinate system (:math:`x_i`).

.. _FiniteElementFormulationKinematicsDeformationGradient:

Deformation Gradient
''''''''''''''''''''
