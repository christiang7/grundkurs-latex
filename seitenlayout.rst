
.. _Seitenlayout:

Seitenlayout
============

Das Standard-Layout eines Dokuments wird in der Präambel der LaTeX-Datei
durch die Wahl der Dokumentklasse sowie eines Seiten-Stils festgelegt.
Bei der Wahl der Dokumentklasse sind für das Seitenlayout insbesondere die
Zusatz-Optionen von Bedeutung:

*Beispiel:*

.. code-block:: tex

    \documentclass[a4paper, 12pt, halfparskip]{article}

.. a4paper is just one of the many pre-defined page sizes built-in, other include:
.. a0paper, a1paper, ..., a6paper, b0paper, b1paper, ..., b6paper, letterpaper,
.. legalpaper, executivepaper.

Durch die im obigen Beispiel angegebenen Optionen wird als Seitengröße des
Dokuments ``DinA4`` gewählt und die Standard-Schriftgröße auf ``\unit[12]{pt}``
gesetzt. Durch Verwendung der Option ``halfparskip`` werden einzelne Absätze, die
im im LaTeX-Code durch leere Zeilen begrenzt werden, auch in der Druckversion
durch eine Leerzeile getrennt.


.. _Einseitige und zweiseitige Dokumente:

.. rubric:: Einseitige und zweiseitige Dokumente

Als weitere Option kann bei der Wahl der Dokumentklasse beispielsweise mittels
``\documentclass[twoside]{report}`` festgelegt werden, dass das vorliegende
Dokument in Buchform gedruckt werden soll. Dies hat als Konsequenz, dass
zwischen ungeradzahligen und geradzahligen Seiten unterschieden werden muss:
Ungeradzahlige Seiten befinden sich bei einem aufgeschlagenen Buch stets auf der
rechten, geradzahlige entsprechend auf der linken Seite.

.. _oneside:

Da Bücher meist von vorne nach hinten durchblättert werden, beginnen neue
Kapitel meist auf den rechten, also ungeradzahligen Seiten; notfalls wird dabei
in Kauf genommen, dass die linke (geradzahlige) Buchseite leer bleibt. Bei der
Dokumentklasse ``book`` beziehungsweise der auf europäische Seitenformate
angepassten Version ``scrbook`` wird ein zweiseitiges Dokumentenlayout als
Standard angesehen; man kann dies bei Bedarf mittels
``\documentclass[oneside]{scrbook}`` ändern.

Standardmäßig gelten für die Standard-Dokumentklassen folgende Einstellung:

* Bei ``book`` beziehungsweise ``scrbook`` wird ohne weitere Einstellungen
  *zweiseitig* gedruckt.

* Bei ``report`` beziehungsweise ``scrreprt``  wird ohne weitere Einstellungen
  *einseitig* gedruckt.

* Bei ``article`` beziehungsweise ``scrartcl`` wird ohne weitere Einstellungen
  *einseitig* gedruckt.

Auch "einseitige" Dokumente können selbstverständlich beim Drucken beidseitig
gedruckt werden; die Bezeichnung bezieht sich lediglich auf das Layout des
PDF-Dokuments: Die Festlegung auf ``oneside`` beziehungsweise ``twoside`` hat
unter anderem auch Auswirkungen auf Kopf- und Fußzeilen sowie auf die jeweiligen
Seitenränder.


.. index:: Kopfzeile, Fußzeile
.. _Kopf- und Fußzeilen:

Kopf- und Fußzeilen
-------------------

LaTeX druckt mit den Standard-Einstellungen automatisch auf jede Seite unten
mittig die jeweilige Seitennummer. Soll dies verhindert oder zusätzlich der
jeweilige Abschnittsname als Kopfzeile jeder Seite gedruckt werden, so kann
dieses mittels der Funktion ``\pagestyle{}`` angepasst werden:

* Mit ``\pagestyle{empty}`` wird festgelegt, dass weder Kopf- noch Fußzeilen
  gedruckt werden.
* Mit ``\pagestyle{plain}`` wird festgelegt, dass ausschließlich Fußzeilen,
  jedoch keine Kopfzeilen gedruckt werden.
* Mit ``\pagestyle{headings}`` wird festgelegt, dass sowohl Fußzeilen als auch
  Kopfzeilen mit den jeweiligen Abschnitts-Überschriften gedruckt werden.

