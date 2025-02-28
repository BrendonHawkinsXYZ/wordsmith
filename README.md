# Word Smith - LLM Prompt Testing Tool

Word Smith is an open source tool for testing and comparing different prompts across various settings. It allows you to visualize and analyze the differences between responses, helping you refine your prompting techniques.

## Features

- Compare outputs from different LLM providers side-by-side
- Highlight differences between responses
- Configure model parameters (temperature, top_p, etc.)
- Support for multiple providers:
  - OpenAI (GPT-4o)
  - Azure OpenAI
  - Anthropic (Claude)
- Export results to PDF
- Simple and intuitive interface

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- OpenAI API key (for OpenAI models)
- Azure OpenAI API key and endpoint (for Azure OpenAI models)
- Anthropic API key (for Claude models)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/word-smith.git
   cd word-smith
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # OpenAI API key
   export OPENAI_API_KEY="your-openai-api-key"
   
   # Azure OpenAI credentials
   export AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
   export AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
   export AZURE_OPENAI_API_VERSION="2023-05-15"  # Optional, defaults to this version
   
   # Anthropic API key
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:8000`

## Usage

### Basic Workflow

1. Enter your base text in the "Global Input" field
2. Select the LLM providers and configure settings for each prompt
3. Enter two different prompts to compare
4. Click "Run Comparison" to send the prompts to the selected models
5. View the highlighted differences in the output panels
6. Export the results to PDF if needed

### Configuring Azure OpenAI

To use Azure OpenAI:

1. Select "Azure OpenAI" from the model dropdown
2. Enter your deployment name (the name you gave to your model in Azure)
3. Set temperature and top_p values
4. Enter your prompts and run the comparison

> **Note**: Make sure you have properly set up your Azure OpenAI service and deployed at least one model before using this feature.

## Architecture

The application consists of:

- FastAPI backend (`main.py`) for handling API requests to various LLM providers
- HTML/CSS/JavaScript frontend (`static/index.html`) for the user interface
- PDF export functionality using jsPDF

## API Endpoints

- `GET /`: Serves the main application page
- `POST /api/process`: Processes prompt requests and returns completions from selected models

## Troubleshooting

### Common Issues

- **API Key Issues**: Ensure all required API keys are properly set as environment variables
- **Azure OpenAI Errors**: Verify that your deployment name exactly matches what's set up in your Azure portal
- **Model Availability**: Make sure you have access to the requested models in your subscription

## Development

### Project Structure

```
word-smith/
├── main.py                # FastAPI backend
├── static/                # Static files
│   └── index.html         # Main application interface
├── templates/             # Jinja2 templates (if used)
└── requirements.txt       # Python dependencies
```

### Adding New LLM Providers

To add a new LLM provider:

1. Create a client initialization in `main.py`
2. Add a completion function for the new provider
3. Update the `get_completion` function to route to the new provider
4. Add the provider to the frontend model selection dropdowns
5. Add any provider-specific settings to the UI

## License

[MIT License](LICENSE)

## Acknowledgments

- FastAPI for the backend framework
- OpenAI, Azure, and Anthropic for their LLM APIs
- jsPDF for PDF generation
- diff_match_patch for text comparison
