# Word Smith - Local Prompt Testing Tool

A lightweight, local tool for structured, real-time prompt comparison and optimization for LLM-based products.

## Features

- **Simple UI**: Clean interface with instruction field, global input, and two prompt testing areas
- **Real-time Comparison**: Side-by-side output comparison with difference highlighting
- **Export Functionality**: Generate PDF reports of your prompt testing results
- **Self-Contained**: Runs locally with minimal dependencies

## Tech Stack

- **Frontend**: Vanilla JavaScript (no frameworks)
- **Backend**: FastAPI
- **Model Integration**: OpenAI GPT-4o
- **PDF Generation**: jsPDF

## Installation & Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   ```
   # For Windows
   set OPENAI_API_KEY=your_api_key_here
   
   # For macOS/Linux
   export OPENAI_API_KEY=your_api_key_here
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

1. **Instructions Field**: Enter model behavior instructions
2. **Global Input**: Add context that applies to both prompts
3. **Prompts**: Enter two different prompts for comparison
4. **Submit**: Process both prompts and view the outputs
5. **Clear**: Reset all fields
6. **Save**: Export the results as a PDF document

## Project Structure

```
.
├── main.py            # FastAPI backend
├── requirements.txt   # Python dependencies
├── static/            # Static files directory
│   └── index.html     # Frontend HTML file
└── templates/         # Template directory for Jinja2
```

## Notes

- The application is designed for local use only and does not include authentication or security measures
- Only one model (GPT-4o) is supported
- The API key is hardcoded in the backend for simplicity
