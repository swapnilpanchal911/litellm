from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    openai_api_base="http://localhost:4000",
    openai_api_key="", #add your api key here
    model = "gemini/gemini-flash-lite-latest",
    temperature=0.1
)

messages = [
    SystemMessage(
        content="You are a helpful python assistant."
    ),
    HumanMessage(
        content="how to install python on macos?"
    ),
]
response = chat(messages)

print(response)
