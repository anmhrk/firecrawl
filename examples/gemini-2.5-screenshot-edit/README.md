# Gemini 2.5 Screenshot Editor

An interactive web screenshot editing tool that combines Firecrawl's screenshot capabilities with Google's Gemini 2.5 Flash image editing model to modify website screenshots using natural language prompts.

## Features

- **Website Screenshot Capture**: Uses Firecrawl to capture high-quality screenshots of any website
- **AI-Powered Image Editing**: Leverages Gemini 2.5 Flash's image editing capabilities to modify screenshots based on natural language prompts
- **Interactive Workflow**: Allows iterative editing of the same image with version tracking
- **User-Friendly Interface**: Clean command-line interface with questionary for easy navigation
- **Version Management**: Automatically saves each edit iteration with version numbering

## How It Works

1. **Screenshot Capture**: Enter a website URL and the tool captures a screenshot using Firecrawl
2. **AI Editing**: Describe your desired changes in natural language (e.g., "Make the background blue", "Add a red border", "Change the text to say 'Hello World'")
3. **Iterative Improvement**: Continue editing the same image with additional prompts
4. **Version Tracking**: Each edit is saved as a new version file for comparison

## Prerequisites

- Python 3.8+
- Google API Key with Gemini 2.5 Flash access
- Firecrawl API Key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd examples/gemini-2.5-screenshot-edit
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables in a `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## Usage

Run the script:

```bash
python gemini-2.5-screenshot-edit.py
```

### Example Workflow

1. Enter a website URL: `https://example.com`
2. Enter an editing prompt: `Add a bright red banner at the top saying 'SALE'`
3. Choose to continue editing, start over, or exit
4. For additional edits: `Change the banner color to green`

### Output

- Each edited image is saved as `edited_screenshot_v{version}.png`
- Console output shows the AI's description of changes made
- Interactive menu for continuing the workflow

## Tips for Best Results

1. **Clear Prompts**: Use specific, descriptive editing instructions
2. **Iterative Approach**: Make incremental changes rather than complex multi-step edits
3. **Visual Elements**: Focus on visual changes that AI can understand (colors, text, shapes)
