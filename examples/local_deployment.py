#!/usr/bin/env python3
"""
Local Deployment Example for GPT OSS
Demonstrates how to run gpt-oss models locally
"""

import os
import subprocess
import sys
from openai import OpenAI

def ollama_deployment():
    """Example using Ollama for local deployment"""
    print("=== Ollama Local Deployment ===")
    
    # Check if Ollama is installed
    try:
        subprocess.run(["ollama", "--version"], check=True, capture_output=True)
        print("✓ Ollama is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Ollama not found. Install from: https://ollama.com/download")
        return
    
    print("\n1. Pull the gpt-oss-20b model:")
    print("   ollama pull gpt-oss:20b")
    
    print("\n2. Run the model:")
    print("   ollama run gpt-oss:20b")
    
    print("\n3. Use with OpenAI client:")
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"  # Ollama doesn't require a real API key
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=[
                {"role": "user", "content": "Hello! How are you today?"}
            ],
            max_tokens=100
        )
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure Ollama is running with: ollama serve")

def vllm_deployment():
    """Example using vLLM for local deployment"""
    print("\n=== vLLM Local Deployment ===")
    
    print("1. Install vLLM with GPT OSS support:")
    print("   pip install --pre vllm==0.10.1+gptoss \\")
    print("     --extra-index-url https://wheels.vllm.ai/gpt-oss/ \\")
    print("     --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \\")
    print("     --index-strategy unsafe-best-match")
    
    print("\n2. Start the server:")
    print("   vllm serve openai/gpt-oss-20b")
    
    print("\n3. Use with OpenAI client:")
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="dummy"  # vLLM doesn't require authentication
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-oss-20b",
            messages=[
                {"role": "user", "content": "What is machine learning?"}
            ],
            max_tokens=150
        )
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure vLLM server is running")

def transformers_deployment():
    """Example using Transformers for local deployment"""
    print("\n=== Transformers Local Deployment ===")
    
    print("1. Install dependencies:")
    print("   pip install transformers torch accelerate")
    
    print("\n2. Python code example:")
    code_example = '''
from transformers import pipeline
import torch

# Load the model
pipe = pipeline(
    "text-generation",
    model="openai/gpt-oss-20b",
    torch_dtype="auto",
    device_map="auto",
)

# Generate text
messages = [
    {"role": "user", "content": "Explain quantum computing in simple terms."}
]

outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1])
'''
    
    print(code_example)
    
    # Try to run the example if transformers is available
    try:
        from transformers import pipeline
        print("\n3. Running example...")
        
        pipe = pipeline(
            "text-generation",
            model="openai/gpt-oss-20b",
            torch_dtype="auto",
            device_map="auto",
        )
        
        messages = [
            {"role": "user", "content": "What is artificial intelligence?"}
        ]
        
        outputs = pipe(messages, max_new_tokens=100)
        print(f"Response: {outputs[0]['generated_text'][-1]}")
        
    except ImportError:
        print("Transformers not installed. Run: pip install transformers torch accelerate")
    except Exception as e:
        print(f"Error: {e}")

def system_requirements():
    """Show system requirements for local deployment"""
    print("\n=== System Requirements ===")
    
    print("Minimum Requirements:")
    print("- gpt-oss-20b: 16GB RAM, 8GB VRAM")
    print("- gpt-oss-120b: 80GB VRAM (single H100 GPU)")
    
    print("\nRecommended Requirements:")
    print("- gpt-oss-20b: 32GB RAM, 16GB VRAM")
    print("- gpt-oss-120b: 80GB VRAM, 4x H100 GPUs")
    
    print("\nDeployment Options:")
    print("1. Ollama: Easiest for consumer hardware")
    print("2. vLLM: Best performance, requires more resources")
    print("3. Transformers: Most flexible, slower inference")

def performance_comparison():
    """Compare different deployment methods"""
    print("\n=== Performance Comparison ===")
    
    comparison = """
    | Method      | Setup Difficulty | Speed | Memory | Best For |
    |-------------|------------------|-------|--------|----------|
    | Ollama      | Easy            | Fast  | Low    | Development |
    | vLLM        | Medium          | Fast  | Medium | Production |
    | Transformers| Easy            | Slow  | Low    | Research |
    """
    
    print(comparison)

if __name__ == "__main__":
    print("GPT OSS Local Deployment Examples")
    print("=" * 40)
    
    ollama_deployment()
    vllm_deployment()
    transformers_deployment()
    system_requirements()
    performance_comparison()
    
    print("\n=== Next Steps ===")
    print("1. Choose your deployment method based on your hardware")
    print("2. Follow the installation instructions above")
    print("3. Test with the provided examples")
    print("4. Check the official documentation for advanced features") 