from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

planner_agent = AssistantAgent(
    name="Holiday_Planner",
    description="A Holiday planner agent that helps users plan their trips.",
    model_client=model_client,
    system_message="""
    are a Holiday Planner.
    Give concise, structured travel plans.
    Avoid repetition.
    Do NOT repeat what other Youagents say.
    Limit response to max 10 bullet points.
    Be clear, direct, and practical.
    """
)