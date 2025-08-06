# 🚀 How to Use GPT OSS

> **Just Launched**: OpenAI's gpt-oss-120b and gpt-oss-20b - Advanced Open-Weight Language Models

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

## What is GPT OSS?

GPT OSS represents OpenAI's breakthrough release of two powerful open-weight language models:

- **gpt-oss-120b**: 117B parameters, 5.1B active, 80GB memory - for production use
- **gpt-oss-20b**: 21B parameters, 3.6B active, 16GB memory - for local deployment

## Quick Start

### Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/how-to-use-gpt-oss.git
cd how-to-use-gpt-oss

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from openai import OpenAI

# Initialize client
client = OpenAI()

# Simple chat completion
response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    max_tokens=200,
    temperature=0.7
)

print(response.choices[0].message.content)
```

### Local Deployment

```bash
# Using Ollama (Recommended)
ollama pull gpt-oss:20b
ollama run gpt-oss:20b

# Using vLLM
vllm serve openai/gpt-oss-20b

# Using Transformers
python -c "
from transformers import pipeline
pipe = pipeline('text-generation', model='openai/gpt-oss-20b')
print(pipe('Hello, how are you?')[0]['generated_text'])
"
```

## Key Features

- **Apache 2.0 License**: Completely free for commercial use
- **Advanced Reasoning**: Superior performance on complex tasks
- **Tool Integration**: Native function calling, web browsing, Python execution
- **Efficient Deployment**: Runs on consumer hardware with MXFP4 quantization
- **Configurable Reasoning**: Low, medium, high reasoning levels

## Examples

Check out the examples directory for practical code samples:

- [Basic Chat](examples/basic_chat.py)
- [Function Calling](examples/function_calling.py)
- [Chain of Thought](examples/cot_reasoning.py)
- [Tool Integration](examples/tool_use.py)
- [Local Deployment](examples/local_deployment.py)

## Resources

- [Official OpenAI Blog](https://openai.com/blog/introducing-gpt-oss)
- [Model Card](https://huggingface.co/openai/gpt-oss-120b)
- [Harmony Format](https://github.com/openai/harmony)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: gpt-oss, openai, language models, reasoning, open source, gpt-oss-120b, gpt-oss-20b, apache 2.0, machine learning, AI