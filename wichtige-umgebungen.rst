.. _Wichtige Umgebungen:

Wichtige Umgebungen
===================

So genannte Umgebungen werden in LaTeX verwendet, um einzelne Absätze zu
gestalten. Üblicherweise werden Umgebungen mit ``\begin{umgebung}`` eingeleitet
und mit ``\end{umgebung}`` abgeschlossen.

.. todo Verschachtelungen?

``center``, ``flushleft``, ``flushright`` -- Textausrichtung
------------------------------------------------------------

Normalerweise wird Text in Latex als Blocksatz dargestellt. LaTeX optimiert
dabei den Abstand zwischen einzelnen Wörtern und nimmt automatisch eine
Silbentrennung vor. Mittels der folgenden Umgebungen kann die Ausrichtung eines
Absatzes manuell geändert werden:

.. index:: center (Umgebung)

* *Zentrierung:* Bereiche eines LaTeX-Dokuments, die zwischen ``\begin{center}`` und
  ``\end{center}`` stehen, werden mittig auf der Seite ausgegeben.

.. index:: flushleft (Umgebung), flushright (Umgebung)

* *Flattersatz:* Bereiche eines LaTeX-Dokuments, die innerhalb einer
  ``\begin{flushleft}`` und ``\end{flushleft}`` stehen, werden linksbündig als
  Flattersatz ausgegeben. Entsprechend werden Bereiche, die zwischen
  ``\begin{flushright}`` und ``\end{flushright}`` stehen, rechtsbündig als
  Flattersatz ausgegeben.

.. todo raggedright, raggedleft

Die Flattersatz-Umgebungen werden üblicherweise für Text oder mathematische
Formeln verwendet; Zentrierungen sind hingegen auch für Abbildungen, Tabellen
oder dergleichen üblich.

.. only:: html

    .. index:: Aufzählung

.. _itemize:
.. _enumerate:
.. _description:

``itemize``, ``enumerate`` und ``description`` -- Aufzählungen
--------------------------------------------------------------

In LaTeX gibt es folgende Umgebungen für Aufzählungen:

.. index:: Aufzählung; nicht nummeriert, itemize (Umgebung)

* Mit einer ``itemize``-Umgebung kann eine nicht nummerierte Aufzählung
  erstellt werden. Die einzelnen aufzuzählenden Punkte werden mittels
  der Anweisung ``\item`` gelistet:

  .. code-block:: tex

      \begin{itemize}

          \item ...
          \item ...
          \item ...

      \end{itemize}

  Innerhalb der einzelnen Einträge werden Leerzeilen berücksichtigt,
  zwischen den einzelnen Einträgen werden Leerzeilen ignoriert.

.. index:: Aufzählung; nummeriert, enumerate (Umgebung)

* Mit einer ``enumerate``-Umgebung kann eine nummerierte Aufzählung erstellt
  werden. Die einzelnen aufzuzählenden Punkte werden ebenfalls mittels der
  Anweisung ``\item`` gelistet:

  .. code-block:: tex

      \begin{enumerate}

          \item ...
          \item ...
          \item ...

      \end{enumerate}

.. index:: description (Umgebung)

* Mit einer ``description``-Umgebung kann eine Stichwort-Aufzählung erstellt
  werden. Die einzelnen aufzuzählenden Punkte werden mittels der Anweisung
  ``\item[Stichwort]`` gelistet:

  .. code-block:: tex

      \begin{description}

          \item[Stichwort 1:] ...
          \item[Stichwort 2:] ...
          \item[Stichwort 3:] ...

      \end{description}

Aufzählungs-Umgebungen können in LaTeX auch (maximal vierfach) geschachtelt
auftreten, beispielsweise kann eine ``itemize``-Umgebung innerhalb einer
``enumerate``-Umgebung stehen:

.. code-block:: tex

    \begin{enumerate}

        \item ...

        \item

        \begin{itemize}

            \item ...
            \item ...

        \end{itemize}

        \item ...

    \end{enumerate}

