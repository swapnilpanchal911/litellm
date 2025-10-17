# Pre-requisite

docker setup on local machine

# Setup LiteLLM locally using Docker

1) Get the code

**curl -O https://raw.githubusercontent.com/BerriAI/litellm/main/docker-compose.yml**

**curl -O https://raw.githubusercontent.com/BerriAI/litellm/main/prometheus.yml**

2) Add the master key - you can change this after setup

**echo 'LITELLM_MASTER_KEY="sk-1234"' > .env**

**echo 'LITELLM_SALT_KEY="sk-1234"' >> .env**

3) **source .env**

4) Start

**docker compose up**
