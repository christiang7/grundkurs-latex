.. _Einführung:

Einführung
==========

LaTeX-Quellcode wird üblicherweise in Dateien mit der Endung ``tex``
geschrieben. Mit dem Programm ``pdflatex`` kann daraus ein PDF-Dokument erstellt
werden.

.. _Ein Latex-Minimalbeispiel:

Ein Latex-Minimalbeispiel
-------------------------

Eine minimale LaTeX-Quelldatei sieht beispielsweise folgendermaßen aus:

.. code-block:: tex

    % Datei: hallo-welt.tex

    % Papierformat, Schriftgröße und Dokumentklasse festlegen:
    \documentclass[a4paper, 12pt]{article}

    % Beginn des Dokuments:
    \begin{document}

    Hallo Welt!

    % Ende des Dokuments:
    \end{document}

.. index:: Kommentar

Bei allen Zeilen, die mit einem Prozentzeichen (``%``) beginnen, handelt es sich um
Kommentare, die von LaTeX beim Übersetzen des Quellcodes in eine PDF-Datei
ignoriert werden.

Wird der obige Quelltext als Datei ``hallo-welt.tex`` in einem beliebigen
Verzeichnis gespeichert, so kann in einer Shell durch einen Aufruf von
``pdflatex hallo-welt.tex`` in diesem Verzeichnis das entsprechende PDF-Dokument
``hallo-welt.pdf`` erstellt werden.

.. _Aufbau eines LaTeX-Dokuments:

Aufbau eines LaTeX-Dokuments
----------------------------

.. index:: \documentclass{}

In der ersten Zeile einer ``.tex``-Datei wird mit der Anweisung
``\documentclass`` die Dokumentklasse festgelegt. Neben den auf amerikanische
Layout-Formate zugeschnittenen Standard-Klassen ``article``, ``report`` und
``book`` können auch die europäischen Formate ``scrartcl`` für kurze Artikel,
``scrreprt`` für (längere) Berichte und ``scrbook`` für Bücher gewählt werden.
Zudem gibt es beispielsweise die Dokumentklassen ``scrlettr`` für Briefe und
``beamer`` für Präsentationen.

Allgemein hat die ``\documentclass``-Anweisung folgende Syntax:

.. code-block:: tex

    \documentclass[optionen]{dokumentklasse}

Optionale Argumente werden allgemein in eckige Klammern gesetzt und können
weggelassen werden, notwendige Argumente werden in geschweifte Klammern gesetzt.

Mögliche Optionen für Dokumentklassen sind beispielsweise:

.. list-table::
    :name: tab-documentclass-optionen
    :widths: 50 50

    * - Option
      - Beschreibung
    * - ``10pt`` oder ``12pt``
      - Festlegung der Standard-Schriftgröße
    * - ``oneside`` oder ``twoside``
      - Erstellen einseitiger oder zweiseitiger Dokumente
    * - ``twocolumn``
      - Zweispaltige Textausgabe
    * - ``noparskip`` oder ``halfparskip``
      - Festlegung des Abstands zwischen Absätzen


.. index:: Präambel, \usepackage{}
.. _Präambel:

In den darauf folgenden Zeilen, der so genannten "Präambel" einer LaTeX-Datei,
können mit der Anweisung ``\usepackage`` Zusatzpakete geladen werden. Durch eine
passende Auswahl an solchen Paketen kann LaTeX bei bestmöglicher Performance auf
die jeweilige Aufgabe angepasst werden.

Die ``\usepackage``-Anweisung hat allgemein folgende Syntax:

.. code-block:: tex

    \usepackage[optionen]{paketname}

Häufig genutzte Pakete sind beispielsweise ``graphicx`` zum Einbinden von
Bildern oder ``color`` zum Drucken von farbigem Text. Viele Pakete werden ohne
eine Angabe von Optionen geladen. Solche Pakete können auch folgendermaßen
importiert werden:

.. code-block:: tex

    \usepackage{paket1, paket2, ...}

Anschließend beginnt das eigentliche Dokument. Es wird von ``\begin{document}``
und ``\end{document}`` eingeschlossen.

Eine :ref:`Gliederung eines Dokuments <Abschnitte und Überschriften>` in Kapitel
(möglich in den Dokumentklassen ``scrbook`` und ``scrreprt``) und Abschnitte
(möglich in allen Dokumentklassen) ist durch die Anweisungen ``\chapter{}``
beziehungsweise ``\section{}`` an den entsprechenden Stellen möglich. Wahlweise
kann anhand dieser Untergliederungen auch ein Inhaltsverzeichnis durch die
Anweisung  ``\tableofcontents`` erstellt und an der entsprechenden Stelle in das
Dokument eingefügt werden.

Ein etwas ausführlicheres Beispiel eines LaTeX-Dokuments sieht somit
folgendermaßen aus:

.. code-block:: tex

    \documentclass[a4paper, 12pt]{scrbook}

    \begin{document}

    % Inhaltsverzeichnis anzeigen:
    \tableofcontents

    % Neue Seite beginnen:
    \newpage

    % Überschrift eines Kapitels:
    \chapter{Einleitung}

    ...

    \newpage

    % Überschrift eines Kapitels:
    \chapter{Theoretische Grundlagen}

    % Überschrift eines Abschnittes:
    \section{Allgemeines}

    ...

    % Überschrift eines Abschnittes:
    \section{Konkreteres}

    ...

    \end{document}