LaTeX passt die Einrückungstiefen der Aufzählungen sowie die Art der
Anführungszeichen, soweit nicht manuell vorgegeben, automatisch an. Einrückungen
innerhalb des Quellcodes haben keine Auswirkung auf die PDF-Datei, sind aber für
eine bessere Lesbarkeit empfehlenswert.

.. index:: figure (Umgebung), Abbildung, Graphik, \includegraphics{}
.. _figure:

``figure`` -- Abbildungen
-------------------------

Die ``figure``-Umgebung ist zum Einbinden von Abbildungen vorgesehen; hierzu
muss in der Präambel des Dokuments das Paket ``graphicx`` mittels
``\usepackage{graphicx}`` geladen werden.

Bei der ``figure``-Umgebung handelt es sich um eine so genannte "Fließumgebung",
bei der LaTeX selbst anhand von angegebenen Optionen entscheidet, an welcher
Stelle die Abbildung am besten eingebaut wird:

.. code-block:: tex

    \begin{figure}[htb]
        \centering
        \includegraphics[width=0.8\linewidth]{image-filename.png}
        \caption{Hier kommt die Bildunterschrift hin.}
        \label{fig:image-label}
    \end{figure}

In diesem Beispiel sind als Optionen für mögliche Positionierungen der Abbildung
``htb`` angegeben: ``h`` ("here") steht für die aktuelle Position, ``t`` ("top")
für den Beginn der aktuellen Seite, ``b`` ("bottom") für das Ende der aktuellen
Seite; eine weitere mögliche Option ist ``p`` ("page"), bei der die Abbildung
optional auch auf einer separaten Seite gedruckt werden darf. Mittels eines
Ausrufezeichens kann eine Position erzwungen werden, beispielsweise bewirkt eine
Optionsangabe von ``[h!]``, dass die Abbildung nur an der aktuellen Stelle
eingebunden werden darf.

Das eigentliche Einfügen der Graphik wird durch die Anweisung
``\includegraphics{}`` übernommen. Als Optionen kann hierbei mittels ``width``
oder ``height`` die Größe der Abbildung im Dokument festgelegt werden, mittels
``angle=90`` kann die Abbildung zudem bei Bedarf um den angegebenen Winkel
(gegen den Uhrzeigersinn) gedreht werden. Als Bildformate können bei Verwendung
von ``pdflatex`` wahlweise ``png``, ``jpg`` oder ``bmp`` verwendet werden.

Befinden sich die Bilddateien nicht im gleichen Verzeichnis wie die
``.tex``-Datei, so kann bei der ``\includegraphics{}``-Anweisung auch ein
relativer oder absoluter Pfad angegeben werden. Hierbei muss allerdings geachtet
werden, dass in dem Pfadnamen keine Leerzeichen oder Unterstriche vorkommen; ist
dies der Fall, so muss vor diese "Sonderzeichen" je ein Backslash-Zeichen ``\``
geschrieben werden. Empfehlenswert ist es daher, alle zu einem LaTeX-Dokument
gehörenden Bilddateien in einem Unterordner ``pics`` abzulegen und darauf zu
achten, dass in den Dateinamen Leerzeichen und Unterstriche beispielsweise durch
Minus-Zeichen ersetzt sind.

Die ``\includegraphics{}``-Anweisung kann auch ohne eine umschließende
``figure``-Umgebung verwendet werden; in diesem Fall wird die Abbildung genau an
der Stelle im Dokument eingebunden, an der die ``\includegraphics{}``-Anweisung
steht. In diesem Fall ist es allerdings nicht möglich, die Abbildung mit einer
Bildunterschrift ("Caption") und einem Label zu versehen, mit dessen Hilfe an
einer anderen Stelle im Dokument auf die Abbildung verwiesen werden kann.
Umgekehrt können allerdings innerhalb einer ``figure``-Umgebung auch mehrere
``\includegraphics{}``-Anweisungen vorkommen, wenn beispielsweise mehrere Bilder
nebeneinander oder untereinander abgebildet werden sollen. Im letzteren Fall
muss zwischen den einzelnen ``\includegraphics{}``-Anweisungen eine
Neue-Zeile-Anweisung ``\\`` stehen, zudem können die Anweisungen ``\hspace{}``
und ``\vspace{}`` für die Ausrichtungen der Abbildungen nützlich sein.