Die Anweisung ``\pagestyle{}`` kann sowohl in der Präambel als auch an jeder
anderen Stelle im Dokument genutzt werden; sie hat Auswirkung auf alle folgenden
Seiten. Soll nur das Layout der jeweils aktuellen Seite verändert werden, so
kann anstelle von ``\pagestyle{}`` die Funktion ``\thispagestyle{}`` mit
gleicher Syntax verwendet werden.

Mit ``\pagestyle{myheadings}`` kann das Design der Kopf- und Fußzeilen
individuell festgelegt werden; üblicherweise werden dafür allerdings die im
Folgenden näher beschriebenen Pakete ``fancyhdr`` oder ``scrlayer-scrpage``
verwendet.

.. _Individuelle Kopf- und Fußzeilen mit fancyhdr:

.. rubric:: Individuelle Kopf- und Fußzeilen mit ``fancyhdr``:

Das Paket `fancyhdr
<ftp://ftp.rrzn.uni-hannover.de/pub/mirror/tex-archive/help/Catalogue/entries/fancyhdr.html>`__,
das für die Dokumentklassen ``article``, ``report`` und ``book`` vorgesehen ist,
stellt den neuen Pagestyle ``fancy`` bereit. Das Paket mit den
Basis-Einstellungen wird folgendermaßen eingebunden: [#]_

.. code-block:: tex

    % In der Präambel:
    \usepackage{fancyhdr}

    % ...

    \pagestyle{fancy}

Für das Layout der Kopfzeilen steht anschließend die Anweisung
``\fancyhead{}``, für die Definition der Fußzeilen die Anweisung
``\fancyfoot{}`` zur Verfügung. Als Argumente werden in geschweiften Klammern
die zu druckenden Informationen angegeben; zudem wird in eckigen Klammern die
horizontale Position festgelegt, an der die Informationen gedruckt werden
sollen: ``L`` steht für "left", ``R`` für "right" und ``C`` für "center";
diese Angaben können wahlweise mit ``O`` für "odd" (ungeradzahlig, rechts)
oder ``E`` für "even" (geradzahlig, links) kombiniert werden:

.. code-block:: tex

    % Bisherige Einstellungen deaktivieren (optional):
    \fancyhead{}
    \fancyfoot{}

    \fancyhead[RO,LE]{\today}     % Aktuelles Datum auf ungeradzahligen Seiten rechts,
                                  % auf geradzahligen links ausgeben.

    \fancyfoot[RO,LE]{\thepage}   % Seitennummer auf ungeradzahligen Seiten rechts,
                                  % auf geradzahligen links ausgeben.


Zudem kann festgelegt werden, ob beziehungsweise mit welcher Stärke eine
horizontale Linie zwischen dem eigentlichen Text und der Kopf- beziehungsweise
Fußzeile gedruckt werden soll:

.. code-block:: tex

    \renewcommand\headrulewidth{2pt}    % Liniendicke zwischen Kopfzeile und Text festlegen
    \renewcommand\footrulewidth{0pt}    % Linie zwischen Fußzeile und Text deaktivieren

Auch mehrzeilige Kopfzeilen sind möglich; hierfür muss allerdings mittels
beispielsweise ``\setlength\headheight{24pt}`` die Höhe der Kopfzeilen-Box
angepasst werden. Bei der Festlegung der Kopfzeile kann die Zeilentrennung
dann wie üblich mittels ``\\`` erreicht werden.

.. Inhalte:
.. Namen: \chaptermark, \sectionmark
.. Nummern: \thechapter, \thesection
.. \renewcommand{\chaptermark}[1]%
.. {\markboth{\MakeUppercase{\thechapter.\ #1}}{}}
.. \renewcommand{\sectionmark}[1]%
.. {\markright{\MakeUppercase{\thesection.\ #1}}}

.. _Individuelle Kopf- und Fußzeilen mit scrlayer-scrpage:

.. rubric:: Individuelle Kopf- und Fußzeilen mit ``scrlayer-scrpage``:

.. https://www.ctan.org/pkg/scrlayer-scrpage?lang=de

Das Paket `scrlayer-scrpage <https://ctan.org/pkg/scrlayer-scrpage>`__, das für
die Dokumentklassen ``scrartcl``, ``scrrprt`` und ``scrbook`` vorgesehen ist,
stellt den neuen Pagestyle ``scrheadings`` bereit. Die Syntax für das Einbinden
des Pakets und die Festlegung der einzelnen Informationen sieht für einseitige
Dokumente beispielsweise folgendermaßen aus: [#]_


.. code-block:: tex

    % Präambel:

    \documentclass{scrartcl}
    \usepackage{scrlayer-scrpage}

    % Bisherige Einstellungen für Kopf- und Fußzeilen löschen:
    \clearpairofpagestyles

    % Zentriert auf linken Seiten die aktuelle Kapitelüberschrift,
    % auf rechten Seiten die Überschrift des aktuellen Abschnitts ausgeben:
    \chead{\headmark}

    % Zentriert die Seitenzahl ausgeben (auch beim Seitenstil "scrplain"):
    \cfoot*{\pagemark}


    \pagestyle{scrheadings}

Durch die Anweisung ``\headmark`` wird bei Verwendung der Voreinstellungen
automatisch auf linken Seiten die aktuelle Kapitelüberschrift, und auf rechten
Seiten die Überschrift des aktuellen Abschnitts inklusive Nummer ausgegeben.
Diese Voreinstellungen können mit den Anweisungen ``\automark{}``
beziehungsweise  ``\automark*{}`` angepasst werden; erstere überschreibt alle
bisherigen Einstellungen, letztere "überlagert" lediglich die bisherigen
Einstellungen.

Möchte man beispielsweise auf den rechten Seiten so lange die
Kapitel-Überschrift ausgeben, bis der erste Abschnitt beginnt, so kann dies
folgendermaßen erreicht werden:

.. code-block:: tex

      % Sowohl auf rechten Seiten (eckige Klammern) als auch auf linken Seiten
      % (geschweifte Klammern) Kapitel-Überschriften ausgeben:
      \automark[chapter]{chapter}

      % Linke Seiten-Definitionen unverändert lassen, auf rechten hingegen
      % -- sofern vorhanden -- Abschnitts-Überschriften ausgeben:
      \automark*[section]{}

Bei einseitigen Dokumenten existieren für LaTeX nur "rechte" Seiten; die
Seiten werden dann also unabhängig von ihrer Nummer als ungerade gewertet. Für
zweiseitige Dokumente können die einzelnen Informationen mittels folgender
Anweisungen explizit gesetzt werden:

.. code-block:: tex

    % Inhalte der Kopfzeilen für rechte Seiten:
    \lehead[Inhalt plain.scrheadings]{Inhalt scrheadings} % left even
    \cehead[Inhalt plain.scrheadings]{Inhalt scrheadings} % center even
    \rehead[Inhalt plain.scrheadings]{Inhalt scrheadings} % right even

    % Inhalte der Kopfzeilen für linke Seiten:
    \lohead[Inhalt plain.scrheadings]{Inhalt scrheadings} % left odd
    \cohead[Inhalt plain.scrheadings]{Inhalt scrheadings} % center odd
    \rohead[Inhalt plain.scrheadings]{Inhalt scrheadings} % right odd

In den eckigen Klammern können optional die Inhalte für den Seitenstil
``scrplain`` festgelegt werden; soll dieser für eine bestimmte Angabe mit dem
Inhalt des Seitenstils ``scrheadings`` übereinstimmen, so kann beispielsweise
anstelle von ``\cehead[Inhalt]{Inhalt}`` auch ``\cehead*{Inhalt}`` geschrieben
werden. Sollen die gleichen Einstellungen sowohl für ungerade als auch für
gerade Seitenzahlen gelten, so kann beispielsweise auch einfacher ``\chead{}``
als Anweisung genutzt werden.

Allgemein müssen nicht alle obigen Anweisungen genutzt werden, sondern nur
diese, die für die gewünschten Positionen vorgesehen sind. Für die Fußzeilen
existieren die gleichen Anweisungen, wobei lediglich ``head`` durch ``foot``
ersetzt werden muss.



.. \usepackage{lastpage}
.. \cfoot{\thepage\ of \pageref{LastPage}}


.. index:: Seitenrand
.. _Seitenränder:

Seitenränder
------------

In LaTeX werden bei Verwendung von ``a4paper`` als Dokumentgröße und
Standard-Einstellungen verhältnismäßig breite Seitenränder :math:`(\unit[1]{in}
\approx \unit[2,54]{cm})` gedruckt. Dies hat damit zu tun, dass aus Sicht der
Typographie die einzelnen Zeilen nicht zu viel Text beinhalten sollten (nur
circa :math:`70` Zeichen), um die Lesbarkeit zu erhöhen.

Bei zweiseitigen Dokumenten ist der innere Rand schmäler als der äußere; er ist
so breit gewählt, dass ein Buch nach der Bindung im aufgeschlagen Zustand mittig
ebenso viel Abstand zwischen den Texten auf der linken und der rechten Seite
aufweist wie die Texte zu den jeweiligen Seitenrändern.


.. _Anpassung der Seitenränder mittels geometry:

.. rubric:: Anpassung der Seitenränder mittels ``geometry``

Möchte man die Seitenränder allgemein anpassen, so ist dies am einfachsten durch
Verwendung des `geometry
<http://ftp.fernuni-hagen.de/ftp-dir/pub/mirrors/www.ctan.org/macros/latex/contrib/geometry-de/geometry-de.pdf>`__-Pakets
möglich:

.. code-block:: tex

    % In der Präambel:

    \usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}

Sollen die so definierten Einstellungen, die Auswirkungen auf das gesamte
Dokument haben, zu einem späteren Zeitpunkt innerhalb des Dokuments wieder
geändert werden, so ist dies mittels der ``\newgeometry{}``-Anweisung möglich:

.. code-block:: tex

    % Innerhalb des Dokuments:

    \newgeometry{left=1cm, right=1cm, top=2.5cm, bottom=2.5cm}

Diese Anweisung hat Auswirkungen auf das Layout der aktuellen und aller
folgenden Seiten beziehungsweise bis eine neue ``\newgeometry{}``-Anweisung
gesetzt wird. Um lediglich die aktuelle Seite etwas zu vergrößern, kann zudem
als Anweisung ``\enlargethispage{3cm}`` o.ä. verwendet werden.


.. _Abstände manuell festlegen:

.. rubric:: Abstände manuell festlegen

In LaTeX gibt es mehrere Variablen, die das Seitenlayout beeinflussen. Mittels
der Pakete `layout <https://ctan.org/pkg/layout>`__  beziehungsweise `layouts
<https://ctan.org/pkg/layouts>`__ können die Namen dieser Variablen sowie die
bei den aktuellen Einstellungen vorherrschenden Werte angezeigt werden.

* Die für das Seitenlayout relevanten Variablen sowie ihre aktuellen Werte
  können mittels des ``layout``-Pakets folgendermaßen angezeigt werden:

  .. code-block:: tex

      % Präambel:
      \documentclass[halfparskip,12pt,twoside]{scrreprt}
      \usepackage[utf8]{inputenc}
      \usepackage[T1]{fontenc}
      \usepackage[german]{babel}
      \usepackage[top=2cm,bottom=2.5cm]{geometry}
      \usepackage{layout}

      \begin{document}

      % Seitenlayout-Variablen und aktuelle Werte ausgeben:
      \layout

      \end{document}

  Der obige Code liefert etwa folgendes Ergebnis:

  .. image:: pics/layout.png
      :align: center
      :width: 60%

  Die einzelnen Längen können mittels ``\setlength{laengen-variable}{wert}``
  gesetzt werden, beispielsweise ``\setlength{\oddsidemargin}{36pt}``;
  selbstverständlich können auch andere :ref:`Längenmaße <Einheiten>` wie
  ``mm``, ``cm`` oder ``in`` genutzt werden.
  Die Werte der Längen-Variablen ``\topmargin``, ``\oddsidemargin`` und
  ``\evensidemargin`` werden dabei zu den beispielsweise mittels des
  ``geometry``-Pakets eingestellten Randwerten hinzuaddiert.

* Weitere beispielsweise für das Layout der einzelnen Absätze relevanten
  Variablen sowie ihre aktuellen Werte lassen sich mittels des Pakets
  ``layouts`` folgendermaßen anzeigen:

  .. code-block:: tex

    % Präambel:
    \documentclass[halfparskip,12pt,twoside]{scrreprt}
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage[german]{babel}
    \usepackage[top=2cm,bottom=2.5cm]{geometry}
    \usepackage{layouts}
    \usepackage{caption}

    \begin{document}

    \setuplayouts

    % Allgemeines Absatz-Layout anzeigen:
    \begin{figure}
        \paragraphdiagram
        \caption*{Für einzelne Absätze relevante Variablen.}
    \end{figure}

    % Aktuelles Absatz-Layout anzeigen:
    \begin{figure}
        \currentparagraph
        \paragraphdesign
        \caption*{Absatz-Variablen des aktuellen Dokuments.}
    \end{figure}

    \end{document}

  Als Ergebnis erhält man beispielsweise:

  .. image:: pics/layouts-paragraph-diagrams.png
      :align: center
      :width: 50%

.. Juergens FernuniHagen2 S.22:
.. Noch eine Anmerkung zum Erstzeileneinzug: Die erste Zeile eines neuen Absatzes
.. wird standardmäßig um die Größenangabe, die durch ``\parindent`` definiert ist,
.. eingezogen. Sollen einzelne Absätze nicht eingezogen werden, so kann direkt vor
.. diese Absätze die Anweisung ``\noindent`` gesetzt werden.

* Nach dem gleichen Prinzip lassen sich mittels des ``layouts``-Pakets auch die
  für Aufzählungen relevanten Variablen und ihre Werte anzeigen:

  .. code-block:: tex

      \begin{figure}
          \listdiagram
          \caption*{Für Listen relevante Variablen.}
      \end{figure}

      \begin{figure}
          \listdesign
          \caption*{Listen-Variablen des aktuellen Dokuments.}
      \end{figure}

  Ergebnis:

  .. image:: pics/layouts-listdiagram.png
      :align: center
      :width: 50%

  .. image:: pics/layouts-listdesign.png
      :align: center
      :width: 50%

In der `Dokumentation des layouts-Pakets
<http://ftp.gwdg.de/pub/ctan/macros/latex/contrib/layouts/layman.pdf>`__ sind
weitere entsprechende Beispiele aufgelistet, welche die Platzierung von Fußnoten
sowie das Aussehen des Inhaltsverzeichnisses näher beschreiben.

.. % Allgemeines Seitenlayout erstellen:
.. \begin{figure}[h!]
..     \drawparameterstrue
..     \printparameterstrue
..     \oddpagelayoutfalse
..     \twocolumnlayoutfalse
..     \pagediagram
..     \caption*{Einseitiges geradzahliges Seitenlayout.}
.. \end{figure}

.. \newpage

.. % Seitenlayout mit aktueller Werte-Tabelle erstellen:
.. \begin{figure}
..     \currentpage
..     \drawparameterstrue
..     \oddpagelayouttrue
..     \pagedesign
..     \caption*{Ungeradzahliges Seitenlayout des aktuellen Dokuments.}
.. \end{figure}



.. To create a typical two-column layout:

.. \begin{multicols}{2}
..   lots of text
..   \ldots
.. \end{multicols}

.. The parameter \columnseprule holds the width of the vertical rules. By default,
.. the lines are omitted as this parameter is set to a length of 0pt. Do the
.. following before the beginning of the environment:

.. \setlength{\columnseprule}{1pt}

.. This will draw a thin line of 1pt in width. A thick line would not look very
.. pleasing, however, you are free to put in any length of your choosing. Also, to
.. change the horizontal space in between columns (the default is set at 10pt,
.. which is quite narrow) then you need to change the \columnsep parameter:

.. \setlength{\columnsep}{20pt}


.. Daumen-Index: "Thumb-Index"



.. TODO margins

.. TODO titelseite, siehe http://tobiw.de/tbdm/titelseiten

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Sollte die normale Textbreite ``\textwidth`` manuell geändert werden, so
    muss ``\pagestyle{fancy}`` anschließend erneut aufgerufen werden, da sich
    das Layout der Kopf- und Fußzeilen an dieser Länge orientiert.

.. [#] In der  `Original-Anleitung
    <http://ftp.fernuni-hagen.de/ftp-dir/pub/mirrors/www.ctan.org/macros/latex/contrib/koma-script/doc/scrguide.pdf>`__
    wird empfohlen, das Paket ``scrlayer-scrpage`` nicht in Kombination mit den
    Seitenstilen ``headings`` und ``myheadings`` zu verwenden; stattdessen
    sollte unbedingt ``scrheadings`` verwendet werden.

    Das Paket ``scrlayer-scrpage`` ist mit dem Vorgänger-Paket ``scrpage2``
    weitestgehend abwärts-kompatibel, so dass für eine Aktualisierung in den
    meisten Dokumenten lediglich ``\usepackage{scrpage2}`` durch
    ``\usepackage{scrlayer-scrpage}`` ersetzt werden muss.

