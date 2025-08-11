"""
Quick Start Script for AutoGen Multi-Agent Example

This script helps you get started quickly with the AutoGen multi-agent coding example.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def check_dependencies():
    """Check if required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    missing_deps = []
    
    try:
        import autogen
        print("✅ autogen - installed")
    except ImportError:
        missing_deps.append("pyautogen")
        print("❌ autogen - not installed")
    
    try:
        import openai
        print("✅ openai - installed")
    except ImportError:
        missing_deps.append("openai")
        print("❌ openai - not installed")
    
    try:
        import pytest
        print("✅ pytest - installed")
    except ImportError:
        missing_deps.append("pytest")
        print("❌ pytest - not installed")
    
    return missing_deps

def check_api_key():
    """Check if OpenAI API key is configured."""
    print("\n🔑 Checking API key configuration...")
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        print("✅ OPENAI_API_KEY environment variable is set")
        return True
    else:
        print("❌ OPENAI_API_KEY environment variable not found")
        return False

def show_setup_instructions():
    """Show setup instructions for missing dependencies or API key."""
    print("\n📋 Setup Instructions:")
    print("=" * 40)
    
    missing_deps = check_dependencies()
    has_api_key = check_api_key()
    
    if missing_deps:
        print(f"\n1. Install missing dependencies:")
        print(f"   pip install {' '.join(missing_deps)}")
        print(f"   Or run: pip install -r requirements.txt")
    
    if not has_api_key:
        print(f"\n2. Set up your OpenAI API key:")
        print(f"   Windows: set OPENAI_API_KEY=your_api_key_here")
        print(f"   Or create .env file with: OPENAI_API_KEY=your_api_key_here")
    
    if not missing_deps and has_api_key:
        print("✅ All dependencies and configuration ready!")
        return True
    
    return False

def run_demo():
    """Run the appropriate demo based on setup status."""
    print("\n🚀 Starting AutoGen Demo...")
    print("=" * 40)
    
    if check_api_key():
        print("Running full multi-agent example...")
        try:
            exec(open("multi_agent_coding_example.py").read())
        except FileNotFoundError:
            print("❌ multi_agent_coding_example.py not found")
        except Exception as e:
            print(f"❌ Error running example: {e}")
            print("🎯 Running simple demo instead...")
            exec(open("simple_demo.py").read())
    else:
        print("Running simple demo (no API key required)...")
        try:
            exec(open("simple_demo.py").read())
        except FileNotFoundError:
            print("❌ simple_demo.py not found")

def run_tests():
    """Run the test suite if pytest is available."""
    print("\n🧪 Running Test Suite...")
    print("=" * 40)
    
    try:
        import pytest
        import subprocess
        result = subprocess.run([sys.executable, "-m", "pytest", "test_bank_account.py", "-v"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except ImportError:
        print("❌ pytest not installed. Install with: pip install pytest")
    except FileNotFoundError:
        print("❌ test_bank_account.py not found")

def show_menu():
    """Show interactive menu for different options."""
    print("\n🎯 AutoGen Multi-Agent Coding Example")
    print("=" * 50)
    print("1. Check setup and dependencies")
    print("2. Run demo")
    print("3. Run test suite")
    print("4. Show sample output")
    print("5. Exit")
    print("=" * 50)
    
    while True:
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            show_setup_instructions()
        elif choice == "2":
            run_demo()
        elif choice == "3":
            run_tests()
        elif choice == "4":
            try:
                exec(open("sample_output.py").read())
            except FileNotFoundError:
                print("❌ sample_output.py not found")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")

def main():
    """Main function to run the quick start script."""
    print("🚀 AutoGen Multi-Agent Quick Start")
    print("=" * 50)
    
    # Check if we're in the right directory
    current_dir = Path.cwd()
    required_files = ["multi_agent_coding_example.py", "simple_demo.py", "requirements.txt"]
    
    missing_files = [f for f in required_files if not (current_dir / f).exists()]
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        print("Please run this script from the autogen project directory.")
        return
    
    # Show interactive menu
    show_menu()

if __name__ == "__main__":
    main()
