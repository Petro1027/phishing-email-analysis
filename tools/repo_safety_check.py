from pathlib import Path

# Repository root = one level above /tools
REPO_ROOT = Path(__file__).resolve().parent.parent

IGNORED_DIRS = {
    ".git",
    ".idea",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
}

# File extensions that should usually NOT be uploaded to this public portfolio repo
BLOCKED_EXTENSIONS = {
    ".pst",
    ".ost",
    ".eml",
    ".msg",
    ".zip",
    ".7z",
    ".rar",
    ".exe",
    ".dll",
    ".bat",
    ".cmd",
    ".scr",
    ".js",
    ".vbs",
}

# Filenames that commonly contain secrets or local-only config
SUSPICIOUS_FILENAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "secrets.txt",
    "credentials.txt",
    "tokens.txt",
    "passwords.txt",
}

# Optional content indicators to warn about
SUSPICIOUS_CONTENT_MARKERS = [
    "api_key",
    "apikey",
    "secret",
    "password=",
    "authorization:",
    "bearer ",
    "private key",
]

TEXT_EXTENSIONS_TO_SCAN = {
    ".md",
    ".txt",
    ".py",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def scan_files():
    blocked_files = []
    suspicious_name_files = []
    suspicious_content_files = []

    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue

        if should_skip(path):
            continue

        relative_path = path.relative_to(REPO_ROOT)

        if path.suffix.lower() in BLOCKED_EXTENSIONS:
            blocked_files.append(relative_path)

        if path.name.lower() in SUSPICIOUS_FILENAMES:
            suspicious_name_files.append(relative_path)

        if path.suffix.lower() in TEXT_EXTENSIONS_TO_SCAN:
            try:
                content = path.read_text(encoding="utf-8", errors="ignore").lower()
            except Exception:
                continue

            for marker in SUSPICIOUS_CONTENT_MARKERS:
                if marker in content:
                    suspicious_content_files.append((relative_path, marker))
                    break

    return blocked_files, suspicious_name_files, suspicious_content_files


def print_section(title: str):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    print(f"Scanning repository: {REPO_ROOT}")

    blocked_files, suspicious_name_files, suspicious_content_files = scan_files()

    print_section("Blocked extension files")
    if blocked_files:
        for file_path in blocked_files:
            print(f"[WARNING] {file_path}")
    else:
        print("No blocked-extension files found.")

    print_section("Suspicious filenames")
    if suspicious_name_files:
        for file_path in suspicious_name_files:
            print(f"[WARNING] {file_path}")
    else:
        print("No suspicious filenames found.")

    print_section("Suspicious content markers")
    if suspicious_content_files:
        for file_path, marker in suspicious_content_files:
            print(f"[WARNING] {file_path} -> contains marker: {marker}")
    else:
        print("No suspicious content markers found.")

    print_section("Final result")
    total_issues = (
        len(blocked_files)
        + len(suspicious_name_files)
        + len(suspicious_content_files)
    )

    if total_issues == 0:
        print("Repository safety check passed.")
    else:
        print(f"Repository safety check finished with {total_issues} warning(s).")
        print("Review flagged files before pushing to GitHub.")


if __name__ == "__main__":
    main()