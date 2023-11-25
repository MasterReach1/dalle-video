from openai import OpenAI

client = OpenAI(
    api_key="PUT API KEY HERE"
)

response = client.images.create_variation(
  image=open("mug.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url
print(image_url)