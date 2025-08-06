#!/usr/bin/env python3
"""
Function Calling Example for GPT OSS
Demonstrates how to use function calling with gpt-oss models
"""

import os
import json
from openai import OpenAI

def weather_function_example():
    """Example of function calling with a weather function"""
    print("=== Weather Function Example ===")
    
    client = OpenAI()
    
    # Define the function
    functions = [
        {
            "name": "get_weather",
            "description": "Get current weather information for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use"
                    }
                },
                "required": ["location"]
            }
        }
    ]
    
    # Make the request
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "user", "content": "What's the weather like in New York?"}
        ],
        functions=functions,
        function_call="auto"
    )
    
    # Check if the model wants to call a function
    if response.choices[0].message.function_call:
        function_call = response.choices[0].message.function_call
        print(f"Function called: {function_call.name}")
        print(f"Arguments: {function_call.arguments}")
        
        # Parse the arguments
        args = json.loads(function_call.arguments)
        print(f"Location: {args.get('location')}")
        print(f"Unit: {args.get('unit', 'fahrenheit')}")
    else:
        print("No function call requested")
        print(response.choices[0].message.content)

def calculator_example():
    """Example of function calling with a calculator function"""
    print("\n=== Calculator Function Example ===")
    
    client = OpenAI()
    
    functions = [
        {
            "name": "calculate",
            "description": "Perform mathematical calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-oss-20b",
        messages=[
            {"role": "user", "content": "What is 15 * 23 + 7?"}
        ],
        functions=functions,
        function_call="auto"
    )
    
    if response.choices[0].message.function_call:
        function_call = response.choices[0].message.function_call
        print(f"Function called: {function_call.name}")
        print(f"Expression: {json.loads(function_call.arguments)['expression']}")
    else:
        print("No function call requested")
        print(response.choices[0].message.content)

def multiple_functions_example():
    """Example with multiple available functions"""
    print("\n=== Multiple Functions Example ===")
    
    client = OpenAI()
    
    functions = [
        {
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        },
        {
            "name": "get_time",
            "description": "Get current time for a timezone",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {"type": "string"}
                },
                "required": ["timezone"]
            }
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "user", "content": "What's the weather in Tokyo and what time is it there?"}
        ],
        functions=functions,
        function_call="auto"
    )
    
    if response.choices[0].message.function_call:
        function_call = response.choices[0].message.function_call
        print(f"Function called: {function_call.name}")
        print(f"Arguments: {function_call.arguments}")
    else:
        print("No function call requested")
        print(response.choices[0].message.content)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please set your OPENAI_API_KEY environment variable")
        exit(1)
    
    print("GPT OSS Function Calling Examples")
    print("=" * 40)
    
    try:
        weather_function_example()
        calculator_example()
        multiple_functions_example()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have access to the gpt-oss models and your API key is valid.") 