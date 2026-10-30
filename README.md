# Schrijfwerk

Claude schrijft concepten, een tweede Claude toetst ze, Rob corrigeert. Elke correctie kan een regel worden. Naar het idee van Ruben Hassid (How to AI, 27 okt 2026), ingepast in Cowork.

```
  Rob: idee + mening
          |
          v
  Claude 1 schrijft  ----------->  concept.md   (blijft ongewijzigd)
          |
          v
  Claude 2 toetst aan regels --->  check.md
          |
          v
  Rob herschrijft  ------------->  definitief.md
          |
          v
  tools/vergelijk.py  ---------->  edits.md     ("Rob hield 22% letterlijk")
          |
          v
  Claude stelt regel voor, Rob zegt ja  -->  regels/  +  correcties/log.md
          |
          '--> volgende concept begint met die regel
```

## Wat waar staat

| Map | Inhoud |
|---|---|
| `CLAUDE.md` | De werkwijze, ~200 woorden. Claude leest dit elke keer. |
| `regels/stem.md` | Regels voor alle stromen. Hooguit 15. |
| `stromen/<stroom>/regels.md` | Regels per stroom. Hooguit 10. |
| `stromen/<stroom>/voorbeelden/` | Verstuurde stukken. Hieruit leert Claude je stem. |
| `stromen/<stroom>/stukken/` | Per stuk: concept, check, definitief, edits. |
| `correcties/log.md` | Je correcties, letterlijk. |
| `checker/checker.md` | Opdracht voor de tweede Claude. |
| `tools/` | Vergelijken, bewaren op GitHub. |

Stromen: `linkedin-contractadvies`, `wijngaard-nieuwsbrief`, `ovhzw`. Nieuwe stroom = nieuwe map met `regels.md` en `voorbeelden/`.

## Wat je zegt in Cowork

- **"Schrijf een LinkedIn-post over ..."** en je mening erbij. Claude schrijft, laat checken, toont het resultaat.
- **"Dit is de definitieve versie"** (plak of wijs het bestand aan). Claude vergelijkt en stelt regels voor.
- **"Ruim de regels op"**, elk halfjaar.

GitHub open je niet. De map gaat elk uur vanzelf naar je privé repo `schrijfwerk`.

## Eenmalig

In Terminal op de Mac:
```
bash ~/"Claude Cowork/Schrijfwerk/tools/setup-github.sh"
```
Daarna in elke stroom een paar verstuurde stukken in `voorbeelden/` zetten.
