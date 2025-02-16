from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)
#response=llm.invoke("What is groq?")
#print("response:",response.content)

try:
    n = int(input("Enter the number of queries you want to ask: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        for i in range(n):
            user_prompt = input("Enter query : ")
            try:
                response = llm.invoke(user_prompt)
                print("Response :", response.content)
            except Exception as e:
                print("Error in query :", e)

except ValueError:
    print("Invalid input! Please enter a valid number.")