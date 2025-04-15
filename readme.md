# Playwright GitHub Agent Demo

This repository demonstrates the use of [Playwright](https://playwright.dev/) for end-to-end testing and automation. The project showcases how to automate workflows and test web applications effectively harnessing the power of GenAI in the form of GitHub Copilot using the integrated powerful Playwright LLM Agents

## Features

- Cross-browser testing with Playwright.
- Automated workflows for GitHub integration.
- Example scripts for testing web applications.

## Prerequisites to activate Copilot Agent mode on VSCode

- [Node.js](https://nodejs.org/) (v16 or later)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/playwright-githubagent-demo.git
    cd playwright-githubagent-demo
    ```
2. Setup and activate your virtual environment using your preferred choice.

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. [Installing Playwright Agents (MCP) on VSCode](https://github.com/microsoft/playwright-mcp)

## Usage

### Activate the virtual environment
```bash
source .venv/bin/activate
```

### Run Tests
Execute the Playwright tests:
```bash
pytest tests.py --headed
```

```bash
((.venv) ) [18:33:55] sridhariyer:playwright-githubagent-demo $ pytest tests.py --headed          
=============================================== test session starts ================================================
platform darwin -- Python 3.12.10, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/sridhariyer/Documents/Playwright-Projects/playwright-githubagent-demo
plugins: playwright-0.7.0, base-url-2.1.0
collected 2 items                                                                                                  

tests.py ..                                                                                                  [100%]

================================================ 2 passed in 16.83s ================================================
((.venv) ) [18:34:24] sridhariyer:playwright-githubagent-demo $ 
```


## Resources

- [Playwright Documentation](https://playwright.dev/docs/intro)

## License

This project is licensed under the [MIT License](LICENSE).