.. index:: Tabbing
.. _tabbing:

``tabbing`` -- Ausgerichteter Text
----------------------------------

In einer ``tabbing``-Umgebung werden üblicherweise innerhalb der ersten Zeile
mittels ``\=`` Tabulatorpositionen festgelegt, an denen in den übrigen Zeilen
der Text mittels den Sprungmarken ``\>`` ausgerichtet werden kann:

.. code-block:: tex

    \begin{tabbing}

    Name1: \= Text1 \\

    Name2: \> Text2 \\
    Name3: \> Text3 \\
    ...

    \end{tabbing}

Durch die ``tabbing``-Umgebung im obigen Beispiel könnte beispielsweise ein
Dialog dargestellt werden, der sich auch über mehrere Seiten erstrecken darf;
es können allerdings auch mehrere Tabulatoren innerhalb einer Zeile auftreten.

Tabulatoren können jederzeit neu gesetzt werden, wobei die bisherigen
überschrieben werden. üblicherweise möchte man allerdings bereits in der ersten
Zeile die Tabulatoren anhand des längsten in einer "Spalte" vorkommenden Textes
festlegen. Dazu gibt es im wesentlichen zwei Möglichkeiten:

* Die erste Textzeile wird an notwendigen Stellen durch unsichtbaren Text
  aufgefüllt, der mittels ``\phantom{Text}`` erzeugt werden kann.
* Die längste Textzeile wird kopiert, am Anfang der ``tabbing``-Umgebung mit
  Tabulator- statt Sprungmarken eingefügt und mittels ``\\ \kill`` beendet. Die
  ``\kill``-Anweisung bewirkt dabei, dass die soeben abgeschlossene Textzeile
  nicht gedruckt wird (die Tabulatoren bleiben jedoch gesetzt).

.. index:: tabular (Umgebung), Tabelle
.. _tabular:
.. _Tabellen:

``tabular`` und ``table`` -- Tabellen
-------------------------------------

Tabellen werden in LaTeX üblicherweise mit Hilfe der ``tabular``-Umgebung
dargestellt. Diese hat folgende Syntax:

.. code-block:: tex

    \begin{tabular}{Spaltenoptionen}

    ...

    \end{tabular}

.. rubric:: Spaltenoptionen

Mit den Spaltenoptionen wird festgelegt, wie die Ausrichtung der einzelnen
Spalten erfolgen soll. Dabei sind folgende Angaben üblich:

* ``l``: Spalte wird linksbündig ausgerichtet
* ``r``: Spalte wird rechtbündig ausgerichtet
* ``c``: Spalte wird zentriert
* ``p{4cm}``: Spalte wird linksbündig mit fester Breite ausgerichtet

Die Anzahl an Spalten einer Tabelle wird durch die Anzahl an angegebenen
Spaltenausrichtungen festgelegt. Sollen am Rand der Tabelle oder zwischen den
einzelnen Spalten vertikale Striche entlang der Tabelle gedruckt werden, so kann
zwischen den einzelnen Spaltenausrichtungen ein ``|``-Zeichen gesetzt werden;
beispielsweise wird mit ``\begin{tabular}{|l|c|c|}`` eine Tabelle mit einer
linksbündigen und zwei zentrierten Spalten eingeleitet, zwischen denen jeweils
trennende Striche gezogen werden.

Bei den Optionen ``l``, ``r`` und ``c`` wird die Spaltenbreite von LaTeX anhand
des längsten Eintrags in der jeweiligen Spalte berechnet. Möchte man eine
*linksbündige* Spalte mit fester Breite und gegebenenfalls automatischen
Zeilenumbrüchen, so kann ``p{breite}`` verwendet werden.

