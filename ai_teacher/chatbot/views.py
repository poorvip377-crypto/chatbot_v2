<<<<<<< HEAD
import os
from dotenv import load_dotenv
from google import genai
from django.shortcuts import render

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)
=======
from django.shortcuts import render
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
>>>>>>> 1599528dc1b563fe6c53fb9c4039f8961d63a1a4


def home(request):

    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        answer = response.text

<<<<<<< HEAD
    return render(request, "chatbot/index.html", {"answer": answer})
print(api_key)
=======
    return render(request, "index.html", {"answer": answer})
>>>>>>> 1599528dc1b563fe6c53fb9c4039f8961d63a1a4
