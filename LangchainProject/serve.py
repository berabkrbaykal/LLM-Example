from dotenv import load_dotenv
from langchain_openai import  ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes


load_dotenv()
model = ChatOpenAI(temperature=0.1)
#messages = [
#    SystemMessage("Translate the following English to Spanish"),
#    HumanMessage("Hi!"),
#]

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)

parser = StrOutputParser()
chain = prompt_template | model | parser

app = FastAPI(
    title="Translator",
    description="Translated Chat Server",
    version="1.0.0",
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)