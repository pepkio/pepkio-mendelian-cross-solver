# Pepkio Mendelian Cross Solver

Build Punnett squares for complete, incomplete, codominant, sex-linked, and ABO crosses with genotype and phenotype ratios, step-by-step walkthroughs, and exportable grids—via browser or Python API.

# Overview

Genetics coursework and teaching labs routinely require Punnett squares for monohybrid and dihybrid crosses, incomplete dominance, codominance, ABO blood types, and X-linked traits. Hand-drawing grids for each problem is slow and error-prone, especially when dominance relationships differ between traits or when sex-linked notation (X^A, X^a, Y) is required. Many free online calculators handle only simple complete-dominance monohybrid crosses and omit non-Mendelian modes, step-by-step explanations, or export for slides and worksheets.

The Pepkio Mendelian Cross Solver (tool ID: `mendelian-cross-solver`) builds Punnett squares for five inheritance modes: complete dominance, incomplete dominance, codominance, multiple alleles (ABO blood types in MVP), and sex-linked traits. Enter parent genotypes or load a textbook preset; the engine returns a filled grid, genotype and phenotype ratios, a step-by-step walkthrough (gamete formation, grid fill, ratio derivation), and warnings when applicable. This repository provides a Python client and CLI for the same calculation engine used by the hosted [Mendelian Cross Solver](https://www.pepkio.com/tools/mendelian-cross-solver) web application.

Researchers and students use Punnett square calculators for introductory genetics problem sets, ABO and blood-type crosses, X-linked recessive and dominant trait modeling, incomplete-dominance flower-color examples, dihybrid 9:3:3:1 ratio exercises, and preparing lecture slides and worksheets. Alternative search terms include Punnett square generator, Mendelian cross calculator, monohybrid cross, dihybrid cross, incomplete dominance Punnett square, codominance calculator, ABO blood type cross, X-linked inheritance Punnett square, sex-linked trait cross, and genetics homework checker.

# Features

- **Five dominance modes:** `complete`, `incomplete`, `codominant`, `multiple_alleles` (ABO only in MVP), and `sex_linked`
- **Parent genotypes:** Enter genotypes for both parents; sex-linked mode uses Parent 1 as female and Parent 2 as male with X^A / X^a / Y notation
- **Custom phenotype labels:** Optional `custom_phenotypes` for dominant, recessive, and heterozygous names
- **Allele symbols and hierarchy:** `allele_symbols` for superscript complete-dominance crosses; `allele_hierarchy` for ABO dominance order (I^A, I^B, i)
- **Sex-linked trait mode:** `sex_linked_trait` of `recessive` (default) or `dominant` controls carrier-female labeling
- **Preset library:** Optional `preset_id` for curated textbook examples (web UI offers 28 curated textbook presets)
- **Structured output:** `can_compute`, `grid`, `genotype_ratios`, `phenotype_ratios`, `walkthrough`, `warnings`, and `error`
- **Manifest examples:** `complete_monohybrid`, `incomplete_snapdragon`, `abo_cross`, `sex_linked_hemophilia`, `codominant_roan`, `dihybrid_pea`, `sex_linked_dominant`
- **Python API and CLI:** `PepkioClient`, `get_manifest`, `list_examples`, `get_example_input`, `run`
- **Shareable runs:** API returns `permalink` URLs for each completed run

The hosted web version adds a live Punnett grid that updates as you type, genotype and phenotype labels in each cell, reduced ratios with visual proportion bars, collapsible step-by-step walkthroughs, 28 curated textbook presets (hemophilia, sickle cell, snapdragon flower color, and others), custom phenotype names, PNG and SVG download for slides and worksheets, copy-grid-as-table, shareable links that restore the exact cross, print-friendly toggle, color-coded grids, and recent-cross browser history. No account or install is required for the browser calculator.

# Common Use Cases

- **Introductory genetics problem sets:** Verify monohybrid crosses such as Aa × Aa (manifest example `complete_monohybrid`, phenotype ratio 3:1)
- **Incomplete dominance:** Model snapdragon flower color Rr × Rr (`incomplete_snapdragon`, phenotype ratio 1:2:1)
- **Codominance:** Model roan cattle R^R R^W × R^R R^W (`codominant_roan`, phenotype ratio 1:2:1)
- **ABO blood types:** Cross I^A i × I^B i (`abo_cross`, phenotype ratio 1:1:1:1); multiple-allele mode supports ABO blood types only in MVP
- **X-linked recessive traits:** Hemophilia carrier female × unaffected male (`sex_linked_hemophilia`, X^H X^h × X^H Y)
- **X-linked dominant traits:** Affected heterozygous female × unaffected male (`sex_linked_dominant`, X^D X^d × X^d Y)
- **Dihybrid Mendelian crosses:** Pea plant AaBb × AaBb (`dihybrid_pea`, phenotype ratio 9:3:3:1)
- **Teaching materials:** Export print-ready Punnett squares as PNG or SVG for lecture slides and worksheets via the web application
- **Scripted workflows:** Re-run crosses from notebooks, teaching scripts, or CI via the Python client

# Why This Tool Exists

Spreadsheets can tally offspring ratios manually but lack gamete enumeration, non-Mendelian dominance modes, sex-linked notation, and step-by-step walkthroughs in one workflow. Omni Calculator and punnettsquare.org handle simple dominant/recessive crosses but not incomplete dominance, codominance, or ABO typing in one place; most skip step-by-step explanations and offer no PNG or SVG export. Bifido Pro covers non-Mendelian modes but requires Windows and manual trait-file setup.

Mendelian Cross Solver combines five inheritance modes, collapsible gamete-to-ratio walkthroughs, color-coded grids, and one-click PNG, SVG, table, or share-link export in the browser—free, with no install or account. The Python client runs the same engine from scripts or pipelines via the Pepkio Tools REST API.

# Installation

```bash
pip install pepkio-mendelian-cross-solver
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add pepkio-mendelian-cross-solver
```

Programmatic runs require a Pepkio API key with **tools:run** scope. Create one at [https://www.pepkio.com/account/api-keys](https://www.pepkio.com/account/api-keys).

```bash
export PEPKIO_API_KEY="your-key"
```

| Variable | Description |
|----------|-------------|
| `PEPKIO_API_KEY` | Production API key |
| `LOCAL_PEPKIO_API_KEY` | Local dev key when base URL points to `tools.localtest.me` |
| `PEPKIO_API_BASE_URL` | Override API host (default: `https://tools.pepkio.com`) |
| `PEPKIO_SSL_VERIFY` | Set to `0`/`false` to disable TLS verify (auto-off for localtest.me) |

Manifest inspection does not require an API key.

# Quick Start

### Python

```python
from pepkio_mendelian_cross_solver import PepkioClient

with PepkioClient() as client:
    inp = client.get_example_input("complete_monohybrid")
    result = client.run(inp)
    print(result.status, result.permalink)
    ratios = result.result["phenotype_ratios"]
    print("phenotype ratio:", ratios["ratio"])
    grid = result.result["grid"]
    print(f"grid cells: {len(grid)}")
```

### CLI

```bash
# Manifest (no API key)
pepkio-mendelian-cross-solver manifest
pepkio-mendelian-cross-solver manifest --examples

# Run a named example (API key required)
pepkio-mendelian-cross-solver run --example complete_monohybrid
pepkio-mendelian-cross-solver run --example abo_cross
pepkio-mendelian-cross-solver run --example dihybrid_pea

# Run custom JSON input
pepkio-mendelian-cross-solver run --input-json '{"dominance_mode":"complete","parent1_genotype":"Aa","parent2_genotype":"Aa"}'
```

Options: `--api-key`, `--base-url`, `--label`, `--idempotency-key`.

# Example Output

Running the `complete_monohybrid` manifest example against the production API returns a completed run with `can_compute: true`, a non-empty `grid` array, and `phenotype_ratios.ratio` of `"3:1"`. Representative structure:

```json
{
  "run_id": "<uuid>",
  "status": "completed",
  "result": {
    "can_compute": true,
    "grid": ["..."],
    "genotype_ratios": {},
    "phenotype_ratios": {
      "ratio": "3:1"
    },
    "walkthrough": ["..."],
    "warnings": []
  },
  "permalink": "https://tools.pepkio.com/r/<uuid>"
}
```

Verified phenotype ratios from manifest examples:

| Example | Dominance mode | Phenotype ratio |
|---------|----------------|-----------------|
| `complete_monohybrid` | complete | 3:1 |
| `incomplete_snapdragon` | incomplete | 1:2:1 |
| `codominant_roan` | codominant | 1:2:1 |
| `abo_cross` | multiple_alleles | 1:1:1:1 |
| `dihybrid_pea` | complete | 9:3:3:1 |

Sex-linked examples (`sex_linked_hemophilia`, `sex_linked_dominant`) return `can_compute: true` with a populated `grid`.

# Scientific Background

**Complete dominance.** For a monohybrid cross Aa × Aa, gametes are A and a from each parent; offspring genotypes are AA, Aa, Aa, and aa in a 1:2:1 genotype ratio and a 3:1 phenotype ratio when A is dominant over a.

**Incomplete dominance.** Heterozygotes express an intermediate phenotype. For Rr × Rr (e.g. snapdragon flower color), genotype ratio is 1:2:1 and phenotype ratio is 1:2:1 (red : pink : white when custom labels are set).

**Codominance.** Both alleles are fully expressed in heterozygotes. Roan cattle R^R R^W × R^R R^W yields a 1:2:1 phenotype ratio (red : roan : white).

**Multiple alleles (ABO).** ABO blood types use alleles I^A, I^B, and i with codominance between I^A and I^B. Cross I^A i × I^B i yields offspring phenotypes A, B, AB, and O in a 1:1:1:1 ratio. Multiple-allele mode supports ABO blood types only in MVP.

**Sex-linked inheritance.** X-linked traits use X-chromosome notation. Parent 1 is female (e.g. X^H X^h) and Parent 2 is male (e.g. X^H Y). Recessive X-linked traits (default `sex_linked_trait`) label carrier females; dominant X-linked traits use `sex_linked_trait: dominant`.

**Dihybrid crosses.** For AaBb × AaBb under complete dominance with independently assorting genes, the classic phenotype ratio is 9:3:3:1.

**Terminology.** Researchers search for Punnett square, Mendelian inheritance, monohybrid cross, dihybrid cross, incomplete dominance, codominance, ABO blood type genetics, X-linked inheritance, hemophilia Punnett square, and genetics ratio calculator—these workflows are what Mendelian Cross Solver addresses.

# Frequently Asked Questions

**What is a Punnett square?**
A Punnett square is a grid used to predict offspring genotypes and phenotypes from parental gametes. Rows and columns represent gametes from each parent; each cell shows a possible offspring genotype.

**How do I cross Aa × Aa?**
Set `dominance_mode` to `complete`, `parent1_genotype` to `Aa`, and `parent2_genotype` to `Aa`. Run manifest example `complete_monohybrid` for a verified 3:1 phenotype ratio.

**What is the difference between incomplete dominance and codominance?**
Incomplete dominance produces a blended intermediate phenotype in heterozygotes (e.g. pink snapdragon flowers). Codominance expresses both alleles distinctly in heterozygotes (e.g. roan coat color). This tool supports both modes via `incomplete` and `codominant` dominance settings.

**How do I model ABO blood type crosses?**
Set `dominance_mode` to `multiple_alleles` and enter genotypes using I^A, I^B, and i alleles. Example: I^A i × I^B i (`abo_cross`) yields a 1:1:1:1 phenotype ratio (types A, B, AB, O). Multiple-allele mode supports ABO blood types only in MVP.

**How do I set up an X-linked Punnett square?**
Set `dominance_mode` to `sex_linked`. Parent 1 is the female (e.g. X^H X^h) and Parent 2 is the male (e.g. X^H Y). Use `sex_linked_trait` of `recessive` (default) or `dominant` to control carrier-female labeling. See examples `sex_linked_hemophilia` and `sex_linked_dominant`.

**What is a carrier female in X-linked recessive inheritance?**
A female heterozygous for a recessive X-linked allele (e.g. X^H X^h for hemophilia) carries one mutant allele but may not show the recessive phenotype. The tool labels carrier females when `sex_linked_trait` is `recessive`.

**What phenotype ratio does a dihybrid cross give?**
For AaBb × AaBb under complete dominance with independent assortment, the classic ratio is 9:3:3:1. Run manifest example `dihybrid_pea` to reproduce.

**What dominance modes does the tool support?**
Five modes: `complete`, `incomplete`, `codominant`, `multiple_alleles` (ABO only in MVP), and `sex_linked`.

**Can I customize phenotype names?**
Yes. Pass `custom_phenotypes` with `dominant`, `recessive`, and optionally `heterozygous` labels. The snapdragon example uses Red, White, and Pink.

**What is preset_id?**
An optional input referencing a curated textbook preset from the preset library. The web application offers 28 curated textbook presets; the API manifest lists seven named runnable examples.

**What does the walkthrough contain?**
The `walkthrough` array in API output documents gamete formation, grid fill, and ratio derivation step by step. The web application presents this as a collapsible step-by-step section.

**How do I export a Punnett square for a slide?**
The web application at [https://www.pepkio.com/tools/mendelian-cross-solver](https://www.pepkio.com/tools/mendelian-cross-solver) supports PNG and SVG download, copy-grid-as-table, and a print-friendly toggle. The Python API returns structured JSON including the `grid` array.

**Can I share a cross with a student?**
The web application generates shareable links that restore the exact cross. API runs return a `permalink` URL for each completed run.

**Does the Python client work offline?**
No. Punnett square arithmetic runs on Pepkio servers via the REST API. A network connection and API key are required for `run()`. Manifest fetch works without a key.

**What manifest examples are available?**
`complete_monohybrid`, `incomplete_snapdragon`, `abo_cross`, `sex_linked_hemophilia`, `codominant_roan`, `dihybrid_pea`, and `sex_linked_dominant`.

**How does this compare to punnettsquare.org?**
The Pepkio tool page notes that punnettsquare.org handles simple dominant/recessive crosses but not incomplete dominance, codominance, or ABO typing in one place, and most such tools skip step-by-step explanations and PNG/SVG export.

**What notation is used for sex-linked alleles?**
Sex-linked crosses use X^A / X^a / Y notation with Parent 1 as female and Parent 2 as male, per the tool manifest `agent_notes`.

**What warnings can the tool return?**
The `warnings` array in output lists non-blocking issues. Blocking problems appear in the `error` field and set `can_compute` to false when applicable.

# Web Application

For researchers who prefer a graphical interface, an interactive [Mendelian Cross Solver](https://www.pepkio.com/tools/mendelian-cross-solver) (Punnett Square Generator) is available in the browser.

The web version provides five inheritance modes (complete, incomplete, codominant, multiple alleles for ABO, and sex-linked), a live Punnett grid with genotype and phenotype labels, reduced ratios with visual proportion bars, 28 curated textbook presets, collapsible gamete-to-ratio walkthroughs, custom phenotype names, color-coded grids with a print-friendly toggle, PNG and SVG export, copy-grid-as-table, shareable permalinks, and recent-cross browser history. No account or install is required.

Use the [web tool](https://www.pepkio.com/tools/mendelian-cross-solver) for interactive grids and export; use this Python package for scripted crosses, teaching automation, or pipeline integration.

# Related Resources

GitHub Repository: [https://github.com/pepkio/pepkio-mendelian-cross-solver](https://github.com/pepkio/pepkio-mendelian-cross-solver)

PyPI Package: [https://pypi.org/project/pepkio-mendelian-cross-solver/](https://pypi.org/project/pepkio-mendelian-cross-solver/)

Web Application: [https://www.pepkio.com/tools/mendelian-cross-solver](https://www.pepkio.com/tools/mendelian-cross-solver)

# About Pepkio

[Pepkio](https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and [analysis services](https://www.pepkio.com/cro). Explore additional calculators on the Pepkio website.

# License

No license file is present in this repository at the time of writing.

# Keywords

Punnett square, Punnett square generator, Mendelian cross solver, Mendelian inheritance calculator, monohybrid cross, dihybrid cross, genetics ratio calculator, complete dominance Punnett square, incomplete dominance calculator, codominance Punnett square, ABO blood type cross, blood type genetics calculator, X-linked inheritance, sex-linked Punnett square, hemophilia Punnett square, carrier female genetics, snapdragon incomplete dominance, roan cattle codominance, dihybrid 9:3:3:1 ratio, pea plant genetics cross, genetics homework checker, Punnett square online, Mendelian genetics tool, genotype phenotype ratio, gamete formation walkthrough, Punnett grid export PNG, Punnett square SVG download, genetics teaching tool, introductory genetics problem set, pepkio-mendelian-cross-solver, Python Punnett square API, REST API genetics calculator, Punnett square step by step, multiple allele inheritance, ABO I^A I^B i cross, sex-linked recessive trait, sex-linked dominant trait, Punnett square for lecture slides, shareable genetics cross link, genetics worksheet generator, Mendelian cross ratios, phenotype ratio 3:1, phenotype ratio 1:2:1, how to build a Punnett square for Aa x Aa, calculate offspring ratio incomplete dominance Rr x Rr, ABO blood type Punnett square I^A i x I^B i, X-linked hemophilia carrier female cross, dihybrid cross AaBb x AaBb expected ratio, export Punnett square for PowerPoint slide, check genetics homework Punnett square online, Punnett square with custom phenotype labels, codominance roan cattle offspring ratio, genetics problem set monohybrid and dihybrid, model X-linked trait with standard notation, Punnett square without hand drawing grid, automate genetics teaching examples Python API, compare incomplete dominance vs codominance Punnett square, blood type cross calculator for classroom, share exact Punnett square with students via link, five inheritance modes one calculator, textbook preset hemophilia sickle cell snapdragon, Punnett square browser no install required, Mendelian cross API client for notebooks
