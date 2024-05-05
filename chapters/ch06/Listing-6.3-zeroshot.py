import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_version="2022-12-01",
    api_key=os.getenv("AOAI_KEY")
)

prompt_startphrase = "Translate the following to Spanish: I have a small dog called Champ."

response = client.completions.create(
    model="dv3",
    prompt=prompt_startphrase,
    temperature=0.8,
    max_tokens=100,
    stop=None)

#responsetext = response["choices"][0]["text"]
responsetext = response.choices[0].text

print("Prompt:" + prompt_startphrase + "\nResponse:" + responsetext)
