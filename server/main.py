from fastapi import FastAPI
from pydantic import BaseModel
import json
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import Document
from pymilvus import connections
from llama_index.vector_stores.milvus import MilvusVectorStore
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

load_dotenv()

app = FastAPI()


DATABASE_PATH = './database.json'
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


class FormSubmit(BaseModel):
    age: str


def initialize_food_drive_agent(force_reload=False):
    global agent
    global food_drive_engine
    food_drive_persist_dir = "./storage/food_drive"
    index_loaded = False
    food_drive_index = None
    if not force_reload:
        try:
            storage_context = StorageContext.from_defaults(persist_dir=food_drive_persist_dir)
            food_drive_index = load_index_from_storage(storage_context)
            print("Index loaded")
            index_loaded = True
        except Exception as e:
            print("Index not loaded", e)

    if not index_loaded:
        print("Loading index since it was not loaded or force reload is True.")
        # food_drive_docs = SimpleDirectoryReader(
        #     input_files=[
        #         DATABASE_PATH,
        #     ]
        # ).load_data()

        with open(DATABASE_PATH, "r", encoding="utf-8") as file:
            food_drive_data = json.load(file)
        food_drive_docs = [Document(text=json.dumps(item)) for item in food_drive_data]

        food_drive_index = VectorStoreIndex.from_documents(food_drive_docs)

        food_drive_index = VectorStoreIndex.from_documents(food_drive_docs)
        food_drive_index.storage_context.persist(persist_dir=food_drive_persist_dir)
        print("Index loaded")

    food_drive_engine = food_drive_index.as_query_engine(similarity_top_k=3)

    query_engine_tools = [
        QueryEngineTool(
            query_engine=food_drive_engine,
            metadata=ToolMetadata(
                name="food_drive",
                description=(
                    "A search engine for emergency food resources. ",
                    "with a focus on food drives and food banks.",
                ),
            ),
        ),
    ]

    llm = OpenAI(model="gpt-3.5-turbo-0613")

    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=llm,
        verbose=True,
        # context=context
    )
    return agent

agent = initialize_food_drive_agent(force_reload=False)

class ChatForm(BaseModel):
    question: str

@app.post("/chat")
async def chat(item: ChatForm):
    print("Chatting")
    response = agent.chat(item.question)
    return {"response": str(response)}

class FindSemantic(BaseModel):
    query: str
def query_food_drive_items(query: str) -> list:
    global food_drive_engine
    related_food_drive = food_drive_engine.query(query)
    related_food_drive_json = []
    for node in related_food_drive.source_nodes:
        try:
            text_data = json.loads(node.node.text)
        except json.JSONDecodeError:
            text_data = {}
        related_food_drive_json.append({
            **text_data,
            "_score": node.score
        })
    return related_food_drive_json

@app.post("/find-semantic")
async def find_semantic(form: FindSemantic):
    return query_food_drive_items(form.query)

@app.post("/formsubmit")
async def create_item(form: FindSemantic):
    food_drives = query_food_drive_items(form.query)
    formatted_query = "Format the following food drive items into a response: "
    for item in food_drives:
        item_details = ", ".join([f"{key}: {value}" for key, value in item.items()])
        formatted_query += f"{{ {item_details} }}, "
    llm = OpenAI(model="gpt-3.5-turbo-0613")
    formatted_response = llm.complete(formatted_query)
    return {
        "response": formatted_response, 
        "food_drives": food_drives,
    }

@app.get('/reload_index')
async def reload_index():
    import shutil
    try:
        shutil.rmtree('storage')
        print("Storage folder deleted successfully.")
    except Exception as e:
        print(f"Error deleting storage folder: {e}")
    global agent
    agent = initialize_food_drive_agent(force_reload=True)
    return {"status": "success"}

@app.get("/databases")
async def read_databases():
    print("Reading databases")
    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

@app.get("/scrape")
async def scrape():
    return {"scrape": "scrape"}
