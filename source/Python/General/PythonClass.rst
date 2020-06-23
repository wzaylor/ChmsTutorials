.. _PythonGeneralPythonClass:

============
Python Class
============
Purpose
"""""""
This tutorial introduces how to define and use a *class* in Python.

Python is an object-oriented programming language, and most variables are an object. A *class* is used to construct objects.
There are two features of objects that this tutorial covers:

#) *attribute*: Attributes are variables that "belong to" an object.
#) *method*: Methods are functions that "belong to" an object.

Readers are encouraged to run the examples below using the *debugging* tool in PyCharm.

Defining a Class
""""""""""""""""
The highlighted lines in the code block below show how to define a class called *foo* that has one attribute with a variable named *bar*.

.. code-block:: python
    :emphasize-lines: 1, 2

    class foo(object):
        bar = 'helloworld'

    buzz = foo()
    print(buzz.bar)

Most of the time you will use an method with a special name ``__init__``

The ``__init__`` method is called when the class is defined/initialized. Run the example below in *debugging*, and notice how the ``__init__`` method is called at the line ``buzz = foo()`` (in PyCharm, place a breakpoint at that line, run in debugging, then use the step-into button).

.. code-block:: python
    :emphasize-lines: 2,3

    class foo(object):
        def __init__(self):
            self.bar = 'helloworld'

    buzz = foo()
    print(buzz.bar)

Attributes
""""""""""
Attributes are variables that "belong to" the object that a class defines.

**What is** ``self``? When we define a class, we can (and should) define the attributes inside that class definition. The object that is being constructed is represented by a variable that is called ``self`` (note that *self* is the name that is used by convention. This can be called any name, such as *Susan*, but that is not recommended). Below is an example that may better define how ``self`` is used.

.. code-block:: python
    :emphasize-lines: 3-5

    class Person(object):
        def __init__(self, f_name, l_name, heightInches):
            self.firstName = f_name
            self.lastName = l_name
            self.height = heightInches

    DrDavis = Person('Brian', 'Davis', 70.)
    DrSchearer = Person('Eric', 'Schearer', 71.)
    print(DrDavis.firstName)
    print(DrSchearer.firstName)

Below is an example of what you see if run the above example in debugging. **Notice** how the object/variables ``DrDavis`` and ``DrSchearer`` both have the same attributes, however the attributes have different values.

The ability to have the same structure that is populated with different values is extremely useful.

.. image:: /Python/General/img/PersonExample.png
   :width: 400px

Methods
"""""""
Methods are functions that belong to object.

A method always has at least one input variable, and that variable is the current instance of the object (usually called ``self``). Again, this is better explained by example. We will make a method that converts ``self.height`` from inches to cm.

**Notice** in the example below, how the method ``getHeight_cm`` has one input called ``self``, and how that input is used to gain access to the object's attribute ``self.height``.

.. code-block:: python
    :emphasize-lines: 7, 13

    class Person(object):
        def __init__(self, f_name, l_name, heightInches):
            self.firstName = f_name
            self.lastName = l_name
            self.height = heightInches

        def getHeight_cm(self):
            heightcm = self.height*2.54 # Assume self.height is in inches.
            return heightcm

    DrDavis = Person('Brian', 'Davis', 70.)
    DrSchearer = Person('Eric', 'Schearer', 71.)
    foo = DrDavis.getHeight_cm()
    print(foo)

Below is what you see when you run the above example in debugging. **Notice** how we called the ``getHeight_cm`` method for the ``DrDavis`` object, and how the attributes associated with the ``DrDavis`` object are available under ``self``.

**Also notice** how even though there is another instance of the person class (``DrSchearer``), there is no confusion between the data stored in ``DrDavis`` and ``DrSchearer``.

**Furthermore notice** how ``heightcm`` is defined in the ``getHeight_cm`` method, however it is not an attribute (i.e. it is not part of ``self``). Run the above example in debugging and stop at the ``print(foo)`` line. Notice how there is no variable named ``heightcm``. Sometimes we do not need to keep the intermediate variables that we define (though technically ``foo`` has the same value as ``heightcm``. This behavior is more apparent in more complex applications).

.. image:: /Python/General/img/PersonHeightExample.png
   :width: 400px

Finally, we can pass input parameters into methods in the same way that we pass inputs into a function.

Below is an example that takes an input parameter ``hasMustache`` and creates and returns a string variable.

.. code-block:: python
    :emphasize-lines: 11, 23, 24

    class Person(object):
        def __init__(self, f_name, l_name, heightInches):
            self.firstName = f_name
            self.lastName = l_name
            self.height = heightInches

        def getHeight_cm(self):
            heightcm = self.height*2.54 # Assume self.height is in inches.
            return heightcm

        def getMustacheStatus(self, hasMustache):
            # Check if 'hasMustache' is True.
            if hasMustache is True:
                # Construct a string variable and insert specific values
                txt = f'Dr. {self.firstName} {self.lastName} does have a mustache.'
            else:
                # Construct a string variable and insert specific values
                txt = f'Dr. {self.firstName} {self.lastName} does not have a mustache.'
            return txt

    DrDavis = Person('Brian', 'Davis', 70.)
    DrSchearer = Person('Eric', 'Schearer', 71.)
    foo = DrDavis.getMustacheStatus(True)
    bar = DrSchearer.getMustacheStatus(False)

    print(foo)
    print(bar)

Good Habits
"""""""""""
It is generally a good habit to define all of your attributes in the ``__init__`` method. This makes your code easier to read and ensures consistency between objects that use the same class.

From a practical standpoint, we may not have all of our attributes available when we define a class. In that case we can assign place-holder values for the attributes (usually ``None``). For example, we could create the ``Person`` class that doesn't take any inputs to the ``__init__`` method, and we can define methods that reassign the values for the attributes.

.. code-block:: python
    :emphasize-lines: 21-23

    class Person(object):
        def __init__(self):
            self.firstName = None
            self.lastName = None
            self.height = None

        def setName(self, f_name, l_name):
            self.firstName = f_name
            self.lastName = l_name
            return

        def setHeight(self, height_in):
            self.height = height_in
            return

        def getHeight_cm(self):
            heightcm = self.height*2.54 # Assume self.height is in inches.
            return heightcm

    DrDavis = Person()
    DrDavis.setName('Brian', 'Davis')
    DrDavis.setHeight(70.)
    foo = DrDavis.getHeight_cm()
    print(foo)

Note that methods are not required to define attributes, but it is a good habit to assign all of the object's attributes inside the class definition, and using methods dedicated to assigning attribute values is one approach that can be used. For completeness, we can also define attributes outside of a class, however this is a bad habit. For example, we can append the above example (say below ``foo = DrDavis.getHeight_cm()``) with the line ``DrDavis.bad_Habit_Dont_Do_This = 666``.