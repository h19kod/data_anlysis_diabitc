# Contributing to Diabetes Prediction System

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

When creating a bug report, include:
- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- **Clear use case**
- **Detailed description**
- **Potential implementation approach**

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests if available
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
pytest
```

## Style Guidelines

### Python Code
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### Documentation
- Use clear, concise language
- Include code examples where helpful
- Update README.md if needed

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs where appropriate

Example:
```
Add feature: implement patient risk calculation

- Calculate risk based on glucose, age, BMI
- Add visual gauge for risk display
- Update dashboard UI

Closes #123
```

## Code Review Process

- All PRs require review before merging
- Address review comments promptly
- Keep PRs focused on a single feature/fix

## Community

- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and insights

## Questions?

Feel free to open an issue for questions or contact the maintainers.

Thank you for contributing! 🙏
