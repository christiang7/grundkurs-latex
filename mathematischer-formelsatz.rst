.. index:: Mathematische Formel, Formel
.. _Gleichungen:
.. _Mathematischer Formelsatz:

Mathematischer Formelsatz
=========================

LaTeX unterstützt wie kaum ein anderes Textsatzungsprogramm das Einfügen
mathematischer Formeln. Wahlweise können Formeln innerhalb einer Absatzes
("Inline") oder als eigenständiger Absatz in ein Dokument eingefügt werden:
[#]_

* Mit ``$ Formel $`` wird eine Formel innerhalb eines Textabsatzes eingefügt.
* Mit ``$$ Formel $$`` wird eine Formel als eigenständiger Absatz zentriert
  eingefügt.

Sollen auch Zeilenumbrüche innerhalb einer Formel erlaubt sein, so sollte die
Umgebung ``align`` (beziehungsweise ``align*`` für nummerierte beziehungsweise
nicht nummerierte Formeln) gewählt werden:

.. code-block:: tex

    % Standard-Mathe-Umgebung:
    \begin{align}
        E \underset{Einstein}{=} m \cdot c^2
        \underset{Pythagoras}{=} m \cdot (a^2 + b^2)
    \end{align}

*Ergebnis:*

.. math::
    :label: eqn-einstein-pythagoras

    E \underset{Einstein}{=} m \cdot c^2 \underset{Pythagoras}{=} m \cdot (a^2 + b^2)


Der Gleichungs-Zähler kann bei Bedarf mittels ``\setcounter{equation}{1}``
wieder auf den Wert ``1`` (oder einen beliebigen anderen Wert) gesetzt werden.
Mit ``\numberwithin{equation}{section}`` kann zudem festgelegt werden, welcher
Gliederungstiefe die Formeln zugerechnet werden sollen, ob also eine
Nummerierung in der Art :math:`(1), (2), \ldots` oder abschnittsweise
als :math:`(1.1), (1.2), \ldots` erfolgen soll.

.. _Formeln mit mehreren Nummerierungen:

.. rubric:: Formeln mit mehreren Nummerierungen

Die Umgebungen ``align`` und ``align*`` sind für fast alle abgesetzten
Formeln die beste Wahl. Eine Ausnahme bilden mehrere einzeilige Formeln, die
zueinander ausgerichtet, aber einzeln nummeriert werden sollen. Für diesen
Zweck gibt es die Umgebung ``eqnarray``:

.. code-block:: tex

    % Umgebung für mehrere nummerierte Zeilen:
    \begin{eqnarray}
        x^2 &=& 2 \\
        \to x &=& \pm \sqrt{2}
    \end{eqnarray}

*Ergebnis:*

.. only:: html

    .. math::
        :label: eqn-1

        x^2 =& \, 2 {\color{white};;;}\\

    .. math::
        :label: eqn-2

        \to x =& \pm \sqrt{2}

.. raw:: latex

    \begin{eqnarray}
        x^2 &=& 2 \\
        \to x &=& \pm \sqrt{2}
    \end{eqnarray}

Sollen bei verwendung einer ``eqnarray``-Umgebung einzelne Zeilen *nicht*
nummeriert werden, so kann man am Ende der jeweiligen Zeile die Anweisung
``\notag`` einfügen, um eine Nummerierung zu verhindern.

Sollen die einzelnen Zeilen eines Formel-Absatzes zwar eigenständig nummeriert
werden und eigene Labels erhalten, aber letztlich nur als Teile einer ganzen
Formel angesehen werden, so ist dies mittels der ``subequations``-Umgebung
möglich:

*Beispiel:*


.. code-block:: tex

    \begin{subequations}
    \label{maxwell-gleichungen}
        \begin{align}
            \text{div }(\vec{D}) &= 4 \cdot \pi \cdot \rho
            \label{coulomb-gesetz}\\
            \text{rot }(\vec{H}) &= \frac{4 \cdot \pi}{c} \cdot \vec{j}
            \label{ampere-gesetz}\\
            \text{rot }(\vec{E}) &= - \frac{1}{c} \cdot \frac{\partial \vec{B}}{\partial t}
            \label{faraday-gesetz-1} \\
            \text{div }(\vec{B}) &= 0
            \label{faraday-gesetz-2}
        \end{align}
    \end{subequations}


*Ergebnis:*

.. raw:: latex

    \begin{subequations}
    \label{maxwell-gleichungen}
        \begin{align}
            \text{div }(\vec{D}) &= 4 \cdot \pi \cdot \rho
            \label{coulomb-gesetz}\\
            \text{rot }(\vec{H}) &= \frac{4 \cdot \pi}{c} \cdot \vec{j}
            \label{ampere-gesetz}\\
            \text{rot }(\vec{E}) &= - \frac{1}{c} \cdot \frac{\partial \vec{B}}{\partial t}
            \label{faraday-gesetz-1} \\
            \text{div }(\vec{B}) &= 0
            \label{faraday-gesetz-2}
        \end{align}
    \end{subequations}

.. only:: html

    .. image:: pics/subequations.png
        :align: center
        :width: 100%

Auf einzelne Gleichungen kann dann via ``\eqref{}`` wahlweise auf ein Label der
Teilgleichung oder auch auf das Label der gesamten Gleichung verwiesen werden.


.. _Besonderheiten im Mathematik-Modus:

.. rubric:: Besonderheiten im Mathematik-Modus

Der Mathematik-Modus weist gegenüber normalem Text einige Besonderheiten auf:

* Mathematische Formeln dürfen keine leeren Zeilen beinhalten: Jede Formel
  entspricht einem einzigen Absatz.
* Leerzeichen innerhalb von Formeln werden ignoriert und müssen bei Bedarf
  manuell mittels Abstands-Anweisungen wie ``\,`` oder ``\;`` gesetzt werden.
  Vor und nach mathematischen Operatoren wie ``+`` oder ``-`` wird von LaTeX
  automatisch etwas Freiraum eingefügt.
* Buchstaben werden in Formeln grundsätzlich als Namen von Variablen
  interpretiert und daher kursiv gedruckt. Sollen einzelne Buchstaben aufrecht
  gedruckt werden, so ist dies mittels ``\mathrm{}`` möglich; normale
  Textabschnitte (inklusive Leerzeichen) können innerhalb von Formeln mittels
  ``\text{Text}`` eingebettet werden.

.. index:: Mathematische Symbole
.. _Mathematische Symbole:

Mathematische Symbole
---------------------

.. index:: Griechisches Alphabet
.. _Griechisches Alphabet:

.. rubric:: Griechisches Alphabet

In Formeln werden sehr häufig griechische Buchstaben als Variablenbezeichnungen
verwendet. In der folgenden Liste sind die griechischen Buchstaben sowie die
zugehörigen LaTeX-Anweisungen für den Mathe-Modus aufgelistet.

.. list-table:: Griechisches Alphabet
    :widths: 25 25 50 25 25 50
    :header-rows: 0
    :name: tab-griechisches-alphabet

    * - Aussprache
      - Buchstabe
      - LaTeX-Code
      - Aussprache
      - Buchstabe
      - LaTeX-Code
    * - Alpha
      - :math:`A \quad \alpha`
      - ``A          \alpha``
      - Ny
      - :math:`N \quad \nu`
      - ``N          \nu``
    * - Beta
      - :math:`B \quad \beta`
      - ``B          \beta``
      - Xi
      - :math:`\Xi \quad \xi`
      - ``\Xi        \xi``
    * - Gamma
      - :math:`\Gamma \quad \gamma`
      - ``\Gamma     \gamma``
      - Omikron
      - :math:`O \quad o`
      - ``O          o``
    * - Delta
      - :math:`\Delta \quad \delta`
      - ``\Delta     \delta``
      - Pi
      - :math:`\Pi \quad \pi`
      - ``\Pi        \pi``
    * - Epsilon
      - :math:`E \quad \varepsilon`
      - ``E          \varepsilon``
      - Rho
      - :math:`P \quad \rho`
      - ``P          \rho``
    * - Zeta
      - :math:`Z \quad \zeta`
      - ``Z          \zeta``
      - Sigma
      - :math:`\Sigma \quad  \sigma`
      - ``\Sigma     \sigma``
    * - Eta
      - :math:`H \quad \eta`
      - ``H          \eta``
      - Tau
      - :math:`T \quad \tau`
      - ``T          \tau``
    * - Theta
      - :math:`\varTheta \quad \vartheta`
      - ``\varTheta  \vartheta``
      - Ypsilon
      - :math:`\Upsilon \quad \upsilon`
      - ``\Upsilon   \upsilon``
    * - Iota
      - :math:`I \quad \iota`
      - ``I          \iota``
      - Phi
      - :math:`\varPhi \quad  \varphi`
      - ``\varPhi    \varphi``
    * - Kappa
      - :math:`K \quad \kappa`
      - ``K          \kappa``
      - Chi
      - :math:`X \quad \chi`
      - ``X          \chi``
    * - Lambda
      - :math:`\Lambda \quad  \lambda`
      - ``\Lambda    \lambda``
      - Psi
      - :math:`\Psi \quad \psi`
      - ``\Psi       \psi``
    * - My
      - :math:`M \quad \mu`
      - ``M          \mu``
      - Omega
      - :math:`\Omega \quad \omega`
      - ``\Omega     \omega``

Bei manchen griechischen Buchstaben existiert neben den oben angegebenen
Varianten auch noch alternative Darstellungen. Beispielsweise wird ``\theta``
als :math:`\theta` ausgegeben, während ``\vartheta`` als :math:`\vartheta`
gedruckt wird.


.. index:: Mathematische Schriftarten
.. _Mathematische Schriftarten:

.. rubric:: Mathematische Schriftarten

Ebenso wie Texte in normalen Textabsätzen mittels ``\textbf{}``, ``\textit{}``
usw. hervorgehoben werden können, existieren im Mathe-Modus verschiedene
Möglichkeiten, die Form oder den Typ einer Schrift zu verändern:

.. index:: \mathnormal{}

* Ohne explizite Angabe wird ``\mathnormal{}``  als Schrifttyp verwendet.
  Hierbei werden Buchstaben kursiv dargestellt, Zahlen hingegen aufrecht:

  .. math::

      ABCDEF \quad abcdef \quad 123456

.. index:: \mathrm{}
.. _\mathrm{}:

* Mit ``\mathrm{}`` ("Math Roman") werden sowohl Buchstaben als auch Zahlen im
  Mathe-Modus aufrecht gedruckt. Dieser Schrifttyp wird beispielsweise
  geometrische Punkte, für Einheiten oder Symbole in Indizes verwendet.

  .. math::

      \mathrm{ABCDEF} \quad \mathrm{abcdef} \quad \mathrm{123456}

.. index:: \mathit{}
.. _\mathit{}:

* Mit ``\mathit{}`` ("Math Italic") werden sowohl Buchstaben als auch Zahlen im
  Mathe-Modus kursiv gedruckt:

  .. math::

      \mathit{ABCDEF} \quad \mathit{abcdef} \quad \mathit{123456}

.. index:: \mathbf{}
.. _\mathbf{}:

* Mit ``\mathbf{}`` ("Math Bold Font") werden Buchstaben und Zahlen im
  Mathe-Modus aufrecht und fettgedruckt ausgegeben. In manchen Lehrbüchern
  werden auf diese Weise Vektoren gekennzeichnet.

  .. math::

      \mathbf{ABCDEF} \quad \mathbf{abcdef} \quad \mathbf{123456}

.. index:: \mathsf{}
.. _\mathsf{}:

* Mit ``\mathsf{}`` ("Math Sans Serif") werden Buchstaben und Zahlen im
  Mathe-Modus aufrecht und ohne Serifen ausgegeben:

  .. math::

      \mathsf{ABCDEF} \quad \mathsf{abcdef} \quad \mathsf{123456}

.. index:: \mathtt{}
.. _\mathtt{}:

* Mit ``\mathtt{}`` ("Math Typesetter") werden Buchstaben und Zahlen im
  Mathe-Modus aufrecht und nicht-proportional ausgegeben:

  .. math::

      \mathtt{ABCDEF} \quad \mathtt{abcdef} \quad \mathtt{123456}

.. index:: \mathfrak{}
.. _\mathfrac{}:

* Mit ``\mathfrak{}`` ("Math Fraktur") werden Buchstaben und Zahlen im
  Mathe-Modus als Frakturschrift ausgegeben:

  .. math::

      \mathfrak{ABCDEF} \quad \mathfrak{abcdef} \quad \mathfrak{123456}

.. index:: Mengensymbol, \mathbb{}
.. _\mathbb{}:

* Mit ``\mathbb{}`` ("Math Blackboard Bold") werden Großbuchstaben im
  Mathe-Modus als Mengensymbole ausgegeben. Hierzu muss in der Präambel das
  Paket ``amsfonts`` mittels ``\usepackage{amsfonts}`` geladen werden.

  .. math::

      \mathbb{ABCDEF}

.. index:: \mathcal{}
.. _\mathcal{}:

* Mit ``\mathcal}`` ("Math Calligraphy") werden Großbuchstaben im Mathe-Modus
  kalligraphisch ausgegeben:

  .. math::

      \mathcal{ABCDEF}

