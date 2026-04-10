"""
Build script to package Semgrep as a single Windows .exe using PyInstaller.
"""
import semgrep.__main__
import os
import subprocess
import sys


def main():
    entry = os.path.dirname(semgrep.__main__.__file__)
    main_py = os.path.join(entry, "__main__.py")
    print(f"Entry point: {main_py}")

    hidden_imports = [
        "semgrep",
        "semgrep.cli",
        "semgrep.cli.cmds",
        "semgrep.rule",
        "semgrep.rule_match",
        "semgrep.engine",
        "semgrep.target_manager",
        "semgrep.constants",
        "semgrep.error",
        "semgrep.git",
        "semgrep.pattern",
        "semgrep.pmatch",
        "semgrep.profiling",
        "semgrep.rule_board",
        "semgrep.semgrep_main",
        "semgrep.skip_list",
        "semgrep.timeout",
        "semgrep.version",
    ]

    # Build command - use pyinstaller binary directly
    cmd = ["pyinstaller", "--onefile", "--console", "--name", "semgrep",
           "--distpath", "dist", "--workpath", "build"]

    for mod in hidden_imports:
        cmd += ["--hidden-import", mod]

    cmd += ["--collect-all", "semgrep", "entry.py"]

    print(f"Running pyinstaller...")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
