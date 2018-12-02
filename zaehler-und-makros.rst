
.. _Zähler und Makros:

Zähler und Makros
=================

In LaTeX können gibt es einige (Zähl-)Variablen, die standardmäßig genutzt
werden können; zudem können nach Belieben eigene Variablen definiert werden.
Ebenso können eigenen Anweisungen ("Makros") definiert werden, so dass
beispielsweise sich häufig wiederholende Text-Formatierungen mit geringerem
Aufwand erreichen lassen.

.. index:: Counter, Zähler, Variablen
.. _Zähler-Variablen:

Zähler-Variablen
----------------

Alle Zähler-Variablen, die von LaTeX verwendet werden, haben Standard-Namen;
diese wiederum haben entsprechende LaTeX-Anweisungen, welche die jeweiligen
Zähler-Werte ausgeben. Um beispielsweise innerhalb eines LaTeX-Dokuments den
Wert eines Zählers mit dem Namen ``number`` auszugeben, genügt an dieser Stelle
ein Aufruf von ``\thenumber``.

.. .. list-table:: LaTeX-Standardzähler

.. list-table::
    :name: tab-standardzaehler
    :widths: 50 50

    * - Verwendungszweck
      - Zähler-Variablen
    * - Kapiteleinteilung
      - ``part``, ``chapter``, ``section``, ``subsection``, ``subsubsection``,
        ``paragraph``, ``subparagraph``
    * - Seiten-Nummerierung
      - ``page``
    * - Aufzählungs-Nummerierung
      - ``enumi``, ``enumii``, ``enumiii``, ``enumiv``
    * - Sonstige Nummerierungen
      - ``figure``, ``table``, ``footnote``, ``equation``

Sämtliche in der obigen Tabelle aufgelistete Zähler haben zu Beginn eines
Dokuments den Wert Null und beim Aufruf der Anweisung, das die Numerierung
erzeugt, *vor* der Ausgabe um ``1`` erhöht. Eine Ausnahme hierbei bildet der
Zähler ``page``; dieser hat zu Beginn des Dokuments den Wert Eins und wird stets
*nach* einer Ausgabe automatisch erhöht.

Die Anpassung der Zähler wird von LaTeX weitgehend automatisch vorgenommen.
Beispielsweise wird durch die Anweisung ``\section{}`` die Zähler-Variable
``section`` um ``1`` erhöht; zugleich wird dadurch die Zähler-Variable
``subsection`` wieder auf ``0`` gesetzt.

Manuell können folgende Anweisungen genutzt werden, um die jeweilgen Zähler zu 
beeinflussen:

.. list-table::
    :name: tab-zaehler-anweisungen
    :widths: 50 50 

    * - Anweisung
      - Beschreibung
    * - ``\newcounter{name}``
      - Definition eines neuen Zählers
    * - ``\setcounter{name}{Wert}``
      - Wertzuweisung (bisheriger Wert wird überschrieben)
    * - ``\addtocounter{name}{wert}``
      - Addition eines Werts zum aktuellen Zählerwert
    * - ``\stepcounter{name}``
      - Erhöhung des Zählerwerts um :math:`1`
    * - ``\roman{name}``
      - Umschalten des Zählers auf römische Ziffern
    * - ``\arabic{name}``
      - Umschalten des Zählers auf arabische Ziffern
    * - ``\alph{name}``
      - Umschalten des Zählers auf Kleinbuchstaben
    * - ``\Alph{name}``
      - Umschalten des Zählers auf Großbuchstaben

Beispielsweise kann die ``\setcounter{}``-Anweisung genutzt werden, um die
Seitennummerierung im laufenden Dokument zu ändern (beispielsweise wieder bei
:math:`1` beginnen zu lassen).

.. Beispiel für eine alphabetische Auflistung mit LaTeX:

.. .. code-block:: tex

..     \newcounter{ale}
..     \newcommand{\abc}{\item[\alph{ale})]\stepcounter{ale}}
..     \newenvironment{liste}{\begin{itemize}}{\end{itemize}}
..     \newcommand{\aliste}{\begin{liste} \setcounter{ale}{1}}
..     \newcommand{\zliste}{\end{liste}}
..     \newenvironment{abcliste}{\aliste}{\zliste}

