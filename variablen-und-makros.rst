
Zähler und Makros
=================

https://de.sharelatex.com/learn/Counters
https://de.sharelatex.com/learn/Commands
https://de.sharelatex.com/learn/Environments

http://tobiw.de/tex-faq

.. rubric:: Zähler

\newcounter{name}
\setcounter{name}{neuer wert}
\addtocounter{name}{wert}
\stepcounter{name}
\roman{name}
\arabic{name}
\alph{name}
10
Wirkung
definiert einen neuen Zähler
weißt einem Zähler einen neuen Wert zu
Addiert einen Wert zum Zähler dazu
Addiert eine 1 zum Wert des Zählers dazu
zählt mit römischen Ziffern
zählt mit arabischen Ziffern
zählt mit kleinen lateinischen Buchstaben

.. rubric:: Längen

Eine Länge oder auch ein Längenbefehl/‑register repräsentiert in TeX eine
Maßangabe wie 10 mm, 12 pt etc., wobei diese intern immer in Punkt (pt)
gespeichert werden.

\newlength{\laenge}

erzeugt eine neue Länge, die den Wert 0 pt hat. Dieser kann auf verschiedene
Arten geändert werden:

* \setlength{\laenge}{10mm} setzt den Wert der Länge
* \addtolength{\laenge}{10mm} ändert den Wert der Länge (auch negative Werte
  sind erlaubt)
* \settowidth{\laenge}{lang} misst die Breite von lang und setzt die Länge
* \settoheight{\laenge}{lang} misst die Höhe von lang, ab der Grundlinie
  (also ohne den "Schwanz" vom g -- die Unterlänge) und setzt die Länge
* \settodepth{\laenge}{lang} misst die Tiefe von lang unter der Grundlinie
  (also nur die Unterlänge) und setzt die Länge

Dabei versteht TeX Längenangaben unter anderem in den ihm bekannten Einheiten
sowie in der Form von 2.3\laenge oder -\laenge. Für komplexere Berechnungen kann
das Paket calc benutzt werden.

Neben den normalen, gibt es auch noch flexible Längen (im engl. Glue), die in
einem definierten Rahmen gedehnt oder gestaucht werden können, beispielsweise,
um eine Zeile im Blocksatz zu füllen. Diesen Rahmen gibt man durch die
Schlüsselwörter plus und/oder minus an:

\setlength{\laenge}{10mm plus 20mm minus 5mm}

Ein Abstand, der die \laenge zugewiesen bekommt, ist im optimal Fall genau 10 mm
lang, kann bei Bedarf aber auf 5 mm schrumpfen bzw. auf 30 mm wachsen.

.. rubric:: newif



Mit \newif wird eine sogenannte Bool’sche Variable erzeugt, die entweder den
Wert wahr (true oder auch 1) oder falsch (false oder 0) haben kann. Man kann
damit also eine Fallunterscheidung treffen.

Dem Befehl \newif folgt der Name der anzulegenden Variable, wobei es üblich,
aber nicht zwingend ist, diesen mit if zu beginnen. Gleichzeitig werden damit
auch zwei Befehle definiert, um den Status der Variable zu ändern.
Beispielsweise erzeugt \newif\ifquestion gleichzeitig auch \questiontrue und
\questionfalse, mit denen der Zustand der Variable geändert werden kann. Diese
beiden Namen werden aus dem Namen des if-Befehls gebildet, wobei die ersten zwei
Buchstaben abgeschnitten werden; damit ist auch einleuchtend, warum man in der
Regel ein if voranstellt.

Um nun je nach Status der Variable unterschiedlichen Code auszuführen, verwendet
man

.. code-block:: tex

    \ifquestion
       Code für wahr-Fall ...
    \else
       Code für falsch-Fall ...
    \fi

oder wenn nur im wahr-Fall etwas ausgeführt werden soll

.. code-block:: tex

    \ifquestion
       Code für wahr-Fall ...
    \fi

(Man beachte, dass ein \if... mit dem umgedreht geschriebenen \fi beendet wird.)

Eine neue Variable ist standardmäßig auf falsch gesetzt.


.. rubric:: Was macht \makeatletter?

Grundsätzlich können wir zwei Ebenen von Befehlen unterscheiden: 1. Die
Benutzerbefehle, die für alle Anwender im ganzen Dokument verfügbar sind, und 2.
den „internen“ Befehlen, die nur Klassen- und Paketentwicklern zur Verfügung
stehen sollen. Diese Unterscheidung stellt gewissermaßen einen Schutz dar.

Technisch wird diese Unterscheidung umgesetzt, in dem interne Befehle ein @ im
Namen tragen, während Benutzerbefehle dies nicht drüfen. Versucht man in einem
normalen Dokument beispielsweise den Befehl \internes@komando aufzurufen, wird
dieser als der Befehl \internes gefolgt von normalen Buchstaben @komando
interpretiert und folglich eine Fehlermeldung, dass \internes nicht definiert
sei, ausgegeben.

Dennoch ist es manchmal nötig (oder sinnvoll), auch in normalen Dokumenten auf
interne Befehle zurückgreifen zu können, etwa um sie für eigene Definitionen zu
verwenden oder auch auf Dokumentebene die genannte Unterscheidung umsetzen zu
können. In diesem Fall kann man mit \makeatletter das @ sozusagen freischalten.
Allerdings sollte diese Änderung nach der Verwendung der internen Befehle
unbedingt mit \makeatother wieder rückgängig gemacht werden.

.. rubric:: Wie benutzt man \newcommand?

Mit \newcommand kann man in LaTeX eigene Befehle definieren. Der Befehl hat die
Syntax

.. code-block:: tex

    \newcommand{Name}[Arg][oArg]{
       Definition
    }

Dabei gibt es drei Möglichkeiten für Argumente: Der zu definierende Befehl (im
den folgenden Beispielen \test) hat ...

* ... keine Argumente: Beide optionalen Argumente von \newcommand weglassen,
  bspw. \newcommand{\test}{Test}.

* ... nur obligatorische Argumente: mit dem optionalen Argument von
  \newcommand die Anzahl der Argumente des zu definierenden Befehls angeben,
  bspw. \newcommand{\test}[2]{Test: #1 u. #2} für zwei Argumente.

* ... ein optionales Argument und evtl. weitere obligatorische: mit dem ersten
  optionalen Argument von \newcommand die Anzahl der Argumente des zu
  definierenden Befehls angeben und mit dem zweiten optionalen Argument von
  \newcommand den Standardwert für das optionale Argument des zu definierenden
  Befehls, bspw. \newcommand{\test}[1][Standard]{#1-Test} für \test mit nur
  einem optionalen Argument oder \newcommand{\test}[2][Test]{#2-#1} für \test
  mit einem optionalen und einem obligatorischen Argument.

Innerhalb der Definition kann mit #n auf die Argumente des zu definierenden
Befehls zugegriffen werden und insgesamt sind neun Argumente möglich. Außerdem
gibt es die Möglichkeit, die Sternform \newcommand* zu benutzen, dann dürfen die
Argumente keine Absätze enthalten.

Neben \newcommand gibt es noch \renewcommand, um einen existierenden Befehl neu
zu definieren, und \providecommand, um einen Befehl zu definieren, wenn dieser
bisher nicht definiert wurde.