..  :emphasize-lines: 3,5

Die Anweisung ``\newpage`` bewirkt hierbei, dass an der entsprechenden Stelle
eine neue Seite angefangen wird.

.. index:: Sprachunterstützung
.. _Umlaute und deutsche Sprachunterstützung:

.. rubric:: Umlaute und deutsche Sprachunterstützung

LaTeX ist ursprünglich für den englischen Sprachraum entwickelt worden. Es gibt
allerdings Zusatzpakete, die eine Erkennung von beispielsweise deutschen
Umlauten sowie passender Silbentrennung ermöglichen.

In der :ref:`Präambel <Präambel>` eines deutschsprachigen LaTeX-Dokuments
sollten folgende Pakete geladen werden:

.. code-block:: tex

    % deutsche Silbentrennung aktivieren:
    \usepackage[ngerman]{babel}

    % deutsche Umlauten erlauben:
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}

Sollte die deutsche Version des Sprachpakets ``babel`` nicht gefunden werden, so
muss das Paket ``texlive-lang-german`` nachinstalliert werden (``sudo aptitude
install texlive-lang-german``).

.. index:: pdflatex, Hilfsdatei
.. _Erstellen eines PDF-Dokuments aus einer Quelldatei:

Erstellen eines PDF-Dokuments aus einer Quelldatei
--------------------------------------------------

Aus einer ``tex``-Quelldatei kann in einer Shell mittels ``pdflatex`` ein
gleichnamiges PDF-Dokument erstellt werden. Die Syntax dabei lautet:

.. code-block:: bash

    pdflatex datei.tex

Neben dem fertigen Dokument ``datei.pdf`` erzeugt der obige Aufruf zusätzlich
automatisch weitere Dateien, beispielsweise ``datei.aux``, ``datei.log`` und
``datei.toc``. In diesen Dateien werden nötige Hilfsinformationen über interne
Sprungstellen (beispielsweise Fußnoten und Zitate), die Ausgabe des letzten
Aufrufs von ``pdflatex`` oder die Seitenangaben des aktuellen
Inhaltsverzeichnisses abgelegt.

.. list-table::
    :name: tab-hilfsdateien
    :widths: 20 50

    * - Hilfsdatei
      - Bedeutung
    * - ``.log``
      - Protokoll des letzten LaTeX-Aufrufs
    * - ``.aux``
      - Hilfsdatei für Querverweise
    * - ``.toc``
      - Inhaltsverzeichnis
    * - ``.lof``
      - Abbildungsverzeichnis
    * - ``.lot``
      - Tabellenverzeichnis
    * - ``.idx``
      - Index-Register

Üblicherweise kann man die automatisch erzeugten Hilfsdateien weitgehend außer
Acht lassen. Eine Besonderheit liegt jedoch darin, dass LaTeX die Seitenzahlen
für das Inhaltsverzeichnis erst dann komplett in die ``.toc``-Datei schreiben
kann, wenn die Quelldatei vollständig übersetzt ist. Um nach einer Veränderung
einer ``tex``-Quelldatei ein aktualisiertes Inhaltsverzeichnis in der
``pdf``-Druckversion zu erhalten, muss ``pdflatex`` daher ein zweites Mal
aufgerufen werden. Gleiches gilt für Änderungen im Index-Register oder im
Literaturverzeichnis: Auch hier werden erst im Laufe des Übersetzungsvorgangs
die Änderungen in die entsprechenden Hilfsdateien geschrieben, so dass die
gemachten Änderungen erst bei einem zweiten Übersetzungsvorgang berücksichtigt
werden können.


.. Fehlermeldungen..

.. _Grundlegende Konzepte in LaTeX:

Grundlegende Konzepte in LaTeX
------------------------------

Im folgenden sollen einige Prinzipien, die für das Arbeiten mit LaTeX von
Bedeutung sind, in einer knappen Zusammenfassung vorgestellt werden.

.. _Anweisungen, Deklarationen und Umgebungen:

.. rubric:: Anweisungen, Deklarationen und Umgebungen

In LaTeX gibt es dreierlei Arten von "Steuerelementen", die den Ablauf des
Übersetzungsvorgangs beeinflussen können:

.. _Anweisung:

