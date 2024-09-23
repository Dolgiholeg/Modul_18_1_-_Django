from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Max', 'Tom', 'Anna', 'Alex']

def sign_up_by_html(request):
    info = {'error': []}
    i = 0
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if age is None:
            # Обработайте ситуацию, например, верните сообщение об ошибке или установите значение по умолчанию
            return render(request, 'registration_page.html', {'error': 'Age is required'})
        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')
        elif username in users:
            i +=1
            info[f'error {i}'] = HttpResponse('Пользователь уже существует')
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            i +=1
            info[f'error {i}'] = HttpResponse('Пароли не совпадают')
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            i +=1
            info[f'error {i}'] = HttpResponse(f'Вы должны быть старше 18 лет')
            return HttpResponse(f'Вы должны быть старше 18 лет')

    context = {'info':info}
    return render(request, 'registration_page.html', context)




# def sign_up_by_django(request):
#     info = {'error': []}
#     i = 0
#     if request.method == "POST":
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#             if username not in users and password == repeat_password and int(age) >= 18:
#                 users.append(username)
#                 return HttpResponse(f'Приветствуем {username}')
#             elif username in users:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse('Пользователь уже существует')
#                 print(info[f'error {i}'])
#                 return HttpResponse('Пользователь уже существует')
#             elif password != repeat_password:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse('Пароли не совпадают')
#                 print(info[f'error {i}'])
#                 return HttpResponse('Пароли не совпадают')
#             elif int(age) < 18:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse(f'Вы должны быть старше 18 лет')
#                 return HttpResponse(f'Вы должны быть старше 18 лет')
#     else:
#         form = UserRegister()
#         context = {'info': info, 'form': form}
#         return render(request, 'registration_page.html', context)