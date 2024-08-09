import autogen
from autogen import AssistantAgent, Agent, UserProxyAgent, ConversableAgent
from autogen.code_utils import DEFAULT_MODEL, UNKNOWN, content_str, execute_code, extract_code
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-pro"],
    },
)
assistant = AssistantAgent(
    "assistant", llm_config={"config_list": config_list_gemini, "seed": 42}, max_consecutive_auto_reply=6
)
user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding", "use_docker": False},
    human_input_mode="NEVER",
    is_termination_msg=lambda x: content_str(x.get("content")).find("TERMINATE") >= 0,
)
user_proxy.initiate_chat(assistant, message="""
    Do an overall market sentiment analysis in USA for past 1 week by taking into account the news articles and social media posts.Also check for macro economic indicators , how did foreign markets perform and what are the major events that happened in the past week.
    Also what are the overall trend of sectors. Find sentiment of those stocks. Finally write an about 500 word article for above sentiment and researches.
                         
""")