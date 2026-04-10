"""
Custom entry point that calls semgrep's pysemgrep path directly.
"""
import sys
import os

# Fix Windows stdout encoding issues
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

try:
    from semgrep.console_scripts.entrypoint import exec_pysemgrep
    exec_pysemgrep()
except SystemExit as e:
    sys.exit(e.code)
except Exception as e:
    print(f"Failed to start semgrep: {e}", file=sys.stderr)
    sys.exit(1)
