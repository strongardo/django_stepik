from pathlib import Path

from django.shortcuts import render, redirect

app_dir = Path(__file__).resolve().parent
file_path = app_dir / "words.txt"

def read_from_file():
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    words1 = []
    words2 = []
    for line in lines:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2


def add_to_file(word1: str, word2: str):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def home_page(request):
    if request.path == '/':
        return redirect('home')
    return render(request, 'mainapp/home.html')


def words_list_page(request):
    words1, words2 = read_from_file()
    words = zip(words1, words2)
    return render(request, 'mainapp/list.html', {'words': words})


def add_word_page(request):
    if request.method == "POST":
        word1 = request.POST["word1"]
        word2 = request.POST["word2"]
        add_to_file(word1, word2)
        return redirect('home')
    return render(request, 'mainapp/add.html')
