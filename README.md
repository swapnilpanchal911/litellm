# Setup LiteLLM locally using Docker
Get the code
**curl -O https://raw.githubusercontent.com/BerriAI/litellm/main/docker-compose.yml**
**curl -O https://raw.githubusercontent.com/BerriAI/litellm/main/prometheus.yml**

Add the master key - you can change this after setup
**echo 'LITELLM_MASTER_KEY="sk-1234"' > .env**


Add the litellm salt key - you cannot change this after adding a model
It is used to encrypt / decrypt your LLM API Key credentials
We recommend - https://1password.com/password-generator/ 
password generator to get a random hash for litellm salt key
**echo 'LITELLM_SALT_KEY="sk-1234"' >> .env**

**source .env**

Start
**docker compose up**
