from django.shortcuts import render


def главная_view(request):
    title = 'мой сайт начало'
    text = 'Главная страница'
    context = {'title': title, 'text': text}
    return render(request, 'Главная.html', context)

def магазин_view(request):
    title = 'мой сайт магазин'
    text = 'Магазин'
    games = ['S.T.A.L.K.E.R.: Чистое Небо', 'S.T.A.L.K.E.R.: Зов Припяти', 'S.T.A.L.K.E.R.2: Сердце Чернобыля']
    text4 = 'ВЕРНУТЬСЯ НА ГЛАВНУЮ'
    text5 = 'КУПИТЬ'
    context = {'title': title, 'text': text, 'games': games, 'text4': text4, 'text5': text5}
    return render(request, 'Магазин.html', context)

def корзина_view(request):
    title = 'мой сайт корзина'
    text = 'Корзина'
    text1 = 'Выбрано товаров:'
    text2 = 'Первый товар'
    text3 = 'Второй товар'
    text4 = 'ВЕРНУТЬСЯ НА ГЛАВНУЮ'
    text5 = 'ОПЛАТИТЬ'
    text6 = 'УДАЛИТЬ'
    context = {'title': title, 'text': text, 'text1': text1, 'text2': text2, 'text3': text3, 'text4': text4,
               'text5': text5, 'text6': text6}
    return render(request, 'Корзина.html', context)
