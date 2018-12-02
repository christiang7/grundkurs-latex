.. _Weitere Dokumentklassen:

Weitere Dokumentklassen
=======================

LaTeX kann nicht nur zum Schreiben von Artikeln und Büchern verwendet werden --
es gibt einige weitere Dokumentklassen, mit denen auch andere Arten von
Textdokumenten erstellt werden können.

.. index:: scrlttr2 (Dokumentklasse), Briefe
.. _scrlttr2:

``scrlttr2`` -- Briefe und Serienbriefe
---------------------------------------

Die Dokumentklasse ``scrlttr2`` ermöglicht es, auf einfache Weise Briefe mit
gewohnt eleganten LaTeX-Layout zu verfassen. Wie bei anderen Dokumentklassen
können bereits in der ``\documentclass{}``-Anweisung optionale Layout-Angaben
festgelegt werden:

.. https://www.ctan.org/pkg/scrlttr2

.. code-block:: tex

    \documentclass[a4paper, 12pt, halfparskip]{scrlttr2}

Für die typischen ``scrlttr2``-Optionen empfielt es sich der Übersichtlichkeit
halber, diese separat mittels der ``\KOMAoptions{}``-Anweisung festzulegen:

.. code-block:: tex

    \KOMAoptions{
        backaddress,            % Adresse des Absenders im Adressfenster anzeigen
        foldmarks=on,           % Faltungs-Markierungen drucken
        fromalign=left,         % Ausrichtung des Briefkopfes (Absender)
        fromphone,              % Telefonnummer anzeigen
        fromemail,              % Emailadresse des Absenders anzeigen
        fromurl,                % Verweis auf Webseite
      % fromlogo,               % Logo drucken
      % fromfax,                % Faxnummer des Absenders angeben
    }

Auf diese Weise können einzelne Angaben einfach ausgeblendet werden, indem zu
Beginn der jeweiligen Zeile das Kommentarzeichen ``%`` gesetzt wird. Die
einzelnen Angaben können dann folgendermaßen festgelegt werden:

