# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="mixtral-8x7b-32768")
#
#
# if __name__ == "__main__":
#     response = llm.invoke("Two most important ingradient in samosa are ")
#     print(response.content)
#
#
#
#









from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="qwen/qwen3.6-27b"  # Using an available model
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are")
    print(response.content)