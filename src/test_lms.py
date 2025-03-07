import lmstudio as lms

model = lms.llm("meta-llama-3.1-8b-instruct")
result = model.respond("What is the meaning of life?")

print(result)