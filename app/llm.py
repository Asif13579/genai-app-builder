import os

from openai import AsyncOpenAI
from .prompts import SYSTEM_PROMPT,build_prompt
from .schemas import GenerateRequest,GeneratedApplication
from dotenv import load_dotenv

load_dotenv()

class OpenAIProvider:
    def __init__(self):
        self.client=AsyncOpenAI(api_key=os.getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1")

    async def generate(self,request:GenerateRequest) -> GeneratedApplication:
        prompt=build_prompt(request)

        response=await self.client.responses.parse(model=os.getenv("MODEL"),input=
        [
            {"role":"system",'content':SYSTEM_PROMPT},{"role":"user","content":prompt}
        ],text_format=GeneratedApplication)
        return response.output_parsed

