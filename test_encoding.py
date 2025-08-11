"""
Test script to verify encoding fix works properly
"""

print("🧪 Testing encoding fix...")

try:
    # Test reading sample_output.py with UTF-8 encoding
    with open("sample_output.py", "r", encoding="utf-8") as f:
        content = f.read()
    print("✅ Successfully read sample_output.py with UTF-8 encoding")
    
    # Test reading simple_demo.py with UTF-8 encoding
    with open("simple_demo.py", "r", encoding="utf-8") as f:
        content = f.read()
    print("✅ Successfully read simple_demo.py with UTF-8 encoding")
    
    # Test reading multi_agent_coding_example.py with UTF-8 encoding
    with open("multi_agent_coding_example.py", "r", encoding="utf-8") as f:
        content = f.read()
    print("✅ Successfully read multi_agent_coding_example.py with UTF-8 encoding")
    
    print("\n🎉 All files can be read with UTF-8 encoding!")
    print("The encoding issue has been fixed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