..     \begin{small}
..     \begin{verbatim}
..     \newcounter{ale}
..     \newcommand{\abc}{\item[\alph{ale})]\stepcounter{ale}}
..     \newenvironment{liste}{\begin{itemize}}{\end{itemize}}
..     \newcommand{\aliste}{\begin{liste} \setcounter{ale}{1}}
..     \newcommand{\zliste}{\end{liste}}

..     \newenvironment{abcliste}{\aliste}{\zliste}
..     \begin{abcliste}
..     \abc 111
..     \abc 222
..     \abc 333
..     \end{abcliste}


.. index:: Makro, \necommand{}
.. _Makros definieren:

Makros definieren
-----------------

Mit ``\newcommand{}`` kann man in LaTeX eigene Anweisungen ("Makros")
definieren. Die allgemeine Syntax hierzu lautet:

.. code-block:: tex

    \newcommand{\Anweisungsname}[Parameter-Anzahl][Voreinstellungen]{Inhalt}

Der Anweisungsname sowie der eigentliche Inhalt sind Pflichtangaben. Kommt die
selbst definierte Anweisung ohne weitere Parameter aus, so können die übrigen
angaben weggelassen werden:

*Beispiel:*

.. code-block:: tex

    % Neue Anweisungen  definieren:

    \newcommand{\datum}{ 1. April}
    \newcommand{\scherz}{Scherz für den \datum}
    \newcommand{\lx}{\fbox{\LaTeX}}

    % Anweisung nutzen:

    Das ist kein \scherz!

    Hallo \lx

*Ergebnis:*

.. math::

    \newcommand{\datum}{\text{ 1. April}}
    \newcommand{\scherz}{\text{ Scherz für den \datum}}
    \text{Das ist kein} \scherz!

.. math::

    \newcommand{\lx}{\fbox{\LaTeX}}
    \text{Hallo } \lx

Gibt man bei der Definition eines Makros eine bestimmte Anzahl (maximal `9`) an
Parametern an, so muss auch beim Aufruf des Makros genau diese Anzahl an
Parametern angegeben werden. Innerhalb der Makro-Definition werden die Parameter
mit ``#1``, ``#2`` usw. bezeichnet:

*Beispiel:*

