
Bibliographie
=============

.. code-block:: tex

    \begin{thebibliography}{9}
        \bibitem[Frank 04]{Kurs1} \emph{Erste Schritte mit \LaTeX},
            Sascha Frank 2004
        \bibitem[Frank 05]{kurz1} \emph{Kurzdokumentation zu Kurs 1}
            Sascha Frank 2005
    \end{thebibliography}


Zitiert wird mit ``\cite{Kurs1}``

Literaturdatenbank
------------------

Falls man beim Erstellen seiner Arbeiten immer wieder auf dieselben Arbeiten
zurückgreifen muss bzw. kann, empfiehlt sich der Aufbau einer
Literaturdatenbank. Zum Teil gibt es die Bibtex Datei der jeweiligen Quellen zum
runterladen.

In LaTeX geschieht dies mittels einer ``.bib`` Date. In diese werden die
Informationen zu den Quellen eingetragen, die Quellen haben je nach Typ, also
Bücher, Artikel, usw., verschiedene Kann und Pflichtfelder.

.. code-block:: tex

    @Book{,
        ALTauthor =
        {},
        ALTeditor =
        {},
        title = {},
        publisher =
        {},
        year = {},
        OPTkey = {},
        OPTvolume =
        {},
        OPTnumber =
        {},
        OPTseries =
        {},
        OPTaddress =
        {},
        OPTedition =
        {},
        OPTmonth =
        {},
        OPTnote = {},
        OPTannote =
        {}
    }

Die mit OPT beginnenden Felder sind die Kannfelder, falls man sie verwenden will
wird einfach das Kürzel OPT entfernt, z.B. OPTkey wird zu key .

Beispiel für ein Buch:

.. code-block:: tex

    @BOOK{zahl,
        Year = {1996},
        Author = {Georges Ifrah},
        Title = {Universalgeschichte der Zahlen},
        publisher = {abc Verlag}
    }

Zitiert wird im Text mit \cite{zahl} .

An der Stelle an welcher das Literaturverzeichnis eingefügt werden soll, gibt

\bibliography{literatur}
\bibliographystyle{unsrtdin}
Neben der Literaturdatenbank (.bib Datei) wird noch eine Stilldatei eingefügt,
sie ist entscheident für das Aussehen des Verzeichnisses und ist von Fach
zu Fach unterschiedlich je nach Anforderung.

Vorgehen:

1. pdflatex seminar.tex
2. pdflatex seminar.tex
3. bibtex seminar !! Wichtig: Keine Endung !!
4. pdflatex seminar.tex
5. pdflatex seminar.tex

\newpage
\renewcommand{\indexname}{Sachregister}
\addcontentsline{toc}{section}{Sachregister}
\printindex

Sachregister
------------

Benötigtes Paket:
\usepackage{makeidx}

\makeindex
    Wird durch diese Anweidsung **vor** ``\begin{document}``
    Ausgabe des Index mit aktiviert, er muss noch kommen.

\index{wort}
    Mit \index{wichtiges Wort} werden die Wörter makiert.

\printindex
    Ausgabe des Index an dieser Stelle


Falls man statt Index lieber die Bezeichnung Sachregister haben will:
\renewcommand{\indexname}{Sachregister}
\addcontentsline{toc}{section}{Sachregister}

Dateiendung beim Kompilieren: ``.idx``

Glossar
-------

Ähnlich wie ein Index lässt sich auch ein Glossar erstellen.

Benötigtes Paket:

\usepackage{makeidx}

\makeglossary
    Wird durch diese Anweisung **vor** ``\begin{document}`` aktiviert, er muss
    noch kommen.

\glossary{wort}
    Mit \glossary{Wort! Worterkl\"arung ... } werden die Wörter makiert z.B.
    \glossary{Pr\"aambel! Pr\"aambel, auch Vorspann genannt, um ... }

Wenn jetzt nach dem Markieren LaTeXdurchgelaufen ist, wird zusätzlich eine
``.glo`` Datei erzeugt. man braucht eine zusätzliche Stildatei, da es
Glossarentry's und nicht Indexentry's sind usw..

Meine Stildatei heisst glossar.ist und hat folgenden Inhalt:
preamble "\\begin{description}\n"
keyword "\\glossaryentry"
postamble "\n\n\\end{description}\n"
Das Glossar wird in der Form einer description dargestellt.

makeindex -s glossar.ist dateiname.glo

