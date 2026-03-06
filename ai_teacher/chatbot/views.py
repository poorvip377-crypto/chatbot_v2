import os
from dotenv import load_dotenv
from google import genai
from django.shortcuts import render

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)


def home(request):

    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        answer = response.text

    return render(request, "index.html", {"answer": answer})
print(api_key)