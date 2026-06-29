from app.config import OLLAMA_MODEL

from app.platform.llm import LocalLLM


llm = LocalLLM(
    OLLAMA_MODEL
)

response = llm.generate(

    "Say Hello."

)

print(response)