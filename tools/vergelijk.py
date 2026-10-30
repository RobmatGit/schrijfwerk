#!/usr/bin/env python3
"""Vergelijk Claude's concept met Rob's eindversie.

  python3 tools/vergelijk.py stromen/ovhzw/stukken/2026-11-02_onderwerp
      -> telling + alle edits, ook weggeschreven naar edits.md in die map
  python3 tools/vergelijk.py --alles
      -> overzicht van alle stukken + wanneer elke regel voor het laatst een correctie kreeg
"""
import difflib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def woorden(tekst):
    tekst = re.sub(r"^---\n.*?\n---\n", "", tekst, flags=re.S)  # frontmatter eruit
    return tekst.split()


def vergelijk(map_):
    c = (map_ / "concept.md").read_text(encoding="utf-8")
    d = (map_ / "definitief.md").read_text(encoding="utf-8")
    cw, dw = woorden(c), woorden(d)
    sm = difflib.SequenceMatcher(a=cw, b=dw, autojunk=False)
    behouden = sum(b.size for b in sm.get_matching_blocks())
    edits = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        voor = " ".join(cw[max(0, i1 - 6):i1])
        edits.append((op, voor, " ".join(cw[i1:i2]), " ".join(dw[j1:j2])))
    return len(cw), len(dw), behouden, edits


def rapport(map_):
    n_c, n_d, beh, edits = vergelijk(map_)
    pct = 100 * beh / n_c if n_c else 0
    regels = [f"# Edits: {map_.name}", "",
              f"Claude schreef {n_c} woorden. Rob hield er {beh} letterlijk ({pct:.0f}%). Eindversie: {n_d} woorden.",
              f"{len(edits)} edits.", ""]
    soort = {"replace": "vervangen", "delete": "geschrapt", "insert": "toegevoegd"}
    for k, (op, voor, oud, nieuw) in enumerate(edits, 1):
        regels.append(f"## {k}. {soort[op]}")
        regels.append(f"Context: ...{voor}")
        if oud:
            regels.append(f"Claude: {oud}")
        if nieuw:
            regels.append(f"Rob:    {nieuw}")
        regels.append("")
    tekst = "\n".join(regels)
    (map_ / "edits.md").write_text(tekst, encoding="utf-8")
    print(tekst)


def alles():
    print(f"{'stuk':55} {'concept':>8} {'behouden':>9} {'%':>5}")
    for d in sorted(ROOT.glob("stromen/*/stukken/*")):
        if (d / "concept.md").exists() and (d / "definitief.md").exists():
            n_c, _, beh, _ = vergelijk(d)
            naam = f"{d.parent.parent.name}/{d.name}"
            print(f"{naam[:55]:55} {n_c:>8} {beh:>9} {100*beh/max(n_c,1):>4.0f}%")
    log = ROOT / "correcties" / "log.md"
    laatst = {}
    for regel in log.read_text(encoding="utf-8").splitlines():
        delen = [p.strip() for p in regel.split("|")]
        if len(delen) >= 5 and re.match(r"\d{4}-\d{2}", delen[0]):
            for ref in re.findall(r"([\w.-]+(?:\.md)?) #(\d+)", delen[-1]):
                laatst[f"{ref[0]} #{ref[1]}"] = max(laatst.get(f"{ref[0]} #{ref[1]}", ""), delen[0])
    print("\nLaatste correctie per regel (voor het halfjaarlijks opruimen):")
    for k, v in sorted(laatst.items(), key=lambda x: x[1]):
        print(f"  {v:12} {k}")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--alles":
        alles()
    elif len(sys.argv) == 2:
        rapport(Path(sys.argv[1]).resolve())
    else:
        print(__doc__)
