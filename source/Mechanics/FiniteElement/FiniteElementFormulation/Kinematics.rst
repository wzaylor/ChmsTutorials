.. _FiniteElementFormulationKinematics:

Kinematics
""""""""""
We will start the discussion of kinematics by first defining strain. Note that this **does not** assume small strains.

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
    \Delta S^0 = \delta_{ij} \Delta X_i \Delta X_j

And similarly the distance between the points :math:`Q^1` and :math:`Q^2` is defined as

.. math::
    \Delta S^T = \delta_{ij} \Delta x_i \Delta x_j

We will define a measure of strain (:math:`\psi`) as the difference in the squared distance between points at time :math:`t` and time :math:`t_0` (:eq:`fea:kinematicsStrainDistance0`).

.. math::
    \psi = (\Delta S^t)^2 - (\Delta S^0)^2
    :label: fea:kinematicsStrainDistance0

Notice that this is a scalar value, which is invariant, meaning that it is the same value no matter what coordinate system it is defined with respect to. The following sections will defined this strain metric with respect to either the reference configuration (:ref:`Lagrangian strain<FiniteElementFormulationKinematicsLagrangianStrain>`), or the deformed configuration (:ref:`Eularian strain<FiniteElementFormulationKinematicsEularianStrain>`).

.. _FiniteElementFormulationKinematicsLagrangianStrain:

Lagrangian Strain
'''''''''''''''''
Earlier we defined a general defintion of strain (:eq:`fea:kinematicsStrainDistance0`).

.. _FiniteElementFormulationKinematicsEularianStrain:

Eularian Strain
'''''''''''''''
Earlier we defined a general defintion of strain (:eq:`fea:kinematicsStrainDistance0`), however this definition was relatively general.