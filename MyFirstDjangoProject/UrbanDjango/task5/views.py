from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

def sign_up_by_html(request):
    users = ['Fedor', 'Max', 'Vovan']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        try:
            age = int(age)  # Преобразуем возраст в число
        except ValueError:
            info['error'] = 'Возраст должен быть числом.'
            return render(request, './fifth_task/registration_page.html', context={'info': info})

        if password == repeat_password:
            if age >= 18:
                if username not in users:
                    users.append(username)
                    return HttpResponse(f'Приветствуем, {username}!')
                else:
                    info['error'] = f'Пользователь уже существует: user - {username}'
            else:
                info['error'] = f'Вы должны быть старше 18 лет: age - {age}'
        else:
            info['error'] = f'Пароли не совпадают: password - {password}, repeat_password - {repeat_password}'
    else:
        info['error'] = 'Форма заполнена некорректно. Проверьте данные.'
    
    return render(request, './fifth_task/registration_page.html', context={'info': info})



def sign_up_by_django(request):
    users = ['Fedor', 'Max', 'Vovan']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            
            # --- Обработка после POST
            try:
                age = int(age)  # Преобразуем возраст в число
            except ValueError:
                info['error'] = 'Возраст должен быть числом.'
                return render(request, './fifth_task/registration_page.html', context={'info': info, 'form': form})

            if password == repeat_password:
                if age >= 18:
                    if username not in users:
                        users.append(username)
                        return HttpResponse(f'Приветствуем, {username}!')
                    else:
                        info['error'] = f'Пользователь уже существует: user - {username}'
                else:
                    info['error'] = f'Вы должны быть старше 18 лет: age - {age}'
            else:
                info['error'] = f'Пароли не совпадают: password - {password}, repeat_password - {repeat_password}'
        else:
            info['error'] = 'Форма заполнена некорректно. Проверьте данные.'

    else:
        form = UserRegister()  # Пустая форма для GET-запроса
    
    return render(request, './fifth_task/registration_page.html', context={'info': info, 'form': form})