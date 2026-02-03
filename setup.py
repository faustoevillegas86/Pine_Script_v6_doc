#!/usr/bin/env python3
"""
Pine Script V6 - Setup Script
Installs all required dependencies.

Usage:
    python setup.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Install all dependencies."""
    print("=" * 60)
    print("PINE SCRIPT V6 - SETUP")
    print("=" * 60)
    
    root = Path(__file__).resolve().parent
    requirements = root / "requirements.txt"
    
    # Step 1: Install Python dependencies
    print("\n>>> Installing Python dependencies...")
    print("-" * 40)
    
    result = subprocess.run([
        sys.executable, "-m", "pip", "install", "-r", str(requirements)
    ])
    
    if result.returncode != 0:
        print("\n[ERROR] Failed to install Python dependencies")
        sys.exit(1)
    
    print("\n[OK] Python dependencies installed")
    
    # Step 2: Install Playwright browsers
    print("\n>>> Installing Playwright browsers...")
    print("-" * 40)
    
    result = subprocess.run([
        sys.executable, "-m", "playwright", "install", "chromium"
    ])
    
    if result.returncode != 0:
        print("\n[WARNING] Failed to install Playwright browsers")
        print("You may need to run: playwright install chromium")
    else:
        print("\n[OK] Playwright browsers installed")
    
    print("\n" + "=" * 60)
    print("[OK] Setup complete!")
    print("=" * 60)
    print("\nTo extract documentation, run:")
    print("  python src/run_all.py")


if __name__ == "__main__":
    main()
