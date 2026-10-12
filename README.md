# agistrategy.app

Source for agistrategy.app. Cloudflare Pages rebuilds the site every time this repository changes.

- `glossary/entries/` has one file per glossary entry. The file name is the entry's web address, so `scheming.md` becomes `agistrategy.app/glossary/#scheming`.
- `glossary/units.txt` lists the course units.
- `templates/glossary.html` controls the look of the glossary.
- `build.py` turns all of the above into the finished site in `public/`. Don't edit `public/` by hand.

## Editing an entry

1. Open the entry's file in `glossary/entries/` on GitHub and click the pencil icon.
2. Edit the text. Keep the bold labels exactly as they are, e.g. `**Definition:**`.
3. Click **Commit changes**. The site updates in about a minute.

The header at the top of each file controls how the entry is listed:

```
---
title: Scheming / deceptive alignment and sleeper agents
short: Scheming
unit: 3
order: 60
aliases: Deceptive alignment; Sleeper agents
---
```

- **title** is the full name, shown on the card and in the reader.
- **short** is the label used in links and on the map.
- **unit** is the course unit the entry belongs to.
- **order** sets the position within the unit, lowest first. Numbers go up by 10, so you can slot a new entry in between, e.g. at 65.
- **aliases** are other names that should find this entry, separated by semicolons. They show up in search and as "Also find" in the A–Z view.

**Related terms** can name an entry by its title, short name, alias, or file name, separated by ` · `.

## Adding an entry

Copy an existing file, give it a new name (lowercase words joined by hyphens), and change its header and text.

## If an update doesn't appear

A typo in a related term or a missing label stops the build, and the live site stays on the last good version. In Cloudflare, open the project's **Deployments** tab and click the failed build. The log names the file and the problem, e.g.:

```
scheming.md: related term "Sandbaging" does not match any entry
```

## Building locally (optional)

```
python3 build.py
```

Then open `public/glossary/index.html`.
