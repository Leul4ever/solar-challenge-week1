# Create README.md
echo "# Solar Challenge Week 1

## Environment Setup

### Prerequisites
- Python 3.9+
- Git

### Steps to Reproduce Environment

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
   \`\`\`

2. **Create and activate virtual environment**
   \`\`\`bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   
   # Or using conda
   conda create -n solar-challenge python=3.9
   conda activate solar-challenge
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Verify installation**
   \`\`\`bash
   python --version
   pip list
   \`\`\`

### Project Structure
- \`data/\` - Dataset directory (ignored in git)
- \`.github/workflows/ci.yml\` - CI/CD pipeline
- \`requirements.txt\` - Python dependencies
- \`.gitignore\` - Git ignore rules

### Branching Strategy
- \`main\` - Production-ready code
- \`setup-task\` - Environment setup branch" > README.md