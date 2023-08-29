from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def heads_tails(request):
    result = 'HEADS' if randint(0, 1) else 'TAILS'
    logger.info(f'{result}')
    return HttpResponse(result)


def cub(request):
    result = randint(1, 6)
    logger.info(f'{result}')
    return HttpResponse(result)


def rand_num(request):
    result = randint(1, 100)
    logger.info(f'{result}')
    return HttpResponse(result)
