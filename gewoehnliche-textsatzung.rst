
.. _Gewöhnliche Textsatzung:

Gewöhnliche Textsatzung
=======================

.. _Abschnitte und Überschriften:

Abschnitte und Überschriften
----------------------------

Der Inhalt eines Dokuments kann mittels der folgenden Anweisungen hierarchisch
in einzelne Abschnitte untergliedert werden:

.. index:: \part{}, Part

* ``\part{Text}`` kennzeichnet Buchteile. Diese Gliederungsebene existiert nur
  bei den Dokumentklassen ``book`` und ``scrbook``.

.. index:: \chapter{}, Kapitel

* ``\chapter{Text}`` kennzeichnet Kapitel. Diese Gliederungsebene existiert nur
  bei den Dokumentklassen ``book`` und ``scrbook``, ``report`` und ``scrreprt``,
  nicht aber bei ``article`` und ``scrartcl``.

.. index:: \section{}, Abschnitt

* ``\section{Text}`` kennzeichnet Abschnitte. Diese Gliederungsebene ist bei
  Artikeln die höchste, bei Büchern oder Berichten die zweithöchste.

.. index:: \subsection{}, \subsubsection{}

* ``\subsection{Text}`` und ``\subsubsection{Text}`` kennzeichnet Unter- und
  Unterunterabschnitte.

.. index:: \paragraph{}, \subparagraph{}

* ``\paragraph{Text}`` kennzeichnet einzelne Absätze (Paragraphen) im Text. Die
  tiefste Ebene stellt schließlich der ``\subparagraph{Text}`` dar.

In der Präambel kann mittels ``\setcounter{secnumdepth}{tiefe}`` beeinflusst
werden, bis zu welcher Schachtelungstiefe eine Nummerierung der Überschriften
erfolgt. Der Standardwert für ``tiefe`` ist :math:`2`, es erhalten also Kapitel-, Abschnitts-
und Unterabschnittsüberschriften eine fortlaufende Nummer. Setzt man
beispielsweise ``\setcounter{secnumdepth}{1}``, so werden nur noch die Kapitel-
und Abschnittsüberschriften nummeriert, bei ``\setcounter{secnumdepth}{0}`` nur
noch die Kapitelüberschriften. Setzt man ``\setcounter{secnumdepth}{-1}``, so
wird überhaupt keine Überschrift nummeriert.

Wenn bei einer Überschrift ein ``*`` vor die öffnende geschweifte Klammer
gesetzt wird (beispielsweise ``\section*{Text}``), so erfolgt keine Nummerierung
der Überschrift und ebenso kein Eintrag in das Inhaltsverzeichnis.

.. index:: Titelseite, Abstract
.. _Titelseite und Abstract:

.. rubric:: Titelseite und Abstract

Optional können zu Beginn einer LaTeX-Datei mittels der folgenden Anweisungen
Informationen über den Autor und das aktuelle Dokument festgelegt werden:

* ``\title{}``: Der Titel des Dokuments
* ``\author{}``: Der Autor beziehungsweise die Autoren (Aufzählung mittels ``\and``)
* ``\date{}``: Das Datum der Veröffentlichung (``\today`` für das heutige Datum)

Zu Beginn des Dokuments kann dann mittels folgender Anweisung eine automatische
Titelseite erzeugt werden:

.. code-block:: tex

    \maketitle

Die Titelseite kann selbstverständlich auch manuell gestaltet werden. Bei
Büchern folgt auf der zweiten Seite häufig eine kurze Beschreibung des Inhalts,
ein so genannnter "Abstract". Dieser kann folgendermaßen

.. code-block:: tex

    \abstract{Text}

Die Ausrichtung des Abstracts auf der zweiten Seite erfolgt dabei -- ebenso wie
bei ``\maketitle`` -- automatisch.


.. index:: Inhaltsverzeichnis, \tableofcontents
.. _tableofcontents:
.. _Inhaltsverzeichnis:

.. rubric:: Inhaltsverzeichnis

Anhand der Gliederung in Kapitel und Abschnitte kann in LaTeX mittels
``\tableofcontents`` ein automatisch erzeugtes Inhaltsverzeichnis in das
Dokument eingebunden werden:

.. code-block:: tex

    \tableofcontents

Üblicherweise wird das Inhaltsverzeichnis unmittelbar nach der Titelseite und
dem Abstract gesetzt. Die Seiten des Inhaltsverzeichnisses werden von LaTeX
automatisch mit kleinen römischen Buchstaben nummeriert, das eigentliche
Dokument beginnt dann mit :math:`1` als Seitennummer.

In der Präambel kann mittels ``\setcounter{tocdepth}{tiefe}`` beeinflusst
werden, bis zu welcher Schachtelungstiefe die Überschriften des Dokuments
aufgelistet werden sollen. Der Standardwert für ``tiefe`` ist wiederum ``2``, so
dass Kapitel-, Abschnitts- und Unterabschnittsüberschriften aufgelistet werden.
Nummer. Setzt man beispielsweise ``\setcounter{secnumdepth}{1}``,so werden nur
noch die Kapitel- und Abschnittsüberschriften aufgelistet. Überschriften, bei
denen vor die öffnende Klammer ein ``*`` gesetzt wurde (beispielsweise
``\section*{Text}``), werden unabhängig davon im Inhaltsverzeichnis nicht
aufgelistet.

.. Namen des Inhaltsverzeichnisses ändern:
.. \renewcommand*\contentsname{Summary}

Mit folgender Anweisung kann mitten im Dokument manuell ein Eintrag zum
Inhaltsverzeichnis hinzugefügt werden, der dann auf die jeweilige Textstelle
verweist:

.. code-block:: tex

    % Eintrag manuell zum Inhaltsverzeichnis hinzufügen:
    \addcontentsline{toc}{section}{Name des Eintrags}

Anstelle ``section`` kann selbstverständlich auch eine andere Gliederungsebene
wie ``chapter`` oder ``subsection`` gewählt werden. Manuelle Einträge sind an
Stellen sinnvoll, an denen man den Navigations-Komfort des Inhaltsverzeichnisses
(inklusive der automatisch generierten Sprungmarken) nutzen mag, ohne im
Dokument (beispielsweise aus Platzgründen) tatsächlich eine Überschrift setzen
zu wollen.

Werden Änderungen in der Gliederung vorgenommen, so schreibt LaTeX beim
Übersetzen des Quellcodes mittels ``pdflatex`` die Änderungen des
Inhaltsverzeichnisses in eine Hilfsdatei mit der Endung :math:``.toc``; erst bei
einem nochmaligen Übersetzen des Quellcodes mittels ``pdflatex`` werden die
Änderungen auch im PDF-Dokument sichtbar.

.. index:: \listoftables, \listoffigures
.. rubric:: Tabellen- und Abbildungsverzeichnis

Neben einem Inhaltsverzeichnis kann nach Belieben auch mit ``\listoftables``
eine Übersicht aller Tabellen und mit ``\listoffigures`` eine Übersicht über
alle Abbildungen im Dokument ausgegeben werden. Auch hier ist gegebenenfalls
ein zweimaliger Aufruf von ``pdflatex`` nötig, um die Listen (Hilfsdateien
``.lot`` und ``.lof``) im PDF-Dokument zu aktualisieren.



.. index:: \appendix, Anhang
.. rubric:: Anhang

Soll ein Dokument einen Anhang beinhalten, so kann dieser mittels ``\appendix``
eingeleitet werden. Ab dieser Anweisung werden weitere Kapitel anstelle mit
Nummern mit Großbuchstaben :math:`\rm{A}`, :math:`\rm{B}`, usw. durchnummeriert.
Die Seitennummerierung wird unverändert fortgesetzt.


.. _Zeilen- und Seitenumbruch:

.. rubric:: Zeilen- und Seitenumbruch

Einzelne Absätze werden in LaTeX durch Leerzeilen gekennzeichnet. Der Abstand
zwischen Absätzen wird als Option in Verbindung mit der Dokumentklasse
festgelegtals, beispielsweise ``\documentclass[halfparskip]{scrbook}``.

.. TODO parskip, noparskip

.. index:: \newline, \\