.. index:: \mathscr{}
.. _\mathscr{}:

* Mit ``\mathscr{}`` ("Math Script") werden Großbuchstaben im Mathe-Modus in
  einer weiteren Darstellungsvariante ausgegeben.  Hierzu muss in der Präambel
  das Paket ``mathrsfs`` mittels ``\usepackage{mathrsfs}`` geladen werden.


  .. math::

      \mathscr{ABCDEF}

.. index:: Relationszeichen
.. _Relationszeichen:

.. rubric:: Relationszeichen

Die Relationszeichen :math:`=`, :math:`<` und :math:`>` können direkt mittels
der Tastatur eingegeben werden. Weitere Relationszeichen sind in der folgenden
Tabelle aufgelistet.

.. .. list-table:: Relationszeichen

.. list-table::
    :name: tab-relationszeichen
    :widths: 50 50 50 50
    :header-rows: 0

    * - Eingabe
      - Ausgabe
      - Eingabe
      - Ausgabe
    * - ``=``
      - :math:`{\color{white}|}={\color{white}|}`
      - ``\neq``
      - :math:`{\color{white}|}\neq{\color{white}|}`
    * - ``\stackrel{\wedge}=``
      - :math:`{\color{white}|}\stackrel{\wedge}={\color{white}|}`
      - ``\stackrel{!}=``
      - :math:`{\color{white}|}\stackrel{!}={\color{white}|}`
    * - ``\equiv``
      - :math:`{\color{white}|}\equiv{\color{white}|}`
      - ``\cong``
      - :math:`{\color{white}|}\cong{\color{white}|}`
    * - ``\geq``
      - :math:`{\color{white}|}\geq{\color{white}|}`
      - ``\leq``
      - :math:`{\color{white}|}\leq{\color{white}|}`
    * - ``\gg``
      - :math:`{\color{white}|}\gg{\color{white}|}`
      - ``\ll``
      - :math:`{\color{white}|}\ll{\color{white}|}`
    * - ``\approx``
      - :math:`{\color{white}|}\approx{\color{white}|}`
      - ``\sim``
      - :math:`{\color{white}|}\sim{\color{white}|}`
    * - ``\propto``
      - :math:`{\color{white}|}\propto{\color{white}|}`
      - ``\simeq``
      - :math:`{\color{white}|}\simeq{\color{white}|}`
    * - ``\in``
      - :math:`{\color{white}|}\in{\color{white}|}`
      - ``\not\in``
      - :math:`{\color{white}|}\not\in{\color{white}|}`
    * - ``\subset``
      - :math:`{\color{white}|}\subset{\color{white}|}`
      - ``\supset``
      - :math:`{\color{white}|}\supset{\color{white}|}`
    * - ``\subseteq``
      - :math:`{\color{white}|}\subseteq{\color{white}|}`
      - ``\supseteq``
      - :math:`{\color{white}|}\supseteq{\color{white}|}`
    * - ``\cup``
      - :math:`{\color{white}|}\cup{\color{white}|}`
      - ``\cap``
      - :math:`{\color{white}|}\cap{\color{white}|}`
    * - ``\perp``
      - :math:`{\color{white}|}\perp{\color{white}|}`
      - ``\parallel``
      - :math:`{\color{white}|}\parallel{\color{white}|}`

