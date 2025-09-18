# Gemini 2.5 Flash (Nano Banana) Screenshot Editor

An intelligent screenshot editing tool that screenshots websites and transforms them using natural language. Simply describe what you want changed, and watch as Google's Gemini 2.5 Flash brings your vision to life.

## ✨ Key Features

### **Smart Screenshot Capture**

- High-quality website screenshots via Firecrawl
- Automatic URL normalization and validation
- Supports any publicly accessible website

### **AI-Powered Visual Editing**

- **Natural Language Control**: Edit with plain English descriptions
- **Advanced Image Understanding**: Gemini 2.5 Flash interprets visual context
- **Creative Transformations**: Add elements, change styles, modify layouts

### **Flexible Workflow Options**

- **Iterative Editing**: Build changes progressively
- **Smart Redo System**: Try different approaches for the same edit
- **Version Branching**: Keep original while exploring alternatives

### **Intelligent File Management**

- Automatic timestamped filenames
- Version tracking (v1, v2, v3...)
- Redo variant tracking (-redo suffix)
- PNG format preservation

## 🚀 What You Can Do

Transform websites with prompts like:

| **Style Transformations**         | **Content Modifications**            | **UI Enhancements**          |
| --------------------------------- | ------------------------------------ | ---------------------------- |
| `"Give it a cyberpunk aesthetic"` | `"Change the headline to 'Welcome'"` | `"Add a neon search bar"`    |
| `"Make it look retro/vintage"`    | `"Replace logo with custom text"`    | `"Add colorful buttons"`     |
| `"Apply dark mode styling"`       | `"Insert promotional banners"`       | `"Create floating elements"` |
| `"Add glowing effects"`           | `"Modify navigation text"`           | `"Add visual indicators"`    |

## 🔧 How It Works

1. **URL Input**: Enter any website URL
2. **Screenshot**: Firecrawl captures high-quality image
3. **Edit Prompt**: Describe your desired changes in natural language
4. **AI Processing**: Gemini 2.5 Flash interprets and applies changes
5. **Save Result**: Auto-saved with version tracking
6. **Iterate**: Continue editing, redo, or start fresh

## 📦 Setup

### Prerequisites

- **Python 3.8+** (Tested on 3.13+)
- **Google API Key** ([Get it here](https://aistudio.google.com/apikey))
- **Firecrawl API Key** ([Get it here](https://www.firecrawl.dev/app/api-keys))

### Getting Started

1. Clone the repository:

```bash
git clone <repository-url>
cd examples/gemini-2.5-screenshot-edit
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in a `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

### Usage

```bash
python gemini-2.5-screenshot-edit.py
```

## Example Session

```
URL: github.com
Screenshot captured!

Edit 1: "add neon blue accents to the navigation"
→ edited_screenshot_v1_[timestamp].png

Edit 2: "make the background darker"
→ edited_screenshot_v2_[timestamp].png

Redo v2: "add purple gradient background instead"
→ edited_screenshot_v2-redo_[timestamp].png
```

## 🎨 Creative Prompt Examples

### **Visual Style Changes**

```
"Transform into a retro 80s aesthetic with neon colors"
"Apply a minimalist, clean white design"
"Make it look like a hand-drawn sketch"
"Add a festive holiday theme with decorations"
```

### **UI Modifications**

```
"Replace the search bar with a glowing neon version"
"Add floating action buttons in the corners"
"Create a sticky navigation with drop shadows"
"Insert a promotional banner at the top"
```

### **Content Updates**

```
"Change the main headline to 'Welcome to the Future'"
"Replace all button text with emoji equivalents"
"Add price tags to product images"
"Insert testimonial quotes in speech bubbles"
```

## 💡 Pro Tips

### **For Better Results**

- **Be Specific**: `"Add a red banner"` vs `"Add a bright red banner at the top with white text"`
- **Incremental Changes**: Build complexity through multiple edits
- **Visual Language**: Use color, shape, and position descriptions
- **Context Matters**: Reference existing elements (`"below the header"`, `"next to the logo"`)

### **Workflow Optimization**

- **Version Strategy**: Use progressive editing for major changes
- **Redo Feature**: Try multiple approaches without losing progress
- **Batch Similar Sites**: Process multiple pages from same domain
- **Save Originals**: Keep unedited screenshots for reference

## 🐛 Troubleshooting

| Issue                          | Solution                                |
| ------------------------------ | --------------------------------------- |
| `Invalid URL format`           | Use full URLs: `https://example.com`    |
| `Failed to capture screenshot` | Check if website is publicly accessible |
| `No response from Gemini`      | Verify API key and model availability   |
| `Failed to edit screenshot`    | Try simpler, more specific prompts      |
