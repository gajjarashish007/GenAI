#!/bin/bash

# IAM User to Role Converter Launcher Script
# This script checks prerequisites and launches the conversion tool

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

print_error() {
    echo -e "${RED}❌${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ️${NC} $1"
}

echo "=================================================="
echo "🔄 IAM User to Role Converter"
echo "=================================================="
echo ""

# Check if running in the correct directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

print_info "Checking prerequisites..."

# Check Python 3
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    print_status "Python 3 is installed (version $PYTHON_VERSION)"
else
    print_error "Python 3 is not installed"
    echo "Please install Python 3 and try again"
    exit 1
fi

# Check pip3
if command -v pip3 &> /dev/null; then
    print_status "pip3 is available"
else
    print_warning "pip3 not found, trying pip"
    if ! command -v pip &> /dev/null; then
        print_error "Neither pip3 nor pip is available"
        exit 1
    fi
fi

# Check boto3
if python3 -c "import boto3" 2>/dev/null; then
    BOTO3_VERSION=$(python3 -c "import boto3; print(boto3.__version__)" 2>/dev/null)
    print_status "boto3 is installed (version $BOTO3_VERSION)"
else
    print_warning "boto3 is not installed, attempting to install..."
    if command -v pip3 &> /dev/null; then
        pip3 install boto3
    else
        pip install boto3
    fi
    
    if python3 -c "import boto3" 2>/dev/null; then
        print_status "boto3 installed successfully"
    else
        print_error "Failed to install boto3"
        exit 1
    fi
fi

# Check AWS CLI
if command -v aws &> /dev/null; then
    AWS_VERSION=$(aws --version 2>&1 | cut -d' ' -f1 | cut -d'/' -f2)
    print_status "AWS CLI is installed (version $AWS_VERSION)"
else
    print_warning "AWS CLI is not installed"
    print_info "You can install it with: pip3 install awscli"
fi

# Check AWS credentials
print_info "Checking AWS credentials..."

if aws sts get-caller-identity &> /dev/null; then
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text 2>/dev/null)
    USER_ARN=$(aws sts get-caller-identity --query Arn --output text 2>/dev/null)
    print_status "AWS credentials are configured"
    print_info "Account ID: $ACCOUNT_ID"
    print_info "User/Role: $USER_ARN"
else
    print_error "AWS credentials are not configured or invalid"
    echo ""
    echo "Please configure your AWS credentials using one of these methods:"
    echo ""
    echo "1. AWS CLI configuration:"
    echo "   aws configure"
    echo ""
    echo "2. Environment variables:"
    echo "   export AWS_ACCESS_KEY_ID=your_access_key"
    echo "   export AWS_SECRET_ACCESS_KEY=your_secret_key"
    echo "   export AWS_DEFAULT_REGION=us-east-1"
    echo ""
    echo "3. IAM roles (if running on EC2)"
    echo ""
    exit 1
fi

# Check IAM permissions
print_info "Checking IAM permissions..."

REQUIRED_ACTIONS=(
    "iam:ListUsers"
    "iam:GetUser"
    "iam:ListAttachedUserPolicies"
    "iam:ListUserPolicies"
    "iam:GetUserPolicy"
    "iam:CreateRole"
    "iam:AttachRolePolicy"
    "iam:PutRolePolicy"
    "sts:GetCallerIdentity"
)

# Test basic IAM access
if aws iam list-users --max-items 1 &> /dev/null; then
    print_status "Basic IAM permissions verified"
else
    print_warning "Cannot verify IAM permissions - you may encounter issues"
    print_info "Required IAM permissions:"
    for action in "${REQUIRED_ACTIONS[@]}"; do
        echo "  - $action"
    done
    echo ""
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if files exist
REQUIRED_FILES=(
    "iam_user_to_role.html"
    "iam_conversion_backend.py"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [[ -f "$file" ]]; then
        print_status "Found $file"
    else
        print_error "Missing required file: $file"
        exit 1
    fi
done

# Check if port 8081 is available
if lsof -Pi :8081 -sTCP:LISTEN -t >/dev/null 2>&1; then
    print_warning "Port 8081 is already in use"
    print_info "Attempting to find the process using port 8081..."
    PROCESS_INFO=$(lsof -Pi :8081 -sTCP:LISTEN 2>/dev/null | tail -n +2)
    if [[ -n "$PROCESS_INFO" ]]; then
        echo "$PROCESS_INFO"
        echo ""
        read -p "Kill the process and continue? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            PID=$(echo "$PROCESS_INFO" | awk '{print $2}')
            kill -9 "$PID" 2>/dev/null || true
            sleep 2
            print_status "Process killed"
        else
            print_info "You can change the port in iam_conversion_backend.py"
            exit 1
        fi
    fi
else
    print_status "Port 8081 is available"
fi

echo ""
print_info "All prerequisites met! Starting the IAM User to Role Converter..."
echo ""

# Make the Python script executable
chmod +x iam_conversion_backend.py

# Start the server
print_info "Starting backend server on port 8081..."
echo ""
echo "=================================================="
echo "🌐 Open your browser to: http://localhost:8081"
echo "=================================================="
echo ""
echo "🔐 Login Credentials:"
echo "   Username: admin"
echo "   Password: 123@admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Python backend
python3 iam_conversion_backend.py
