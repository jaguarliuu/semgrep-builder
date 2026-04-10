"""
Custom entry point that calls semgrep_main.main() directly,
avoiding the 'python -m semgrep' deprecation warning.
"""
import sys
import os

# Suppress the deprecation warning about `python -m semgrep`
# Semgrep checks this in its __main__.py
os.environ["SEMGREP_SUPPRESS_SARIF_PROJECT_NAME_CHANGE_WARNING"] = "1"
os.environ["SEMGREP_SKIP_ADHOC_RULES"] = "0"

try:
    from semgrep import semgrep_main
    sys.exit(semgrep_main.main())
except SystemExit as e:
    sys.exit(e.code)
except Exception as e:
    print(f"Failed to start semgrep: {e}", file=sys.stderr)
    sys.exit(1)
