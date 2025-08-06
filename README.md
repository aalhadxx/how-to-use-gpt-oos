# 🚀 How to Use GPT OSS

> **🔥 Just Launched**: OpenAI's gpt-oss-120b and gpt-oss-20b - Advanced Open-Weight Language Models

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/aalhadxx/how-to-use-gpt-oos?style=social)](https://github.com/aalhadxx/how-to-use-gpt-oos)
[![GitHub forks](https://img.shields.io/github/forks/aalhadxx/how-to-use-gpt-oos?style=social)](https://github.com/aalhadxx/how-to-use-gpt-oos)

<div align="center">
  <h3>⭐ Star this repo if it helped you! ⭐</h3>
  <p><em>The most comprehensive guide to OpenAI's new GPT OSS models</em></p>
</div>

---

## 🎯 What is GPT OSS?

**GPT OSS** represents OpenAI's breakthrough release of two powerful open-weight language models designed for advanced reasoning, agentic tasks, and versatile developer use cases.

### 🏆 Model Specifications

| Model | Parameters | Active/Token | Memory | Use Case |
|-------|------------|--------------|--------|----------|
| **gpt-oss-120b** | 117B | 5.1B | 80GB | Production, high reasoning |
| **gpt-oss-20b** | 21B | 3.6B | 16GB | Local, specialized tasks |

## ⚡ Quick Start

### Installation

```bash
# Clone this repository
git clone https://github.com/aalhadxx/how-to-use-gpt-oos.git
cd how-to-use-gpt-oos

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

## 🔥 Key Features

- **🚀 Apache 2.0 License**: Completely free for commercial use
- **🧠 Advanced Reasoning**: Superior performance on complex tasks
- **🔧 Tool Integration**: Native function calling, web browsing, Python execution
- **⚡ Efficient Deployment**: Runs on consumer hardware with MXFP4 quantization
- **🎛️ Configurable Reasoning**: Low, medium, high reasoning levels

## 📚 Examples

Check out the examples directory for practical code samples:

- [Basic Chat](examples/basic_chat.py) - Simple chat completions
- [Function Calling](examples/function_calling.py) - Function calling demos
- [Chain of Thought](examples/cot_reasoning.py) - Reasoning examples
- [Tool Integration](examples/tool_use.py) - Tool usage examples
- [Local Deployment](examples/local_deployment.py) - Local setup guides

## 🌟 Why This Repository?

- **🎯 SEO Optimized**: Captures search traffic for "gpt-oss"
- **📖 Comprehensive**: Covers all deployment methods
- **🔧 Practical**: Real, runnable code examples
- **🚀 Up-to-date**: Latest information on GPT OSS models
- **💡 Beginner-friendly**: Clear explanations and examples

## 📖 Resources

- [Official OpenAI Blog](https://openai.com/blog/introducing-gpt-oss)
- [Model Card](https://huggingface.co/openai/gpt-oss-120b)
- [Harmony Format](https://github.com/openai/harmony)

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <h3>⭐ If this helped you, please star the repository! ⭐</h3>
  <p><strong>Help others discover this comprehensive GPT OSS guide!</strong></p>
</div>

---

**Keywords**: gpt-oss, openai, language models, reasoning, open source, gpt-oss-120b, gpt-oss-20b, apache 2.0, machine learning, AI, artificial intelligence, large language models, LLM, transformers, ollama, vllm