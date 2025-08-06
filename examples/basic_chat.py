#!/usr/bin/env python3
"""
Basic Chat Example for GPT OSS
Simple examples of using gpt-oss-120b and gpt-oss-20b
"""

import os
from openai import OpenAI

def basic_chat_example():
    """Basic chat completion with gpt-oss-120b"""
    print("=== Basic Chat with gpt-oss-120b ===")
    
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "user", "content": "Explain quantum computing in simple terms."}
        ],
        max_tokens=200,
        temperature=0.7
    )
    
    print(response.choices[0].message.content)
    print()

def compare_models():
    """Compare responses between gpt-oss-120b and gpt-oss-20b"""
    print("=== Comparing gpt-oss-120b vs gpt-oss-20b ===")
    
    client = OpenAI()
    question = "What are the three laws of robotics?"
    
    # Test with gpt-oss-120b
    response_120b = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[{"role": "user", "content": question}],
        max_tokens=150,
        temperature=0.7
    )
    
    # Test with gpt-oss-20b
    response_20b = client.chat.completions.create(
        model="gpt-oss-20b",
        messages=[{"role": "user", "content": question}],
        max_tokens=150,
        temperature=0.7
    )
    
    print("gpt-oss-120b response:")
    print(response_120b.choices[0].message.content)
    print()
    print("gpt-oss-20b response:")
    print(response_20b.choices[0].message.content)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please set your OPENAI_API_KEY environment variable")
        print("You can set it with: export OPENAI_API_KEY='your-api-key-here'")
        exit(1)
    
    print("GPT OSS Basic Chat Examples")
    print("=" * 40)
    print()
    
    try:
        basic_chat_example()
        compare_models()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have access to the gpt-oss models and your API key is valid.") 