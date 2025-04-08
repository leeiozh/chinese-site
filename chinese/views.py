from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Character
from .forms import CharacterForm


def home(request):
    total = Character.objects.count()
    return render(request, 'chinese/home.html', {'total': total})


def add_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Character added!')
            return redirect('add')
    else:
        form = CharacterForm()
    return render(request, 'chinese/add.html', {'form': form})


def practice(request):
    if request.method == 'POST':
        user_translation = request.POST.get('translation')
        char_id = request.POST.get('char_id')

        try:
            character = Character.objects.get(id=char_id)
        except Character.DoesNotExist:
            return render(request, 'chinese/practice.html', {'result': 'error', 'character': None})

        if user_translation.strip().lower() == character.translation.strip().lower():
            result = 'correct'
            character.correct_count += 1
        else:
            result = 'incorrect'
            character.incorrect_count += 1
        character.save()

        request.session["last_character_id"] = character.id

        queryset = Character.objects.all()
        if queryset.count() > 1:
            queryset = queryset.exclude(id=character.id)
        new_character = queryset.order_by('?').first()

        return render(request, 'chinese/practice.html', {
            'result': result,
            'character': new_character
        })

    else:
        character = Character.objects.order_by('?').first()
        return render(request, 'chinese/practice.html', {'character': character})


def stats(request):
    characters = Character.objects.all()

    if request.method == 'POST':
        if 'reset' in request.POST:
            for char in characters:
                char.correct_count = 0
                char.incorrect_count = 0
                char.save()
            messages.success(request, "Stats reset :(")
        elif 'delete_id' in request.POST:
            char_id = request.POST.get('delete_id')
            Character.objects.filter(id=char_id).delete()
            messages.success(request, "Character deleted!")

        characters = Character.objects.all()

    return render(request, 'chinese/stats.html', {'characters': characters})


def dictionary(request):
    characters = Character.objects.all()
    return render(request, 'chinese/dictionary.html', {'characters': characters})
