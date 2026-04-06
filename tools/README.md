# Tools

## repo_safety_check.py
This helper script scans the repository for files and content that may be unsafe or inappropriate for a public cybersecurity portfolio repository.

### What it checks
- blocked file extensions such as `.pst`, `.ost`, `.eml`, `.msg`, `.exe`
- suspicious filenames such as `.env` or `credentials.txt`
- simple content markers that may suggest secrets or tokens

### How to run
From the repository root:

```bash
python tools/repo_safety_check.py