from pydantic import BaseModel,Field
from typing import List

class GenerationInstructions(BaseModel):
    platform: str="android"
    language:str="kotlin"
    architecture:str="mvvm"

class GenerateRequest(BaseModel):
    user_story: str=Field(min_length=5)
    instructions:GenerationInstructions

class GeneratedFile(BaseModel):
    path:str 
    type:str 
    content:str 

class GeneratedApplication(BaseModel):
    files:List[GeneratedFile]
    dependencies:List[str]=[]

class Screen(BaseModel):
    name:str
    route:str 
    description: str

class Component(BaseModel):
    name:str 
    description:str 

class GeneratedApplication(BaseModel):
    app_name:str
    platform:str 
    framework:str 
    description:str 
    screens:list[Screen]
    components:list[Component]


