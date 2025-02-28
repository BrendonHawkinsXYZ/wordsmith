# Word Smith - Local Prompt Testing Tool

A lightweight, local tool for structured, real-time prompt comparison and optimization for LLM-based products.

## Features

- **Simple UI**: Clean interface with global input and two prompt testing areas
- **Multi-model Support**: Test prompts across different models (OpenAI GPT and Anthropic Claude)
- **Customizable Parameters**: Adjust temperature, top-p, and token limits for each prompt
- **Real-time Comparison**: Side-by-side output comparison with difference highlighting
- **Export Functionality**: Generate PDF reports of your prompt testing results
- **Self-Contained**: Runs locally with minimal dependencies

## Tech Stack

- **Frontend**: Vanilla JavaScript (no frameworks)
- **Backend**: FastAPI
- **Model Integration**: OpenAI GPT-4o and Anthropic Claude
- **PDF Generation**: jsPDF

## Installation & Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your API keys as environment variables:
   ```
   # For Windows
   set OPENAI_API_KEY=your_openai_api_key_here
   set ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # For macOS/Linux
   export OPENAI_API_KEY=your_openai_api_key_here
   export ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```
4. Create necessary directories:
   ```
   mkdir -p static templates
   ```
5. Move the `index.html` file to the `static` directory

## Running the Application

1. Start the FastAPI server:
   ```
   python main.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Usage Instructions

1. **Global Input**: Add context that applies to both prompts
2. **Model Settings**: Click the Settings button to configure:
   - Model selection (GPT-3.5, GPT-4o, or Claude)
   - Temperature (0-1)
   - Top-p value (0-1)
   - Maximum token output
3. **Prompts**: Enter two different prompts for comparison
4. **Run Comparison**: Process both prompts and view the outputs with differences highlighted
5. **Clear**: Reset all fields
6. **Save**: Export the results as a PDF document

## Project Structure

```
.
├── main.py            # FastAPI backend with OpenAI and Anthropic integration
├── requirements.txt   # Python dependencies
├── static/            # Static files directory
│   └── index.html     # Frontend HTML file
└── templates/         # Template directory for Jinja2
```

## Dependencies

- fastapi
- uvicorn
- openai
- anthropic
- jinja2

## Notes

- The application is designed for local use only and does not include authentication or security measures
- API keys for both OpenAI and Anthropic are required and should be set as environment variables
- The UI is optimized for desktop use but is responsive for other devices
