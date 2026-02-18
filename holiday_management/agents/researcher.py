from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

researcher_agent = AssistantAgent(
    name="Holiday_Researcher",
    description="A holiday researcher agent that helps users research about their holiday destinations.",
    model_client=model_client,
    system_message="""
    You are a Holiday Researcher.
    Provide ONLY additional useful information.
    Do NOT repeat the planner.
    Keep responses under 8 bullet points.
    Be concise and practical.
    No summaries.
    """
)