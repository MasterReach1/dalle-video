from openai import OpenAI

client = OpenAI(
    api_key="PUT API KEY HERE"
)

response = client.images.generate(
  model="dall-e-3",
  prompt="victorian-style coffee mug",
  size="1024x1024",
  quality="standard",
)

image_url = response.data[0].url
print(image_url)