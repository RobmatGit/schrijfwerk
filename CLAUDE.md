# Schrijfwerk

Hier leert Claude schrijven zoals Rob. Niet uit een beschrijving van Rob, maar uit zijn stukken en zijn correcties.

## Elke keer
1. Lees `regels/stem.md`, de `regels.md` van de stroom en 2 tot 3 stukken uit `voorbeelden/` van die stroom. Verboden woorden: `../About me/anti-ai-writing-style.md`, sectie 4.
2. Het idee en de mening komen van Rob. Ontbreken ze, vraag ernaar. Vul ze niet zelf in.
3. Schrijf het concept naar `stromen/<stroom>/stukken/<datum>_<onderwerp>/concept.md`. Dat bestand verandert daarna nooit meer.
4. Laat een tweede, verse Claude het concept toetsen met `checker/checker.md`. Rapport naar `check.md` in dezelfde map. Herstel wat de checker vond in een nieuwe versie, toon Rob die plus de punten waar de checker hem nodig heeft.
5. Rob's eindversie gaat naar `definitief.md`. Zijn opmerkingen gaan letterlijk naar `correcties/log.md`.

## Leren
Na elk definitief stuk: `python3 tools/vergelijk.py <map van het stuk>`. Stel per patroon in de edits een regel voor, in Rob's woorden. Pas na zijn ja in `regels/`, met datum en herkomst. Geen regel zonder edit of correctie erachter.

## Klein houden
Hooguit 15 regels in `stem.md`, 10 per stroom. Elk halfjaar opruimen: wat niet meer gecorrigeerd wordt, gaat eruit.

Nooit in deze repo: klantmateriaal, Schuberg Philis-bronnen, persoonsgegevens van derden.
