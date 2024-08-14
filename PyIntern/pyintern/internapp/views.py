from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import InputForm
from . import main
import os


def last_file_f():
    directory = '//conent'
    files = os.listdir(directory)
    files = [os.path.join(directory, f) for f in files]
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
                # Обработка данных, введенных пользователем
            result = process_user_input(user_input)
            return FileResponse(open(last_file_f(), 'r+b'), as_attachment=True, filename='vid.mp4')
    else:
        form = InputForm()

    return render(request, 'internapp/dataForm.html', {'form': form})

def process_user_input(input_data):
    main.f = input_data
    o_vid = main.RunningText()
    o_vid.construct()
    #main.db.input_psql(main.f)
    return input_data.upper()
