import os
import streamlit as st
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials, APIClient

load_dotenv()

API_KEY = st.secrets.get("IBM_API_KEY", os.getenv("IBM_API_KEY"))
URL = st.secrets.get("WATSONX_URL", os.getenv("WATSONX_URL"))
SPACE_ID = st.secrets.get("SPACE_ID", os.getenv("SPACE_ID"))
DEPLOYMENT_ID = st.secrets.get("DEPLOYMENT_ID", os.getenv("DEPLOYMENT_ID"))


def get_farming_advice(question):

    credentials = Credentials(
        url=URL,
        api_key=API_KEY
    )

    client = APIClient(credentials)

    client.set.default_space(SPACE_ID)

    payload = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }

    result = client.deployments.run_ai_service(
        DEPLOYMENT_ID,
        payload
    )

    if "error" in result:
        raise Exception(result["error"])
    try:
        return result["choices"][0]["message"]["content"]
    except:
        try:
            return result["body"]["choices"][0]["message"]["content"]
        except:
            return str(result)

    try:
        return result["body"]["choices"][0]["message"]["content"]

    except Exception:
        return str(result)


if __name__ == "__main__":

    question = """
    Explain rice blast disease.
    """

    answer = get_farming_advice(question)

    print(answer)