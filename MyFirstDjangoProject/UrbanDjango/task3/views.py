from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def main_page_index(request):
    title = 'platform'
    main_h1_text = 'Главная страница'
    main_page_link_text = 'Главная'
    catalog_page_link_text = 'Магазин'
    cart_page_link_text = 'Корзина'
    context = {
        'title': title,
        'main_h1_text': main_h1_text,
        'main_page_link_text': main_page_link_text,
        'catalog_page_link_text': catalog_page_link_text,
        'cart_page_link_text': cart_page_link_text
    }
    return render(request, 'third_task/main_page.html', context)

def catalog_page_index(request):
    title = 'games'
    catalog_h1_text = 'Игры'
    game1_text = 'Atomic Heart'
    game2_text = 'Cyberpunk 2077'
    game3_text = 'PayDay 2'
    return_text = 'Вернуться обратно'
    button_text = 'Купить'
    context = {
        'title': title,
        'catalog_h1_text': catalog_h1_text,
        'game1_text': game1_text,
        'game2_text': game2_text,
        'game3_text': game3_text,
        'button_text': button_text,
        'return_text': return_text
    }
    return render(request, 'third_task/catalog_page.html', context)

def cart_page_index(request):
    title = 'cart'
    cart_h1_text = 'Извините, ваша корзина пуста'
    return_text = 'Вернуться обратно'
    context = {
        'title': title,
        'cart_h1_text': cart_h1_text,
        'return_text': return_text
    }
    return render(request, 'third_task/cart_page.html', context)