Möchte man innerhalb eines Absatzes eine neue Zeile erzeugen, so kann dies
mittels ``\newline`` oder der Kurzform ``\\`` erfolgen. Unmittelbar im Anschluss
an ``\\`` kann zudem in eckigen Klammern ein Längenmaß angegeben werden, um
das der Abstand zur nächsten Zeile verkleinert oder vergrößert wird;
beispielsweise bewirkt bei einer Schriftgröße von ``12pt`` ein Zeilenumbruch
mittels ``\\[6pt]`` einen :math:`1,5`-fachen Zeilenabstand.

.. ``\\*[abstand]``
.. Die ``*``-Form verhindert, dass nach dem Zeilenwechsel ein Seitenumbruch vor der
.. nächsten Zeile auftreten kann.

.. index:: Seitenumbruch, \pagebreak, \newpage

Eine Wechsel auf eine neue Seite kann mittels ``\pagebreak`` oder ``\newpage``
manuell erzwungen werden.

.. \newpage
..     Der Rest der Seite bleibt leer. Bei twocolumn wird die laufende Spalte
..     beendet und eine neue begonnen.

.. \clearpage
..     Die laufende Seite wird beendet und alle bis hierher definierten und noch
..     nicht ausgegebenen Tabellen und Bilder werden ggf. auf einer oder oder
..     mehreren daran anschließenden Seiten ausgegeben.

.. \cleardoublepage
..     Bei twoside beendet die laufende Seite. Alle noch nicht bearbeiteten
..     gleitenden Bilder und Tabellen auf eigenen Seiten ausgegeben. Als nächste
..     Seite wird dann stets eine ungerade Seite gestartet.


.. \samepage
..     erlaubt einen Seitenumbruch nur zwischen Absätzen. Ein Seitenumbruch wird
..     zusätzlich unmittelbar vor oder hinter abgesetzten Formeln oder Einrückungen
..     verhindert. Im Vorspann wirkt auf das ganze Dokument, andernfalls bis zum
..     Ende der laufenden Umgebung.

.. \begin {samepage} Text \end {samepage}
..     Umgebung mit der Wirkung wie bei \samepage.


.. _Aufteilung eines Dokuments in mehrere Dateien:

.. rubric:: Aufteilung eines Dokuments in mehrere Dateien

Umfangreiche LaTeX-Dokumente können, beispielsweise kapitelweise, in mehrere
``.tex``-Dateien aufgeteilt werden. In der Hauptdatei kann der Inhalt dieser
Dateien dann mittels der Anweisung ``\input{kapitelname}`` eingefügt werden; die
Endung ``.tex`` wird dabei automatisch ergänzt.

.. code-block:: tex

    % Beispiel einer aufgeteilten Haupt-Datei:

    \input{preambel}
    \input{kapitel1}
    \input{kapitel2}
    \input{kapitel3}
    \input{anhang}

Die einzelnen Kapitel können bei umfangreichen Dokumenten auch in verschiedene
Unterverzeichnisse abgelegt werden, um dort beispielsweise die zugehörigen Bild-
oder Code-Dateien mit abzuspeichern.

Auf eine sehr ähnliche Weise kann die LaTeX-Anweisung ``\include{}`` verwendet
werden. Auch bei dieser Anweisung wird der Name der angegebenen Datei um die
Endung ``.tex`` ergänzt; der Inhalt der Datei wird allerdings erst auf einer
neuen Seite (quasi nach einer ``\newpage``-Anweisung) eingebettet. Die
``\include{}``-Anweisung kann folglich nur einzelne Kapitel-Dateien in das
Dokument einbauen; beispielsweise für die Präambel muss hingegen die
``\input{}``-Anweisung verwendet werden.

.. _frontmatter, mainmatter und backmatter:

.. rubric:: ``\frontmatter``, ``\mainmatter`` und ``\backmatter``

Bücher werden oftmals in Vorspann, Hauptteil und Nachspann aufgeteilt.
Auch bei den LaTeX-Dokumentklassen ``book`` beziehungsweise ``scrbook``
exisiteren entsprechende Gliederungsebenen:

.. code-block:: tex

    % Vorspann einleiten:
    \frontmatter

    % Hauptteil einleiten:
    \mainmatter

    % Nachspann einleiten:
    \backmatter

