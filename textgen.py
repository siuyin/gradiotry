# from transformers import pipeline
# pipeline = pipeline("text-generation", model="google/gemma-3-1b-it", device=-1)
# print(pipeline("How many planets are there?",max_length=500,truncation=True))

# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="google/gemma-3-1b-it")
res = pipe(messages)
print(res)