Allgemein können die obigen Relationssymbole, wie am Beispiel :math:`\not\in`
(``\not \in``) gezeigt, durch ein Voranstellen von ``\not`` invertiert werden;
beispielsweise ergibt eine Eingabe von ``\not\ge`` das Zeichen :math:`{\color{white}|}\not\ge{\color{white}|}`.

.. .. index:: Pfeilsymbole
.. .. _Pfeilsymbole:

.. .. rubric:: Pfeilsymbole

.. .. list-table::
..     :name: tab-pfeilsymbole
..     :widths: 55 50 50 50
..     :header-rows: 0

..     * - Eingabe
..       - Ausgabe
..       - Eingabe
..       - Ausgabe
..     * - ``\rightarrow`` oder ``\to``
..       - :math:`{\color{white}|}\rightarrow{\color{white}|}`
..       - ``\Rightarrow``
..       - :math:`{\color{white}|}\Rightarrow{\color{white}|}`
..     * - ``\leftarrow``
..       - :math:`{\color{white}|}\leftarrow{\color{white}|}`
..       - ``\Leftarrow``
..       - :math:`{\color{white}|}\Leftarrow{\color{white}|}`
..     * - ``\longrightarrow``
..       - :math:`{\color{white}|}\longrightarrow{\color{white}|}`
..       - ``\Longrightarrow``
..       - :math:`{\color{white}|}\Longrightarrow{\color{white}|}`
..     * - ``\longleftarrow``
..       - :math:`{\color{white}|}\longleftarrow{\color{white}|}`
..       - ``\Longleftarrow``
..       - :math:`{\color{white}|}\Longleftarrow`
..     * - ``\leftrightarrow``
..       - :math:`{\color{white}|}\leftrightarrow{\color{white}|}`
..       - ``\Leftreftarrow``
..       - :math:`{\color{white}|}\Leftrightarrow{\color{white}|}`
..     * - ``\longleftrightarrow``
..       - :math:`{\color{white}|}\longleftrightarrow{\color{white}|}`
..       - ``\Longleftreftarrow``
..       - :math:`{\color{white}|}\Longleftrightarrow{\color{white}|}`
..     * - ``\uparrow``
..       - :math:`{\color{white}|}\uparrow{\color{white}|}`
..       - ``\Uparrow``
..       - :math:`{\color{white}|}\Uparrow{\color{white}|}`
..     * - ``\downarrow``
..       - :math:`{\color{white}|}\downarrow{\color{white}|}`
..       - ``\Downarrow``
..       - :math:`{\color{white}|}\Downarrow{\color{white}|}`
..     * - ``\updownarrow``
..       - :math:`{\color{white}|}\updownarrow{\color{white}|}`
..       - ``\Updownarrow``
..       - :math:`{\color{white}|}\Updownarrow{\color{white}|}`
..     * - ``\hookrightarrow``
..       - :math:`{\color{white}|}\hookrightarrow{\color{white}|}`
..       - ``\hookleftarrow``
..       - :math:`{\color{white}|}\hookleftarrow{\color{white}|}`
..     * - ``\nwarrow``
..       - :math:`{\color{white}|}\nwarrow{\color{white}|}`
..       - ``\nearrow``
..       - :math:`{\color{white}|}\nearrow{\color{white}|}`
..     * - ``\swarrow``
..       - :math:`{\color{white}|}\swarrow{\color{white}|}`
..       - ``\searrow``
..       - :math:`{\color{white}|}\searrow{\color{white}|}`


