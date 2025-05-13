import ollama


response = ollama.list()


# == Chat Example =======
res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content":"why is the sky blue?"}
    ]
)

#print(res)

# we can also get only the content
print(res["message"]["content"])






# ====Chat example streaming  ========#

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content":"why is the ocean so salty?",
        },
    ],
    stream=True
)
#when we want to stream we have to loop through a for loop using chunk

for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)