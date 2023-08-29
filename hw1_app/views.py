from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def first_site(request):
    form = """
        <ul class="nav nav-pills justify-content-end align-items-end">
        <li class="nav-item"><a href="/hw/site/"
                                class="nav-link">Главная</a></li>
        <li class="nav-item"><a href="/hw/about/"
                                class="nav-link">О себе</a></li>
        <li class="nav-item"><a href="/hw/contacts/"
                                class="nav-link">Контакты</a></li>
        </ul>
        <form method=post enctype=multipart/form-data>
        <h1>Мой первый сайт на Django</h1>
        </form>
        """
    logger.info('Visited home page')
    return HttpResponse(form)


def about(request):
    form = """
        <form method=post enctype=multipart/form-data>
        <li class="nav-item"><a href="/hw/site/"
        class="nav-link">Главная</a></li>
        <h1>Меня зовут Галина</h1>
        <h2>Я люблю путешествовать</h2>
        </form>
        """
    logger.info('Visited the page about yourself')
    return HttpResponse(form)


def contacts(request):
    form = """<div class="row">
    <li class="nav-item"><a href="/hw/site/"
        class="nav-link">Главная</a></li>
        <h1>Contact: </h1>
        <p>Email: pol@mail.ru</p>
        <p>Phone: +7-999-777-11-11</p>
    </div>
    """
    logger.info('Visited the page contacts')
    return HttpResponse(form)