.. rubric:: Weitere mathematische Symbole

.. list-table::
    :name: tab-mathematische-symbole
    :widths: 50 50 50 50
    :header-rows: 0

    * - Eingabe
      - Ausgabe
      - Eingabe
      - Ausgabe
    * - ``\pm``
      - :math:`{\color{white}|}\pm{\color{white}|}`
      - ``\mp``
      - :math:`{\color{white}|}\mp{\color{white}|}`
    * - ``\div{}``
      - :math:`{\color{white}|}\div{}{\color{white}|}`
      - ``\setminus``
      - :math:`{\color{white}|}\setminus{\color{white}|}`
    * - ``\cdot``
      - :math:`{\color{white}||\!}\cdot{\color{white}|}`
      - ``\times``
      - :math:`{\color{white}|}\times{\color{white}|}`
    * - ``\ast``
      - :math:`{\color{white}|}\ast{\color{white}|}`
      - ``\star``
      - :math:`{\color{white}|}\star{\color{white}|}`
    * - ``\circ``
      - :math:`{\color{white}|}\circ{\color{white}|}`
      - ``\bullet``
      - :math:`{\color{white}|}\bullet{\color{white}|}`
    * - ``\varangle``
      - :math:`{\color{white}||\!}\varangle{\color{white}|}`
      - ``\angle``
      - :math:`{\color{white}|}\angle{\color{white}|}`
    * - ``\vee``
      - :math:`{\color{white}|}\vee{\color{white}|}`
      - ``\wedge``
      - :math:`{\color{white}|}\wedge{\color{white}|}`
    * - ``\forall``
      - :math:`{\color{white}||}\forall{\color{white}|}`
      - ``\exists``
      - :math:`{\color{white}||}\exists{\color{white}|}`
    * - ``\infty``
      - :math:`{\color{white}|}\infty{\color{white}|}`
      - ``\emptyset``
      - :math:`{\color{white}||}\emptyset{\color{white}|}`
    * - ``\partial``
      - :math:`{\color{white}||}\partial{\color{white}|}`
      - ``\nabla``
      - :math:`{\color{white}|}\nabla{\color{white}|}`
    * - ``\oplus``
      - :math:`{\color{white}|}\oplus{\color{white}|}`
      - ``\ominus``
      - :math:`{\color{white}|}\ominus{\color{white}|}`
    * - ``\odot``
      - :math:`{\color{white}|}\odot{\color{white}|}`
      - ``\oslash``
      - :math:`{\color{white}|}\oslash{\color{white}|}`
    * - ``\Box``
      - :math:`{\color{white}||}\Box{\color{white}|}`
      - ``\checkmark``
      - :math:`{\color{white}||}\checkmark{\color{white}|}`
    * - ``\clubsuit``
      - :math:`{\color{white}||}\clubsuit{\color{white}|}`
      - ``\spadesuit``
      - :math:`{\color{white}||}\spadesuit{\color{white}|}`
    * - ``\heartsuit``
      - :math:`{\color{white}||}\heartsuit{\color{white}|}`
      - ``\diamondsuit``
      - :math:`{\color{white}||}\diamondsuit{\color{white}|}`

.. http://latex.wikia.com/wiki/List_of_LaTeX_symbols
.. https://de.wikipedia.org/wiki/Liste_mathematischer_Symbole

.. index:: Mathematische Ausdrücke
.. _Mathematische Ausdrücke:

Mathematische Ausdrücke
-----------------------

.. index:: Index, Exponent
.. _Indizes und Exponenten:

.. rubric:: Indizes und Exponenten

Soll im Mathe-Modus eine einzelne Ziffer oder ein einzelner Buchstabe als Index
einer Variablen gesetzt werden, so ist dies mittels ``x_1, x_2, ..., x_n``
möglich; die Ausgabe würde in diesem Fall :math:`x_1,\, x_2,\, \ldots,\, x_n`
lauten. Soll der Index aus mehr als einem Zeichen bestehen, so müssen diese in
geschweifte Klammern gesetzt werden, also beispielsweise ``x_{1,2}`` für
:math:`x _{1,2}`. Lässt man die geschweiften Klammern weg, so springt LaTeX nach
dem ersten Index-Zeichen wieder in den normalen Mathe-Modus zurück und druckt
die restlichen Zeichen als normal große Variablennamen.

Um im Mathe-Modus eine einzelne Ziffer oder einen einzelnen Buchstaben als
Exponent einer Variablen zu setzen, so ist dies mittels ``x^1, x^2, ...,
x^n`` möglich; die Ausgabe würde in diesem Fall :math:`x^1,\, x^2,\, \ldots,
x^n` lauten. Auch bei Exponenten müssen geschweifte Klammern gesetzt werden,
sofern diese aus mehr als einem Zeichen bestehen.

