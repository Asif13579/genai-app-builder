from .schemas import GenerateRequest

SYSTEM_PROMPT="""
You are an expert Android application generator.

Your task is to convert a user story into application source files.

Generate production-quality starter code.

The application uses:
- Android
- Kotlin
- MVVM architecture

Return ONLY the requested structured response.

Do not return markdown.
Do not return explanations.
Do not return code fences.

Every generated file must have:
- path
- type
- content

Do not generate files outside the application project.
"""

def build_prompt(request:GenerateRequest) -> str:
    return f"""
USER STORY:

{request.user_story}

TECHNICAL REQUIREMENTS:

Platform:
{request.instructions.platform}

Language:
{request.instructions.language}

Architecture:
{request.instructions.architecture}


Generate the required application files.

For a login screen, for example, you may need:

- XML layout
- Activity
- ViewModel
- API interface

Only generate files that are relevant to the user story.
"""

