"""
AutoGen Multi-Agent Coding Example

This example demonstrates a collaborative coding workflow with four specialized agents:
🧠 CodeAssistant - Generates Python code
🧐 CriticAgent - Reviews and suggests improvements  
🧪 TestAgent - Writes tests to validate the code
🙋 UserProxyAgent - Initiates tasks and manages the workflow

Dependencies:
pip install pyautogen openai
"""

import autogen
from typing import Dict, List, Optional
import os

# Configuration for the LLM
config_list = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),  # Set your OpenAI API key as environment variable
    }
]

llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
    "timeout": 120,
}

def create_agents():
    """Create and configure all four agents for the coding workflow."""
    
    # 🧠 CodeAssistant - Specialized in generating Python code
    code_assistant = autogen.AssistantAgent(
        name="CodeAssistant",
        system_message="""🧠 You are CodeAssistant, a specialized Python code generator.
        
Your responsibilities:
- Generate clean, efficient, and well-documented Python code
- Follow PEP 8 style guidelines
- Include proper error handling and type hints
- Write modular and reusable functions
- Provide clear docstrings for all functions and classes

When generating code:
1. Start with imports and any necessary setup
2. Write the main functionality with proper structure
3. Include error handling where appropriate
4. Add comprehensive docstrings
5. Use meaningful variable and function names

Always explain your code design decisions and implementation approach.""",
        llm_config=llm_config,
    )
    
    # 🧐 CriticAgent - Reviews code and suggests improvements
    critic_agent = autogen.AssistantAgent(
        name="CriticAgent", 
        system_message="""🧐 You are CriticAgent, a meticulous code reviewer and improvement specialist.

Your responsibilities:
- Review code for bugs, security issues, and performance problems
- Suggest improvements for code quality, readability, and maintainability
- Ensure adherence to Python best practices and PEP 8
- Identify potential edge cases and error scenarios
- Recommend optimizations and refactoring opportunities

Review criteria:
1. Code correctness and logic
2. Error handling and edge cases
3. Performance and efficiency
4. Code style and readability
5. Security considerations
6. Documentation quality

Provide specific, actionable feedback with examples when suggesting improvements.""",
        llm_config=llm_config,
    )
    
    # 🧪 TestAgent - Writes comprehensive tests
    test_agent = autogen.AssistantAgent(
        name="TestAgent",
        system_message="""🧪 You are TestAgent, a specialized testing expert.

Your responsibilities:
- Write comprehensive unit tests using pytest
- Create test cases for normal scenarios, edge cases, and error conditions
- Ensure high test coverage
- Write clear, maintainable test code
- Include setup and teardown when necessary

Testing approach:
1. Analyze the code to identify all testable components
2. Write tests for normal functionality
3. Create tests for edge cases and boundary conditions
4. Add tests for error handling and exceptions
5. Include integration tests if needed
6. Provide clear test descriptions and assertions

Use pytest conventions and include fixtures when appropriate.""",
        llm_config=llm_config,
    )
    
    # 🙋 UserProxyAgent - Manages the workflow and represents the user
    user_proxy = autogen.UserProxyAgent(
        name="UserProxyAgent",
        system_message="""🙋 You are UserProxyAgent, the workflow manager and user representative.

Your responsibilities:
- Initiate coding tasks and manage the collaborative process
- Coordinate between different agents
- Ensure the final deliverable meets requirements
- Execute code when requested
- Provide feedback and guidance to other agents

Workflow management:
1. Present clear requirements to CodeAssistant
2. Facilitate review process with CriticAgent
3. Coordinate testing with TestAgent
4. Ensure iterative improvement based on feedback
5. Validate final implementation""",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
        code_execution_config={
            "work_dir": "autogen_workspace",
            "use_docker": False,
        },
        llm_config=llm_config,
    )
    
    return code_assistant, critic_agent, test_agent, user_proxy

def setup_group_chat(agents):
    """Set up a group chat for collaborative coding."""
    code_assistant, critic_agent, test_agent, user_proxy = agents
    
    # Create group chat with all agents
    groupchat = autogen.GroupChat(
        agents=[user_proxy, code_assistant, critic_agent, test_agent],
        messages=[],
        max_round=15,
        speaker_selection_method="round_robin",
    )
    
    # Create group chat manager
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
    )
    
    return manager

def main():
    """Main function to demonstrate the multi-agent coding workflow."""
    
    print("🚀 Starting AutoGen Multi-Agent Coding Example")
    print("=" * 60)
    
    # Create agents
    agents = create_agents()
    code_assistant, critic_agent, test_agent, user_proxy = agents
    
    # Set up group chat
    manager = setup_group_chat(agents)
    
    # Example coding task
    coding_task = """
    I need you to create a Python class called 'BankAccount' that can:
    
    1. Initialize with account holder name and initial balance
    2. Deposit money (with validation)
    3. Withdraw money (with balance checking)
    4. Check current balance
    5. Get account holder name
    6. Transfer money to another account
    
    Requirements:
    - Handle negative amounts gracefully
    - Prevent overdrafts
    - Include proper error handling
    - Add logging for transactions
    - Use type hints throughout
    
    Please follow this workflow:
    1. CodeAssistant: Generate the initial implementation
    2. CriticAgent: Review and suggest improvements
    3. CodeAssistant: Implement suggested improvements
    4. TestAgent: Write comprehensive tests
    5. Final review and validation
    """
    
    print(f"📋 Task: {coding_task}")
    print("=" * 60)
    
    # Start the collaborative coding process
    user_proxy.initiate_chat(
        manager,
        message=coding_task,
    )

if __name__ == "__main__":
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: Please set your OPENAI_API_KEY environment variable")
        print("You can set it by running: set OPENAI_API_KEY=your_api_key_here")
        print("Or create a .env file with your API key")
    else:
        main()