Möchte man eine *zentrierte* Spalte mit fester Spaltenbreite erzeugen, so ist
die in LaTeX mittels des Pakets ``array`` möglich, das in der Präambel mittels
``\usepackage{array}`` geladen werden muss. Am Beginn einer ``tabular``-Umgebung
kann dann beispielsweise anstelle von ``p{5cm}`` als Spaltenoption
``>{\centering\arraybackslash}m{5cm}`` angegeben werden. Noch praktischer ist
es, in der Präambel hierfür eigene Spaltentypen zu definieren: [#]_

.. code-block:: tex

    \usepackage{array}

    \newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
    \newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
    \newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

Damit können beispielsweise ``L{5cm}``, ``R{5cm}`` oder ``C{5cm}`` als
Spaltenoptionen verwendet werden, um linksbündige, rechtsbündige oder zentrierte
Spalten mit fester Breite zu definieren. Der Text wird dabei vertikal stets
zentriert ausgerichtet, also jeweils mittig in die Reihen der Tabellen gesetzt.

Soll die vertikale Ausrichtung der Zeilen jeweils bündig am unteren Zeilenrand
erfolgen, wie dies beispielsweise für das Setzen von sehr langen Spaltennamen
mittels :ref:`\rotatebox{} <Gedrehter Text>` vorteilhaft sein kann, so können
nach dem obigen Prinzip weitere Spaltentypen definiert werden, wobei lediglich
``m{#1}`` ("middle") durch ``b{#1}`` ("bottom") ersetzt werden muss.

Bei Verwendung von Spaltenoptionen mit fester Breite wird der Spaltentext bei
Bedarf automatisch in der nächsten Zeile weitergeführt. Bei Verwendung der oben
definierten Spaltenoptionen ``L``, ``C`` und ``R`` kann eine Fortsetzung des
Spaltentexts in der nächsten Zeile manuell mittels ``\newline`` explizit
erzwungen werden.


.. _Spaltentrennzeichen:

.. rubric:: Spaltentrennzeichen und neue Zeilen

Innerhalb der ``tabular``-Umgebung werden die einzelnen Reihen allgemein mittels
der Neue-Zeile-Anweisung  ``\\`` voneinander getrennt. Eine Tabellenspalte kann
sich im Quellcode gegebenenfalls also  auch über mehrere Zeilen erstrecken, wenn
dies einer besseren Lesbarkeit dient.

Innerhalb einer Reihe bewirkt das Zeichen ``&`` ein Trennen der einzelnen
Spalten. Um horizontale Linien am Rand der Tabelle oder zwischen einzelnen
Reihen zu ziehen, kann zu Beginn der Tabelle sowie jeweils hinter einem ``\\``
die Anweisung ``\hline`` ("horizontal line") geschrieben werden.

Jede Reihe sollte bei :math:`n` Spalten stets :math:`(n-1)` Spaltentrennzeichen
``&`` beinhalten. Ist dies nicht der Fall, verbleibt bei einer umrandeten
Tabelle der rechte Spaltenrand in dieser Reihe.

Nach einer Neuen-Zeile-Anweisung ``\\`` kann wiederum ein in eckigen Klammern
eine Längenangabe geschrieben werden, um die aktuelle Reihe um diesen Wert zu
in ihrer Höhe zu verändern. Beispielsweise würde ein Zeilenumbruch
:math:`\\[6pt]` hinter der aktuellen Reihe einen vertikalen Abstand von ``6pt``
einfügen, was bei einer Schriftgröße von ``12pt`` einem :math:`1,5`-fachen
Zeilenabstand entspräche.

.. index:: \arraystretch{}
.. _arraystretch:

Soll der Abstand zwischen den einzelnen Reihen allgemein vergrößert werden, so
ist dies folgendermaßen möglich:

.. code-block:: tex

    % Reihenabstand auf den 1,25-fachen Wert festlegen:
    \renewcommand{\arraystretch}{1.25}

    \begin{tabular}{Spaltenoptionen}

    %%% Die eigentliche Tabelle %%%

    \end{tabular}

    % Reihenabstand wieder auf den normalen Wert zurücksetzen
    \renewcommand{\arraystretch}{1}


.. index:: \multicolumn{}
.. _multicolumn und multirow:

.. rubric:: multicolumn und multirow

Soll sich ein Eintrag einer Reihe über mehrere Spalten erstrecken, so ist dies
mittels des Pakets ``multicol``, das in der Präambel mittels
``\usepackage{multicol}`` geladen werden muss, und folgender Syntax möglich:

.. code-block:: tex

    \multicolumn{AnzahlSpalten}{Ausrichtung}{Text}

Die Ausrichtung des angegebenen Textes beginnt dann mit in der Spalte, in der
die ``\multicol{}``-Anweisung steht, und umfasst insgesamt die mit
``AnzahlSpalten`` angegebene Anzahl an Spalten. Als Ausrichtung kann ``l``,
``c`` oder ``r`` gewählt werden, Trennstriche mittels ``|`` sind ebenfalls
erlaubt.

.. index:: \multirow{}

Mittels des Pakets ``multirow``, das in der Präambel mittels
``\usepackage{multirow}`` geladen werden muss, kann ein Eintrag einer Reihe
vertikal über mehrere Reihen hinweg ausgerichtet werden:

.. code-block:: tex

    \multirow{AnzahlReihen}{Breite}{Text}

Die Ausrichtung des angegebenen Textes innerhalb der Spalte, in der die
``\multirow{}``-Anweisung steht,  beginnt mit der aktuellen Reihe und umfasst
insgesamt die mit ``AnzahlReihen`` angegebene Anzahl an Reihen. Der Inhalt der
Reihe wird zentriert zu den mit ``AnzahlReihen`` angegebenen Reihen
ausgerichtet. Als vertikal für den Text zu reservierende Breite wird meist
``*`` für eine automatische Breite gewählt, die Breite der auszurichtenden Reihe
entspricht dann der Breite der angegebenen Anzahl von Reihen.

.. index:: table (Umgebung)
.. _table:

.. rubric:: Die ``table``-Umgebung

Die eigentliche Tabelle, die durch ``\begin{tabular}`` und ``\end{tabular}``
begrenzt ist, kann zusätzlich in eine ``table``-Umgebung gepackt werden. Dabei
handelt es sich, ebenso wie bei :ref:`figure <figure>`, um eine Fließumgebung,
bei der LaTeX anhand von den angegebenen Optionen die Positionierung der Tabelle
selbst vornimmt.

.. code-block:: tex

    \begin{table}[htpb]
    \centering
    \caption{cHier kommt die Tabellenbeschriftung hin.}
    \label{tab:table-label}

    \begin{tabular}{|c|l|}
        \hline
        1 & Erste Zeile \\
        2 & erste Zeile \\
        \hline
    \end{tabular}

    \end{table}

Auch bei der ``table``-Umgebung sind folgende Optionen für mögliche
Positionierungen der Tabelle möglich: ``h`` ("here") steht für die aktuelle
Position, ``t`` ("top") für den Beginn der aktuellen Seite, ``b`` ("bottom") für
das Ende der aktuellen Seite; eine weitere mögliche Option ist ``p`` ("page"),
bei der die Tabelle optional auch auf einer separaten Seite gedruckt werden
darf. Mittels eines Ausrufezeichens kann eine Position erzwungen werden,
beispielsweise bewirkt eine Optionsangabe von ``[h!]``, dass die Tabelle nur an
der aktuellen Stelle eingebunden werden darf.

Mittels der ``\caption{}``-Anweisung kann die Tabelle beschriftet werden; in der
klassischen Textsatzung wird diese Beschriftung, anders als bei Abbildungen,
allerdings *über* die eigentliche Tabelle gesetzt. Mittels der
``\label{}``-Anweisung kann die Tabelle zudem mit einem Label versehen werden,
so dass auf sie an einer anderen Stelle im Dokument verwiesen werden kann.

.. TODO snippets ref href


.. _Mehrseitige Tabellen:

.. rubric:: Mehrseitige Tabellen

Tabellen, die mittels einer ``tabular`` bzw. ``table``-Umgebung erstellt werden,
erlauben keinen Seitenumbruch innerhalb der Tabelle. Bei längeren Tabellen
empfiehlt sich die Verwendung des Pakets ``longtable``, mit dem sich mehrseitige
Tabellen erstellen lassen.



.. index:: verbatim (Umgebung), verb (Umgebung)
.. _verbatim:

``verbatim`` -- Quelltext
-------------------------

Text innerhalb einer ``verbatim``-Umgebung wird von LaTeX nicht interpretiert,
sondern genau so dargestellt, wie er eingegeben wurde. Es finden also
beispielsweise keine automatischen Zeilenumbrüche und keine Silbentrennungen
statt; zusätzlich wird der :ref:`Schrifttyp <Schrifttyp>` auf ``typewriter``
umgestellt. [#]_

Innerhalb eines Absatzes können kurze Quelltext-Passagen mittels ``\verb|
Quelltext |`` hervorgehoben werden. Kommt in dem angegebenen Quelltext das
Symbol ``|`` vor, so kann auch ein anderes Begrenzungszeichen für ``\verb``
verwendet werden, beispielsweise ``\verb= Quelltezt =``.

.. index:: landscape (Umgebung), Querformat
.. _landscape:

``landscape`` -- Text im Querformat
-----------------------------------

Die ``landscape``-Umgebung wird dazu verwendet, um beispielsweise einen
Textteil, eine Tabelle oder eine Abbildung im Querformat auszugeben.
Hierfür muss in der Präambel das Paket ``lscape`` geladen werden:

.. code-block:: tex

    % In der Präambel:
    \usepackage{lscape}

    % ...

    % Im Dokument:

    \begin{landscape}

    %%% Der eigentliche Inhalt %%%

    \end{landscape}


.. _quote:
.. _quotation:
.. _verse:

``quote``, ``quotation`` und ``verse`` -- Einrückungen
------------------------------------------------------

.. index:: quote (Umgebung)

* Diese Umgebung wird üblicherweise für kurze Zitate verwendet, die aus einem
  einzelnen Absatz bestehen. Text innerhalb von ``\begin{quote}`` und
  ``\end{quote}`` wird links und rechts etwas eingerückt, die Zeilenlänge wird
  also gegenüber dem restlichen Text etwas verringert. Neue Absätze innerhalb
  einer ``quote``-Umgebung beginnen ebenfalls linksbündig.

.. index:: quotation (Umgebung)

* Diese Umgebung wird üblicherweise für längere Zitate verwendet, die aus mehr
  als einem Absatz bestehen. Text innerhalb von ``\begin{quotation}`` und
  ``\end{quotation}`` wird ebenfalls links und rechts etwas eingerückt, die
  Zeilenlänge wird also gegenüber dem restlichen Text etwas verringert. Auch
  innerhalb einer ``quotation``-Umgebung werden Absätze linksbündig dargestellt,
  wobei die erste Zeile eines neuen Absatzes leicht eingerückt wird.

.. index:: verse (Umgebung)

* Diese Umgebung wird üblicherweise für Gedichte verwendet. Innerhalb von
  ``begin{verse}`` und ``\end{verse}`` werden einzelne Zeilen durch ``\\``
  explizit beendet; sehr lange Zeilen werden in den nachfolgenden Zeilen
  zusätzlich eingerückt und so als zusammengehörig gekennzeichnet. Leerzeilen
  werden zur Trennung von Absätzen verwendet.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Siehe: https://tex.stackexchange.com/questions/12703/how-to-create-fixed-width-table-columns-with-text-raggedright-centered-raggedlef

.. [#] Die Quelltext-Umgebung ``verbatim`` kann auch durch ``\begin{verbatim*}``
    und ``\end{verbatim*}`` begrenzt werden, wobei bei dieser Version
    Leerzeichen durch ein eigenes Symbol (:math:`\textvisiblespace`) dargestellt werden. Dies kann
    zur Hervorhebung der Anzahl von Leerzeichen in einer Codestelle nützlich
    sein.


