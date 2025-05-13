import ollama

# create a new model with modelfile

modelfile = """
FROM llama3.2
SYSTEM You are very smart assistant who knows everything about ocean
PARAMETER temperature 0.1
"""

#Creating the new llm with modelfile
ollama.create(model="knowall", modelfile=modelfile§)

## Now we can go ahead and generate something
res = ollama.generate(model="knowall", prompt="why is the ocean so salty")

print(res["response"])