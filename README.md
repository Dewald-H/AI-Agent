# LLM Code Agent

> ⚠️ **Important:** Read this entire file before using.

This is an experimental AI code agent that uses the **Gemini flash 2.5** model and a constrained set of tools to read, analyze, and modify code within a specified working directory.

This project started as a guided Boot.dev lesson and was refactored into a reusable package so you can run the agent at the root of _your_ projects (while keeping it sandboxed to a chosen working directory).

> ⚠️ **Important:**  This is an **educational and experimental** project. It is **not** hardened, audited, nor does it have production‑ready security. Treat it as a learning and eperimental tool.

## Features

- Uses an LLM (Gemini flash 2.5) to:
  - Inspect files in a codebase
  - Diagnose simple bugs or issues
  - Propose and apply changes
  - Optionally loop until tests or goals are met
- File operations are **sandboxed** to a chosen working directory:
  - The agent can only read/write within that directory
  - Attempts to use `..`, absolute paths, or symlinks to escape are blocked
- Can be installed and used as a Python package
- Optionally provides a simple CLI entry point

---

## How It Works (High-Level)

At a high level, the agent:

1. Is given a **working directory** (e.g. your project root).
2. Exposes a small set of tools to the LLM, such as:
   - `read_file(path)`
   - `write_file(path, content)`
   - `list_files()`
   These tools internally enforce the sandbox.
3. Sends the user’s request and a description of the tools to the LLM.
4. The LLM “decides” when to call tools (e.g. to inspect code, run tests, or apply changes).
5. The agent loop continues until:
   - A stopping condition is met (e.g. tests pass), or
   - A maximum number of steps is reached.

All tools compute paths relative to that working directory and rejects anything outside of it.

 ---
## Installation and Usage

You can install the agent as a Python package, either globally or in a virtual environment. I reccomend doing it in a virtual environment.

### 1) Get a Gemini API key

Open Google’s “Using Gemini API keys” guide and follow the steps to create an API key.

(Shortcut) You can also go straight to the Google AI Studio API key page

### 2) Install ai-agent from GitHub (recommended for users)

From the root of your own project (the project where you want to use ai-agent), create/activate a virtual environment, then install directly from GitHub:

```bash
# Create & activate a virtual environment (example)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install ai-agent from GitHub
pip install "git+https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git"
```
After this, the ai-agent command should be available in that environment:
```bash
ai-agent --help
```
### 3) Add your Gemini API key

You have two common options. Use whichever matches how your code loads configuration.

#### Option A (most universal): set an environment variable

macOS/Linux (bash/zsh):
```bash
export GEMINI_API_KEY="YOUR_KEY_HERE"
```
Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY="YOUR_KEY_HERE"
```
#### Option B: use a .env file

If your project loads environment variables from a .env file (for example via python-dotenv), create a file named .env in the place your app expects (commonly your project root) and add:
```dotenv
GEMINI_API_KEY='YOUR_KEY_HERE'
```
### 4) Run it

Once installed and your API key is set, you can run the agent:
```bash
ai-agent "your prompt here"
```
You can use --verbose for more detailed output:
```bash
ai-agent "your prompt here" --verbose
```
Example usage:
```bash
ai-agent "What files are in the root of my project?"
```
Example usage:
```bash
ai-agent "Fix the bug in the main file. Explain what was fixed and what the problem was."
```
---

## Note
> ⚠️ **Important:** It is reccomended to run the agent at the root of your project so that the LLM cannot access any files outside of your project. LLM's accessing files outside of your project is problematic and potentially very dangerous. But this agent is designed so that it cannot access files above you current working directory, so just keep within your project, don't run the agent anywhere else and you will be fine.

> Also use Git to keep track of changes because the agent may make unwanted changes to your project if given the wrong prompts. Make regular commits and Git will allow you to backtrack those unwanted changes.