In Exponenten werden Buchstaben in LaTeX standardmäßig aufrecht gedruckt, in
Indizes hingegen kursiv. Möchte man, wie es in der Textsatzung üblich ist,
aufrechte Indizes erhalten, so müssen diese in geschweifte Klammern gesetzt und
mittels ``\mathrm{}`` explizit in aufrechter Form ausgegeben werden (Zahlen
werden auch in LaTeX stets aufrecht gedruckt).


.. _Einheiten:

.. rubric:: Einheiten

In Mathe-Umgebungen können Einheiten -- ebenso wie in normalen Text-Bereichen --
am einfachsten mittels des :ref:`units <units>`-Pakets gesetzt werden. Die
Syntax dafür ist denkbar einfach:

*Beispiel:*

.. code-block:: tex

    % Größe mit Einheit setzen:
    \unit[1]{Liter} = \unit[1]{dm^3}

*Ergebnis:*

.. math::

    % Größe mit Einheit setzen:
    \unit[1]{Liter} = \unit[1]{dm^3}

Die ``units``-Anweisung hat einerseits den Effekt, dass die in den geschweiften
Klammern angegebene Einheit nicht wie im Mathe-Modus üblich kursiv, sondern
aufrecht gedruckt wird; andererseits wird der Abstand zwischen dem Zahlenwert
und der Einheit etwas reduziert. Die ``units{}``-Anweisung kann auch ohne Angabe
eines Zahlenwerts genutzt werden, beispielsweise um reine Einheits-Gleichungen
zu setzen. Innerhalb der geschweiften Klammern sind auch weitere
LaTeX-Anweisungen, wie beispielsweise :ref:`Brüche <Brüche>` oder :ref:`Wurzeln
<Wurzeln>`, erlaubt.

.. .. rubric:: Standard-Funktionen

.. \arccos
.. \arcsin
.. \arctan
.. \arg
.. \cos
.. \cosh
.. \cot
.. \coth
.. \csc
.. \deg
.. \det
.. \dim
.. \exp
.. \gcd
.. \hom
.. \inf
.. \ker
.. \lg
.. \lim
.. \liminf
.. \limsup
.. \ln
.. \log
.. \max
.. \min
.. \Pr
.. \sec
.. \sin
.. \sinh
.. \sup
.. \tan
.. \tanh


.. index:: Klammern
.. _Klammern:

.. rubric:: Klammern

Runde und eckige Klammern können in LaTeX-Formeln als gewöhnliche Zeichen
gesetzt werden, bei geschweiften Klammern muss ein Backslash-Zeichen vor die
öffnende und schließende Klammer gesetzt werden.

*Beispiel:*

.. code-block:: tex

    % Verschiedene Klammern in LaTeX:
    (a)     \qquad [b] \qquad \{c\} \qquad |d| \quad \langle e \rangle

*Ergebnis:*

.. math::

    (a)     \qquad [b] \qquad \{c\} \qquad |d| \quad \langle e \rangle

Möchte man die Größe einer Klammer anpassen, wenn beispielsweise ein Bruch
innerhalb der Klammer vorkommt, so kann die Klammergröße automatisch oder
manuell festgelegt werden:

* Mit ``\left`` und ``\right`` wird die Größe der darauf folgenden öffnenden
  beziehungsweise schließenden Klammer automatisch an den Inhalt der Klammer
  angepasst. Für runde Klammern mit autoamtische Größenanpassung kann man also
  ``\left(`` beziehungsweise ``\right)`` schreiben:

  *Beispiel:*

  .. code-block:: tex

      (a^{b^{c^d}}) \ne \left( d^{c^{b^a}} \right)

  *Ergebnis:*

  .. math::

      (a^{b^{c^d}}) \ne \left( d\;\!^{c^{b^a}} \right)

  Das gleiche funktioniert auch mit eckigen und geschweiften
  Klammern, wobei bei letzteren ``\left\{`` beziehungsweise ``\right\}``
  geschrieben werden müssen.

* Mit ``\big( ... \big)``, ``\Big( ... \Big)``, ``\bigg( ... \bigg)`` oder
  ``\Bigg( ... \Bigg)`` kann die Größe der öffnenden beziehungsweise
  schließenden runden Klammern manuell festgelegt werden. Das gleiche
  funktioniert ebenfalls mit vertikalen Strichen (beispielsweise
  Betragstrichen), die direkt mittels des Pipe-Zeichens ``|`` eingegeben werden
  können.

Bisweilen sind auch "liegende" geschweifte Klammern nützlich, um beispielsweise
eine Erklärung für einen auftretenden Term in die Gleichung mit aufzunehmen.
Bindet man in der Präambel das Paket ``mathtools`` mit ein, so kann man dafür
Anweisung die Anweisungen ``\underbrace{}`` beziehungsweise ``\overbrace{}``
nutzen:

*Beispiel:*

.. code-block:: tex

     \overbrace{n \cdot n \cdot n \cdot \ldots \cdot n}^{\text{$k$ mal} } = n^k \\
    \underbrace{n \cdot n \cdot n \cdot \ldots \cdot n}_{\text{$k$ mal} } = n^k

*Ergebnis:*

.. math::

     \overbrace{n \cdot n \cdot n \cdot \ldots \cdot n}^{\text{$k$ mal} } &= n^k \\[6pt]
    \underbrace{n \cdot n \cdot n \cdot \ldots \cdot n}_{\text{$k$ mal} } &= n^k



.. index:: Pfeile
.. _Pfeile:

.. rubric:: Pfeile

Pfeile können entweder über oder zwischen mathematischen Symbolen stehen.
Pfeile über mathematischen Symbolen markieren Vektoren oder gerichtete Strecken.
Im Fall von Vektoren, wenn sich der Pfeil über ein einzelnes Zeichen erstreckt,
kann man die Anweisung ``\vec{}`` verwenden, für Pfeile über mehreren
mathematischen Symbolen muss hingegen ``\overrightarrow{}`` (oder
``\overline{}`` für Strecken ohne Richtung) verwendet werden:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \vec{a}
        \overrightarrow{\mathrm{BC}}
        \overline{\mathrm{DE}}
    \end{align*}

*Ergebnis:*

.. math::

    \vec{a} \qquad \overrightarrow{\mathrm{BC}} \qquad \overline{\mathrm{DE}}

