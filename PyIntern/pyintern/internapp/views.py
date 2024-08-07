from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from . import main


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
                # Обработка данных, введенных пользователем
            result = process_user_input(user_input)
            return HttpResponse(f'Processed input: {result}')
    else:
        form = InputForm()

    return render(request, 'internapp/dataForm.html', {'form': form})

def process_user_input(input_data):
    main.f = input_data
    o_vid = main.RunningText()
    o_vid.construct()
    main.db.input_psql(main.f)
    return input_data.upper()