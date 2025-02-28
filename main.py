from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
from openai import OpenAI, AzureOpenAI
import anthropic

app = FastAPI(title="Word Smith - LLM Prompt Testing Tool")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a directory for static files if it doesn't exist
os.makedirs("static", exist_ok=True)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define request model with settings
class PromptRequest(BaseModel):
    global_input: str
    prompt1: str
    prompt2: str
    settings1: Dict[str, Any]
    settings2: Dict[str, Any]

# Initialize OpenAI client - API key should be set in environment variable OPENAI_API_KEY
client_openai = OpenAI()

# Initialize Azure OpenAI client - API key, endpoint, and other settings should be set in environment variables
client_azure = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize Anthropic client - API key should be set in environment variable ANTHROPIC_API_KEY
client_anthropic = anthropic.Anthropic()

# Function to get completion from OpenAI
def get_openai_completion(prompt_text, settings):
    try:
        completion = client_openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt_text}],
            temperature=settings.get("temperature", 0.7),
            top_p=settings.get("top_p", 1.0),
            max_tokens=settings.get("max_tokens", 1000)
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

# Function to get completion from Azure OpenAI
def get_azure_openai_completion(prompt_text, settings):
    try:
        # Get the deployment name from settings or use a default
        deployment_name = settings.get("deployment_name", "gpt-4")
        
        completion = client_azure.chat.completions.create(
            model=deployment_name,  # This is the deployment name in Azure
            messages=[{"role": "user", "content": prompt_text}],
            temperature=settings.get("temperature", 0.7),
            top_p=settings.get("top_p", 1.0),
            max_tokens=settings.get("max_tokens", 1000)
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Azure OpenAI API error: {str(e)}")

# Function to get completion from Anthropic
def get_anthropic_completion(prompt_text, settings):
    try:
        completion = client_anthropic.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=settings.get("max_tokens", 1000),
            temperature=settings.get("temperature", 0.7),
            top_p=settings.get("top_p", 1.0),
            messages=[
                {"role": "user", "content": prompt_text}
            ]
        )
        return completion.content[0].text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Anthropic API error: {str(e)}")

# Function to get completion based on model selection
def get_completion(prompt_text, settings):
    model = settings.get("model", "openai")
    
    if model == "openai":
        return get_openai_completion(prompt_text, settings)
    elif model == "azure":
        return get_azure_openai_completion(prompt_text, settings)
    elif model == "anthropic":
        return get_anthropic_completion(prompt_text, settings)
    else:
        raise HTTPException(status_code=400, detail=f"Unknown model: {model}")

# We'll remove the server-side comparison since we've moved this to the client side
# The frontend will handle the text comparison with diff_match_patch.js
def compare_texts(text1, text2):
    # This function is kept for compatibility but no longer used
    return ""

# API endpoint for processing prompts
@app.post("/api/process")
async def process_prompts(request: PromptRequest):
    # Structure the prompts with prompt text first, then the global input without labels
    full_prompt1 = f"{request.prompt1}\n\n{request.global_input}"
    full_prompt2 = f"{request.prompt2}\n\n{request.global_input}"
    
    # Log the prompts being sent (for debugging)
    print(f"Sending Prompt 1 to {request.settings1.get('model', 'openai')}:\n{full_prompt1}\n")
    print(f"Sending Prompt 2 to {request.settings2.get('model', 'openai')}:\n{full_prompt2}\n")
    
    # Get completions from the selected models
    output1 = get_completion(full_prompt1, request.settings1)
    output2 = get_completion(full_prompt2, request.settings2)
    
    # Generate comparison
    comparison = compare_texts(output1, output2)
    
    return {
        "output1": output1,
        "output2": output2,
        "comparison": comparison,
        "full_prompt1": full_prompt1,  # Return the full prompts for display
        "full_prompt2": full_prompt2
    }

# Serve the index.html page
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
