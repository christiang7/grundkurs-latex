.. _Installation von LaTeX:

Installation von LaTeX
======================

.. only:: latex

    LaTeX ist definitiv der Standard als wissenschaftliches Textsatzungssystem. Es
    wurde bereits ab Beginn der 1980er Jahre von `Donald Knuth
    <http://de.wikipedia.org/wiki/Donald_Ervin_Knuth>`_ entwickelt und wurde bzw.
    wird seitdem beständig weiterentwickelt und ergänzt. Lag die Stärke von LaTeX
    ursprünglich in der Darstellung von mathematischen Formeln und Quellcode,
    existieren inzwischen ausgereifte Pakete für Briefe, Präsentationen, Notensatz
    uvm.

    Dokumente werden in LaTeX nicht mittels einer graphischen Bedienoberfläche
    gesetzt, sondern gewissermaßen "programmiert". Dies ermöglicht nicht nur ein
    Aufteilen von umfangreichen Werken in kleinere Bestandteile und eine
    Wiederverwertbarkeit von Code-Stücken, es macht obendrein das Erstellen von
    PDF-Dateien "skriptbar". Einige Wiki-Werkzeuge, beispielsweise :ref:`Sphinx
    <Sphinx-Tool>`, können so aus einer eigenen (meist kürzeren) Syntax heraus
    LaTeX- bzw. PDF-Dokumente erzeugen.


Für wissenschaftliche Publikationen, insbesondere für mathematische und
naturwissenschaftliche Formeln, ist ein umfangreiches LaTeX-System
empfehlenswert. Sofern genügend Festplattenspeicher vorhanden ist, sollten
folgende Pakete installiert werden:

.. code-block:: bash

    sudo aptitude install texlive-base texlive-common texlive-latex-base \
        texlive-latex-recommended texlive-latex-extra texlive-math-extra \
        texlive-science texlive-extra-utils texlive-lang-german

Zur Installation der obigen Pakete wird insgesamt etwa 1 GB an
Festplattenspeicher benötigt.


.. index:: CTAN, Paket, texhash, mktexlsr
.. _CTAN-Zusatzpakete installieren:

.. rubric:: CTAN-Zusatzpakete installieren

LaTeX in seiner Grundform kann durch zahlreiche Pakete erweitert werden. Eine
ausführliche Übersicht (inklusive der Paket-Dokumentationen) findet sich im so
genannten `CTAN <http://www.ctan.org/>`_ ("Comprehensive TeX Archive Network").

.. `CTAN-Paket-Index <http://www.bitlib.net/mirror/ctan/help/Catalogue/alpha.html>`_.

Um ein CTAN-Paket zu installieren, lädt man die jeweilige ``.zip``-Datei
herunter, entpackt sie und kopiert sie mit Superuser-Rechten in den LaTeX-Pfad,
unter Linux meist ``/usr/share/texmf/tex/latex``. Anschließend muss die
Veränderung der LaTeX-Datenbank noch mitgeteilt werden. Hierzu gibt man in einem
Shell-Fenster folgendes ein:

.. code-block:: bash

    sudo texhash && sudo mktexlsr

Anschließend kann das Paket in der Dokument-Präambel (meist) als
``\usepackage{paketname}`` eingebunden werden. Nähere Beschreibungen finden sich
in den jeweiligen Paket-Dokumentationen.


