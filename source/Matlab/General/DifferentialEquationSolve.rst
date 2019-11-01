.. _MatlabGeneralDifferentialEquationSolve:

=============================================
Numerical Solutions of Differential Equations
=============================================
This tutorial is adapted from a seminar handout originally authored by Sandy Hnat, Anne Koelewijn, and Huawei Wang.

Purpose
"""""""
In this tutorial, we will use MATLAB to simulate a dynamics problem. Code blocks are provided for each step. 

Problem
"""""""
We will look at a simple spring damper problem, which is shown in the figure below.

.. figure:: /Matlab/img/DifferentialEquationSolveMassSpringDamper.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Mass-spring-damper system

The equation of motion of this system is as follows:

.. math::

    m\ddot{q} + b\dot{q} + kq = 0

where the mass m = 1 kg, the damping coefficient c = 2 Ns/m and the stiffness constant is k = 5 N/m. 

Solution
""""""""
This equation of motion is quite simple and could be solved analytically by solving the differential equation. However, we are going to solve this equation numerically. Later, we will use the analytical solution to see how well our numerical methods work.

.. code-block:: matlab

    % Write code to define constant paramters here:
    m = 1
    c = 2
    k = 5

Convert high oder differential equation to first order differential equation:

.. math::

    \begin{split}
        x_1 &= x \\
        x_2 &= \dot{x} \\
        \begin{bmatrix} \dot{x_1}\\ \dot{x_2} \end{bmatrix} &= \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{c}{m} \end{bmatrix} \begin{bmatrix} x_1\\ x_2 \end{bmatrix}
    \end{split}

Change the first order differential equation into incremental format:

.. math::

    \begin{bmatrix} \Delta x_1 \\ \Delta x_2 \end{bmatrix} = 
    \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{c}{m} \end{bmatrix}
    \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \cdot \Delta t

Use for loop to numerically calculate the motion of the mass-spring-damper system. Let's set total time of calculation to 6 sconds, :math:`\Delta t =0.1` second, :math:`x(0) = [1, 0]^T`.

.. code-block:: matlab

    % Write code to numerically calcuate system trajectory here:
    T = 6;
    dt = 0.1;
    x0 = [1 0]'  % x0 = [1; 0]
    t = 0:dt:T;
    x_save = zeros(2, length(t));
    x_save(:, 1) = x0;

    for i = 2:length(t)
        
        dx = [0, 1; -k/m, -c/m]*x_save(:, i-1)*dt;
        x_save(:, i) = x_save(:,i-1) + dx;
        
    end

    x_save

Plot the calculated result using plot command:

.. code-block:: matlab

    % Write plot code here
    figure(1)
    plot(t, x_save(1,:), 'ro-');
    xlabel('Time (s)');
    ylabel('X(t) (m)');

Compare with the analytical solution:

.. math:: 

    x = c_1e^{-t} \cdot sin(2t) + c_2 e^{-t}cos(2t)

With starting point :math:`[1, 0]`, then :math:`c_1 = 0.5`, :math:`c_2 = 1`.

.. code-block:: matlab

    % Write code calculate analytic motion data here
    x_real = 0.5*exp(-t).*sin(2*t) + 1*exp(-t).*cos(2*t);
    % Write code to plot analytic motion into previous plot
    hold on
    plot(t, x_real, 'b-')
    legend('numerical solution', 'analytical solution')
    hold off

.. figure:: /Matlab/img/DifferentialEquationSolveMassSpringDamperPlot1.png
    :width: 300px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Analytical and numerical solution for the mass' position vs. time.

**Why are these different?**

Zoom in to the beginning of the plot to see the difference at the second point in the numerical solution.

**Reason**: Use the derivative of one point and assume it works for all following points in .
**Solution 1**:  using smaller :math:`\Delta t`

**Solution 2**: estimate more accurate increment of :math:`x`.

.. figure:: /Matlab/img/DifferentialEquationSolveMassSpringDamperPlot2.png
    :width: 200px
    :align: center
    :alt: alternate text
    :figclass: align-center

    The first few points of the analytical and numerical solutions showing the difference in solutions.

Instead of using the derivative of time :math:`t` to calculate the increments of :math:`t + \Delta t` comparing to time :math:`t`. Value of :math:`t + \Delta t/2` is calculated first and then use the derivative of time :math:`t + \Delta t/2` to calculate the increments of :math:`t + \Delta t` comparing to time :math:`t`.

Therefore, in the for loop, the value of :math:`t + \Delta t/2` needs to be calculated first.

.. code-block:: matlab

    % Write code of middle point ODE solver here
    x_save_mid = zeros(2, length(t));
    x_save_mid(:, 1) = x0;
    for j = 2:length(t)
        
        dx_half = [0, 1; -k/m, -c/m]*x_save_mid(:, j-1)*dt/2;
        x_half = x_save_mid(:, j-1) + dx_half;
        
        dx = [0, 1; -k/m, -c/m]*x_half*dt;
        x_save_mid(:, j) = x_save_mid(:, j-1) + dx ;
        
    end

Then plot the motion comparing with real motion:

.. code-block:: matlab

    % Write code to compare the previous result with real motion
    figure(2)
    plot(t, x_save_mid(1,:), 'ro-')
    xlabel('Time (s)')
    ylabel('X(t) (m)')
    hold on
    plot(t, x_real, 'b-')
    legend('numerical solution', 'analytical solution')
    hold off

.. figure:: /Matlab/img/DifferentialEquationSolveMassSpringDamperPlot3.png
    :width: 200px
    :align: center
    :alt: alternate text
    :figclass: align-center

    The analytical and the numberical solution of mass position vs time. Note that this plot was generated using the middle point ODE solver in the numerical solution.

More higher order ode solving method can be seen here: 

`<https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods>`_

Matlab provide tool functions in ode solver: 

`<http://www.mathworks.com/help/matlab/math/choose-an-ode-solver.html>`_

Let's try to use ode45 to solve the difference equation mass-spring-damper system. The explaination of ode45 can be found here:

`<https://www.mathworks.com/help/matlab/ref/ode45.html?searchHighlight=ode45&s_tid=doc_srchtitle>`_

.. code-block:: matlab

    % Write ode45 code to calculate the system motion numerically 
    Tspan = [0, 6];
    x0 = [1, 0]';

    [t_ode45, x_ode45] = ode45(@MSD, Tspan, x0);

    % Write code to plot ode45 result here
    figure(3)
    plot(t_ode45, x_ode45(:, 1), 'ro-')
    xlabel('Time (s)')
    ylabel('X(t) (m)')
    hold on
    plot(t, x_real, 'b-')
    legend('numerical solution', 'analytical solution')
    hold off

Let's play around the options: 

`<http://www.mathworks.com/help/matlab/ref/odeset.html>`_

.. code-block:: matlab

    % Write code to set ode options and recalcualte using these options
    options = odeset('AbsTol', 1e-5)
    [t_ode45_opt, x_ode45_opt] = ode113(@MSD, Tspan, x0, options)

    % Write code to plot new ode45 result here
    figure(4)
    plot(t_ode45_opt, x_ode45_opt(:, 1), 'ro-')
    xlabel('Time (s)')
    ylabel('X(t) (m)')
    hold on
    plot(t, x_real, 'b-')
    legend('numerical solution', 'analytical solution')
    hold off

