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
            with open("multi_agent_coding_example.py", "r", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            print("❌ multi_agent_coding_example.py not found")
        except Exception as e:
            print(f"❌ Error running example: {e}")
            print("🎯 Running simple demo instead...")
            try:
                with open("simple_demo.py", "r", encoding="utf-8") as f:
                    exec(f.read())
            except Exception as demo_error:
                print(f"❌ Error running simple demo: {demo_error}")
                show_demo_description()
    else:
        print("Running simple demo (no API key required)...")
        try:
            with open("simple_demo.py", "r", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            print("❌ simple_demo.py not found")
        except Exception as e:
            print(f"❌ Error running simple demo: {e}")
            show_demo_description()

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
                with open("sample_output.py", "r", encoding="utf-8") as f:
                    exec(f.read())
            except FileNotFoundError:
                print("❌ sample_output.py not found")
            except Exception as e:
                print(f"❌ Error running sample output: {e}")
                show_sample_description()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")

def show_demo_description():
    """Show demo description when the actual demo can't run."""
    print("\n🚀 AutoGen Multi-Agent Coding Demo")
    print("=" * 50)
    
    print("👥 Agents Overview:")
    print("🧠 CodeAssistant - Python code generator")
    print("   - Generates clean, efficient Python code")
    print("   - Follows PEP 8 style guidelines")
    print("   - Includes proper error handling and type hints")
    print()
    
    print("🧐 CriticAgent - Code reviewer") 
    print("   - Reviews code for bugs and security issues")
    print("   - Suggests improvements for code quality")
    print("   - Ensures best practices adherence")
    print()
    
    print("🧪 TestAgent - Test writer")
    print("   - Writes comprehensive unit tests using pytest")
    print("   - Creates test cases for normal and edge scenarios")
    print("   - Ensures high test coverage")
    print()
    
    print("🙋 UserProxyAgent - Workflow manager")
    print("   - Initiates coding tasks")
    print("   - Coordinates between agents")
    print("   - Executes code when needed")
    print()
    
    print("📝 Example Workflow:")
    print("1. UserProxy presents a coding task")
    print("2. CodeAssistant generates initial implementation")
    print("3. CriticAgent reviews and suggests improvements")
    print("4. CodeAssistant refines the code")
    print("5. TestAgent writes comprehensive tests")
    print("6. UserProxy validates the final solution")

def show_sample_description():
    """Show sample output description when the actual sample can't run."""
    print("\n🏦 Sample BankAccount Implementation")
    print("=" * 50)
    
    print("📋 What the agents would collaboratively produce:")
    print()
    print("🧠 CodeAssistant generated:")
    print("   - Complete BankAccount class with proper structure")
    print("   - Comprehensive error handling and validation")
    print("   - Transaction logging with timestamps")
    print()
    
    print("🧐 CriticAgent suggested improvements:")
    print("   - Use Decimal for precise monetary calculations")
    print("   - Add proper exception classes")
    print("   - Include transaction rollback for failed transfers")
    print()
    
    print("🧪 TestAgent created:")
    print("   - 25+ comprehensive test cases")
    print("   - Coverage for normal operations, edge cases, and errors")
    print("   - Proper test fixtures and organization")

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
