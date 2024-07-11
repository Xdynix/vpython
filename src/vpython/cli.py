import subprocess
import sys
from pathlib import Path

VENV_NAMES = [
    "venv",
    ".venv",
]
IS_WIN = sys.platform == "win32"
BIN = "Scripts" if IS_WIN else "bin"


def main():
    """Run `python` in virtualenv."""
    python = Path(sys.executable)
    target = Path(sys.argv[1]).resolve()
    root = target.parent
    executable = next(
        (
            path
            for venv in VENV_NAMES
            if (path := root / venv / BIN / python.name).is_file()
        ),
        python,
    )
    subprocess.run(  # noqa: S603
        [executable, target, *sys.argv[2:]],
        check=True,
        cwd=root,
    )


if __name__ == "__main__":
    main()
