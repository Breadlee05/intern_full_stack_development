from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Question
import requests
import os
from dotenv import load_dotenv
import json

import requests

def get_ai_answer(question):
    """Get answer from Groq Free AI (LLaMA 3)"""
    try:
        load_dotenv()  
        api_key = os.getenv("GROQ_API_KEY")  

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an expert in electrical machines including "
                        "DC motors, AC motors, induction motors, synchronous motors, transformers, "
                        "generators, and machine principles. Provide clear, accurate, technical answers."
                    )
                },
                {"role": "user", "content": question}
            ],
            "temperature": 0.5,
            "max_tokens": 300
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" not in result:
            return f"API Error: {result}"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"



def home(request):
    """Render the home page"""
    return render(request, "home.html")


@login_required
def ask_question(request):
    if request.method == "POST":
        question_text = request.POST.get("question", "").strip()
        
        if not question_text:
            messages.error(request, "Please enter a question.")
            return redirect('/ask/')
        
        
        answer = get_ai_answer(question_text)

    
        Question.objects.create(
            user=request.user,
            question_text=question_text,
            answer_text=answer,
            category="Electrical Machines"
        )

    
        request.session['last_question'] = question_text
        request.session['last_answer'] = answer

        return redirect('/ask/')

    # GET request
    last_question = request.session.pop('last_question', None)
    last_answer = request.session.pop('last_answer', None)

    return render(request, "ask_question.html", {
        "question_text": last_question,
        "answer": last_answer
    })


@login_required
def question_history(request):
    """Display user's question history"""
    questions = Question.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "question_history.html", {
        "questions": questions
    })


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/ask/')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    """User logout view"""
    logout(request)
    return redirect('/accounts/login/')
