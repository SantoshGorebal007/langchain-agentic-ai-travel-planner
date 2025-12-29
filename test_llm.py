from src.llm.groq_client import GroqLLM

llm = GroqLLM()

response = llm.generate(
    prompt="Say hello in one clear sentence."
)

print(response)
