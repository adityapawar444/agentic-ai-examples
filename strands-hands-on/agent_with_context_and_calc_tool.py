from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import calculator, http_request

system_prompt = """You are an expert Maths Teacher and your intended audience is students from class 5.
Articulate response is an engaging and friendly way such that it encourages their curiosity in Mathematics.
"""

query="""List down first 10 prime numbers and then calculate thier sum and summarize the history of prime numbers from wikipedia
"""

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

agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[calculator, http_request]
)

response = agent(query)
