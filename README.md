# File Organizer

A simple Python script that organizes files in a folder (e.g. your Downloads folder) into subfolders based on file type — Images, Documents, Videos, Audio, Archives, Code, Installers, and Others.

## Requirements

- Python 3.8+
- No external dependencies — uses only the standard library (`argparse`, `pathlib`, `shutil`).

## Usage

```bash
python organizer.py [-p PATH] [-r] [-t]
```

### Options

| Flag | Long form      | Description                                                        | Default            |
|------|----------------|---------------------------------------------------------------------|---------------------|
| `-p` | `--path`       | Folder to organize                                                  | `~/Downloads`        |
| `-r` | `--recursive`  | Also organize files inside sub-folders, not just the top level      | Off (top-level only) |
| `-t` | `--test`       | Dry run — print what would be moved without moving anything         | Off                  |

### Examples

Organize your Downloads folder (top-level files only):
```bash
python organizer.py
```

Organize a specific folder, including its subfolders:
```bash
python organizer.py -p ~/Desktop/Messy -r
```

Preview what a run would do, without moving any files:
```bash
python organizer.py -p ~/Downloads -t
```

## How it works

The script scans the target folder and sorts files into these categories based on extension:

| Category   | Extensions |
|------------|------------|
| Images     | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`, `.webp` |
| Documents  | `.pdf`, `.txt`, `.docx`, `.doc`, `.odt`, `.rtf`, `.md` |
| Videos     | `.mp4`, `.mkv`, `.mov`, `.avi` |
| Audio      | `.mp3`, `.wav`, `.flac`, `.aac`, `.m4a` |
| Archives   | `.zip`, `.tar`, `.gz`, `.rar`, `.7z` |
| Code       | `.py`, `.cpp`, `.c`, `.java`, `.js`, `.html`, `.css`, `.json` |
| Installers | `.exe`, `.msi`, `.apk`, `.dmg` |
| Others     | anything not listed above |

If a file with the same name already exists in the destination folder, the script appends a counter (e.g. `photo_1.png`) instead of overwriting it.

By default, only files directly inside the target folder are organized. Use `-r` to also walk into subfolders. Note: the script does not delete or clean up empty subfolders left behind after a recursive run.

## Notes

- Files already inside one of the category folders (e.g. re-running the script on an already-organized `Downloads`) are skipped.
- Use `-t` first if you want to double-check what will happen before committing to a real run, especially the first time you use it on a folder you care about.