Für Pfeile zwischen mathematischen Symbolen gibt es mehrere Anweisungen. Ein
einfacher waagrechter Pfeil, wie er beispielsweise geschrieben wird, wenn eine
Zahl gegen einen bestimmten Grenzwert geht, kann einfach mit ``\to`` gesetzt werden.
Mehr Flexibilität bieten die Anweisungen der Art ``\leftarrow`` und ``\rightarrow``:

.. list-table::
    :name: tab-pfeile
    :widths: 60 40 50

    * - LaTeX-Code
      - Ergebnis
      - Beschreibung
    * - ``\leftarrow`` und ``\rightarrow``
      - :math:`\leftarrow \;\; \text{ und } \;\; \rightarrow`
      - waagrechter Pfeil
    * - ``\Leftarrow`` und ``\Rightarrow``
      - :math:`\Leftarrow \;\; \text{ und } \;\; \Rightarrow`
      - waagrechter Pfeil mit Doppelstrich
    * - ``\longleftarrow`` und ``\longrightarrow``
      - :math:`\longleftarrow \text{ und } \longrightarrow`
      - langer waagrechter Pfeil
    * - ``\Longleftarrow`` und ``\Longrightarrow``
      - :math:`\Longleftarrow \text{ und } \Longrightarrow`
      - langer waagrechter Pfeil mit Doppelstrich
    * - ``\leftrightarrow`` und ``\Leftrightarrow``
      - :math:`\leftrightarrow \;\; \text{ und } \;\; \Leftrightarrow`
      - beidseitiger Pfeil
    * - ``\longleftrightarrow`` und ``\Longleftrightarrow``
      - :math:`\Longleftrightarrow \! \text{ und } \! \Longleftrightarrow`
      - langer beidseitiger Pfeil

Mittels ``\uparrow`` und ``\downarrow`` lassen sich entsprechend nach oben
(:math:`\uparrow`) beziehungsweise nach unten (:math:`\downarrow`) zeigende
Pfeile setzen; auch diese können wie ``\leftarrow`` und ``\rightarrow`` gemäß
der obigen Tabelle modifiziert werden. Für diagonale Pfeile gibt es die
Anweisungen ``\nwarrow`` und ``\nearrow`` (:math:`\nwarrow` und
:math:`\nearrow`) beziehungsweise ``\swarrow`` und ``\searrow``
(:math:`\swarrow` und :math:`\searrow`), wobei die ersten beiden Buchstaben
jeweils die Himmelsrichtung angeben, in die der Pfeil zeigen soll.

Mittels ``\circlearrowleft`` und ``\circlearrowright`` lassen
sich die zur Kennzeichnung von Drehmomenten verwendeten kreisförmige Pfeile
(:math:`\circlearrowleft` und :math:`\circlearrowright`) setzen, mittels
``\curvearrowleft`` beziehungsweise ``\curvearrowright`` gebogene Pfeile
(:math:`\curvearrowleft` und :math:`\curvearrowright`).

Beschriftete waagrechte Pfeile können zudem mittels ``\xleftarrow{}``
beziehungsweise ``\xrightarrow{}`` erstellt werden. Die Länge eines solchen
Pfeils wird von LaTeX automatisch anhand der Länge des über beziehungsweise
unter dem Pfeil stehenden Textes bestimmt.

*Beispiel:*

.. code-block:: tex

    \mathrm{A} \quad \xleftarrow[\phantom{\text{was sonst?}}]{-1} \quad
    \mathrm{B} \quad \xrightarrow[\text{was sonst?}]{+1} \quad C

*Ergebnis:*

.. math::

    \mathrm{A} \quad \xleftarrow[\phantom{\text{was sonst?}}]{-1} \quad
    \mathrm{B} \quad \xrightarrow[\text{was sonst?}]{+1} \quad C

Eine vollständige Übersicht über die verschiedenen Pfeil gibt es beispielsweise
`hier <http://www.latex-pfeile.de/>`__.


.. index::
    single: Mathematische Ausdrücke; Wurzeln
    single: Mathematische Ausdrücke; Brüche
    single: Mathematische Ausdrücke; Binomialkoeffizienten

.. _Wurzeln, Brüche und Binomialkoeffizienten:
.. _Wurzeln:
.. _Brüche:
.. _Binomialkoeffizienten:
.. _Binomial-Koeffizienten:

.. rubric:: Wurzeln, Brüche und Binomialkoeffizienten

Wurzeln werden in LaTeX-Formeln mittels ``\sqrt{}`` gesetzt. Möchte man keine
Quadrat-Wurzel ausgeben, sondern eine Wurzel mit einem anderen Wurzelexponenten,
so kann für die :math:`n`-te Wurzel aus einer Zahl ``\sqrt[n]{Zahl}``
geschrieben werden.

*Beispiel:*

.. code-block:: tex

    % "Normale" Quadrat-Wurzel:
    \sqrt{16} = 4

    % Kubische Wurzel:
    \sqrt[3]{8} = 2

*Ergebnis:*

.. math::

    \sqrt{16} = 4 \\[8pt]
    \sqrt[3]{8} = 2


Innerhalb der ``\sqrt{}``-Anweisung können auch andere Mathe-Anweisungen wie
Pfeile oder Brüche gesetzt werden; Diese werden in LaTeX mittels
``\frac{Zähler}{Nenner}`` gesetzt:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}
    \end{align*}

*Ergebnis:*

.. math::

    \frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}

Innerhalb des Zähler und/oder Nenners können wiederum ``\frac{}``-Anweisungen
auftreten, so dass sich damit auch verschachtelte Brüche bilden lassen. Die
Größe der Schriften sowie die Dicke der Bruchstriche werden dabei automatisch
angepasst:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}
    \end{align*}

*Ergebnis:*

.. math::

    \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}

Die automatische Anpassung der Schriftgröße bei der ``\frac{}``-Anweisung kann
umgangen werden, wenn man mit ansonsten gleicher Syntax die ``\tfrac{}`` oder
``\dfrac{}``-Anweisung verwendet:

* Bei der ``\tfrac{}``-Anweisung wird automatisch die Option ``\textstyle``
  aktiviert; der Bruch wird dadurch möglichst so dimensioniert, dass er in eine
  normale Textzeile passt.

* Bei der ``\dfrac{}``-Anweisung wird automatisch die Option ``\displaystyle``
  aktiviert; eine automatische Verkleinerung der Schriftgröße findet dabei auch
  bei verschachtelten Brüchen nicht statt.

