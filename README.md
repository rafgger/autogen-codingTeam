# AutoGen Multi-Agent Coding Example

This project demonstrates a collaborative coding workflow using AutoGen with four specialized agents working together to solve programming tasks.

## 🤖 Agents Overview

### 🧠 CodeAssistant
- **Role**: Python code generator
- **Responsibilities**: 
  - Generate clean, efficient Python code
  - Follow PEP 8 style guidelines
  - Include proper error handling and type hints
  - Write modular and reusable functions
  - Provide comprehensive docstrings

### 🧐 CriticAgent
- **Role**: Code reviewer and improvement specialist
- **Responsibilities**:
  - Review code for bugs and security issues
  - Suggest improvements for code quality
  - Ensure best practices adherence
  - Identify edge cases and performance issues
  - Recommend optimizations

### 🧪 TestAgent
- **Role**: Testing specialist
- **Responsibilities**:
  - Write comprehensive unit tests using pytest
  - Create test cases for normal and edge scenarios
  - Ensure high test coverage
  - Include proper test documentation
  - Design integration tests when needed

### 🙋 UserProxyAgent
- **Role**: Workflow manager and user representative
- **Responsibilities**:
  - Initiate coding tasks
  - Coordinate between agents
  - Execute code when needed
  - Ensure final deliverable meets requirements
  - Manage the collaborative process

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone or download this project**
   ```cmd
   cd c:\Users\Lenovo\Documents\coding\autogen
   ```

2. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   **Option A: Environment Variable**
   ```cmd
   set OPENAI_API_KEY=your_actual_api_key_here
   ```
   
   **Option B: Create .env file**
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## 🎯 Usage

### Running the Full Example
```cmd
python multi_agent_coding_example.py
```

### Running the Demo (No API Key Required)
```cmd
python simple_demo.py
```

## 📋 Example Workflow

The agents follow this collaborative process:

1. **Task Initiation**: UserProxyAgent presents a coding requirement
2. **Code Generation**: CodeAssistant creates initial implementation
3. **Code Review**: CriticAgent reviews and suggests improvements
4. **Code Refinement**: CodeAssistant implements suggested changes
5. **Test Creation**: TestAgent writes comprehensive tests
6. **Final Validation**: UserProxyAgent verifies the complete solution

## 🏗️ Project Structure

```
autogen/
├── multi_agent_coding_example.py  # Main multi-agent example
├── simple_demo.py                 # Demo without API requirements
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── autogen_workspace/             # Generated during execution
```

## 💡 Example Tasks

The example includes a complete BankAccount class implementation with:
- Account initialization and management
- Deposit and withdrawal operations
- Balance checking and validation
- Money transfer between accounts
- Transaction logging
- Comprehensive error handling
- Full test suite

## 🔧 Customization

### Adding New Agents
```python
new_agent = autogen.AssistantAgent(
    name="NewAgent",
    system_message="Your specialized role and responsibilities...",
    llm_config=llm_config,
)
```

### Modifying Workflow
```python
groupchat = autogen.GroupChat(
    agents=[user_proxy, code_assistant, critic_agent, test_agent, new_agent],
    messages=[],
    max_round=20,  # Adjust conversation length
    speaker_selection_method="round_robin",  # or "auto"
)
```

## 📚 Key Features

- **Collaborative Development**: Multiple specialized agents working together
- **Quality Assurance**: Built-in code review and testing processes
- **Best Practices**: Enforcement of Python coding standards
- **Comprehensive Testing**: Automated test generation and validation
- **Error Handling**: Robust error management throughout the workflow
- **Documentation**: Clear code documentation and explanations

## 🎁 Benefits

1. **Code Quality**: Multi-agent review ensures high-quality output
2. **Comprehensive Testing**: Automated test creation reduces bugs
3. **Best Practices**: Enforced coding standards and conventions
4. **Collaborative Learning**: See how different aspects of development work together
5. **Scalability**: Easy to add new agents for specialized tasks

## 🤝 Contributing

Feel free to extend this example by:
- Adding new specialized agents (DocumentationAgent, SecurityAgent, etc.)
- Implementing different coding tasks
- Enhancing the workflow patterns
- Adding more sophisticated testing scenarios

## 📄 License

This example is provided for educational purposes. Please ensure you comply with OpenAI's usage policies when using their API.

## 🔗 Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Best Practices](https://pep8.org/)
- [pytest Documentation](https://docs.pytest.org/)