.. code-block:: tex

    % In der Präambel:
    % \usepackage{shadow}

    % Neue Anweisung mit _einem_ Parameter definieren:
    \newcommand{\shac}[1]{\shabox{ \centering \textsc{ #1 } }}

    % Anweisung nutzen:
    \shac{Hallo Welt!}

*Ergebnis:*

.. math::

    \newcommand{\shac}[1]{\shabox{ \centering \textsc{ #1 } }}
    \shac{Hallo Welt!}

Möchte man ein Makro definieren, das neben einem Pflicht-Parameter auch einen
optionalen Parameter hat, so kann man für diesen einen Standard-Wert festlegen.
Innerhalb der Makro-Definition wird der optionale Parameter automatisch mittels
``#1`` bezeichnet.

*Beispiel:*

.. code-block:: tex

    % In der Präambel:
    % \usepackage{shadow}

    % Neue Anweisung mit Pflicht- und optionalem Parameter definieren:
    \newcommand{\shaC}[2][5cm]{ \shabox{\parbox{#1}{ \centering \textsc{ #2 } }} }

    % Anweisung nutzen:
    \shaC{Hallo Welt!} \\
    \shaC[10cm]{Hallo Welt!}

*Ergebnis:*

.. math::

    \newcommand{\shaC}[2][5cm]{ \shabox{\parbox{#1}{ \centering  \textsc{ #2 } }} }
    \shaC{Hallo Welt!}

.. math::

    \newcommand{\shaC}[2][5cm]{ \shabox{\parbox{#1}{ \centering \textsc{ #2 } }} }
    \shaC[10cm]{Hallo Welt!}

Sollte eine mathematische Formel innerhalb der Makro-Definition vorkommen, so
sollte diese unbedingt mit der Anweisung ``\ensuremath{Formel}`` umschlossen
werden. Hierdurch wird sichergestellt, dass das Makro korrekt abläuft,
unabhängig davon, ob das Makro im Mathe-Modus aufgerufen wird oder nicht.


.. Overwriting existing commands

.. If you define a command that has the same name as an already existing LaTeX
.. command you will see an error message in the compilation of your document and
.. the command you defined will not work. If you really want to override an
.. existing command this can be accomplished by renewcommand:

.. \renewcommand{\S}{\mathbb{S}}

... to be continued ...

.. Just as with commands, you can define new environments.
.. Defining simple environments

.. The new environment definition is achieved by the \newenvironment tag:

.. \newenvironment{boxed}
..     {\begin{center}
..     \begin{tabular}{|p{0.9\textwidth}|}
..     \hline\\
..     }
..     { 
..     \\\\\hline
..     \end{tabular} 
..     \end{center}
..     }
.. %--------------------------------------------------
 
.. Below this line a boxed environment is used
 
.. \begin{boxed}
.. This is the text formatted by the boxed environment
.. \end{boxed}
 
.. This text is again outside the environment


.. Eigene Variablen definieren:

.. add the following to you preamble:

.. \newcommand{\newCommandName}{text to insert}

.. Then you can just use \newCommandName{} in the text
.. You can also use just \newCommandName, but take care of whitespaces then!

.. Use \def command:

.. \def \variable {Something that's better to use as a variable}

.. Be aware that \def overrides preexisting macros without any warnings and
.. therefore can cause various subtle errors. To overcome this either use
.. namespaced variables like my_var or fall back to \newcommand, \renewcommand
.. commands instead.

.. For variables describing distances, you would use \newlength (and manipulate the
.. values with \setlength, \addlength, \settoheight, \settolength and \settodepth).

.. Similarly you have access to \newcounter for things like section and figure
.. numbers which should increment throughout the document. I've used this one in
.. the past to provide code samples that were numbered separatly of other
.. figures...

.. \setcounter{page}{1}

.. Simple usage example like \newlength{\hcolw} and \setlength{\hcolw}{0.47\textwidth} would be useful.

.. https://de.sharelatex.com/learn/Environments

.. Defining environments with parameters

.. Environments that accept parameters can also be defined. Let's enhance the previous example to put a title for the box:

.. \newenvironment{boxed}[1]
..     {\begin{center}
..     #1\\[1ex]
..     \begin{tabular}{|p{0.9\textwidth}|}
..     \hline\\
..     }
..     { 
..     \\\\\hline
..     \end{tabular} 
..     \end{center}
..     }
.. %--------------------------------------------------
 
.. Below this line a boxed environment is used
 
.. \begin{boxed}{Title of the Box}
.. This is the text formatted by the boxed environment
.. \end{boxed}
 
.. This text is again outside the environment

.. As you see, the command definition is almost the same as in the example of the
.. previous section, except for [1] that sets the number of parameters to be used
.. in the environment; and #1\\[1ex] that inserts the parameter at the top of the
.. box and also separates the title from the box by a 1ex blank space.

.. See the reference guide for a more complex example. 

.. %In the preamble
.. ---------------------------------
.. %Numbered environment
.. \newcounter{example}[section]
.. \newenvironment{example}[1][]{\refstepcounter{example}\par\medskip
..    \noindent \textbf{Example~\theexample. #1} \rmfamily}{\medskip}
 
 
.. %Numbered environment defined with Newtheorem
.. \usepackage{amsmath}
.. \newtheorem{SampleEnv}{Sample Environment}[section]
.. --------------------------------------------------------------------
 
 
.. \begin{example}
.. User-defined numbered environment
.. \end{example}
 
.. \begin{SampleEnv}
.. User-defined environment created with the \texttt{newtheorem} command.
.. \end{SampleEnv}

.. In the manually-defined environment the command \newcounter{example}[section]
.. creates a counter called example that will be reset every time a new section is
.. started. The counter is printed with \refstepcounter{example} within the
.. environment definition, and its value is incremented by one. See the article
.. about counters to learn more. 

.. https://de.sharelatex.com/learn/Counters

.. The command \newenvironment from the package amsmath also creates a numbered
.. environment, this command takes three parameters: the name of the new
.. environment, the text to be printed in blackbold font at the beginning of the
.. line and an optional parameter that determines how the counter is printed and
.. when it's reset. In the example the values are SampleEnv, Sample Environment and
.. section respectively. 

.. https://en.wikibooks.org/wiki/LaTeX/Counters


