"""
Build script to package Semgrep as a single Windows .exe using PyInstaller.
Run: python build.py
"""
import semgrep.__main__
import os
import subprocess
import sys


def main():
    entry = os.path.dirname(semgrep.__main__.__file__)
    main_py = os.path.join(entry, "__main__.py")
    print(f"Entry point: {main_py}")

    # All semgrep modules to include
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

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console",
        "--name", "semgrep",
        "--distpath", "dist",
        "--workpath", "build",
        "--add-hidden-import", "semgrep",
    ]

    # Add individual hidden imports
    for mod in hidden_imports:
        cmd += ["--add-hidden-import", mod]

    # Collect all data from semgrep
    cmd += ["--collect-all", "semgrep"]

    # Add the entry point
    cmd.append(main_py)

    print(f"Running: {' '.join(cmd[:10])} ...")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