In ähnlicher Weise wie Brüche lassen sich auch :ref:`Binomial-Koeffizienten
<gwm:Kombinationen ohne Wiederholung>` setzen. Auch wenn diese aus
mathematischer Sicht eine andere Bedeutung haben, sind sie aus Sicht der
Textsatzung den Brüchen ähnlich, nur dass der Bruchstrich zwischen der oberen
und der unteren Zahl fehlt.

*Beispiel:*

.. code-block:: tex

    % Binomialkoeffizient:
    \begin{align*}
        \binom{n}{k} = \frac{n!}{(n - k)! \cdot k!}
    \end{align*}

*Ergebnis:*

.. math::

    \binom{n}{k} = \frac{n!}{(n - k)! \cdot k!}



.. index:: Summenzeichen, \sum
.. _Summen, Produkte und Integrale:
.. _Summenzeichen:
.. _Integrale:

.. rubric:: Summen, Produkte und Integrale

Das Summenzeichen :math:`\sum` kann im Mathe-Modus mittels ``\sum`` gedruckt
werden. Üblicherweise wird dabei unterhalb des Summenzeichens die Untergrenze
und oberhalb die Obergrenze der zu summierenden Größe angegeben. In LaTeX wird
dazu die für Indizes und Exponenten übliche Syntax genutzt und somit
``\sum_{}^{}`` geschrieben:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \sum_{i=1}^{n} i =  \frac{n \cdot (n+1)}{2}
    \end{align*}

*Ergebnis:*

.. math::

    \sum_{i=1}^{n} i =  \frac{n \cdot (n+1)}{2}

In gleicher Weise kann das (seltener vorkommende) Produkt-Zeichen :math:`\prod`
genutzt werden:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \sum_{i=1}^{n} i =  \frac{n \cdot (n+1)}{2}
    \end{align*}

*Ergebnis:*

.. math::

    \prod_{i=1}^{n} i = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1 = n!

.. index:: Integralzeichen, \int

Das Integralzeichen :math:`\int` kann im Mathe-Modus mittels ``\int`` gedruckt
werden. Üblicherweise wird auch hierbei unterhalb des Integralzeichens die
Untergrenze und oberhalb die Obergrenze der zu integrierenden Größe angegeben.
In LaTeX wird dazu wiederum die für Indizes und Exponenten übliche Syntax genutzt und
somit ``\int_{}^{}`` geschrieben. Ohne weitere Voreinstellungen werden die
Integralgrenzen etwas versetzt gedruckt; möchte man dies unterbinden, so kann
man dies durch ein Einfügen von ``\limits`` vor den Integralgrenzen erreichen:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \int_{a}^{b}        f(x) \cdot \mathrm{d} x = F(b) - F(a) \\
        \int\limits_{a}^{b} f(x) \cdot \mathrm{d} x = F(b) - F(a)
    \end{align*}

*Ergebnis:*

.. math::

    \int_{a}^{b} f(x) \cdot \mathrm{d} x &= F(b) - F(a)  \\[4pt]
    \int\limits_{a}^{b} f(x) \cdot \mathrm{d} x &= F(b) - F(a)

Mehrfachintegrale (Flächen- und Volumenintegrale) können entsprechend mittels
``\iint``, ``\iiint`` gesetzt werden, geschlossene Linien-Integrale mittels
``\oint``.

*Beispiel:*

.. code-block:: tex

    % Gaußscher Integralsatz:
    \iiint_{V}^{} \text{div } \vec{E} (\vec{r}) \cdot \mathrm{d}^3 r  =
    \oint\limits_{S(V)}^{} \vec{E} \cdot \mathrm{d} \vec{f}


*Ergebnis:*

.. math::

    \iiint_{V}^{} \text{div } \vec{E} (\vec{r}\,) \cdot \mathrm{d}^3 r  =
    \oint\limits_{S(V)}^{} \vec{E} \cdot \mathrm{d} \vec{f}

.. Limits direkt unter/über Summen- beziehungsweise Integralzeichen:
.. \newcommand{\I}{\int\limits}
.. \newcommand{\Sum}{\sum\limits}
.. \newcommand{\Prod}{\prod\limits}

.. todo  Mehrfachintegrale Kurvenintegrale

.. index:: 
    single: Mathematische Ausdrücke; Determinanten
    single: Mathematische Ausdrücke; Matrizen
    single: Mathematische Ausdrücke; Vektoren

.. _Matrizen und Determinanten:

.. rubric:: Matrizen und Determinanten

Zum Setzen von :ref:`Matrizen <gwm:Matrizen>`  beziehungsweise Determinanten
stellt das Paket ``amsmath`` für den Mathe-Modus mehrere Umgebungen bereit:

+-------------+-------------------------------------+
| ``matrix``  | Matrizen ohne Klammern              |
+-------------+-------------------------------------+
| ``pmatrix`` | Matrizen mit runden Klammern        |
+-------------+-------------------------------------+
| ``bmatrix`` | Matrizen mit eckigen Klammern       |
+-------------+-------------------------------------+
| ``vmatrix`` | Matrizen mit eckigen Betragstrichen |
+-------------+-------------------------------------+

Innerhalb einer Matrix-Umgebung werden die einzelnen Spalten, ähnlich wie bei
:ref:`Tabellen <Tabellen>`, durch ``&``-Zeichen getrennt; Zeilenumbrüche lassen
sich wie gewöhnlich mittels ``\\`` erreichen.

*Beispiel:*

