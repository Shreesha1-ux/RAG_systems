import os  #
from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings  #embeddign model
from langchain_chroma import Chroma  #chroma vecto database like chroma is good
from dotenv import load_dotenv

load_dotenv()