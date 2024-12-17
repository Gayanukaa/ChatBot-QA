# API Endpoints

## `/chat` [POST]

- **Description**: Sends user input to the chatbot and retrieves a response.

- **Request Body**:

  ```json
  {
      "user_input": "Your question here"
  }
  ```
  
## Environment Variables

The following environment variables are required for the chatbot to interact with Azure OpenAI:

- **AZURE_OPENAI_API_KEY**: Your Azure OpenAI API key.
- **AZURE_OPENAI_DEPLOYMENT_NAME**: The deployment name configured in your Azure OpenAI resource.
- **AZURE_OPENAI_ENDPOINT**: The endpoint URL for your Azure OpenAI resource, e.g., `https://<your-resource-name>.openai.azure.com/`.
- **OPENAI_API_VERSION**: The API version, e.g., `2023-06-01-preview`.
