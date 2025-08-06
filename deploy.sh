#!/bin/bash

# GPT OSS Local Deployment Script
# This script helps you set up a local environment for running gpt-oss models

set -e  # Exit on any error

echo "🚀 GPT OSS Local Deployment Script"
echo "=================================="
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    print_warning "Windows detected. Some features may not work optimally."
    print_warning "Consider using WSL2 for better compatibility."
fi

# Check Python version
print_status "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -o '3\.[0-9]\+' || python --version 2>&1 | grep -o '3\.[0-9]\+')

if [[ -z "$python_version" ]]; then
    print_error "Python 3 not found. Please install Python 3.12+ first."
    exit 1
fi

# Extract major and minor version
major_version=$(echo $python_version | cut -d. -f1)
minor_version=$(echo $python_version | cut -d. -f2)

if [[ "$major_version" -lt 3 ]] || [[ "$major_version" -eq 3 && "$minor_version" -lt 12 ]]; then
    print_error "Python 3.12+ required. Found: $python_version"
    print_error "Please upgrade Python to version 3.12 or higher."
    exit 1
fi

print_success "Python version: $python_version"

# Check if virtual environment exists
if [[ ! -d "venv" ]]; then
    print_status "Creating virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_status "Virtual environment already exists"
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate || source venv/Scripts/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Check for CUDA (optional)
print_status "Checking for CUDA support..."
if command -v nvidia-smi &> /dev/null; then
    print_success "NVIDIA GPU detected"
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader,nounits
else
    print_warning "No NVIDIA GPU detected. GPU acceleration will not be available."
fi

# Check for Ollama
print_status "Checking for Ollama..."
if command -v ollama &> /dev/null; then
    print_success "Ollama found"
    
    # Check if gpt-oss models are available
    if ollama list | grep -q "gpt-oss"; then
        print_success "GPT OSS models already downloaded"
    else
        print_status "Downloading GPT OSS models..."
        echo "This may take a while depending on your internet connection."
        
        read -p "Do you want to download gpt-oss-20b? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ollama pull gpt-oss:20b
            print_success "gpt-oss-20b downloaded successfully!"
        fi
        
        read -p "Do you want to download gpt-oss-120b? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_warning "gpt-oss-120b requires significant resources (80GB+ RAM)"
            ollama pull gpt-oss:120b
            print_success "gpt-oss-120b downloaded successfully!"
        fi
    fi
else
    print_warning "Ollama not found. Install from: https://ollama.com/download"
    print_status "After installing Ollama, run: ollama pull gpt-oss:20b"
fi

# Check for vLLM
print_status "Checking for vLLM..."
if command -v vllm &> /dev/null; then
    print_success "vLLM found"
    print_status "You can serve models with: vllm serve openai/gpt-oss-20b"
else
    print_warning "vLLM not found. Install with:"
    echo "pip install vllm"
fi

# Check for Hugging Face CLI
print_status "Checking for Hugging Face CLI..."
if command -v huggingface-cli &> /dev/null; then
    print_success "Hugging Face CLI found"
else
    print_status "Installing Hugging Face CLI..."
    pip install huggingface_hub
fi

# Create .env file if it doesn't exist
if [[ ! -f ".env" ]]; then
    print_status "Creating .env file..."
    cat > .env << EOF
# OpenAI API Configuration
OPENAI_API_KEY=your-api-key-here

# Model Configuration
GPT_OSS_120B_MODEL=gpt-oss-120b
GPT_OSS_20B_MODEL=gpt-oss-20b

# Local Deployment
OLLAMA_BASE_URL=http://localhost:11434/v1
VLLM_BASE_URL=http://localhost:8000/v1

# Environment
REASONING_EFFORT=medium
MAX_TOKENS=1000
TEMPERATURE=0.7
EOF
    print_success ".env file created"
    print_warning "Please update OPENAI_API_KEY in .env file with your actual API key"
else
    print_status ".env file already exists"
fi

# Test basic setup
print_status "Testing basic setup..."
python3 -c "
import openai
import os
from dotenv import load_dotenv

load_dotenv()

print('✓ OpenAI library imported successfully')
print('✓ Environment variables loaded')
print('✓ Basic setup complete')
"

print_success "Deployment setup complete!"
echo

# Display next steps
echo "🎯 Next Steps:"
echo "=============="
echo
echo "1. Set your OpenAI API key in .env file"
echo "2. Run examples:"
echo "   python examples/basic_chat.py"
echo "   python examples/function_calling.py"
echo "   python examples/cot_reasoning.py"
echo
echo "3. For local deployment:"
echo "   ollama run gpt-oss:20b"
echo "   # or"
echo "   vllm serve openai/gpt-oss-20b"
echo
echo "4. Check the README.md for more examples and documentation"
echo

# Check system resources
print_status "System Resource Check:"
total_ram=$(free -h 2>/dev/null | grep Mem | awk '{print $2}' || echo "Unknown")
available_ram=$(free -h 2>/dev/null | grep Mem | awk '{print $7}' || echo "Unknown")

echo "Total RAM: $total_ram"
echo "Available RAM: $available_ram"

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    total_ram_mb=$(sysctl -n hw.memsize 2>/dev/null | awk '{print $1/1024/1024}' || echo "0")
    if [[ "$total_ram_mb" -gt 16384 ]]; then
        print_success "Sufficient RAM for gpt-oss-20b"
    else
        print_warning "Limited RAM. Consider using cloud deployment for larger models"
    fi
fi

echo
print_success "Setup complete! Happy coding with GPT OSS! 🚀" 