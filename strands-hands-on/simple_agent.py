from strands import Agent
from strands.models.gemini import GeminiModel

model = GeminiModel(
    client_args={
        "api_key": "",
    },
    model_id="gemini-2.5-flash",
    params={ 
        "temperature": 0.7,
        "max_output_tokens": 2048,
        "top_p": 0.9,
        "top_k": 40
    }
)

agent = Agent(model=model)
response = agent("What is Agentic AI in 25 words ?")