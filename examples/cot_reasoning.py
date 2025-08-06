#!/usr/bin/env python3
"""
Chain of Thought Reasoning Example for GPT OSS
Demonstrates reasoning capabilities with different effort levels
"""

import os
from openai import OpenAI

def math_reasoning_example():
    """Example of mathematical reasoning with step-by-step thinking"""
    print("=== Mathematical Reasoning Example ===")
    
    client = OpenAI()
    
    math_problem = "If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?"
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful math tutor. Always show your step-by-step reasoning before giving the final answer."
            },
            {
                "role": "user",
                "content": f"Please solve this problem step by step:\n{math_problem}"
            }
        ],
        max_tokens=400,
        temperature=0.3
    )
    
    print(f"Problem: {math_problem}")
    print(f"Solution: {response.choices[0].message.content}")

def logical_reasoning_example():
    """Example of logical reasoning"""
    print("\n=== Logical Reasoning Example ===")
    
    client = OpenAI()
    
    logic_puzzle = """
    Three people are in a room: Alice, Bob, and Charlie. 
    - Alice says: "Bob is lying"
    - Bob says: "Charlie is lying" 
    - Charlie says: "Alice is lying"
    
    If exactly one person is telling the truth, who is it?
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a logic expert. Analyze the problem step by step and explain your reasoning."
            },
            {
                "role": "user",
                "content": f"Solve this logic puzzle:\n{logic_puzzle}"
            }
        ],
        max_tokens=300,
        temperature=0.2
    )
    
    print(f"Puzzle: {logic_puzzle}")
    print(f"Analysis: {response.choices[0].message.content}")

def reasoning_levels_comparison():
    """Compare different reasoning effort levels"""
    print("\n=== Reasoning Levels Comparison ===")
    
    client = OpenAI()
    
    question = "Explain why the sky appears blue during the day but red during sunset."
    
    reasoning_levels = ["low", "medium", "high"]
    
    for level in reasoning_levels:
        print(f"\n--- Reasoning Level: {level.upper()} ---")
        
        response = client.chat.completions.create(
            model="gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": f"Reasoning: {level}. Provide an explanation appropriate for this reasoning level."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=200,
            temperature=0.5
        )
        
        print(response.choices[0].message.content)

def code_reasoning_example():
    """Example of reasoning about code"""
    print("\n=== Code Reasoning Example ===")
    
    client = OpenAI()
    
    code_snippet = """
    def mystery_function(n):
        if n <= 1:
            return 1
        return n * mystery_function(n - 1)
    
    result = mystery_function(5)
    print(result)
    """
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a programming expert. Analyze the code step by step and explain what it does."
            },
            {
                "role": "user",
                "content": f"Analyze this code and explain what it does:\n{code_snippet}"
            }
        ],
        max_tokens=250,
        temperature=0.3
    )
    
    print(f"Code: {code_snippet}")
    print(f"Analysis: {response.choices[0].message.content}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please set your OPENAI_API_KEY environment variable")
        exit(1)
    
    print("GPT OSS Chain of Thought Reasoning Examples")
    print("=" * 50)
    
    try:
        math_reasoning_example()
        logical_reasoning_example()
        reasoning_levels_comparison()
        code_reasoning_example()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have access to the gpt-oss models and your API key is valid.") 