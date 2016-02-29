.. index:: Mathematische Formel, Formel
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

Sollen mehrzeilige Formeln gesetzt werden, so muss eine spezielle
Mathematik-Umgebung wie beispielsweise ``align`` beziehungsweise  ``align*`` für
nummerierte beziehungsweise nicht nummerierte Formeln gewählt werden.

.. code-block:: tex

    \begin{align}
        E \underset{Einstein}{=} m \cdot c^2
        \underset{Pythagoras}{=} m \cdot (a^2 + b^2)
    \end{align}

*Ergebnis:*

.. math::
    :label: eqn-einstein-pythagoras

    E \underset{Einstein}{=} m \cdot c^2 \underset{Pythagoras}{=} m \cdot (a^2 + b^2)

Die Umgebungen ``align`` und ``align*`` sind für fast alle abgesetzten
Formeln die beste Wahl. Eine Ausnahme bilden mehrere einzeilig Formeln, die
zueinander ausgerichtet, aber einzeln nummeriert werden sollen. Für diesen
Zweck gibt es die Umgebung ``eqnarray``:

.. code-block:: tex

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

Der Gleichungs-Zähler kann bei Bedarf mittels ``\setcounter{equation}{1}``
wieder auf den Wert ``1`` (oder einen beliebigen anderen Wert) gesetzt werden.
Mit ``\numberwithin{equation}{section}`` kann zudem festgelegt werden, welcher
Gliederungstiefe die Formeln zugerechnet werden sollen, ob also eine
Nummerierung in der Art :math:`(1), (2), \ldots` oder abschnittsweise
als :math:`(1.1), (1.2), \ldots` erfolgen soll.

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

      \mathbb{ABCDEF} \quad \phantom{\mathtt{abcdef}} \quad \phantom{\mathtt{123456}}

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

.. index:: Pfeilsymbole
.. _Pfeilsymbole:

.. rubric:: Pfeilsymbole

.. list-table::
    :name: tab-pfeilsymbole
    :widths: 55 50 50 50
    :header-rows: 0

    * - Eingabe
      - Ausgabe
      - Eingabe
      - Ausgabe
    * - ``\rightarrow`` oder ``\to``
      - :math:`{\color{white}|}\rightarrow{\color{white}|}`
      - ``\Rightarrow``
      - :math:`{\color{white}|}\Rightarrow{\color{white}|}`
    * - ``\leftarrow``
      - :math:`{\color{white}|}\leftarrow{\color{white}|}`
      - ``\Leftarrow``
      - :math:`{\color{white}|}\Leftarrow{\color{white}|}`
    * - ``\longrightarrow``
      - :math:`{\color{white}|}\longrightarrow{\color{white}|}`
      - ``\Longrightarrow``
      - :math:`{\color{white}|}\Longrightarrow{\color{white}|}`
    * - ``\longleftarrow``
      - :math:`{\color{white}|}\longleftarrow{\color{white}|}`
      - ``\Longleftarrow``
      - :math:`{\color{white}|}\Longleftarrow`
    * - ``\leftrightarrow``
      - :math:`{\color{white}|}\leftrightarrow{\color{white}|}`
      - ``\Leftreftarrow``
      - :math:`{\color{white}|}\Leftrightarrow{\color{white}|}`
    * - ``\longleftrightarrow``
      - :math:`{\color{white}|}\longleftrightarrow{\color{white}|}`
      - ``\Longleftreftarrow``
      - :math:`{\color{white}|}\Longleftrightarrow{\color{white}|}`
    * - ``\uparrow``
      - :math:`{\color{white}|}\uparrow{\color{white}|}`
      - ``\Uparrow``
      - :math:`{\color{white}|}\Uparrow{\color{white}|}`
    * - ``\downarrow``
      - :math:`{\color{white}|}\downarrow{\color{white}|}`
      - ``\Downarrow``
      - :math:`{\color{white}|}\Downarrow{\color{white}|}`
    * - ``\updownarrow``
      - :math:`{\color{white}|}\updownarrow{\color{white}|}`
      - ``\Updownarrow``
      - :math:`{\color{white}|}\Updownarrow{\color{white}|}`
    * - ``\hookrightarrow``
      - :math:`{\color{white}|}\hookrightarrow{\color{white}|}`
      - ``\hookleftarrow``
      - :math:`{\color{white}|}\hookleftarrow{\color{white}|}`
    * - ``\nwarrow``
      - :math:`{\color{white}|}\nwarrow{\color{white}|}`
      - ``\nearrow``
      - :math:`{\color{white}|}\nearrow{\color{white}|}`
    * - ``\swarrow``
      - :math:`{\color{white}|}\swarrow{\color{white}|}`
      - ``\searrow``
      - :math:`{\color{white}|}\searrow{\color{white}|}`


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