* Im Vorspann werden die Seiten mit kleinen römischen Ziffern durchnummeriert.
  Der Vorspann enthält üblicherweise nur die Titelseite, das Inhaltsverzeichnis
  (bisweilen auch ein Abbildungs- und Tabellenverzeichnis) sowie möglicherweise
  ein Vorwort. Meist kommt der Vorspann daher mit einer einzigen
  Kapitelüberschrift aus, die ohne Nummerierung erscheint. [#]_

* Im Hauptteil werden die Seiten mit arabischen Zahlen nummeriert, wobei die
  Nummerierung erneut mit ``1`` beginnt.

* Im Nachspann wird bisweilen nur das Literatur- und/oder Stichwortverzeichnis
  gesetzt, manchmal jedoch auch der gesamte Anhang. Der Nachspann gleicht
  bezüglich der Gliederungsüberschriften dem Vorspann, die Kapitel werden jedoch
  mit Großbuchstaben gekennzeichnet (beginnend mit ``A``). Eine getrennte
  Seitennummerierung ist nicht vorgesehen.


.. index:: Schriftart, Schriftfamilie, Texthervorhebung
.. _Schriftarten und Texthervorhebungen:

Schriftfamilien und Texthervorhebungen
--------------------------------------

Üblicherweise werden mehrere Schriftarten zu einer Schriftfamilie
zusammengefasst, die zwar das gleiche Design aufweisen, sich aber in
Neigungsgrad, Fettschrift, Zeichenabstand und weiteren Merkmalen unterscheiden
können. Die Standard-Schriftfamilie von LaTeX heißt "Computer Modern".

Innerhalb einer Schriftfamilie kann die Darstellung von Text folgendermaßen
verändert werden:

.. _Schriftstärke:

.. index:: \textbf{}

* *Schriftstärke:* Mit ``textbf{Text}`` ("bold font") wird Text fettgedruckt, mit
  ``\textmd{Text}`` ("medium", Standard) in normaler Schriftstärke ausgegeben.

  .. list-table::
      :name: tab-text-normal-fett
      :widths: 50 50

      * - ``\textbf{Ein Blindtext.}``
        - :math:`\text{\textbf{Ein Blindtext.}}`
      * - ``\textmd{Ein Blindtext.}``
        - :math:`\text{\textmd{Ein Blindtext.}}`

.. index:: \textsl{}, \textsc{}, \textit{}, \emph{}

.. _Schriftform:

* *Schriftform:* Mit ``\textit{Text}`` ("italic") wird der angegebene Text
  kursiv, mit ``textsl{Text}`` ("slanted") schräggestellt gedruckt. Als Standard
  wird die Text aufrecht ausgegeben  (entspricht ``\textup{Text}``).

  .. list-table::
      :name: tab-text-schraeg
      :widths: 50 50

      * - ``\textit{Ein Blindtext.}``
        - :math:`\text{\textit{Ein Blindtext.}}`
      * - ``\textsl{Ein Blindtext.}``
        - :math:`\text{\textsl{Ein Blindtext.}}`
      * - ``\textup{Ein Blindtext.}``
        - :math:`\text{\textup{Ein Blindtext.}}`

  .. index:: Kapitälchen, \emph{}

  Mit ``\emph{Text}`` ("emphasize") wird Text hervorgehoben; er wird dann
  innerhalb einer normalen Textzeile kursiv gedruckt, innerhalb einer kursiven
  Textzeile jedoch aufrecht dargestellt.
  Mit ``\textsc{Text}`` ("small caps") wird Text in unterschiedlich großen
  Großbuchstaben ("Kapitälchen") ausgegeben; mittels ``\underline{Text}`` kann
  Text unterstrichen ausgegeben werden.

  .. list-table::
      :name: tab-text-hervorhebung
      :widths: 50 50

      * - ``\emph{Ein Blindtext.}``
        - :math:`\text{\emph{Ein Blindtext.}}`
      * - ``\textsc{Ein Blindtext.}``
        - :math:`\text{\textsc{Ein Blindtext.}}`
      * - ``\underline{Ein Blindtext.}``
        - :math:`\text{\underline{Ein Blindtext.}}`

  Bindet man in der Präambel das Paket ``soul`` ein (``\usepackage{soul}``), so
  kann Text auch durchgestrichen ausgegeben werden:

  .. list-table::
      :name: tab-text-hervorhebung-soul
      :widths: 50 50

      * - ``\st{Ein Blindtext.}``
        - :math:`\text{\st{Ein Blindtext.}}`

.. http://www.namsu.de/latex/latexeinfuehrung_2/Latexeinfuehrung.html
.. * - ``\so{Ein Blindtext.}``
.. - :math:`\text{\so{Ein Blindtext.}}`
.. * - ``\caps{Ein Blindtext.}``
.. - :math:`\text{\caps{Ein Blindtext.}}`

.. _Schrifttyp:

.. index:: Serifen, \textrm{}, \textsf{}, \texttt{}

* *Schrifttyp:* Standardmäßig wird Text als ``\textrm{Text}`` ("roman"), d.h.
  mit so genannten Serifen ausgegeben. Serifen sind kleine Füßchen und Häkchen
  an den einzelnen Buchstaben, die eine Schrift für das Auge besser lesbar
  machen. Serifen-Schiften sollten für längere Texte bevorzugt werden, während
  beispielsweise für die Erstellung von Plakaten mit ``textsf{Text}`` ("sans
  serif") auch eine serifenlose Schrift gewählt werden kann.

  .. list-table::
      :name: tab-text-schrifttyp
      :widths: 50 50

      * - ``\textrm{Ein Blindtext.}``
        - :math:`\text{\textrm{Ein Blindtext.}}`
      * - ``\textsf{Ein Blindtext.}``
        - :math:`\text{\textsf{Ein Blindtext.}}`
      * - ``\texttt{Ein Blindtext.}``
        - :math:`\text{\texttt{Ein Blindtext.}}`

  Üblicherweise nehmen die einzelnen Buchstaben einer Schrift beim Druck, da
  sie unterschiedlich breit sind, unterschiedlich viel Platz ein. Beispielsweise
  zur Darstellung von Quellcode wird jedoch bevorzugt eine nicht-proportionale
  Schrift verwendet, um eine optische Absetzung vom restlichen Text zu bewirken.
  Dies kann mit ``\texttt{Text}`` ("typewriter") erreicht werden.

.. index:: Unterstreichung, \underline{}

Die obigen Anweisungen können verschachtelt auftreten, es kann also
beispielsweise ein Text fett *und* kursiv gedruckt werden.
Die Anweisungen sind jedoch auf einzelne Textelemente innerhalb
eines Absatzes begrenzt.

.. \bfseries
.. \mdseries

.. In TeX werden die Buchstabenkombinationen ff, fi, fl, ffi, ffl als Ligaturen gesetzt.
.. Mit \/ innerhalb einer Ligatur kann dies unterbunden werden.

.. .. _Verwendung anderer Schriftarten:

.. .. rubric:: Verwendung anderer Schriftarten

.. Soll eine andere Schriftfamilie als die LaTeX-Standard-Schrift "Computer Modern"
.. verwendet werden, so muss in der Präambel ein ensprechendes Zusatzpaket geladen
.. werden. Beispielsweise existierien die Pakete ``uarial`` als Nachbau der
.. Schriftart "Arial", oder ``helvet`` als Nachbau der Schriftart "Helvetica".

.. Ausführliche Erklärung:
.. https://tex.stackexchange.com/questions/25249/how-do-i-use-a-particular-font-for-a-small-section-of-text-in-my-document/25251#25251

.. \usepackage{uarial}
.. \renewcommand{\familydefault}{\sfdefault}

.. Die in Latex verwendete Standardschriftart heißt Computer Modern Schriftfamilie
.. (CM), diese setzt sich aus verschieden Computer Modern Schriftarten zusammen. Da
.. sie nicht alle europäischen Zeichen umfasst sollte das Usepackage fontenc
.. eingebunden werden, um Probleme bei der Darstellung von Umlauten zu vermeiden.

.. \usepackage[scaled]{uarial}
.. http://www.cs.sfu.ca/pub/math/pub/lachlan/latex/arial/uarial.sty


.. index:: Farbiger Text, \color{}
.. _Farben:
.. _Farbiger Text:

.. rubric:: Farbiger Text

Um Farben nutzen zu können, muss in der :ref:`Präambel <Präambel>` des
LaTeX-Dokuments das Paket ``xcolor`` geladen werden:

.. \usepackage[table]{xcolor}

.. code-block:: tex

    \usepackage{xcolor}

Innerhalb des Dokuments lässt sich dann durch die Anweisung ``\color{farbname}``
die Standardfarbe auf eine gewünschte Farbe ändern. Der Farbname kann einer
Standardfarbe (``black``, ``white``, ``darkgray``, ``gray``, ``lightgray``,
``brown``, ``red``, ``green``, ``blue``, ``cyan``, ``magenta`` oder ``yellow``)
entsprechen oder eine selbst definierte Farbe bezeichnen.

Um einen Farbwechsel nicht wieder explizit rückgängig machen zu müssen, kann die
Wirkung des Farbwechsels mittels einer :ref:`Deklaration <Deklaration>` auf
einen Textblock beschränkt werden, beispielsweise ``Text { \color{red} roter
Text hier } Text``. Derartige Textblöcke können auch mehrere Absätze umfassen.

Eine andere Möglichkeit ist, einen Textabschnitt mittels
``\textcolor{farbname}{Text}`` hervorzuheben; hierbei ist die Länge des Textes
allerdings auf maximal einen einzelnen Absatz begrenzt.

Neben den Standard-Farben können folgendermaßen auch eigene Farben definiert werden:

*Beispiel:*

.. code-block:: tex

    \textcolor[rgb]{0.85, 0.00, 0.15}{Rot}         \\ % rot-gruen-blau (prozentual)
    \textcolor[RGB]{ 240,  115,  40}{Orange}       \\ % Rot-Gruen-Blau (Farbwerte 0..255)
    \textcolor[HTML]{F0E10F}{Gelb}                 \\ % HTML-Code      (hexadeximal)
    \textcolor[cmyk]{0.25, 0.10, 0.35, 0.08}{Grün} \\ % CMYK-Anteile   (für Druckereien)
    \textcolor[wave]{450}{Blau}                    \\ % Wellenlänge    (380..750)

    \textcolor[gray]{0.75}{Grau}                   \\ % Grau-Anteil    (0..1)

*Ergebnis:*

.. math::

    &\text{\textcolor[rgb]{0.85, 0.0, 0.15}{Rot}} \\
    &\text{\textcolor[RGB]{240,115,40}{Orange}} \\
    &\text{\textcolor[HTML]{F0E10F}{Gelb}} \\
    &\text{\textcolor[cmyk]{0.25, 0.10, 0.35, 0.08}{Grün}} \\
    &\text{\textcolor[wave]{450}{Blau}} \\[12pt]
    &\text{\textcolor[gray]{0.75}{Grau}}

Möchte man eine Farbe nicht nur einmalig verwenden, so kann man ihr einen Namen
zuweisen; die Farbe kann anschließend wie eine Standard-Farbe verwendet werden:

.. code-block:: tex

    % Eigenen Farbnamen definieren:
    \definecolor{deeppurple}{RGB}{50, 25, 150}

Mittels des ``xcolor``-Pakets kann Text auch mit einem farbigen Rahmen versehen
werden:

*Beispiel:*

.. code-block:: tex

    % Text mit farbigem Hintergund:
    \colorbox{blue}{Text}

    % Text mit farbiger Umrandung:
    \fcolorbox{blue}{white}{Text}

*Ergebnis:*

.. math::

    &\colorbox{blue}{\text{Text}} \\[6pt]
    &\fcolorbox{blue}{white}{\text{Text}}

Mit beiden Anweisungen werden :ref:`LR-Boxen <LR-Box>` erzeugt (siehe Abschnitt
:ref:`Boxen <Boxen>` weiter unten). In einer derartigen Box ist kein allgemein
kein Zeilenumbruch möglich, außer man umschließt damit eine :ref:`Parbox
<Parbox>`. Alle von ``xcolor`` bereitgestellten Anweisungen lassen sich auch im
Mathe-Modus und in Tabellen nutzen; für farbige Texteinträge in Tabellen lohnt
es sich allerdings, auch einen Blick auf das :ref:`colortbl <colortbl>`-Paket zu
werfen.

Allgemein sollten Farben sparsam verwendet werden. Zueinander passende Farben
lassen sich beispielsweise mit dem Programm ``agave`` ausfindig machen -- dieses
ist über das gleichnamige Paket via :ref:`apt <gwl:apt>` installierbar.


.. Farbige Rahmen und/oder Hinterlegungen für einzelne Wörter erzeugen wir mit
.. \colorbox und \fcolorbox.
.. \colorbox{yellow}{Gelber Kasten}
.. \fcolorbox{blue}{yellow}{Gelb-blauer Kasten}


.. index:: \rotatebox{}
.. _Gedrehter Text:

.. rubric:: Gedrehter Text

Um Text vertikal oder schräg zu setzen, muss zunächst in der Präambel des
Dokuments das Paket ``graphicx`` geladen werden. Innerhalb des Dokuments lässt
sich dann durch die Anweisung ``\rotatebox{Winkel}{Text}`` der angegebene Text
um den angegebenen Winkel drehen.

*Beispiel:*

.. code-block:: tex

    % In der Präambel:

    \usepackage{graphicx}

    % Innerhalb des Dokuments:

    \rotatebox{90}{Hallo Welt!}

Der Drehwinkel wird dabei im mathematischen Sinn interpretiert, eine Angabe von
``90`` entspricht also einer Drehung um :math:`90\degree` gegen den
Uhrzeigersinn.


.. index:: Schriftgröße
.. _Schriftgrößen und Längenmaße:

Schriftgrößen und Längenmaße
----------------------------

In LaTeX wird die Standard-Größe für ein Dokument in Verbindung mit der
Dokumentklasse festgelegt, beispielsweise ``\documentclass[12pt]{scrbook}`` für
ein Buch mit einer normalen Schriftgröße von ``12pt``. Die Größe einer Schrift
kann dann innnerhalb des Dokuments folgendermaßen angepasst werden, wobei die
Abstufungen relativ zur Standard-Schriftgröße und in harmonischen
Größenverhältnissen erfolgen:

.. hlist::
    :columns: 2

    * ``\tiny``
    * ``\scriptsize``
    * ``\footnotesize``
    * ``\small``
    * ``\normalsize``
    * ``\large``
    * ``\Large``
    * ``\LARGE``
    * ``\huge``
    * ``\Huge``

Eine Änderung der Schriftgröße kann entweder mittels ``\normalsize`` beendet
oder mittels einer :ref:`Deklaration <Deklaration>`  auf einen Textbblock
beschränkt werden, beispielsweise ``Text { \large großer Text hier } Text``.
Derartige Textblöcke können auch mehrere Absätze umfassen; ebenso kann ein
solcher Bereich mittels ``\begin{large}`` und ``\end{large}`` begrenzt werden.

.. index:: \fontsize{}

Soll innerhalb des Dokuments die Standard-Größe der Schrift verändert werden, so
ist dies mit folgender Syntax möglich:

.. code-block:: tex

    \fontsize{12pt}{14.4pt}
    \selectfont

Der ``\fontsize{}``-Anweisung werden hierbei die neue Schriftgröße sowie der
neue Standard-Zeilenabstand als Argumente übergeben. Möchte man eine andere
Schriftgröße angeben, so sollte das Verhältnis von Schriftgröße sowie
Zeilenabstand beibehalten, also beide Werte um den gleichen Faktor skaliert
werden.

.. index:: Längenmaß, pt (Einheit), em (Einheit), ex (Einheit)
.. _Längenmaße:
.. _Längeneinheiten:

In LaTeX können allgemein folgende Längenmaße verwendet werden:

* ``in``: Ein Zoll ("inch") entspricht :math:`\unit[2,54]{cm}`.
* ``pt``: Der "point" ist eine Maßgröße aus der ursprünglichen Textsatzung. Es
  gilt :math:`\unit[1]{pt} \approx \unit[0,0351]{cm}`
* ``em``: Ein ``em`` war früher als die Breite des großen 'M' definiert. Bei der
  LaTeX-Standard-Schrift ("Computer Modern") sind beispielsweise Ziffern ``0.5em`` breit.
* ``ex``: Ein ``ex`` ist in etwa die Höhe des kleinen 'x'.

.. _Sonderzeichen:
.. _Spezielle Zeichen:

Spezielle Zeichen
-----------------

.. todo anführungszeichen

LaTeX kennt drei Arten von Zeichen: Normale Zeichen, Steuerzeichen und
Sonderzeichen:

* Normale Zeichen sind alle "normalen" Buchstaben (``a`` bis ``z``
  beziehungsweise ``A`` bis ``Z``) sowie die Ziffern und Satzzeichen.

.. index:: Steuerzeichen

* Steuerzeichen steuern LaTeX. Das Steuerszeichen ``\`` bedeutet
  beispielsweise, dass anschließend eine LaTeX-Anweisung folgt; so bewirkt
  beispielsweise ``\textbf{Text}``, dass der Text innerhalb der geschweiften
  Klammern fett gedruckt werden soll.

  Sollen Zeichen, die in LaTeX Sonderbedeutungen als Steuerzeichen haben, als
  normale Zeichen gedruckt werden, so müssen sie gemäß der folgenden Tabelle im
  laufenden Text eingegeben werden:

  .. list-table::
      :name: tab-steuerzeichen
      :widths: 50 50 50 50

      * - Eingabe
        - Ausgabe
        - Eingabe
        - Ausgabe
      * - ``\{``
        - :math:`{\color{white}|}\text{\{}{\color{white}|}`
        - ``\}``
        - :math:`{\color{white}|}\text{\}}{\color{white}|}`
      * - ``\#``
        - :math:`{\color{white}|}\text{\#}{\color{white}|}`
        - ``\&``
        - :math:`{\color{white}|}\text{\&}{\color{white}|}`
      * - ``\_``
        - :math:`{\color{white}|}\text{\_}{\color{white}|}`
        - ``\%``
        - :math:`{\color{white}|}\text{\%}{\color{white}|}`
      * - ``\$``
        - :math:`{\color{white}|}\text{\$}{\color{white}|}`
        - ``\^{}``
        - :math:`{\color{white}|}\text{\^{}}{\color{white}|}`
      * - ``\textasciitilde``
        - :math:`{\color{white}|}\text{\textasciitilde}{\color{white}|}`
        - ``\textbackslash``
        - :math:`{\color{white}|}\text{\textbackslash}{\color{white}|}`

.. .. index:: Anführungszeichen

.. * Die gewöhnlichen

.. index:: Umlaute

* Umlaute und andere Sonderzeichen sind oftmals länderspezifisch. Für
  deutschsprachige Dokumente sollten daher, wie bereits im Abschnitt
  :ref:`Umlaute und deutsche Sprachunterstützung <Umlaute und deutsche
  Sprachunterstützung>` beschrieben, in der Präambel des Dokuments folgende
  Pakete eingebunden werden:

  .. code-block:: tex

      \usepackage[ngerman]{babel}
      \usepackage[utf8]{inputenc}
      \usepackage[T1]{fontenc}

  Gewöhnliche deutschsprachige Umlaute können damit wie normale Zeichen im
  laufenden Text eingegeben werden. Weitere Sonderzeichen werden üblicherweise
  mittels eines ``\``-Zeichens eingeleitet.

  .. list-table::
      :name: tab-umlaute
      :widths: 50 50 50 50

      * - Eingabe
        - Ausgabe
        - Eingabe
        - Ausgabe
      * - ``\`a``
        - :math:`{\color{white}|}\text{\`a}{\color{white}|}`
        - ``\'a``
        - :math:`{\color{white}|}\text{\'a}{\color{white}|}`
      * - ``\.a``
        - :math:`{\color{white}|}\text{\.a}{\color{white}|}`
        - ``\^a``
        - :math:`{\color{white}|}\text{\^a}{\color{white}|}`
      * - ``\~a``
        - :math:`{\color{white}|}\text{\~a}{\color{white}|}`
        - ``\={a}``
        - :math:`{\color{white}|}\text{\={a}}{\color{white}|}`
      * - ``\u{a}``
        - :math:`{\color{white}|}\text{\u{a}}{\color{white}|}`
        - ``\v{a}``
        - :math:`{\color{white}|}\text{\v{a}}{\color{white}|}`
      * - ``\k{a}``
        - :math:`{\color{white}|}\text{\k{a}}{\color{white}|}`
        - ``\c{c}``
        - :math:`{\color{white}|}\text{\c{c}}{\color{white}|}`
      * - ``\"a``
        - :math:`{\color{white}|}\text{\"a}{\color{white}|}`
        - ``\ss``
        - :math:`{\color{white}|}\text{\ss}{\color{white}|}`

  Beispielsweise können also spanisch-sprachige Umlaute mittels ``\'`` und
  ``\~`` vor dem eigentlichen Buchstaben erzeugt werden. So ergibt die Eingabe
  von ``aqu\'i`` als Ausgabe :math:`\text{aqu\'i}`; eine Eingabe von
  ``sen\~nor`` ergibt entsprechend :math:`\text{se\~nor}`. Bei Verwendung der
  beiden obigen Pakete und einer spanisch-sprachigen Tastatur können die Umlaute
  und Sonderbuchstaben jedoch auch als normaler Text eingegeben werden.

Einige weitere Sonderzeichen sind in der folgenden Tabelle aufgelistet:

.. list-table::
    :name: tab-sonderzeichen
    :widths: 50 50 50 50

    * - Eingabe
      - Ausgabe
      - Eingabe
      - Ausgabe
    * - ``\oe``
      - :math:`{\color{white}|}\text{\oe}{\color{white}|}`
      - ``\OE``
      - :math:`{\color{white}|}\text{\OE}{\color{white}|}`
    * - ``\ae``
      - :math:`{\color{white}|}\text{\ae}{\color{white}|}`
      - ``\AE``
      - :math:`{\color{white}|}\text{\AE}{\color{white}|}`
    * - ``\aa``
      - :math:`{\color{white}|}\text{\aa}{\color{white}|}`
      - ``\AA``
      - :math:`{\color{white}|}\text{\AA}{\color{white}|}`
    * - ``\o``
      - :math:`{\color{white}|}\text{\o}{\color{white}|}`
      - ``\O``
      - :math:`{\color{white}|}\text{\O}{\color{white}|}`
    * - ``\l``
      - :math:`{\color{white}|}\text{\l}{\color{white}|}`
      - ``\L``
      - :math:`{\color{white}|}\text{\L}{\color{white}|}`
    * - ``\P``
      - :math:`{\color{white}|}\text{\P}{\color{white}|}`
      - ``\S``
      - :math:`{\color{white}|}\text{\S}{\color{white}|}`
    * - ``\textexclamdown``
      - :math:`{\color{white}|}\text{\textexclamdown}{\color{white}|}`
      - ``\textquestiondown``
      - :math:`{\color{white}|}\text{\textquestiondown}{\color{white}|}`
    * - ``\pounds``
      - :math:`{\color{white}|}\text{\pounds}{\color{white}|}`
      - ``\copyright``
      - :math:`{\color{white}|}\text{\copyright}{\color{white}|}`

Für manche Sonderzeichen müssen zusätzliche Pakete geladen werden;
beispielsweise sollte in der Präambel grundsätzlich das Paket ``marvosym``
geladen werden, da damit unter anderem mittels ``\EUR`` das Euro-Zeichen
:math:`\text{\EUR}` gesetzt werden kann.

.. _Griechische Buchstaben:

.. index:: Griechische Buchstaben

Griechische Buchstaben werden gewöhnlich mit Hilfe des Mathematik-Modus
eingegeben; dabei werden sie allerdings als Bezeichnungen für Variablen
angesehen und damit kursiv gedruckt. Sollen griechische Buchstaben in
Normalschrift in den Text eingebaut werden, so kann beispielsweise in der
Präambel das Paket ``textgreek`` geladen und anschließend die Buchstaben mittels
``\textalpha``, ``\textbeta`` usw. gesetzt werden. Als Alternative kann anstelle
des Pakets ``babel`` das Paket ``betababel`` mit den gleichen Optionen
(beispielsweise ``ngerman``) geladen werden, um innerhalb des Dokuments
beispielsweise mittels ``\bcode{logos}`` den Schriftzug :math:`\mathrm{\lambda o
\gamma o \varsigma}` zu erhalten.

.. http://www.ctan.org/pkg/textgreek

Eine sehr ausführliche Übersicht von LaTeX-Symbolen gibt es im `LaTeX-Wikibook
(Sonderzeichen)
<https://de.wikibooks.org/wiki/LaTeX-Kompendium:_Sonderzeichen>`_ und in der
PDF-Datei `Symbols-A4
<http://ftp.gwdg.de/pub/ctan/info/symbols/comprehensive/symbols-a4.pdf>`_.


.. index:: Silbentrennung
.. _Silbentrennung:

Silbentrennung
--------------

In LaTeX wird eine sprachspezifische Silbentrennung in der Präambel über das
Paket ``babel`` aktiviert, beispielsweise wird mittels
``\usepackage[ngerman]{babel}`` die Silbentrennung für die neue deutsche
Rechtschreibung aktiviert. Die Silbentrennung erfolgt in LaTeX automatisch, kann
allerdings manuell angepasst werden.

* Soll an einer Leerstelle ein Zeilenumbruch verhindert werden, kann anstelle
  eines Leerzeichens das Tilde-Zeichen ``~`` eingesetzt werden; beispielsweise
  würde ``Seite~9`` nicht zwischen ``Seite`` und ``9`` getrennt.

* Soll an einer bestimmten Stelle innerhalb eines Wortes ein Zeilenumbruch
  erzwungen werden, so ist dies mittels ``\-`` möglich, beispielsweise
  ``Archeo\-pterix``. Der Zeilenumbruch an dieser Stelle wird allerdings nur
  dann durchgeführt, wenn das Wort auch am Ende einer Zeile steht und getrennt
  werden muss; andernfalls wird die Trenn-Anweisung ``\-`` von LaTeX ignoriert.

.. index:: \hyphenation{}

Dank des ``babel``-Pakets werden zwar die meisten Wörter der deutschen Sprache
bei Zeilenumbrüchen richtig getrennt. Kommen im Text allerdings Wörter vor,
für die keine mögliche Silbentrennung bekannt ist, so kann der
``\hyphenation{}``-Anweisung am Ende der Präambel eine Liste mit
Trenn-Empfehlungen festgelegt werden: [#]_

.. code-block:: tex

    % Trennempfehlungen für folgende Wörter festlegen:
    \hyphenation{Ar-cheo-pte-rix Stau-becken Nach-kom-ma Stel-len}

Die ``\hyphenation{}``-Liste kann beliebig lang sein und sollte alle Wörter
umfassen, die beim Durchblättern des fertigen PDF-Dokuments am rechten
Seitenrand auffallen, weil sie nicht automatisch getrennt werden konnten.


.. index:: Abstand
.. _Vertikale und horizontale Abstände:

Vertikale und horizontale Abstände
----------------------------------

Einzelne Absätze werden in LaTeX durch leere Zeilen voneinander getrennt. Kommen
mehrere aufeinander folgende leere Zeilen vor, so werden die folgenden
ignoriert, der Abstand zwischen den einzelnen Absätzen bleibt somit gleich.

.. index:: Abstand; vertikal, Vertikale Abstände

Um den vertikalen Abstand zwischen einzelnen Zeilen zu verändern, gibt es
mehrere Möglichkeiten:

* Mit beispielsweise ``\\[6pt]`` wird eine neue Zeile eingeleitet mit einem
  zusätzlichen Abstand von ``6pt`` (entspricht etwa :math:`\unit[2]{mm}`).

* Zwischen zwei Absätzen kann mittels ``\vspace{Länge}`` ein beliebig
  langer vertikaler Abstand an dieser Stelle eingefügt werden, beispielsweise
  mittels ``\vspace{3cm}`` ein ``3cm`` breiter vertikaler Abstand.

.. \par
..     fügt eine Leerzeile zur Absatztrennung ein.

.. index:: Zeilenabstand, spacing (Umgebung)

* Lädt man in der Präambel mittels ``\usepackage{setspace}`` das Zusatz-Paket
  `setspace <https://ctan.org/pkg/setspace>`__, so kann man mittels der
  Anweisungen ``\onehalfspacing`` beziehungsweise ``\doublespacing`` im
  folgenden Dokumentteil einen eineinhalb-fachen beziehungsweise doppelten
  Zeilenabstand einstellen. Der ursprüngliche Zeilenabstand kann mittels
  ``\singlespacing`` wieder hergestellt werden.

* Möchte man einen anderen, selbst definierten Zeilenabstand wählen, so ist
  dies mittels der ``spacing``-Umgebung möglich:

  .. code-block:: tex

      % In der Präambel:

      \usepackage{setspace}

      % Innerhalb des Dokuments:


      \begin{spacing}{Zahl}

          % ... Inhalt ...

      \end{spacing}

  Im diesem Beispiel würde ein angegebener Zahlenwert von :math:`1,5` zu einem
  eineinhalb-fachen Zeilenabstand führen. Gibt man einen Wert kleiner als Eins
  an, so wird der Zeilenabstand entsprechend verkleinert.

.. index:: Abstand; horizontal, Horizontale Abstände

Innerhalb der einzelnen Zeilen wird das Leerzeichen als Worttrennzeichen
verwendet; hierbei werden, wenn mehrere aufeinander folgende Leerzeichen
vorkommen, die folgenden ignoriert. LaTeX richtet in Textbereichen *automatisch*
die Abstände zwischen den einzelnen Worten (und sogar den Abstand zwischen den
Buchstaben innerhalb der Worte) so aus, dass sich -- unter Berücksichtigung
möglicher Silbentrennungen -- innerhalb des jeweiligen Absatzes ein möglichst
harmonisches Gesamtbild ergibt.

Um horizontale Abstände einzufügen, gibt es ebenfalls mehrere Möglichkeiten:

.. index:: \hspace{}

* Mittels ``\hspace{}`` kann an der jeweiligen Stelle ein horizntaler Abstand
  mit einer festgelegten Länge erzeugt werden, beispielsweise mittels
  ``\hspace{1 in}`` ein Abstand von einem Zoll. Auch beliebige andere
  :ref:`Längeneinheiten <Längeneinheiten>` können gewählt werden.

* Mittels :math:`\hfill` wird in der aktuellen Zeile so viel Platz eingefügt,
  dass der anschließend eingegebene Text rechtsbündig am Zeilenrand gedruckt
  wird. Beispielsweise kann man mittels ``\hfill \today`` erreichen, dass das
  aktuelle Datum am rechten Rand der aktuellen Zeile ausgegeben wird.

.. index:: \phantom{}, Phantom-Text

* Mittels der ``\phantom{}``-Anweisung kann man einen horizontalen Abstand
  einfügen, der ebenso lang ist wie der innerhalb der geschweiften Klammern
  angegebene Text. Mit dieser Anweisung wird also Platz für den als Argument
  agegebenen Text freigehalten, dieser aber nicht gedruckt.

.. Die ``\phantom{}``-Anweisung kann auch in Tabellen oder in Mathe-Umgebungen
.. genutzt werden.


.. \setlength {\parindent} {tiefe}
..     legt die Einrücktiefe der ersten Zeile eines jeden Absatzes fest.

.. \noindent
.. \indent
..     wirken nur auf den unmittelbar folgenden Absatz.

.. todo manueller horizontaler Abstand

.. https://de.wikibooks.org/wiki/LaTeX-Wörterbuch:_Leerzeichen


.. index:: Fußnote, Randnotiz, \footnote{}, \marginpar{}
.. _Fußnote:
.. _Randnotiz:
.. _Fußnoten und Randnotizen:

Fußnoten und Randnotizen
------------------------

Innerhalb eines Textabschnitts kann mit ``\footnote{Text}`` eine Fußnote
erstellt werden. Der angegebene Text wird dabei in einer kleineren Schrift an
das Seitenende geschrieben und automatisch mit einer Nummerierung versehen.

*Beispiel:*

.. code-block:: tex

    Hier ist ein Text.\footnote{Und hier ist die zugehörige Fußnote --
    automatisch nummeriert und an der richtigen Stelle platziert!}

Standardmäßig werden Fußnoten in den Dokumentenklassen ``article`` und
``scrartcl`` durch das gesamte Dokument fortlaufend nummeriert, bei den
Dokumentklassen ``book``, ``scrbook``, ``report`` und ``scrreprt`` findet eine
Nummerierung kapitelweise statt. Überlange Fußnoten werden von LaTeX automatisch
auf mehrere aufeinander folgende Seiten aufgeteilt.

Neben Fußnoten können beispielsweise einzelne Schlagwörter oder
Kurzbeschreibungen auch auf den Seitenrändern ausgegeben werden. Die Anweisung
hierfür lautet ``\marginpar{Text}``, wobei der angegebene Text an der jeweiligen
Stelle im Dokument auf den Außenrand der Seite gedruckt wird. Möchte man auf den
anderen Rand der Seite drucken, so kann die Standard-Einstellung mittels
``\reversemarginpar`` geändert werden.


.. Randbemerkungen: \marginpar{Text}

.. index:: Querverweise, Label, Referenz, \label{}, \ref{}, \pageref{}
.. _Querverweise:

Querverweise
------------

Innerhalb eines Dokumentes können beliebige Stellen mittels so genannten Labels
markiert werden. Die Syntax für eine solche Markierung ist:

.. code-block:: tex

    % Label erzeugen:
    \label{Stichwort}

Von anderen Stellen aus kann auf die markierten Stellen mittels Querverweisen
("Referenzen") Bezug genommen werden. Es ist empfehlenswert, für
unterschiedliche Arten von Sprungmarken eigene Label-Präfixe zu verwenden,
beispielsweise können mit ``eq-`` beginnende Labels für :ref:`Gleichungen
<Gleichungen>` , mit ``fig-`` beginnende Labels für :ref:`Abbildungen
<Abbildungen>`, und mit ``tab-`` beginnende Labels :ref:`Tabellen <Tabellen>`
gesetzt werden.

Beim Verweis auf die Sprungmarke kann entweder die Kapitel- oder die
Seitennummer angezeigt werden:

.. code-block:: tex

    % Auf Label verweisen:
    Siehe Kapitel \ref{Stichwort} auf Seite \pageref{Stichwort}.

Innerhalb eines Dokuments können Querverweise auch auf sich weiter hinten
befindende Labels beziehen. Die einzelnen Querverweise werden beim Erzeugen der
fertigen PDF-Datei mittels ``pdflatex``  in eine Hilfsdatei mit der Endung
``.aux`` gespeichert. Änderungen bei Sprungmarken werden im Allgemeinen erst
beim zweiten Durchlauf von ``pdflatex`` wirksam.

Sprungmarken können nicht nur auf andere Stellen im gleichen Dokument, sondern
unter Verwendung des Zusatz-Pakets :ref:`hyperref <hyperref>` beispielsweise
auch auf Web-Adressen gesetzt werden.

.. index:: Box
.. _Boxen:
.. _Boxen, Balken und Minipages:

Boxen, Balken und Minipages
---------------------------

Ein Grundprinzip von LaTeX besteht darin, sämtliche Inhalte einer Seite auf
verschiedene Boxen aufzuteilen und diese dann zu platzieren. Die wichtigsten
Typen von Boxen sind folgende:

.. index:: Box; LR-Box
.. _LR-Box:

* ``LR-Box``:

  In einer solchen Box wird Text von links nach rechts *ohne* Zeilenumbruch
  gesetzt.

  LR-Boxen können wahlweise mit oder ohne Rahmen gesetzt werden. Soll sich die
  Größe der Box nach dem darin enthaltenen Text richten, so können folgende
  Anweisungen genutzt werden:

  .. code-block:: tex

      % LR-Box ohne Rahmen setzen:
      \mbox{Ein Text-Beispiel.}

      % LR-Box mit Rahmen setzen:
      \fbox{Ein Text-Beispiel.}

  Die Höhe einer LR-Box wird von LaTeX automatisch anhand der Größe des Inhalts
  ermittelt. Enthält beispielsweise eine ``fbox`` nur einen kurzen Text, so wird
  die Höhe der Box auf eine Zeilenhöhe festgelegt; enthält sie hingegen eine
  Abbildung mit Bildunterschrift, so wird die Höhe der Box daran festgelegt.
  Mittels LR-Boxen können also beliebige Objekte mit einem Rahmen versehen
  werden.

  Weitere LR-Boxen ohne feste Breite können beispielsweise mittels der
  Anweisungen ``\shadowbox{}``, ``\doublebox{}`` oder ``\ovalbox{}`` gesetzt
  werden; diese Boxen sind dann mit einer Schattierung hinterlegt
  beziehungsweise doppelt oder oval umrandet.

  .. index:: \makebox{}, \framebox{}


  Soll die Breite einer LR-Box explizit vorgegeben werden, so können folgende
  Anweisungen genutzt werden:

  .. code-block:: tex

      % LR-Box mit fester Breite setzen (ohne Rahmen):
      % Optionale Argumente: Breite, Ausrichtung (l,c,r)
      \makebox[8.0cm][c]{Ein Text-Beispiel (zentriert).}

      % LR-Box mit fester Breite setzen (mit Rahmen):
      \framebox[8.0cm][c]{Ein Text-Beispiel (zentriert).}



  Bei LR-Boxen *mit* Umrandung kann die Dicke des Rahmens und der Leerraum
  zwischen Umrandung und Inhalt über folgende zwei Variablen festgelegt werden:

    .. code-block:: tex

        % Rahmenbreite festlegen:
        \setlength{\fboxrule}{0.1cm}

        % Abstand zwischen Rahmen und Inhalt festlegen:
        \setlength{\fboxsep }{0.5cm}

  Um farbige Boxen zu setzen, kann, wie :ref:`weiter oben beschrieben <Farbiger
  Text>`, in der Präambel das Paket ``xcolor`` geladen werden; innerhalb des
  Dokuments können dann die Anweisungen ``\colorbox{farbname}{text}``
  beziehungsweise ``\fcolorbox{rahmenfarbe}{boxfarbe}{Text}`` genutzt werden.


  *Beispiel:*

  .. code-block:: tex

      % In der Präambel:
      % \usepackage{xcolor}

      % ...
      % Im Dokument:

      \fcolorbox{blue}{white}{\makebox[8.0cm][c]{Hallo Welt!}}

  *Ergebnis:*

  .. math::

      \fcolorbox{blue}{white}{\makebox[8.0cm][c]{Hallo Welt!}}

  Vom Paket `fancybox
  <ftp://ftp.fu-berlin.de/tex/CTAN/help/Catalogue/entries/fancybox.html>`_
  werden weitere LR-Boxen bereitgestellt:

  * Mit ``\ovalbox{Text}`` beziehungsweise ``\Ovalbox{Text}`` kann der
    angegebene Text mit einer ovalen Umrandung versehen werden.
  * Mit ``\doublebox{Text}`` wird der angegebene Text mit einem doppelten Rahmen
    versehen.
  * Mit ``\shadowbox{Text}`` wird der angegebene Text mit einem Rahmen mit
    Schattierung versehen.

  *Beispiel:*

  .. code-block:: tex

      % In der Präambel:
      % \usepackage{fancybox}

      % ...
      % Im Dokument:


      % Box mit Schattierung:
      \shadowbox{\makebox[8.0cm][c]{Hallo Welt!}}

  *Ergebnis:*

  .. math::

      \shadowbox{\makebox[8.0cm][c]{Hallo Welt!}}

  Auch das Paket `shadow
  <ftp://ftp.fu-berlin.de/tex/CTAN/help/Catalogue/entries/shadow.html>`_ stellt
  mit der Anweisung ``\shabox{}`` eine schattierte LR-Box bereit; bei dieser
  sind die Abstände zur Umrandung bewusst groß gewählt, so dass sich diese Box
  beispielsweise gut für Titelseiten eignet

  *Beispiel:*

  .. code-block:: tex

      % In der Präambel:
      % \usepackage{shadow}

      % Box mit Schattierung:
      \shabox{\makebox[8.0cm][c]{Hallo Welt!}}

  *Ergebnis:*

  .. math::

      \shabox{\makebox[8.0cm][c]{Hallo Welt!}}

  Da bei LR-Boxen kein Zeilenumbruch erfolgt, muss man selbst darauf achten,
  dass der Inhalt nicht über den Rand der Box beziehungsweise über den Rand der
  Seite hinausragt; ein weiterer Trick besteht in der Nutzung der im folgenden
  beschriebenen Parboxen.

  .. Paket fancybox für Schmuck-Rahmen

.. index:: Box; Parbox, \parbox{}
.. _Parbox:

* ``Parbox``:

  In einer solchen Box wird Text als Blocksatz gesetzt, also gegebenenfalls
  *mit* Zeilenumbruch. Insgesamt darf der Text, wie der Name der Box schon
  andeutet, maximal einen Absatz ("Paragraph") umfassen. Die Syntax dafür lautet
  etwa folgendermaßen:

  .. code-block:: tex

      % Parbox mit 8cm Breite erstellen:
      \parbox[c]{8.0cm}{\blindtext}

  Die ``\parbox{}``-Anweisung kann auch mit zusätzlichen Argumenten aufgerufen
  werden, und zwar mit der Syntax ``\parbox[pos][hoehe][ipos]{breite}{Text}``.
  Hierbei gibt ``pos`` die vertikale Ausrichtung der Box am aktuellen Absatz an;
  als mögliche Ausrichtungen sind dabei ``t`` für "top", ``c`` für "center" oder
  ``b`` für "bottom" möglich. Wird zudem über das optionale Argument ``hoehe``
  die Höhe der Parbox explizit angegeben, so kann mittels des optionalen
  Arguments ``ipos`` festgelegt werden, wie die vertikale Positionierung
  innerhalb der Parbox erfolgen soll. Neben ``b``, ``c`` und ``t`` gibt es hier
  auch die Option ``s`` ("stretched") für eine gleichmäßige Verteilung des
  Inhalts auf die gesamte Höhe der Box.

  Parboxen können auch innerhalb von LR-Boxen verwendet werden, um in diesen
  indirekt Zeilenumbrüche zu ermöglichen. Beispielsweise kann man so einen
  farbigen Rahmen um eine mehrzeilige Formel zeichnen:

  .. code-block:: tex

      % In der Präambel:
      % \usepackage{shadow}

      \shabox{
          \parbox{0.10\textwidth}{
              Hallo \\
              Welt!
          }
      }

  .. math::

      \shabox{
          \parbox{0.10\textwidth}{
              Hallo \\
              Welt!
          }
      }

.. index:: Box; Rule-Box, \rule{}
.. _Rule-Box:

* ``Rule-Box``:

  Eine solche Box dient vorwiegend zum Setzen von Linien und Balken.

  Rule-Boxen werden hauptsächlich benutzt, um einzelne Text-Abschnitte
  untereinander abzugrenzen.

  .. code-block:: tex

      % Horizontale Linie mit 5 cm Breite und 0.5 cm Höhe erstellen:
      % Allgemeine Syntax: \rule[verschiebung]{breite}{hoehe}
      \rule[0cm]{5.0cm}{0.5cm}

  .. math::

      \rule[0cm]{5.0cm}{0.5cm}

  Über das erste (optionale) Argument kann eine vertikale Verschiebung des
  Balkens gegenüber der Grundlinie der aktuellen Zeile angegeben werden. Für die
  Breite oder die Höhe kann bei Bedarf auch der Wert Null angegeben werden, um
  einen unsichtbaren Balken zu erstellen; hierdurch kann beispielsweise ein
  vertikaler Versatz an einer Stelle bewirkt werden, an dem die Anweisung
  ``\vspace{}`` nicht möglich ist (beispielsweise innerhalb eines Absatzes oder
  innerhalb einer LR-Box).

.. index:: Minipage
.. _Minipage:
.. _Minipages:

.. rubric:: Minipages

Eine ``parbox`` kann nur einen einzelnen Absatz beinhalten. Möchte man
allerdings mehrere Absätze oder sogar Abbildungen und Tabellen in eine einzelne
Box packen, so bietet sich hierfür die sogenannte "Minipage"-Umgebung an. [#]_

Die Syntax der Minipage-Umgebung ist der einer :ref:`parbox <Parbox>` sehr
ähnlich:

.. code-block:: tex

    % Minipage mit 8cm Breite erstellen:

    \begin{minipage}[c]{8.0cm}

        % ... Inhalt ...

    \end{minipage}

Auch die ``minipage``-Umgebung kann auch mit zusätzlichen Argumenten aufgerufen
werden, und zwar mit der Syntax ``\begin{minipage}[pos][hoehe][ipos]{breite}``.
Hierbei gibt ``pos`` wiederum die vertikale Ausrichtung der Box zwischen dem
vorherigen und dem nächsten Absatz an; als mögliche Ausrichtungen sind dabei
``t`` für "top", ``c`` für "center" oder ``b`` für "bottom" möglich. Wird zudem
über das optionale Argument ``hoehe`` die Höhe der Parbox explizit angegeben, so
kann mittels des optionalen Arguments ``ipos`` festgelegt werden, wie die
vertikale Positionierung innerhalb der Parbox erfolgen soll.

.. Minipages können auch beispielsweise innerhalb einer ``figure``-Umgebung
.. verwendet werden, um mehrere unterschiedlich breite Graphiken nebeneinander zu
.. positionieren

.. \begin{figure}[h]
.. \begin{minipage}[b]{0.45\textwidth}
.. \includegraphics...
.. \end{minipage}
.. \hfill
.. \begin{minipage}[b]{0.45\textwidth}
.. \includegraphics...
.. \end{minipage}
.. \caption{}
.. \end{figure}


.. Eine Minipage stellt somit gewissermaßen eine eigene "kleine Seite" dar.
.. Aufteilung auf mehrere Seiten:
.. \usepackage{framed}

.. \begin{framed}
.. Here is text
.. \begin{quote}
.. Here is quote
.. \end{quote}
.. \end{framed}

.. \fbox {\rule [-lift] {0cm} {höhe} text }
..     «Der einzurahmende Text besteht aus einem unsichtbaren vertikalen Strich,
..     der lift unterhalb der Grundlinie beginnt und höhe lang ist, gefogt von dem
..     Wort text.» Der vertikale Strich bleibt zwar unsichtbar, aber er bestimmt
..     die Unterkante und Höhe des Rahmens.



.. Möchte man die Rahmen noch weiter verändern, so kann man mit den Befehlen
.. \setlenght{\fboxrule}{}
.. \setlenght{\fboxsep}{}
.. die Strichstärke des Rahmens verändern und den Abstand zwischen dem Boxenrand und dem Inhalt
.. festsetzen.

.. \colorbox{white}{}
.. \parbox[t]{}
.. \shadowbox{}

.. ... to be continued ...

.. Horizontale Linie außerhalb von Tabelle:
..     \rule{\linewidth}{0.5pt}

.. \usepackage{tgheros} % Kommt Helvetica sehr nahe und hat gute Mathe Einbindung "Klon von Helvetica"
.. \renewcommand{\familydefault}{\sfdefault} % Schriftartwechsel komplett

.. "\usepackage{times}": sieht alles passabel nach Times aus.
.. \usepackage[scaled=.9]{helvet} für helvetica
.. Übrigens ist das Paket "times" veraltet (läd z. B. keine passenden
.. Matheschriften), siehe LaTeX-Sündenregister
.. `LaTeX Font Catalogue <http://www.tug.dk/FontCatalogue/>`_
.. Vicentino ist ne coole Schrift (handschrift-artig)
.. http://www.tug.dk/FontCatalogue/gnufreefontsans/
.. http://www.tug.dk/FontCatalogue/opensans/
.. http://www.tug.dk/FontCatalogue/dejavusans/

.. Using TrueType fonts with TeX (LaTeX) and pdfTeX (pdfLaTeX):
.. http://www.radamir.com/tex/ttf-tex.htm

.. --
.. http://www.latex-kurs.de/fragen/schriftart.html

.. Klon der Schriftart Arial
.. \documentclass{article}
.. \usepackage[latin1]{inputenc}
.. \usepackage[T1]{fontenc}
.. \usepackage{ngerman}
.. \usepackage[scaled]{uarial}
.. \begin{document}
.. Dieser Text ist in so was ähnlichem wie Arial!
.. \end{document}

.. Mehrere Schriften
.. \usepackage{mathptmx} % Hier steckt Times drin
.. \usepackage[scaled]{helvet}
.. \usepackage{courier}
.. \begin{document}
.. Dieser Text ist normaler Text und deshalb in Times.\\
.. \textsf{Dieser Text ist serifenfreier Text und deshalb in Helvetica.}\\
.. \texttt{Dieser Text ist in Maschienenschrift und deshalb in Courier.}\\
.. \end{document}

.. Ich habe mich für meine Dokumente für die Schriftgröße 11pt entschieden.
.. Zusätzlich nutze ich als Serifenfamilie Palatino, als serifenlose Avant Garede Gothic und Adobe Cou-
.. rier als Schreibmaschinenschrift:
.. \usepackage{mathpazo,avant,courier}
.. \fontfamily{pag} \selectfont

.. Dies kann man mit verschiedenen Schrifttypen erreichen, die man mit
.. \fontfamily{schrift } \selectfont
.. setzt.

.. mathpazo die Schrift Palatino

.. TimesRoman ptm
.. Palatino ppl
.. NewCenturySchoolBook pnc
.. Bookmann pbk
.. Helvetiica phv
.. AvantGard pag
.. Courier pcr

.. http://tobiw.de/tbdm/layout-1
.. Die Times wurde ursprünglich für den Einsatz in schmalen Zeitungsspalten
.. entworfen und hat dem entsprechend eine sehr geringe Laufweite. Für diesen Zweck
.. ist sie gut geeignet, für Hausarbeiten im Format DIN A4 aber eher weniger, da
.. hier immer ein schlechter Kompromiss aus zu großen Rändern, zu großem
.. Zeilenabstand (ja, 1,5-fach ist zu groß) oder zu hoher Schriftgröße geschlossen
.. werden muss. Stattdessen sollte man besser weiter laufende Schriften wie die
.. Latin Modern (Paket lmodern) oder die Platino (Paket pxfonts) verwenden. Das ist
.. im Einzelfall natürlich mit dem betreuenden Dozenten zu besprechen.


.. Mehrspaltiger Text (Hommel 48)
.. In LaTeX ist es möglich, das gesamte Dokument zweispaltig zu setzen. Dazu wird
.. der Parameter twocolumn als Option in der Dokumententklasse angegeben. Will man
.. nur einen Teil des Dokuments mit zwei Spalten setzen, kann man dies mit dem
.. Befehl \twocolumn [Einleitung] erreichen. Dieser beginnt eine neue Seite und
.. setzt fortan das Dokument zweispaltig. Der Inhalt des optionalen Parameters
.. Einleitung wird dabei über beide Spalten hinweg gesetzt. Soll wieder in einer
.. Spalte fortgefahren werden, muss man den Befehl \onecolumn aufrufen. Auch dieser
.. beginnt eine neue Seite. Für mehr als zwei Spalten gibt es die
.. multicols-Umgebung. Damit lassen sich beliebig viele Spalten nebeneinander
.. setzen. Der Befehl dazu lautet \begin{multicols} {Spaltenanzahl} [Titel]
.. [Spaltenabstand].

.. https://de.sharelatex.com/learn/Multiple_columns
.. Allgemein gute Seite!

.. [
.. \section{First Section}
.. All human things are subject to decay. And when fate summons, Monarchs must obey.
.. ]
.. Hello, here is some text without a meaning.  This text should show what 
.. a printed text will look like at this place.
.. If you read this text, you will get no information.  Really?  Is there 
.. no information?  Is there...
.. \end{multicols}

.. Spaltenabstand:
.. \setlength{\columnsep}{1cm}

.. Floating elements (tables and figures) can be inserted in a multicolumn document with wrapfig and wraptable. 

.. http://www.namsu.de/Extra/pakete/Acronym.html
.. Abkürzungsverzeichnis mit LaTeX

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Sollte der Vorspann, was nicht empfehlenswert ist, durch
    ``\section{}``-Anweisungen weiter untergliedert werden, so sollte bevorzugt
    die ``\section*{}``-Anweisung für nicht-nummerierte Abschnitts-Überschriften
    gewählt werden.

.. [#] Man kann sich innerhalb des Dokuments auch beispielsweise mittels
    ``\showhyphens{Staubecken}`` ausgeben lassen, wie das angegebene Wort von
    LaTeX automatisch getrennt würde; als Ergebnis erhält man an dieser Stelle
    als Ausgabe ``\tenrm Stau-becken``.

.. [#] Eine Einschränkung bei Minipages besteht darin, dass sie keine
    Fließumgebungen beinhalten dürfen; beispielsweise dürfen mittels der
    :ref:`tabular <tabular>`-Umgebung gesetzte Tabellen enthalten sein; diese
    darf jedoch nicht von einer :ref:`table <table>`-Umgebung umschlossen sein,
    da bei dieser die konkrete Position nicht unmittelbar festgelegt ist.

