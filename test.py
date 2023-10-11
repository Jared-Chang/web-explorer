from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

BASE_URL = "https://chatbot-testing.openai.azure.com/"
API_KEY = "efa828c00f4140eabfa14793d6f479b2"
DEPLOYMENT_NAME = "gpt35-16k"

model = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
)

print(model(
    [
        HumanMessage(
            content="Translate this sentence from English to French. I love programming."
        )
    ]
))
