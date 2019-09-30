.. _DocumentationWebsiteCreateNewTutorial:

Create A New Tutorial
"""""""""""""""""""""
Purpose
'''''''
The purpose of this tutorial is to describe how to use Sphinx to create/build a new tutorial (so meta...)

These tutorials are written in reStructredText, and a program called Sphinx is used to convert reStructuredText files into .html format. The html files can be directly loaded onto the lab website. This allows for a wiki-style documentation.

This tutorial first describes what :ref:`software<DocumentationWebsiteCreateNewTutorialSoftware>` is needed, then how to :ref:`fork<DocumentationWebsiteCreateNewTutorialGithub>` the ChmsTurorials repository. Once users have a local copy of the repository, they can refer to the section that describes how to :ref:`create<DocumentationWebsiteCreateNewTutorialCreateDocument>` a page on the website. This docuemnt also includes a walkthrough that describes how to create an :ref:`example<DocumentationWebsiteCreateNewTutorialExample>` webpage.

.. _DocumentationWebsiteCreateNewTutorialSoftware:

Software
''''''''
There are three software packages that are used when generating the tutorials documentaiton:

#) :ref:`Python<DocumentationWebsiteCreateNewTutorialSoftwarePython>` with the *Sphinx* module installed (required)
#) :ref:`Git<DocumentationWebsiteCreateNewTutorialSoftwareGit>`, this is used to manage the repository that stores the tutorials source files (required).
#) *PyCharm* or *vscode*, these are used as :ref:`text editors <DocumentationWebsiteCreateNewTutorialSoftwareTextEditor>` (not required). 

.. _DocumentationWebsiteCreateNewTutorialSoftwarePython:

Python
------
The documentation is written using reStructuredText files, and these files are built into *.html* pages using a Python module called Sphinx. Users unfamiliar with Python can follow the :ref:`Python Setup<PythonGeneralPythonSetup>` documentation to install *Anaconda*. Installing *Anaconda* will also install the *Sphinx* module.

.. _DocumentationWebsiteCreateNewTutorialSoftwareGit:

Git
---
A repository has been setup to enable collaboration on the *CHSM Tutorials* documentation. Users can manage this repository using *Git*. 

For Windows users, download *Git* from here, `<https://git-scm.com/>`_, and install the file.

For linux/ubuntu users, open a terminal and enter these commands to install git using ``apt``

.. code-block:: none

    sudo apt install git

.. _DocumentationWebsiteCreateNewTutorialSoftwareTextEditor:

Text editor
-----------
The reStructuredText files that are used to create the tutorials can be edited with a simple text editor. IDEs such as *PyCharm* and *vscode* have different features that make life easier, and both of these IDEs have the ability to manage a :ref:`git<DocumentationWebsiteCreateNewTutorialSoftwareGit>`. 

Users who have installed *PyCharm* during :ref:`python setup<PythonGeneralPythonSetup>` will already have the reStructuredText plugin installed by default. This enables syntax highlighting for .rst documents. The repository can be managed from *PyCharm* in a similar way as described in the :ref:`git repository workflow<DocumentationWebsiteCreateNewTutorialGithubWorkflow>` section by right clickling file names and selecting the ``git`` option.

Users can also install *vscode* (`<https://code.visualstudio.com/>`_) to create and edit reStructuredText files in the repository.

.. _DocumentationWebsiteCreateNewTutorialGithub:

Clone Github tutorials repository
'''''''''''''''''''''''''''''''''
You will clone the repository to your local computer once. This is different from simply downloading the repository because *forking/cloning* allows you to push your changes back into the public repository. Follow these steps to *fork* and *clone* the repository.

These tutorials are stored on a public repository located here: `<https://github.com/CSU-CHMS/ChmsTutorials>`_. For users who are unfamiliar with using a git repository, please follow the instructions below to *fork* then *clone* the repository. After you have *forked* and *cloned* the repository, see the :ref:`DocumentationWebsiteCreateNewTutorialGithubWorkflow` section for a description of the general workflow you will use to add and update files in the repository.

#) Create an account on github (`<https://github.com/join>`_)
#) Download and install :ref:`Git<DocumentationWebsiteCreateNewTutorialSoftwareGit>`
#) Go the the repository (`<https://github.com/CSU-CHMS/ChmsTutorials>`_) and click the fork link. *Forking* the repository allows you to clone the repository, then after you make changes locally, you can submit a *pull request*, which is described :ref:`here<DocumentationWebsiteCreateNewTutorialGithubWorkflow>`.

    .. figure:: /Documentation/img/WebsiteTutorialGithubClone1.png
        :width: 300px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Click the ``fork`` button.

#) Enter your username and password if prompted. After the screen stops loading, you will see the web address is something like ``https://github.com/username/ChmsTutorials`` (where your username is in place of *username*). Copy this address.

    .. figure:: /Documentation/img/WebsiteTutorialGithubClone1b.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Copy the web address after clicking the ``fork`` button.

#) Open a terminal (or a command window in Windows) and navigate to a directory where you plan on keeping the repository. For example, ``/home/user-name/Projects`` or ``C:\Projects``
#) In the terminal, enter this command (*paste the clone link*) ``git clone **clone-link**``

    .. figure:: /Documentation/img/WebsiteTutorialGithubClone2.png
        :width: 400px
        :align: center
        :alt: alternate text
        :figclass: align-center

Now you have successfully clone the *ChmsTutorials* repository. You will not need to repeat this process on your local computer. See the :ref:`DocumentationWebsiteCreateNewTutorialGithubWorkflow` section for a description of the workflow you will use to make changes to the repository.

.. _DocumentationWebsiteCreateNewTutorialGithubWorkflow:

Git repository - General workflow
---------------------------------
This section describes the general workflow that is used when making changes to a git repository. This assumes that you already have already :ref:`forked and cloned<DocumentationWebsiteCreateNewTutorialGithub>` the repository. This section describes how to use built-in tools in the text editor *vscode*. Experienced users may use their preferred text editor and means of *pulling* and *pushing* changes to the repository.

#) Update your local version of the repository to the current version with the *pull* command/operation.

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow1a.png
        :width: 400px
        :align: center
        :alt: alternate text
        :figclass: align-center

        First click the *Source Control* tab/button, then the *More Actions* button, then *Pull*

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow1b.png
        :width: 200px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Alternatively, open a terminal (or a command window in Windows) and change directory to the repository directory, and enter the command ``git pull``

#) Make interesting and useful changes and/or additions on your local computer with whatever text editor you prefer. Both *vscode* and *PyCharm* offer several features that are useful, and this section will use *vscode* as a demonstration.
#) If you are using *vscode*, then *stage* the files that you have changed (note that this takes care of *adding* the file to git version control).

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow2a.png
        :width: 300px
        :align: center
        :alt: alternate text
        :figclass: align-center

        In *vscode* stage any changes that you plan on committing to the repository.

#) Give a brief commit message, then click the commit button.

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow2b.png
        :width: 300px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Enter a message, then click the *commit* button.

#) Repeat the previous steps as needed. You can make multiple commits before you *Push* your changes.
#) *Push* your changes to your *fork* of the repository. Enter your username and password when prompted.
    
    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow2c.png
        :width: 300px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Push your committed changes.

#) Continue to add new files or change existing files, and follow the previous steps as needed. Go to the next step when you want to put your changes into the main public repository.
#) After you have *pushed* your changes to your forked repository, go to your account on github.com and create a *New Pull Request*. Then click *Create pull request*. Add any additional comments, then click *Create pull request*.

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow3a.png
        :width: 300px
        :align: center
        :alt: alternate text
        :figclass: align-center

        Create a new pull request.

    .. figure:: /Documentation/img/WebsiteTutorialGithubWorkflow3b.png
        :width: 400px
        :align: center
        :alt: alternate text
        :figclass: align-center


.. _DocumentationWebsiteCreateNewTutorialCreateDocument:

Creating a Document
'''''''''''''''''''
To create a new document/webpage, first you should create a text file with a ``.rst`` extension somewhere in the ``path/to/ChmsTutorials/source`` directory. To keep things organized, create this file in an appropriate directory. For example, put *general python* documentation in ``path/to/ChmsTutorials/source/Python/General``. Note, a text editor such as :ref:`PyCharm<PythonGeneralPythonSetup>` or ``Visual Studio Code`` can have reStructuredText extensions installed to provide syntax highlighting and other convenient features.

.. Note:: The name of the new document can be arbitrarily assigned. However to keep things organized, please give the document a relevant and descriptive name.

Including Document/Tutorial in website
--------------------------------------
``toctree`` is used to organize the different tutorials and provide links to the main Tutorials webpage. The content of the main Tutorials webpage is in ``path/to/ChmsTutorials/source/index.rst``. *index.rst* contains a *toctree* that links to pages that are used to organize high-level content. For example, the following code-block is in *index.rst*, and it links to ``path/to/ChmsTutorials/source/Python/PythonTutorials.rst`` and ``path/to/ChmsTutorials/source/Documentation/DocumentationTutorials.rst``

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
To build the documentation, open a terminal (or a command window in Windows), and navigate to the directory ``path/to/ChmsTutorials``, and enter this command:

.. code-block:: none

    sphinx-build -b dirhtml source chms

This command means the following: ``sphinx-build`` calls the program that is used to build the documentation. ``-b dirhtml`` specifies that the builder name is ``dirhtml``. The ``dirhtml`` builder makes HTML pages. ``source`` specifies that the source code is in the directory named ``source``. ``chms`` the directory where the .html files are built in. See `<https://www.sphinx-doc.org/en/1.2/invocation.html>`_ for more information.

When you build a document, you are generating html code from the reStructuredText files that you have created. These changes are only made on your computer, and there are two ways to view the documents/changes that you have made.

    #) Manually open ``path/to/ChmsTutorials/chms/index.html`` in a web browser, then navigate to the page that you create/changed.
    #) More experienced users can run a local server. Open a terminal (or a command window in Windows), and change directory to ``path/to/ChmsTutorials/chms``. Enter the command ``python -m http.server`` and in a web browser, go to the website ``http://localhost:8000/``. Navigate to the page that you create/changed.

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

#) Open a terminal (or a command window in Windows). Change directroy to ``path/to/ChmsTutorials``

    .. figure:: /Documentation/img/WebsiteTutorialExampleChangeDirectory.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

        An example of a terminal in linux changing directory to ``CHMS_website/ChmsTutorials``

#) Build the website. To build the website, enter this command in the terminal (or a command window in Windows):

    .. code-block:: none

        sphinx-build -b dirhtml source ../chms/tutorials

#) Check the changes. Open a browser, press ``Ctrl+o`` and open ``path/to/ChmsTutorials/chms/index.html``. Then naviage to ``Tutorials > Documentation Tutorials > Website Tutorials > Test header!!!``

    .. figure:: /Documentation/img/WebsiteTutorialsHelloWorldLink.png
        :width: 600px
        :align: center
        :alt: alternate text
        :figclass: align-center

#) Add more content, build and view the changes as needed. 
