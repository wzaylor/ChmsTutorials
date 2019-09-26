.. _DocumentationWebsiteCreateNewTutorial:

Create A New Tutorial
"""""""""""""""""""""
Purpose
'''''''
The purpose of this tutorial is to describe how to use Sphinx to create/build a new tutorial (so meta...)

These tutorials are written in reStructredText, and a program called Sphinx is used to convert reStructuredText files into .html format. The html files can be directly loaded onto the lab website. This allows for a wiki-style documentation.

This tutorial will describe how to generate tutorials, such as this one, while also demonstrating features that you may want to include in your own tutorials.

Software
''''''''
Placeholder

.. _DocumentationWebsiteCreateNewTutorialGithub:

Clone Github tutorials repository
'''''''''''''''''''''''''''''''''
These tutorials are stored on a public repository located here: `<https://github.com/CSU-CHMS/ChmsTutorials>`_. For users who are unfamiliar with using a git repository, please follow the instructions below to *clone* the repository then see the :ref:`DocumentationWebsiteCreateNewTutorialGithubWorkflow` section for a description of the general workflow you will use to add and update files in the repository.

You will clone the repository to your local computer once. This is different from simply downloading the repository because *cloning* allows you to push your changes back into the public repository. Follow these steps to clone the repository:

#) Create an account on github (`<https://github.com/join>`_)
#) Download and install *git*
    
    For Windows users, download from here, `<https://git-scm.com/>`_, and install the file.

    For linux/ubuntu users, open a terminal and enter these commands to install git using ``apt-get``
    
    .. code-block:: none

        sudo apt install git

#) Open a terminal (or a command window in Windows) and navigate to a directory where you plan on keeping the repository. For example, ``/home/user-name/Projects`` or ``C:\Projects``
#) Go the the repository (`<https://github.com/CSU-CHMS/ChmsTutorials>`_) and copy the clone link.

    .. figure:: /Documentation/img/WebsiteTutorialGithubClone1.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

#) In the terminal, enter this command (*paste the clone link*) ``git clone **clone-link**``

    .. figure:: /Documentation/img/WebsiteTutorialGithubClone2.png
            :width: 400px
            :align: center
            :alt: alternate text
            :figclass: align-center

Now you have successfully clone the *ChmsTutorials* repository. You will not need to repeat this process on your local computer. See the :ref:`DocumentationWebsiteCreateNewTutorialGithubWorkflow` section for a description of the workflow you will use to make changes to the repository.

.. _DocumentationWebsiteCreateNewTutorialGithubWorkflow:

Git reposotory - General workflow
---------------------------------
This section describes the general workflow that is used when making changes to a git repository. This assumes that you already have a :ref:`clone<DocumentationWebsiteCreateNewTutorialGithub>` of a repository. This section describes how to use built-in tools in the text editor *PyCharm*. Experienced users may use their preferred means of *pulling* and *pushing* changes to the repository.

#) You will *clone* the repository onto your local computer. This is done once.
#) e
#) Make changes to the files in the repository
#) *commit* your changes. This is 


#) Open the repository (`<https://github.com/CSU-CHMS/ChmsTutorials>`_)

Creating a Document
'''''''''''''''''''
To create a new document/webpage, first you should create a text file with a ``.rst`` extension somewhere in the ``path/to/CHMS_website/ChmsTutorials/source`` directory. To keep things organized, create this file in an appropriate directory. For example, put *general python* documentation in ``path/to/CHMS_website/ChmsTutorials/source/Python/General``. Note, a text editor such as :ref:`PyCharm<PythonGeneralPythonSetup>` or ``Visual Studio Code`` can have reStructuredText extensions installed to provide syntax highlighting and other convenient features.

.. Note:: The name of the new document can be arbitrarily assigned. However to keep things organized, please give the document a relevant and descriptive name.

Including Document/Tutorial in website
--------------------------------------
``toctree`` is used to organize the different tutorials and provide links to the main Tutorials webpage. The content of the main Tutorials webpage is in ``path/to/CHMS_website/ChmsTutorials/source/index.rst``. *index.rst* contains a *toctree* that links to pages that are used to organize high-level content. For example, the following code-block is in *index.rst*, and it links to ``path/to/CHMS_website/ChmsTutorials/source/Python/PythonTutorials.rst`` and ``path/to/CHMS_website/ChmsTutorials/source/Documentation/DocumentationTutorials.rst``

.. code-block:: none

    .. toctree::
      :maxdepth: 2
      :caption: Contents:

      /Python/Python.rst
      /Documentation/Documentation.rst

Notice how the path starts after ``source``.

Add the name of your newly created document/tutorial to the appropriate *toctree* to include it in the website. To keep things organized, there are several levels of *toctree* for different tutorial subjects. For example, this tutorial is included in the webpage with the *toctree* located in ``path/to/ChmsTutorials/source/Documentation/Website_tutorials/Website_tutorials.rst``. The name of this tutorial's *.rst* file is ``CreateNewTutorial.rst``. The following code-block shows the *toctree* in ``Website_tutorials.rst``

.. code-block:: none

    .. toctree::
      :maxdepth: 2
      :caption: Contents:

      /Documentation/Website_tutorials/CreateNewTutorial.rst

Document Content
----------------
The ``.rst`` file contains the content of the document/tutorial. See the :ref:`example<DocumentationWebsiteCreateNewTutorialExample>` below for a general walkthrough that includes basic content.

You can use other tutorials as an example for the content. You can see the content of any *.rst* file in these tutorials by clicking the ``Page source`` link at the bottom of any tutorial.

.. figure:: /Documentation/img/WebsiteTutorialPageSource.png
    :width: 500px
    :align: center
    :alt: alternate text
    :figclass: align-center

Building a Document
'''''''''''''''''''
To build the documentation, open a terminal (or a command window in Windows), and navigate to the directory ``path/to/CHMS_website/ChmsTutorials``, and enter this command:

.. code-block:: none

    sphinx-build -b dirhtml source ../chms/tutorials

This command means the following: ``sphinx-build`` calls the program that is used to build the documentation. ``-b dirhtml`` specifies that the builder name is ``dirhtml``. The ``dirhtml`` builder makes HTML pages. ``source`` specifies that the source code is in the directory names ``source``. ``../chms/tutorials`` is a relative path to the directory where the .html files are built in. See `<https://www.sphinx-doc.org/en/1.2/invocation.html>`_ for more information.

When you build a document, you are generating html code from the reStructuredText files that you have created. These changes are only made on your computer, and there are two ways to view the documents/changes that you have made.

    #) Manually open ``path/to/CHMS_website/chms/index.html`` in a web browser, then navigate to the page that you create/changed.
    #) More experienced users can run a local server. Open a terminal (or a command window in Windows), and change directory to ``path/to/CHMS_website/chms``. Enter the command ``python -m http.server`` and in a web browser, go to the website ``http://localhost:8000/``. Navigate to the page that you create/changed.

.. _DocumentationWebsiteCreateNewTutorialExample:

Hello_World Example Walkthrough
'''''''''''''''''''''''''''''''
This example describes how to create a new webpage/tutorial called ``Hello_World`` that is located in the ``Website_tutorials`` section of the website.

First, you should :ref:`clone the ChmsTutorials repository<DocumentationWebsiteCreateNewTutorialGithub>`. After you have done that, follow these steps.

#) Create a file called ``Hello_World.rst`` in the directory ``path/to/ChmsTutorials/source/Documentation/Website_tutorials``

    .. figure:: /Documentation/img/WebsiteTutorialHelloWorldFile.png
        :width: 150px
        :align: center
        :alt: alternate text
        :figclass: align-center

#) Put a header and some basic content in ``Hello_World.rst``

    .. code-block:: none

        ===============
        Test Header!!!!
        ===============
        Words are here!

        A subheader!
        """"""""""""
        More words!

    .. NOTE:: The equal signs ``===============`` and quotation marks ``""""""""""""`` are used to define a heading and subheading. These should be consistent throughout a *.rst* file, but there are no standard characters used for headings and subheadings. Sphinx sorts out the headings somehow in the buld process.

#) Include ``Hello_World.rst`` in the *toctree* located in ``ChmsTutorials/source/Documentation/Website_tutorials/Website_tutorials.rst`` The code-block below demonstrates this *toctree* in ``Website_tutorials.rst``

    .. code-block:: none

        .. toctree::
            :maxdepth: 2
            :caption: Contents:

            /Documentation/Website_tutorials/CreateNewTutorial.rst
            /Documentation/Website_tutorials/Hello_World.rst

    .. NOTE:: Indentations are used to specify the contents of ``.. toctree::``.

#) Open a terminal (or a command window in Windows). Change directroy to ``path/to/CHMS_website/ChmsTutorials``

    .. figure:: /Documentation/img/WebsiteTutorialExampleChangeDirectory.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

        An example of a terminal in linux changing directory to ``CHMS_website/ChmsTutorials``

#) Build the website. To build the website, enter this command in the terminal (or a command window in Windows):

    .. code-block:: none

        sphinx-build -b dirhtml source ../chms/tutorials

#) Check the changes. Open a browser, press ``Ctrl+o`` and open ``path/to/CHMS_website/chms/tutorials/index.html``. Then naviage to ``Tutorials > Documentation Tutorials > Website Tutorials > Test header!!!``

    .. figure:: /Documentation/img/WebsiteTutorialsHelloWorldLink.png
        :width: 600px
        :align: center
        :alt: alternate text
        :figclass: align-center

#) Add more content, build and view the changes as needed. 