* **Anweisungen** haben folgende Syntax:

  .. code-block:: tex

      \anweisungsname[optionale-argumente]{pflicht-argumente}

  Alle Anweisungen beginnen also mit einem Backslash-Zeichen, gefolgt vom
  eigentlichen Namen der Anweisung. Der Anweisungsname wird allgemein durch ein
  Leerzeichen oder durch ein Sonderzeichen beendet. [#]_

  Der erstere Fall tritt häufig bei Anweisungen auf, die ohne weitere Argumente
  aufgerufen werden, wie beispielsweise ``\newpage``. Der zweite Fall tritt
  stets ein, wenn der Anweisung beim Aufruf optionale oder obligatorische
  Argumente übergeben werden, denn auch die Zeichen ``[`` und ``{`` sind
  Sonderzeichen. Ebenso ist es nach dieser Regel allerdings auch möglich, in
  einer mathematischen Formel beispielsweise ``\alpha_1`` für ein
  :math:`\alpha`-Zeichen mit dem Index :math:`1`, also :math:`\alpha_1` zu
  schreiben.

  Anweisungen sind in LaTeX elementare Bausteine, sie können also nicht weiter
  ineinander verschachtelt werden. Daher ist es beispielsweise nicht möglich,
  innerhalb einer ``\textbf{}``-Anweisung, die den in den geschweiften Klammern
  stehenden Text in Fettdruck ausgibt, mittels ``\newline`` einen manuellen
  Zeilenwechsel zu erzwingen. Anweisungen beziehen sich daher meist auf einzelne
  Textteile innerhalb einer Zeile oder innerhalb eines Absatzes.

.. _Deklaration:

* **Deklarationen** sind lokale Bereiche innerhalb eines LaTeX-Dokuments, die
  innerhalb von geschweiften Klammern gesetzt sind, also von ``{`` und ``}``
  umschlossen sind.

  .. code-block:: tex

      {

          ... Inhalt ...

      }

  Der Vorteil von Deklarationen liegt darin, dass es Anweisungen wie ``\small``
  (Verkleinerung der Schriftart) gibt, die sich normalerweise auf den gesamten
  nachfolgenden Text auswirken -- bis zum Ende des Dokuments, oder bis ihre
  Wirkung durch eine andere Anweisung aufgehoben wird -- im obigen Beispiel
  durch ``\normalsize``.

  Begrenzt man den gewünschten Textabschnitt, der kleingedruckt erscheinen soll,
  allerdings mit geschweiften Klammern und schreibt unmittelbar nach der
  öffnenden Klammer ``{`` die Anweisung ``\small``, so wird deren Wirkung mit
  der schließenden Klammer ``}`` wieder aufgehoben.

  Mittels Deklarationen kann die Wirkung einzelner Anweisungen somit auch auf
  mehrere Zeilen oder Absätze ausgeweitet werden.

.. _Umgebung:

* **Umgebungen** haben stets folgende Syntax:

  .. code-block:: tex

      \begin{umgebung}

          ... Inhalt ...

      \end{umgebung}

  Umgebungen schaffen ebenso wie Deklarationen einen lokalen Bereich, in dem
  bestimmte Bearbeitungsmerkmale wie Schriftgröße, Textbreite, Textausrichtung
  oder ähnliches von den übrigen Text verschieden sein können. In LaTeX
  existieren zahlreiche vordefinierte Umgebungen, die eigene Änderungen mit sich
  bringen; im Kapitel :ref:`Wichtige Umgebungen <wichtige Umgebungen>` werden
  einige davon näher vorgestellt.

  Neben den lokalen Änderungen, welche die jeweiligen Umgebungen von sich aus
  vornehmen, können auch innerhalb von Umgebungen mittels entsprechender
  Anweisungen zusätzliche lokale Änderungen manuell vorgenommen werden.

.. rubric:: Text- und Formelmodus

In LaTeX werden zwischen drei verschiedenen Arten von Text unterschieden:

* Im so genannten "Absatzmodus" wird Text als eine gewöhnliche Sequenz von
  Wörtern angesehen, die bei Bedarf automatisch auf mehrere Zeilen aufgeteilt
  wird (inklusive automatischer Silbentrennung). Dieser Modus ist Standard bei
  der Eingabe von Text.

* Im so genannten "LR-Modus" wird Text ebenfalls als Sequenz von Wörtern
  angesehen, die von links nach rechts abgearbeitet beziehungsweise übersetzt
  wird; im Gegensatz zum Absatzmodus kann in diesem Modus allerdings kein
  Zeilenumbruch zwischen den Wörtern stattfinden.

* Im so genannten "Mathematik-Modus" werden die die eingegebenen Buchstaben und
  Symbole als Teil einer Formel interpretiert. Hierbei werden beispielsweise
  Leerzeichen, die zwischen einzelnen Buchstaben stehen, ignoriert; dafür sind
  bestimmte Syntax-Elemente wie ``^`` oder ``_`` zum Hoch- beziehungsweise
  Tiefstellen von Textelementen ausschließlich in diesem Modus erlaubt.

Da sich der Absatz-Modus und der LR-Modus nur hinsichtlich des
Zeilenumbruch-Verhaltens unterscheiden, werden beide oftmals gemeinsam als
"Textmodus" bezeichnet, um sie von der Eingabe mathematischer Formeln zu
unterscheiden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Manche Anweisungen verlangen auch mehrere Pflicht-Argumente.
    Beispielsweise wird bei ``\setcounter{}{}`` innerhalb der ersten
    geschweiften Klammern der Name einer Zählervariablen, und innerhalb der
    zweiten der zuzuweisende Wert angegeben. Beide Argumente sind beim Aufruf
    der ``\setcounter{}``-Anweisung allerdings notwendig.

