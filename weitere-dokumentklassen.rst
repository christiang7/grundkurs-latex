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
    \fbox{\includegraphics[width=0.80\textwidth]{../../testbrief.pdf}}
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

.. http://www.howtotex.com/general/a-guide-to-building-a-plain-and-simple-latex-cv/
.. http://www.howtotex.com/templates/creating-a-designers-cv-in-latex/

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