.. code-block:: tex

    \setkomavar{fromname}{Vorname Nachname}
    \setkomavar{fromurl}{http://webadresse.de}
    \setkomavar{fromaddress}{Straßenname 1 \\ 123456 Ortsname}
    \setkomavar{fromphone}{01234- 56\,78\,90}
    \setkomavar{fromemail}{vorname.nachname@email.de}

    \setkomavar{backaddressseparator}{
        ~\raisebox{0.25ex}{\textbf{\Large.}}~
        }

    \setkomafont{backaddress}{\sffamily\tiny}
    \setkomafont{fromaddress}{\rmfamily\footnotesize}

Neben diesen Festlegungen können in der Präambel ebenso wie bei anderen
Dokumenten weitere Zusatzpakete mittels ``\usepackage{}`` geladen werden. Das
eigentliche Textdokument wird dann wie üblich durch die ``document``-Umgebung
begrenzt.

Da einem Brief zusätzliche Inhalte als Anhang beigefügt sein können, wird das
eigentliche Anschreiben mittels der innerhalb der ``scrlttr2``-Dokumentklasse
definiierten ``letter``-Umgebung vorgenommen:

.. code-block:: tex

    \begin{letter}{
        Name des Empfängers \\
        Anschrift des Empfängers \\
        PLZ Ort
        }

    \opening{Sehr geehrte Person(en),}

        ... Brieftext ...

    \closing{Mit freundlichen Grüßen,}

    \end{letter}

Am Ende der ``letter``-Umgebung kann optional mittels der Anweisung ``\ps{}``
ein Nachsatz ("Post Scriptum") und/oder mittels der ``\encl{}``-Anweisung eine
Aufzählung der Anhänge ("Enclosures") angefügt werden. [#]_

Ein kompletter Brief kann somit als Minimalbeispiel folgendermaßen aussehen:
:download:`testbrief.tex <testbrief.tex>`

.. code-block:: tex

    \documentclass[a4paper, 12pt, halfparskip]{scrlttr2}

    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage[ngerman]{babel}
    \usepackage{graphicx, blindtext}

    \KOMAoptions{
        backaddress,            % Adresse des Absenders im Adressfenster anzeigen
        foldmarks=on,           % Faltungs-Markierungen drucken
        fromalign=left,         % Ausrichtung des Briefkopfes (Absender)
      % fromfax,                % Faxnummer des Absenders angeben
        fromemail,              % Emailadresse des Absenders anzeigen
        fromphone,              % Telefonnummer anzeigen
      % fromlogo,               % Logo drucken
        fromurl,                % Verweis auf Webseite
        }

    \setkomavar{fromname}{Vorname Nachname}
    \setkomavar{fromurl}[Web:\quad]{http://webadresse.de}
    \setkomavar{fromaddress}{Straßenname 1 \\ 123456 Ortsname}
    \setkomavar{fromphone}{01234- 56\,78\,90}
    \setkomavar{fromemail}{vorname.nachname@email.de}

    \setkomavar{backaddressseparator}{
        ~\raisebox{0.25ex}{\textbf{\Large.}}~
        }

    \setkomafont{backaddress}{\sffamily\tiny}
    \setkomafont{fromaddress}{\rmfamily\footnotesize}

    \begin{document}

    \begin{letter}{
        Name des Empfängers \\
        Anschrift des Empfängers \\
        PLZ Ort
        }

    \opening{Sehr geehrte Person(en),}

        \blindtext  % Das eigentliche Anschreiben

    \closing{Mit freundlichen Grüßen,}

    \ps{P.S.: Hier noch ein kurzer Nachsatz, ausschließlich zu Demonstrationszwecken.}
    \encl{
        Anhang 1 \\
        Anhang 2
        }


    \end{letter}
    \end{document}

Dieses Codebeispiel liefert folgendes Ergebnis: :download:`testbrief.pdf <testbrief.pdf>` [#]_

.. only:: html

    .. image:: pics/testbrief.png
        :align: center
        :width: 80%

.. raw:: latex

    \begin{center}
    \fbox{\includegraphics[width=0.80\textwidth]{/home/grund-wissen/source/informatik/latex/testbrief.pdf}}
    \end{center}

Werden keine weiteren Layout-Vorgaben getroffen, so werden die Briefseiten bei
Verwendung von ``scrlttr2`` ab der zweiten Seite automatisch durchnummeriert.
[#]_


.. _Design der ersten Seite gestalten:

.. rubric:: Design der ersten Seite gestalten

Bei offiziellen Anschreiben weicht oftmals das Layout der ersten Seite von dem
der folgenden Seiten ab. Beispielsweise erscheint nur auf der ersten Seite der
Briefkopf, oftmals mit Briefkopf und Logo, bei geschäftlichen Briefen zusätzlich
mit Kunden- oder Rechnungsnummer; in der Fußzeile finden sich auf der ersten
Seite eines Briefes zudem oftmals Bankverbindungs- und weitere Kontaktdaten.

Offizielle Briefe enthalten häufig zusätzlich zu den oben genannten Angaben
folgende Variablen:

.. code-block:: tex

    \setkomavar{fromurl}[Web:\quad]{http://webadresse.de}
    \setkomavar{fromlogo}{\includegraphics{testlogo.png}}
    \setkomavar{location}{\raggedright Mitglied Nr.~4711\\
                          seit dem 11.09.2001\\
                        Vorsitzender in den Jahren 2003--2005}

    \setkomavar{frombank}{
        IBAN: DE\,0000\,0000\,0000\,0000\,0000 \\
        BIC: XXXXXXXXXXX \\
        Name der Bank
        }

.. Scrguide 177: Coole Übersichtsgraphik
.. http://www.komascript.de/~mkohm/scrguide.pdf

... to be continued ...

.. TODO booklets: http://tobiw.de/tbdm/booklets-erzeugen

.. \includepdf[pages=-,booklet]{einzelseiten}
.. Wie versprochen ist es sehr einfach, eine Broschüre zu erzeugen: Dem Befehl
.. \includepdf geben wir mit pages den zu verwendenden Seitenbereich an, wobei -
.. "alle Seiten" bedeutet (1-8 wären bspw. die ersten acht Seiten), und mit
.. booklet, dass die Seiten als Booklet ausgeschossen werden sollen. Das
.. obligatorische Argument ist der Dateiname der Einzelseiten-PDF.


.. Passen Druckbogen- und Seitenformat nicht zusammen, werden die Einzelseiten
.. skaliert.

.. Todo Index
.. http://tobiw.de/tbdm/index-1
.. http://tobiw.de/tbdm/index-2

.. Todo Curriculum Vitae
.. http://www.howtotex.com/general/a-guide-to-building-a-plain-and-simple-latex-cv/
.. http://www.howtotex.com/templates/creating-a-designers-cv-in-latex/

.. ``beamer`` -- Präsentationen
.. ----------------------------

.. Anders als bei den bisher vorgestellten Klassen, gibt es in Beamer keine Seiten,
.. sondern so genanten "Frames" (Rahmen). Diese stellen den Platz für die
.. Präsentation zur Verfügung. Innerhalb der Frames spielen die Overlays die
.. entscheidende Rolle, sie ermöglichen es das ein Frame mehrere Slides haben kann.
.. Zudem sind zusätzliche Pakete in die Beamer Class eingebunden wie beispielsweise
.. ``xcolor`` und ``hyperref``.
.. Für die Beamer Class gibt eine umfangreiche Sammlung von Vorlagen, eine
.. Übersicht findet sich auf einer meiner Seiten: Beamer Theme Übersicht
.. http://www.namsu.de/latex/themes/uebersicht_beamer.html

.. Die Dokumentenklasse Beamer hat wie die anderen Klassen auch zusätzliche Optionen:

.. * handout -- ignoriert Overlays
.. * draft -- ignoriert Bilder

.. Innerhalb der Präambel kann das spätere Erscheinungsbild mittels eines Themes
.. festgelegt werden:

.. .. rubric:: Frames

.. Wie eingangs erwähnt gibt es keine Seiten sondern Frame's. Der Rahmen selbst hat
.. je nach gewähltem Erscheinungsbild der Präsentation einen oberen, unteren,
.. linken und oder rechten Rand. Neben LaTeX-typischen Umgebungen wie Listen,
.. Aufzählungen usw. gibt es zusätzliche Umgebungen wie z.B. die Blockumgebung.

.. Aufbau des Frames Die Frame Umgebung wird mit \begin{frame} geöffnet und mit
.. \end{frame} geschlossen. Jede Folien sollte einen Titel haben z.B.
.. \frametitle{Keine Folie ohne Titel} ggf. auch einen Untertitle
.. \framesubtitle{falls es noch mehr gibt} .

.. Beispiel:

.. .. code-block:: tex

..     \begin{frame}
..         \frametitle{Titel}
..         % Optional: \framesubtitle{Untertitel}
..         % Inhalt (Text, Bilder, usw.)
..     \end{frame}


.. Mit vordefinierten Blockumgebungen bietet Beamer eine relativ einfache
.. Möglichkeit, Texte innerhalb eines Frames zu strukturieren sowie Beispiele oder
.. Warnungen hervorzuheben:

.. * Standard-Blockumgebung (Farbe: blau)

.. .. code-block:: tex

..     \begin{block}{Block Titel}
..         Text
..     \end{block}

.. * Beispiel-Blockumgebung (Farbe: grün)

.. .. code-block:: tex

..     \begin{exampleblock}{Block Titel}
..         Text
..     \end{exampleblock}

.. * Alarm-Blockumgebung (Farbe: rot)

.. .. code-block:: tex

..     \begin{alertblock}{Block Titel}
..         Text
..     \end{alertblock}

.. Frames erlauben nicht nur eine Einteilung in oben und unten, sondern auch eine
.. aufteilung in links und rechts. Zusammen sollten die Spalten nicht mehr wie 10cm
.. haben.

.. .. code-block:: tex

..     \begin{columns}

..         \begin{column}{5cm}
..             Text der ersten (linken) Spalte ....
..         \end{column}

..         \begin{column}{5cm}
..             Text der zweiten Spalte....
..         \end{column}

..     \end{columns}

.. Overlays
.. Unter einem Overlay versteh ich einen Teil der Folie, der nicht die komplette
.. Zeit in der die Folie als ganzes sichtbar ist, selbst sichtbar ist. Zum Beispiel
.. das einzelne Punkte erst nach und nach erscheinen, oder das beim
.. weiterklicken die alten Punkte verschwinden. Ich setze dies auch oft bei
.. Aufzählungen ein, ein Grund dafür, ist daÿmeiner Meinung nach, die Aufmerk-
.. samkeit des Publikums sich nicht im Gesamttext verliert. Sie sehen das neue
.. und werden nicht durch weiteren Text zu dem man aber erst später kommt

.. Aufzählung zu einem bestimmten Zeitpunkt

.. .. code-block:: tex

..     \begin{itemize}
..     \item<1-> erster Punkt
..     \item<2-> zweiter Punkt
..     \item<3-> dritter Punkt
..     \item<4-> \dots
..     \end{itemize}

.. Innerhalb von Aufzählungen geht das auch recht einfach, man gibt an ab
.. welchem 'Klick' der Punkt erscheien soll. Angenommen er soll ab dem dritten
.. Klick und bis zum Ende erscheinen ``\item<3-> Punkt`` . Soll er nur beim 3,4,5
.. erscheinen ``\item<3-5> Punkt``. Will man einen bestimmten Zeitpunkt bzw. Klick
.. haben muss dies genau angegeben werden.

.. Bei fortlaufenden Aufzählungen lässt sich das ganze zu abkürzen.

.. .. code-block:: tex

..     \begin{itemize}[<+->]
..     \item erster Punkt
..     \item zweiter Punkt
..     \item dritter Punkt
..     \item \dots
..     \end{itemize}

.. .. \pause Mit dem Befehl \pause lassen sich \pause einfach
.. .. Overlays einf\"ugen. \pause

.. .. Neben der Pause gibt es noch die Möglichkeit Text usw. unsichtbar zu machen. Sie
.. .. erscheinen während dieser Zeit nicht auf dem Bildschirm, aber ihr Platz wird
.. .. trotzdem freigehalten. Soll etwas zum Zeitpunkt

.. .. \pause Mit dem \invisible<3,4>{Befehl}
.. .. \invisible \pause werden Dinge unsichtbar.
.. .. \pause Sie sind aber immer noch da.\pause

.. Themes Die Themes in Beamer sind Präsentationsvorlagen, standardmäßig sind 28
.. Stück bei der Beamer class mit dabei. Davon sind 26 Stück nach Städten benannt.
.. Themes bestehen aus mehreren Bestandteilen, die verschiedene Teile der
.. Präsentation bestimmen. Aussehen, Struktur, Farbe, Schrift


.. Inhalt eines Präsentationsthemes

.. * inner theme
.. * outer theme
.. * color theme
.. * font theme


.. Inner Themes verändern

.. * Titelseite
.. * Umgebungen
.. * Aufzählungen
.. * Block ... usw.

.. Einbinden mit \useinnertheme[Option]{inner theme}

.. Outer Themes verändern

.. * Sidebars (Übersicht)
.. * Kopf- und Fuÿzeile
.. * Logo
.. * Folientitel

.. Einbinden mit \useoutertheme{outer theme}

.. Color Themes verändern

.. * Farbe der Präsentation Komplett
.. * Outer Theme
.. * Inner Theme

.. Font Themes verändert Aussehen der Schrift

.. Einbinden mit \usefonttheme{font theme}

.. Es gibt zwei (große) Unterschiede zwischen einer Titelseite in Beamer und in
.. einer anderen Dokumentenklasse. Der Befehl hier ist: \titlepage .
.. Der zweite ist das man für den Titel und den Autor Kurzfassungen mitgeben kann,
.. die dann so auf jeder Folie vorhanden sind. Ein Logo wird durch folgende
.. Anweisung eingefügt:

.. \logo{\includegraphics{dateiname}}

.. \title[Kurztitel]{lange Fassung f\"ur die Titelseite}
.. \author[Autor]{lange Fassung des Autors}
.. \logo{\includegraphics[optionen]{datei}}

.. Schlichte Variante
.. * Titel
.. * Autor
.. * Datum

.. Titelseite (2): etwas mehr

.. * Titel nur noch auf der Titelseite
.. * Kurztitel für alle Folien
.. * Kurzform für den Autor
.. * Logo einbauen

.. \title[Beamer Class]{Pr\"asentationen mit \LaTeX}
.. \author[Sascha Frank]{Sascha Frank\\www.namsu.de}
.. \logo{\includegraphics[scale=0.13]{logo-SF}}

.. Titel und Übersicht

.. .. code-block:: tex

..     \begin{document}
..     \begin{frame}
..     \titlepage
..     \end{frame}

.. Ein Inhaltsverzeichnis in Beamer, ist \tableofcontens
.. in einem Frame:

.. \begin{frame}
.. \frametitle{Übersicht}
.. \tableofcontents
.. \end{frame}


.. Anbei ein Beispiel für eine gute Präsentation mit Latex Beamer Class.

.. Übersicht der usethemes der Beamer class

.. .. code-block:: tex

..     % zusaetzlich ist das usepackage{beamerthemeshadow} eingebunden
..     %
..     % \beamersetuncovermixins{\opaqueness<1>{25}}{\opaqueness<2->{15}}
..     % sorgt dafuer das die Elemente die erst noch kommen nur schwach
..     % angedeutet erscheinen
..     \documentclass{beamer}
..     \usepackage{beamerthemeshadow}
..     \beamersetuncovermixins{\opaqueness<1>{25}}{\opaqueness<2->{15}}
..     \begin{document}
..     \title{Beamer Class ganz nett}
..     \author{Sascha Frank}
..     \date{\today}

..     \frame{\titlepage}

..     \frame{\frametitle{Inhaltsverzeichnis}\tableofcontents}

..     \section{Abschnitt Nr.1}

..     \frame{\frametitle{Titel}
..         Die einzelnen Frames sollte einen Titel haben
..     }

..     \subsection{Unterabschnitt Nr.1.1 }

..     \frame{
..         Denn ohne Titel fehlt ihnen was
..     }

..     \section{Abschnitt Nr. 2}
..     \subsection{Listen I}

..     \frame{\frametitle{Aufz\"ahlung}
..         \begin{itemize}
..             \item Einf\"uhrungskurs in \LaTeX
..             \item Kurs 2
..             \item Seminararbeiten und Pr\"asentationen mit \LaTeX
..             \item Die Beamerclass
..         \end{itemize}
..     }

..     \frame{\frametitle{Aufz\"ahlung mit Pausen}
..         \begin{itemize}
..             \item Einf\"uhrungskurs in \LaTeX \pause
..             \item Kurs 2 \pause
..             \item Seminararbeiten und Pr\"asentationen mit \LaTeX \pause
..             \item Die Beamerclass
..         \end{itemize}
..     }

..     \subsection{Listen II}

..     \frame{\frametitle{Numerierte Liste}
..         \begin{enumerate}
..             \item Einf\"uhrungskurs in \LaTeX
..             \item Kurs 2
..             \item Seminararbeiten und Pr\"asentationen mit \LaTeX
..             \item Die Beamerclass
..         \end{enumerate}
..     }

..     \frame{\frametitle{Numerierte Liste mit Pausen}
..         \begin{enumerate}
..             \item Einf\"uhrungskurs in \LaTeX \pause
..             \item Kurs 2 \pause
..             \item Seminararbeiten und Pr\"asentationen mit \LaTeX \pause
..             \item Die Beamerclass
..         \end{enumerate}
..     }

..     \section{Abschnitt Nr.3}
..     \subsection{Tabellen}

..     \frame{\frametitle{Tabellen}
..         \begin{tabular}{|c|c|c|}
..             \hline
..             \textbf{Zeitpunkt} & \textbf{Kursleiter} & \textbf{Titel} \\
..             \hline
..             WS 04/05 & Sascha Frank & Erste Schritte mit \LaTeX \\
..             \hline
..             SS 05 & Sascha Frank & \LaTeX \ Kursreihe \\
..             \hline
..         \end{tabular}
..     }

..     \frame{\frametitle{Tabellen mit Pause}
..         \begin{tabular}{c c c}
..             A & B & C \\
..             \pause
..             1 & 2 & 3 \\
..             \pause
..             A & B & C \\
..         \end{tabular} 
..     }

..     \section{Abschnitt Nr. 4}
..     \subsection{Bl\"ocke}

..     \frame{\frametitle{Bl\"ocke}
..         \begin{block}{Blocktitel}
..         Blocktext
..         \end{block}
..         \begin{exampleblock}{Blocktitel}
..         Blocktext
..         \end{exampleblock}
..         \begin{alertblock}{Blocktitel}
..         Blocktext
..         \end{alertblock}
..     }

..     \section{Abschnitt Nr. 5}
..     \subsection{Geteilter Bildschirm}

..     \frame{\frametitle{Zerteilen des Bildschirmes}
..         \begin{columns}
..         \begin{column}{5cm}
..             \begin{itemize}
..                 \item Beamer
..                 \item Beamer Class
..                 \item Beamer Class Latex
..             \end{itemize}
..         \end{column}
..         \begin{column}{5cm}
..             \begin{tabular}{|c|c|}
..             \hline
..             \textbf{Kursleiter} & \textbf{Titel} \\
..             \hline
..             Sascha Frank & \LaTeX \ Kurs 1 \\
..             \hline
..             Sascha Frank & \LaTeX \ Kursreihe \\
..             \hline
..             \end{tabular}
..         \end{column}
..         \end{columns}
..     }

..     \subsection{Bilder}

..     \frame{\frametitle{Bilder in Beamer}
..         \begin{figure}
..         \includegraphics[scale=0.5]{PIC1}
..         \caption{Die Abbildung zeigt ein Beispielbild}
..         \end{figure}
..     }

..     \subsection{Bilder und Listen kombiniert}

..     \frame{
..         \frametitle{Bilder und Itemization in Beamer}
..         \begin{columns}
..         \begin{column}{5cm}
..             \begin{itemize}
..             \item<1-> Stichwort 1
..             \item<3-> Stichwort 2
..             \item<5-> Stichwort 3
..             \end{itemize}
..             \vspace{3cm}
..         \end{column}
..         \begin{column}{5cm}
..             \begin{overprint}
..             \includegraphics<2>{PIC1}
..             \includegraphics<4>{PIC2}
..             \includegraphics<6>{PIC3}
..             \end{overprint}
..         \end{column}
..         \end{columns}
..     }

..     \end{document}

.. http://www.namsu.de/latex/themes/uebersicht_beamer.html
.. http://www.namsu.de/latex/themes/Goettingen.html



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Mit ``\setkomavar*{enclseparator}{Anlage}`` kann die als Standard
    definierte Kennzeichnung "Anlage(n):" durch den angegebenen Text ersetzt
    werden.

.. [#] In Sphinx ist es für die HTML-Version leider nicht möglich, "normalen"
    LaTeX-Code als Umgebung zu nutzen, um die jeweiligen Ergebnisse zu rendern;
    es können nur die Ausgaben des LaTeX-Mathe-Modus genutzt werden, um Formeln
    innerhalb einer Zeile oder als eigenen Absatz einzubinden.

    Im obigen Beispiel musste ich daher die erstellte PDF-Datei in eine
    PNG-Graphik umwandeln, um diese als normale Abbildung einbinden zu können.
    Ein Screenshot wäre zwar auch möglich gewesen; ich habe mich für eine
    bessere Auflösung jedoch lieber für eine Konvertierung der PDF-Datei in eine
    PNG-Graphik mittels :ref:`Imagemagick <gwl:Imagemagick>` entschieden:

    | ``convert -verbose -density 150 testbrief.pdf -quality 100 -sharpen 0x1.0
      -border 2x2 testbrief.png``

    Hierbei wird eine Auflösung von :math:`\unit[150]{dpi}` festgelegt; die
    Ausgabe-Qualität soll bestmöglich sein (:math:`100\%`), zudem wird durch
    die ``sharpen``-Option ein pixeliges Aussehen des Ergebnisses weitgehend
    vermieden. Mit der Option ``border`` wird schließlich noch ein Rand mit
    jeweils ``2`` Pixeln Abstand erzeugt.

.. [#] Ich habe die Erfahrung gemacht, dass die erste Seite der Briefe oftmals
    schneller beendet wird, als ich dies erwartet hätte (trotz "nur"
    :math:`\unit[2,5]{cm}` unterem Seitenrand); dies liegt wohl daran, dass die
    Briefklasse ``scrlttr2`` auch dann Platz für eine Fußzeile freihält, auch
    wenn ein solcher Inhalt gar nicht angegeben wird. Man kann an dieser Stelle
    mittels der Anweisung ``\enlargethispage{3cm}`` im Verlauf der ersten Seite
    etwas tricksen.

    Beispielsweise sollte bei Briefen, die nur eine Seite lang sein sollen, auch
    das Brief-Ende noch auf dieser Seite stehen; ist keine Fußzeile explizit
    angegeben, so sieht das Layout durch die manuelle Dehnung der Seite mittels
    ``\enlargethispage{}`` auch nicht gequetscht aus. Bei zwei- oder
    mehrseitigen (Geschäfts-)Briefen mit expliziter Fußzeile kann die erste
    Seite hingegen bei Bedarf auch schon früher manuell mittels ``\newpage``
    beendet werden, um ein harmonisches Gesamtbild zu erhalten. 


.. Box um Graphik herum:
.. -shave 1x1 -bordercolor black -border 1

.. convert -verbose -density 150 testbrief.pdf -quality 100 -sharpen 0x1.0  tmp.png && convert tmp.png -quality 100 -border 2x2 testbrief.png

.. http://www.namsu.de/latex/beamer/Thumbnails.html
.. http://www.namsu.de/latex/themes/Goettingen.html
.. https://www.latex-kurs.de/pakete/pakete.html
.. https://www.latex-kurs.de/vorlagen/vorlagen.html
.. http://www.namsu.de/Extra/latex-fehler.html
.. http://www.namsu.de/Extra/pakete/Acronym.html
.. http://www.namsu.de/Extra/latex-pakete.html

