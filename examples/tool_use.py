#!/usr/bin/env python3
"""
Tool Use Example for GPT OSS
Demonstrates how to use tools like browser, python, and file operations
"""

import os
from openai import OpenAI

def browser_tool_example():
    """Example of browser tool usage"""
    print("=== Browser Tool Example ===")
    
    client = OpenAI()
    
    # System message with browser tool access
    browser_system_message = """
    You have access to a browser tool that can:
    - search: Search for information on the web
    - open: Open a specific webpage
    - find: Find specific content on a page
    
    Use the browser tool when you need current information or to verify facts.
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "system", "content": browser_system_message},
            {"role": "user", "content": "What are the latest AI developments in 2024?"}
        ],
        max_tokens=300,
        temperature=0.7
    )
    
    print("Question: What are the latest AI developments in 2024?")
    print(f"Response: {response.choices[0].message.content}")
    print("\nNote: This is a conceptual example. Actual browser tool implementation requires additional setup.")

def python_tool_example():
    """Example of Python tool usage"""
    print("\n=== Python Tool Example ===")
    
    client = OpenAI()
    
    # System message with Python tool access
    python_system_message = """
    You have access to a Python execution environment that can:
    - Run Python code
    - Perform calculations
    - Process data
    - Generate visualizations
    
    Use the Python tool when you need to perform calculations or data processing.
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-20b",
        messages=[
            {"role": "system", "content": python_system_message},
            {"role": "user", "content": "Calculate the factorial of 10 and show the steps."}
        ],
        max_tokens=250,
        temperature=0.3
    )
    
    print("Question: Calculate the factorial of 10 and show the steps.")
    print(f"Response: {response.choices[0].message.content}")
    print("\nNote: This is a conceptual example. Actual Python tool implementation requires additional setup.")

def file_operations_example():
    """Example of file operations with apply_patch tool"""
    print("\n=== File Operations Example ===")
    
    client = OpenAI()
    
    # System message with file operations
    file_system_message = """
    You have access to file operations that can:
    - create: Create new files
    - update: Modify existing files
    - delete: Remove files
    
    Use file operations when you need to work with local files.
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "system", "content": file_system_message},
            {"role": "user", "content": "Create a simple Python script that prints 'Hello, World!'"}
        ],
        max_tokens=200,
        temperature=0.5
    )
    
    print("Question: Create a simple Python script that prints 'Hello, World!'")
    print(f"Response: {response.choices[0].message.content}")
    print("\nNote: This is a conceptual example. Actual file operations require additional setup.")

def combined_tools_example():
    """Example combining multiple tools"""
    print("\n=== Combined Tools Example ===")
    
    client = OpenAI()
    
    combined_system_message = """
    You have access to multiple tools:
    - Browser: For web search and information gathering
    - Python: For calculations and data processing
    - File operations: For creating and modifying files
    
    Use the appropriate tool based on the task requirements.
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "system", "content": combined_system_message},
            {"role": "user", "content": "Research the current stock price of Apple, calculate the percentage change from yesterday, and save the results to a file."}
        ],
        max_tokens=350,
        temperature=0.4
    )
    
    print("Question: Research the current stock price of Apple, calculate the percentage change from yesterday, and save the results to a file.")
    print(f"Response: {response.choices[0].message.content}")
    print("\nNote: This is a conceptual example. Actual tool implementation requires additional setup.")

def tool_implementation_notes():
    """Provide notes on implementing tools"""
    print("\n=== Tool Implementation Notes ===")
    print("""
    To implement these tools in practice, you would need:
    
    1. Browser Tool:
       - Web scraping capabilities
       - Search API integration
       - Content parsing
    
    2. Python Tool:
       - Secure code execution environment
       - Sandboxed Python interpreter
       - Result capture and formatting
    
    3. File Operations:
       - File system permissions
       - Path validation
       - Backup mechanisms
    
    The gpt-oss models are trained to use these tools, but you need to implement
    the actual tool handlers in your application.
    """)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please set your OPENAI_API_KEY environment variable")
        exit(1)
    
    print("GPT OSS Tool Use Examples")
    print("=" * 40)
    
    try:
        browser_tool_example()
        python_tool_example()
        file_operations_example()
        combined_tools_example()
        tool_implementation_notes()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have access to the gpt-oss models and your API key is valid.") 