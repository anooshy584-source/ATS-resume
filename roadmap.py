
import streamlit as st
from groq import (
    Groq,
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIStatusError
)


def generate_roadmap(field, level, weeks, hours, api_key):

    client = Groq(api_key=api_key)

    prompt = f"""
    Create a personalized learning roadmap.

    Field: {field}
    Skill level: {level}
    Duration: {weeks} weeks
    Available study hours per week: {hours}

    Include:
    1. Learning goals
    2. Weekly topics in learning order
    3. Practical exercises
    4. A final project
    5. Free learning resources
    6. A progress checklist

    Use simple language and a realistic schedule.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert learning roadmap planner."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=3000
        )

        return response.choices[0].message.content

    except AuthenticationError:
        raise RuntimeError(
            "Invalid API key. Check your GROQ_API_KEY in Streamlit Secrets."
        )

    except RateLimitError:
        raise RuntimeError(
            "Groq API rate limit reached. Check your Groq Console limits."
        )

    except APIConnectionError:
        raise RuntimeError(
            "Could not connect to Groq. Check your internet connection."
        )

    except APIStatusError as e:
        raise RuntimeError(
            f"Groq API returned HTTP {e.status_code}. "
            "Check the model and API access in Groq Console."
        )