.. http://latex.wikia.com/wiki/List_of_LaTeX_symbols
.. https://de.wikipedia.org/wiki/Liste_mathematischer_Symbole

.. _Mathematische Ausdrücke:

Mathematische Ausdrücke
-----------------------

.. todo:: lim

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
Indizes hingegen kursiv. Möchte man aufrechte Indizes erhalten, so müssen diese
in geschweifte Klammern gesetzt und mittels ``\mathrm{}`` explizit in aufrechter
Form ausgegeben werden.

.. index:: Klammern, Pfeile
.. _Klammern und Pfeile:

.. rubric:: Klammern und Pfeile

Runde und eckige Klammern können in LaTeX-Formeln als gewöhnliche Zeichen
gesetzt werden, bei geschweiften Klammern muss ein Backslash-Zeichen vor die
öffnende und schließende Klammer gesetzt werden. Möchte man allerdings die
Größe einer Klammer anpassen, wenn beispielsweise ein Bruch innerhalb der
Klammer vorkommt, so kann die Klammergröße automatisch oder manuell festgelegt
werden:

* Mit ``\left( ... \right)`` wird die Größe der öffnenden bzw. schließenden
  runden Klammer automatisch an den Inhalt der Klammer angepasst. Das gleiche
  funktioniert auch mit eckigen Klammern.
* Mit ``\big( ... \big)``, ``\Big( ... \Big)`` kann die Größe der öffnenden
  bzw. schließenden runden Klammern manuell festgelegt werden. Das gleiche
  funktioniert ebenfalls mit vertikalen Strichen (z.B. Betragstrichen), die
  direkt mittels des Pipe-Zeichens ``|`` eingegeben werden können.

Pfeilen können entweder über oder zwischen mathematischen Symbolen stehen.
Pfeile *über* mathematischen Symbolen markieren Vektoren oder gerichtete
Strecken. Im Fall von Vektoren, wenn sich der Pfeil über ein einzelnes Zeichen
erstreckt, kann man die Anweisung ``\vec{}`` verwenden, für Pfeile über
mehreren mathematischen Symbolen muss hingegen ``\overrightarrow{}`` verwendet
werden:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \vec{v}
        \overrightarrow{OP}
    \end{align*}

*Ergebnis:*

.. math::

    \vec{v}  \qquad \overrightarrow{OP}

Für Pfeile *zwischen* mathematischen Symbolen gibt es mehrere Anweisungen. Ein
einfacher waagrechter Pfeil, wie er beispielsweise geschrieben wird, wenn eine
Zahl gegen einen bestimmten Grenzwert geht, kann einfach mit ``\to`` gesetzt
werden. Mehr Flexibilität bieten die Anweisungen der Art ``\leftarrow`` und
``\rightarrow``: Sie können auch als lange Varianten (``\longrightarrow``) oder
mit doppeltem waagrechten Strich (``\Rightarrow)`` ausgegeben werden; auch eine
Kombination beider Varianten ist mittels ``\Longrightarrow`` möglich.

.. rubric:: Wurzeln, Brüche und Binomialkoeffizienten

Wurzeln werden in LaTeX-Formeln mittels ``\sqrt{}`` gesetzt. Möchte man keine
Quadrat-Wurzel ausgeben, sondern eine Wurzel mit einem anderen Wurzelexponenten,
so kann für die :math:`n`-te Wurzel aus einer Zahl ``\sqrt[n]{Zahl}``
geschrieben werden.

Brüche werden in LaTeX mittels ``\frac{Zähler}{Nenner}`` gesetzt.


.. index:: Summenzeichen, \sum
.. _Summen und Integrale:

.. rubric:: Summen und Integrale

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

.. index:: Integralzeichen, \int

Das Integralzeichen :math:`\int` kann im Mathe-Modus mittels ``\int`` gedruckt
werden. Üblicherweise wird auch hierbei unterhalb des Integralzeichens die
Untergrenze und oberhalb die Obergrenze der zu integrierenden Größe angegeben.
In LaTeX wird dazu wiederum die für Indizes und Exponenten übliche Syntax genutzt und
somit ``\int_{}^{}`` geschrieben:

*Beispiel:*

.. code-block:: tex

    \begin{align*}
        \int_{a}^{b} f(x) \cdot \mathrm{d} x = F(b) - F(a)
    \end{align*}

*Ergebnis:*

.. math::

    \int_{a}^{b} f(x) \cdot \mathrm{d} x = F(b) - F(a)


.. rubric:: Matrizen und Determinanten

.. rubric:: Fallunterscheidungen

.. Zeichen über istgleich setzen:
.. \stackrel{\wedge}=

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



