---
title: Microbiome visualisation in R
date: 2025-08-10
tags: [R, Visualisation, Microbiome]
summary: Practical recipes for plotting microbiome data in R — stacked bars that don't lie, ordinations that read at a glance, and tidy taxa wrangling.
---

When you're handed a freshly-processed microbiome dataset, the first thing your collaborators want is *a picture*. The temptation is to crank out a stacked bar of relative abundance and call it a day. Resist that temptation, or at least make the picture say something true.

## The three plots that actually pay rent

Most microbiome papers I read repeat the same trio:

1. A **stacked bar of relative abundance** at some taxonomic rank
2. An **alpha-diversity boxplot** (Shannon, observed features, Faith's PD)
3. A **PCoA / NMDS ordination** with groups colour-coded

Each one fails in a predictable way if you let the defaults win.

## Stacked bars that don't lie

The classic mistake is plotting "top 20 genera" without telling the reader what fraction of the data those 20 represent. If your top-20 only covers 50% of reads, the rest is silently dumped into "Other" — and "Other" looks like a *low-abundance* taxon, when it's actually the dominant one.

Fix it: always sort your "Other" bin to the bottom, label it explicitly, and quote the percentage of total reads it represents in the legend.

```r
top_n <- 15
abund <- ps %>%
  tax_glom(taxrank = "Genus") %>%
  transform_sample_counts(function(x) x / sum(x)) %>%
  psmelt() %>%
  group_by(Sample) %>%
  mutate(rank = rank(-Abundance, ties.method = "first"),
         Genus = ifelse(rank <= top_n, Genus, "Other (low-abundance)"))
```

## Ordinations: pick your distance honestly

Bray-Curtis, weighted UniFrac, Aitchison — they all answer slightly different questions. If your reviewers can't tell which one you used from looking at the figure, your figure is too quiet. Put the distance metric in the axis labels.

## Taxa wrangling

This is the unglamorous bit. Mixing `tidyverse` and `phyloseq` will save your hands. Use `psmelt()` to escape into long-format `dplyr` land for anything beyond the basic plot — joining metadata, filtering by prevalence, computing per-sample relative abundances. Coming back into `phyloseq` after you've changed the data is harder than staying out.

> **Pro tip:** keep one master `phyloseq` object untouched, and create derived tibbles for plotting. Never mutate in place.

That's it. Three plots, three ways to be honest about what's actually there.