.. code-block:: tex

    \begin{pmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{pmatrix}

*Ergebnis:*

.. math::

    \begin{pmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{pmatrix}

Die ``vmatrix``-Umgebung kann insbesondere zur Erzeugung von :ref:`Determinanten
<gwm:Determinanten>` genutzt werden; mittels der ``pmatrix``-Umgebung hingegen
können auch :ref:`Vektoren <gwm:Vektoren>` als einspaltige Matrizen gesetzt
werden.


.. index:: 
    single: Mathematische Ausdrücke; Fallunterscheidungen
.. _Fallunterscheidungen:

.. rubric:: Fallunterscheidungen

Fallunterscheidungen können im Mathe-Modus mittels der ``cases``-Umgebung
verwirklicht werden. Innerhalb einer solchen Umgebung können die einzelnen
Elemente mittels eines ``&``-Zeichens ausgerichtet werden; die vertikale
Ausrichtung übernimmt LaTeX (bis auf manuell zu setzende Zeilenumbrüche)
automatisch.

*Beispiel:*

.. code-block:: tex

    | a | = \begin{cases}
        +a     & \text{ falls } a > 0 \\
        \;\;0  & \text{ falls } a = 0 \\
        -a     & \text{ falls } a < 0
    \end{cases}


*Ergebnis:*

.. math::

    | a | = \begin{cases}
    +a  & \text{ falls } a > 0 \\
    \;\;0  & \text{ falls } a = 0 \\
    -a & \text{ falls } a < 0
    \end{cases}



.. Zeichen über istgleich setzen:
.. \stackrel{\wedge}=

.. index:: array (Umgebung)
.. _array:

.. rubric:: Die ``array``-Umgebung

Die ``array``-Umgebung kann innerhalb von Formeln verwendet werden, um eine
horizontale Ausrichtung der einzelnen Formel-Elemente zu erreichen. Die Syntax
ist dabei der :ref:`tabular <tabular>`-Umgebung sehr ähnlich:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \begin{array}{lcr}
            \text{Erste Zahl}   & x         &  8 \\
            \text{Zweite Zahl}  & y         & 15 \\ \hline
            \text{Summe}        & x + y     & 23 \\
            \text{Differenz}    & x - y     & -7 \\
            \text{Produkt}      & x \cdot y & 120
        \end{array}
    \end{align*}

*Ergebnis:*

.. math::

    \begin{align*}
        \begin{array}{lcr}
            \text{Erste Zahl}   & x         &  8 \\
            \text{Zweite Zahl}  & y         & 15 \\ \hline
            \text{Summe}        & x + y     & 23 \\
            \text{Differenz}    & x - y     & -7 \\
            \text{Produkt}      & x \cdot y & 120
        \end{array}
    \end{align*}

Direkt hinter ``\begin{align}`` werden in geschweiften Klammern die gewünschten
Spalten-Optionen angegeben, wobei ``l`` für eine Links-Ausrichtung der Spalte,
``c`` für eine Zentrierung und ``r`` für eine Rechts-Ausrichtung steht. Die
Anzahl an Spaltenoptionen muss mit der tatsächlichen Spaltenanzahl innerhalb der
Tabelle übereinstimmen. In die einzelnen Felder der ``array``-Umgebung können
wiederum beliebige Formel-Elemente gesetzt werden (sogar Matrizen).

Zwischen den einzelnen Spalten-Optionen können nach Belieben ``|``-Zeichen
eingefügt werden, um (wie bei einer Tabelle) vertikale Striche zwischen den
jeweiligen Spalten (oder am Rand der Tabelle) einzuzeichnen; horizontale Linien
lassen sich jeweils zu Beginn einer neuen Zeile mittels der ``\hline``-Anweisung
verwirklichen.

.. ----

.. .. math:: e^{i\pi} + 1 = 0
..    :label: euler

.. Euler's identity, equation :eq:`euler`, was elected one of the most
.. beautiful mathematical formulas.

.. ----

.. \left[
..   \begin{array}{ c c }
..      1 & 2 \\
..      3 & 4
..   \end{array} \right]

.. Operator-Namen selbst definieren:
.. \newcommand{\arcsinh}{\operatorname{arcsinh}}

.. Zahlenmengen setzen
.. Die natürlichen Zahlen N, R etc. Sollen nat
.. \newcommand{\N}{\ensuremath{\mathbb {N}}}
.. \newcommand{\Z}{\ensuremath{\mathbb {Z}}}
.. \newcommand{\Q}{\ensuremath{\mathbb {Q}}}
.. \newcommand{\R}{\ensuremath{\mathbb {R}}}
.. \newcommand{\C}{\ensuremath{\mathbb {C}}}

.. Polynomdivision setzen:
.. Paket polynom
.. $\polylongdiv[style=C,div=:]{x^3 − 6x^2+11x − 6}{x − 2}$

.. Gauß-Algorithmus setzen
.. Paket gauss
.. $ \begin{gmatrix}[p]
.. − 1 & 8 & 4 && 3,75 \\
.. 5 & 5 & 3 && 4 \\
.. 9 & − 5 & 8 && 5
.. \rowops
.. \mult{0}{5}\add{0}{1}
.. \end{gmatrix} $
.. $ \begin{gmatrix}[p]
.. − 1 & 8 & 4 && 3,75 \\
.. 0 & 45 & 23 && 22,75 \\
.. 9 & − 5 & 8 && 5
.. \rowops
.. \mult{0}{9}\add{0}{2}
.. \end{gmatrix}$
.. $ \begin{gmatrix}[p]
.. − 1 & 8 & 4 && 3,75 \\
.. 0 & 45 & 23 && 22,75 \\
.. 0 & 67 & 44 && 38,75
.. \rowops
.. \mult{2}{45}
.. \mult{1}{67}\add{1}{2}
.. \end{gmatrix}$
.. \end{gmatrix}$
.. $ \begin{gmatrix}[p]
.. − 1 & 8 & 4 && 3,75 \\
.. 0 & 45 & 23 && 22,75 \\
.. 0 & 0 & 439 && 219,5
.. \end{gmatrix}$

.. Damit ist $x_3 = 0,5 $, $x_2 = 0,25$ und $x_1 = 0,25$

.. Grundrechenarten:
.. Paket xlop, Rendtel2009

.. Einheiten im Mathemodus
.. $v = \unitfrac [1]{ m}{s} = \unitfrac [3,6]{ km}{h}$

.. displaystyle bei Brüchen... http://www.andy-roberts.net/writing/latex/mathematics_2





.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Anstelle mit ``$ ... $`` können für Inline-Formeln auch mit ``\( ... \)``
    begrenzt werden. Dies wird beispielsweise vom Dokumentationssystem
    :ref:`Sphinx <gwl:Sphinx>` für automatisch erzeugten LaTeX-Code
    genutzt.

    Anstelle mit ``$$ ... $$`` können eigenständige Formeln auch mit ``\[ ...
    \]`` begrenzt werden.


