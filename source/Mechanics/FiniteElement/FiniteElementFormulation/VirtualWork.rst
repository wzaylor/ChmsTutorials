.. _FiniteElementFormulationVirtualWork:

Virtual Work
""""""""""""

We will start with an aside on virtual work.

Note: Much of this is from *Energy and Variational Methods in Applied Mechanics* by J.N. Reddy, pg. 107.

Consider the functional :math:`I(u)` (i.e. a function that acts on
functions, and not values from the space)

.. math::
    I(u) = \int_a^b F(x, u, u')
    :label: eq:asideFunctional

Where :math:`u' = \frac{\partial u}{\partial x}` in (:eq:`eq:asideFunctional`). This functional is
subject to the boundary conditions

.. math::
    \begin{split}
        u(a) &= u_a \\
        u(b) &= u_b
    \end{split}
   :label: eq:asideFunctionalBCs


Any candidate function that minimizes :math:`I(u)` should satisfy the
boundary conditions. Additionally, any candidate function should be
differentiable. The set of the functions that are differentiable (at
least once), and satisfy the boundary conditions are called *candidate
functions*. An element :math:`u` from the set of admissable functions
can have the following form.

.. math::
    u = u_0 + \alpha v
   :label: eq:asideUFunction


where :math:`u_0` is the unknown function that minimizes :math:`I(u)`,
:math:`\alpha` is a constant, and :math:`v` is a differentiable function
that satisfies the homogeneous form of the boundary conditions of
:math:`I(u)` (:eq:`eq:asideFunctionalBCs`).

.. math::
    \begin{split}
        v(a) &= 0 \\
        v(b) &= 0
    \end{split}
   :label: eq:asideVariationBCs

The set of all functions :math:`v` that satisfy the boundary conditions
(:eq:`eq:asideVariationBCs`) and hold for :eq:`eq:asideUFunction` are called the
set of *admissable variations*.

**We are seeking** a function :math:`u_0(x)` that makes the functional
:math:`I(u)` (:eq:`eq:asideFunctional`) a minimum. Recalling
:eq:`eq:asideUFunction`, the functional :math:`I(u)` (:eq:`eq:asideFunctional`)
is defined to attain a minimum when :math:`\alpha=0`. The derivative of
:math:`I(u)` with respect to :math:`\alpha` is zero when :math:`I(u)` is
minimized. Recognizing that when :math:`u` and :math:`v` are fixed
:math:`I(u) = I(u_0 + \alpha v) = I(\alpha; u_0, v)`. Therefore, the
derivative if :math:`I(u)` with respect to :math:`\alpha` is
:math:`\frac{d I(u)}{d\alpha}`.

.. math::
           \begin{split}
               0 &= \frac{d I(u_0 + \alpha v)}{d\alpha}|_{\alpha=0} \\
               &= \frac{d I(u)}{d\alpha}|_{\alpha=0} \\ 
               &= \frac{d}{d\alpha} \Big[\int_a^b F(x, u, u')dx \Big] |_{\alpha=0} \\
               &= \int_a^b \frac{d}{d\alpha}\big[F(x, u, u')\big]|_{\alpha=0} dx \\
               &= \int_a^b \Big(\frac{\partial F}{\partial u}\frac{\partial u}{\partial \alpha} + \frac{\partial F}{\partial u'}\frac{\partial u'}{\partial \alpha}\Big) |_{\alpha=0}  dx  \\
               &= \int_a^b \Big(\frac{\partial F}{\partial (u_0 + \alpha v)}\frac{\partial (u_0 + \alpha v)}{\partial \alpha} + \frac{\partial F}{\partial (u_0' + \alpha v')}\frac{\partial (u_0' + \alpha v')}{\partial \alpha}\Big) |_{\alpha=0}  dx  \\
               &= \int_a^b \Big(\frac{\partial F}{\partial u_0}v + \frac{\partial F}{\partial u_0'}v' \Big)  dx  \\
           \end{split}
   :label: eq:asideMinimum1

Now we have an expression for the minimum of :math:`I(u)`, but
:math:`u_0` is still unknown, and the variation :math:`v` and its
derivative (:math:`v'`) are also introduced and arbitrarily defined.

We can simplify the expression in :eq:`eq:asideMinimum1` by integrating the
second term by parts
(:math:`\int_a^b g h' dx = gh|_a^b-\int_a^b g'h dx`).

.. math:: \int_a^b \frac{\partial F}{\partial u_0'}v' dx = \frac{\partial F}{\partial u_0'}v|_a^b - \int_a^b v\frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big)dx

Substituting the above equation into :eq:`eq:asideMinimum1`, and recalling
:eq:`eq:asideVariationBCs`.

.. math::
           \begin{split}
               0 &= \int_a^b \Big[\frac{\partial F}{\partial u_0}v - v\frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) \Big] dx + \frac{\partial F}{\partial u_0'}v|_a^b \\
               &= \int_a^b \Big[\frac{\partial F}{\partial u_0}v - v\frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) \Big] dx + \frac{\partial F}{\partial u_0'}v(b) - \frac{\partial F}{\partial u_0'}v(a) \\
               &= \int_a^b v\Big[\frac{\partial F}{\partial u_0} - \frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) \Big] dx \\
           \end{split}
   :label: eq:asideMinimum2

The variation (:math:`v`) has an arbitrary value inside the interval
:math:`(a,b)`, so the expression inside the brackets of
:eq:`eq:asideMinimum2` is identically zero.

.. math::
           \frac{\partial F}{\partial u_0} - \frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) = 0 \text{ in } a < x < b
   :label: eq:asideEulerEq

So the admissable function that satisfies :eq:`eq:asideEulerEq` minimizes
the functional :math:`I(u)`.

**The variation of the functional** :math:`I(u)` is defined as

.. math::
           \delta I(u) = \alpha \Big[\frac{d I(x,u,u')}{d\alpha} \Big]|_{\alpha=0}
   :label: eq:asideVariationDefinition

Recognizing that :eq:`eq:asideMinimum2` can be substituted for
:math:`\frac{d I(x,u,u')}{d\alpha}|_{\alpha=0}`, the variation in the
functional can also be rewritten.

.. math::
           \delta I(u) = \int_a^b \alpha v\Big[\frac{\partial F}{\partial u_0} - \frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) \Big] dx
   :label: eq:asideVariationFunctional

Similarly, the variation of :math:`u` (recalling :eq:`eq:asideUFunction`)
can be written as :math:`\alpha v`.

.. math::
    \begin{split}
        \delta u &= \alpha \Big[\frac{d (u + \alpha v)}{d \alpha}|_{\alpha=0}\Big] \\
        &= \alpha v
    \end{split}
   :label: eq:asideVariationDisplacement

Therefore, the variation in the functional :math:`I(u)` can be
expressed as

.. math:: \delta I(u) = \int_a^b \delta u\Big[\frac{\partial F}{\partial u_0} - \frac{d}{dx}\Big(\frac{\partial F}{\partial u_0'} \Big) \Big] dx
