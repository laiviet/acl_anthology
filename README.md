# Compact ACL Anthology bib files for Overleaf

Due to the limit of Overleaf's project file size of 50MB, using the ACL Anthology bib file is not feasible anymore (it is > 60MB).
This simple repo splits the ACL Anthology bib file into smaller files so you can remove unnecessary bibs while preserving the handy of just copying the bib ID from ACL Anthology's website.

## Usage

Step 1: Clone the repo

Step 2: Run the split script

```
python split_acl_anthology.py
```

Step 3: Upload the needed files to a folder ``bibs`` in your Overleaf's project root.

Step 4: Add bib files to the main tex.
```
\bibliography{bibs/anthology.2016.2018,bibs/anthology.2018.2020,bibs/anthology.2020.2022,bibs/anthology.2022.2024,bibs/anthology.2024.2026}
```

## Customization

The bibs are split by year group, you can split it based on your needs.


