# Pepkio Mendelian Cross Solver

Container image for the Pepkio Mendelian Cross CLI—Punnett squares and offspring ratios for five inheritance modes via the hosted API.

# What It Does

The image runs `pepkio-mendelian-cross-solver`, a client for the Pepkio Mendelian Cross Solver REST API. Submit parent genotypes and a dominance mode; receive filled Punnett grids, genotype and phenotype ratios, walkthrough steps, and warnings.

Typical workflows include genetics homework verification, ABO and X-linked cross modeling, incomplete-dominance and codominance ratio checks, and scripted teaching examples. Calculator logic runs on Pepkio servers; provide a network connection and API key for `run` commands.

# Features

- Five dominance modes: complete, incomplete, codominant, multiple_alleles (ABO only in MVP), sex_linked
- Custom phenotype labels; sex-linked recessive or dominant trait labeling
- Named manifest examples (`complete_monohybrid`, `abo_cross`, `dihybrid_pea`, `sex_linked_hemophilia`, and more)
- Manifest inspection without an API key

# Quick Start

```bash
docker pull pepkio/mendelian-cross-solver:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/mendelian-cross-solver:0.1.0 \
  pepkio-mendelian-cross-solver run --example complete_monohybrid
```

Manifest only (no API key):

```bash
docker run --rm pepkio/mendelian-cross-solver:0.1.0 \
  pepkio-mendelian-cross-solver manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

```bash
docker run --rm -e PEPKIO_API_KEY="$PEPKIO_API_KEY" pepkio/mendelian-cross-solver:0.1.0 \
  pepkio-mendelian-cross-solver run --example abo_cross
```

# Typical Use Cases

- Monohybrid and dihybrid ratio checks in CI or pipeline runners
- ABO blood type crosses without local installs
- X-linked Punnett squares in fixed teaching environments
- Incomplete dominance and codominance homework verification
- Manifest inspection in deployment smoke tests

# Scientific Background

Complete-dominance monohybrid crosses yield a 3:1 phenotype ratio. Incomplete dominance and codominance yield 1:2:1. Dihybrid AaBb × AaBb under independent assortment gives 9:3:3:1. ABO uses multiple alleles; sex-linked crosses use X-chromosome notation with female Parent 1 and male Parent 2.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/mendelian-cross-solver

The web UI adds a live Punnett grid, 28 curated textbook presets, collapsible walkthroughs, PNG/SVG export, copy-grid-as-table, shareable permalinks, and print-friendly display.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-mendelian-cross-solver

Web Application: https://www.pepkio.com/tools/mendelian-cross-solver

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).
