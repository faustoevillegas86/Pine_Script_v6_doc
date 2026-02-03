#!/usr/bin/env python3
"""
Pine Script V6 - Complete Extraction
Runs URL and content extraction in sequence.

Usage:
    python src/run_all.py
"""

import asyncio
import subprocess
import sys
from pathlib import Path

def main():
    """Run all extraction scripts in order."""
    root = Path(__file__).resolve().parent
    
    print("=" * 60)
    print("PINE SCRIPT V6 - COMPLETE EXTRACTION")
    print("=" * 60)
    
    scripts = [
        ("URL Extraction", root / "extract_urls.py"),
        ("Content Extraction", root / "extract_content.py"),
    ]
    
    for name, script in scripts:
        print(f"\n>>> Running: {name}")
        print("-" * 40)
        
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=root.parent,
            env={**__import__('os').environ, 'PYTHONIOENCODING': 'utf-8'}
        )
        
        if result.returncode != 0:
            print(f"\n[ERROR] {name} failed with code {result.returncode}")
            sys.exit(1)
    
    print("\n" + "=" * 60)
    print("[OK] All extractions complete!")
    print("=" * 60)
    print("\nOutput files:")
    output_dir = root.parent / "output"
    for f in output_dir.glob("*.md"):
        size = f.stat().st_size / 1024
        print(f"  - {f.name} ({size:.1f} KB)")


if __name__ == "__main__":
    main()
