---
title: The importance of file naming in bioinformatics
date: 2025-07-29
tags: [Workflow, Reproducibility, Bash]
summary: File-naming conventions are critical for reproducibility and pipeline stability. Here's how I automated naming checks across a lab's shared drives.
---

If you've spent any time in a wet-dry lab, you've seen this folder:

```
sequencing/
├── final_FINAL_v3.fastq.gz
├── sample1.fq
├── Sample 1 (copy).fastq
├── sample01_2024-Mar.fq.gz
└── ~$temp.fastq
```

Every one of those is a bug waiting to happen. They break globs in your pipeline, they confuse `ls` sorting, they get silently overwritten by the colleague who renames "Sample 1" to "sample1". Most of all, they make it impossible to tell six months later what each file actually is.

## The three rules

The conventions I push in our lab are stolen from Jenny Bryan and adapted for genomics:

1. **Machine-readable** — no spaces, no special characters, lowercase
2. **Human-readable** — descriptive enough that you can guess the content
3. **Sortable** — consistent fields in a consistent order, dates as ISO `YYYY-MM-DD`

Apply those, and your filenames look like:

```
2024-03-15_kp-isolate-007_nanopore-r10_basecalled.fastq.gz
2024-03-15_kp-isolate-007_nanopore-r10_assembly.fasta
```

Now `ls` is sorted by date, glob `*kp-isolate-007*` pulls everything for one sample, and a year from now you can still parse what each token means.

## Automating the check

Reading filenames manually doesn't scale. I wrote a small Bash script that watches a directory, validates new files against a naming pattern, and logs deviations. The full version is on [my GitHub](https://github.com/humphreyaddy/file_naming_watcher) — here's the core idea:

```bash
PATTERN='^[0-9]{4}-[0-9]{2}-[0-9]{2}_[a-z0-9-]+_[a-z0-9-]+\.[a-z.]+$'

for f in "$WATCH_DIR"/*; do
  base=$(basename "$f")
  if [[ ! "$base" =~ $PATTERN ]]; then
    echo "$(date -Iseconds) BAD_NAME $base" >> "$LOG"
  fi
done
```

Run it as a cron job. The log becomes your audit trail when a reviewer asks where `sample1.fq` came from.

## Why it matters

Reproducibility doesn't fail because someone forgot to seed an RNG. It fails because three months later, you can't find the file you analysed. Filenames are the cheapest reproducibility infrastructure you can buy.
