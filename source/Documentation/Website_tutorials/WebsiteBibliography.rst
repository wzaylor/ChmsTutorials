.. _DocumentationWebsiteBibliography:

Website Bibliography
""""""""""""""""""""
Purpose
'''''''
The purpose of this tutorial is to describe how CHMS faculty can supply the information needed for their *Recent Publications* section on their faculty page.

In brief, CHMS faculty should supply the CHMS website's webmaster with a ``.bib`` file that contains the publications that will appear in their profile. For best results, the ``.bib`` file should contain a specific field for ``year``. Additionally, the ``.bib`` file shouldn't contain any publications that the faculty member does not want appearing on their profile page.

Below is a brief tutorial describing a workflow that can be used to generate the desired ``.bib`` file. This tutorial will demonstrate using the citation manager *Zotero*. Other citation managers can likely be used.

.bib File Generation
''''''''''''''''''''
#) Start by opening a reference manager, then creating a collection of the publications that will appear on you CHMS profile. Populate that collection with the desired publications.

    .. figure:: /Documentation/img/BibliographyTutorialCollection.png
        :width: 80%
        :align: center
        :alt: alternate text
        :figclass: align-center

        Create a new collection that will contain the desired publications. This image shows a collection of recent publications from *CHMS* center members.

#) Next, export that collection using **BibTeX** format. This format is desired because it generates a specific ``year`` field. This field is needed because the package that is used for the website (`https://bibbase.org/ <https://bibbase.org/>`_) needs a specific ``year`` field to sort publications by year.

    .. figure:: /Documentation/img/BibliographyTutorialExport.png
        :width: 50%
        :align: center
        :alt: alternate text
        :figclass: align-center

        Export the collection using **BibTeX** format.

#) Attentive faculty members should check the ``.bib`` file that was generated to ensure that there is a ``year`` field. Generally, if the field is present for one publication, then it should be present for the others.

    .. code-block:: none
       :emphasize-lines: 11

       @article{zaylor_use_2019,
       title = {Use of distraction loading to estimate subject-specific knee ligament slack lengths},
       volume = {92},
       issn = {0021-9290},
       url = {http://www.sciencedirect.com/science/article/pii/S0021929019303161},
       doi = {10.1016/j.jbiomech.2019.04.040},
       abstract = {Knee ligaments guide ...},
       journal = {Journal of Biomechanics},
       author = {Zaylor, William and Stulberg, Bernard N. and Halloran, Jason P.},
       month = jul,
       year = {2019},
       keywords = {Distraction loading, Knee model, Ligament properties, Optimization},
       pages = {1--5},
       }

#) Email the ``.bib`` file to the CHMS website webmaster.