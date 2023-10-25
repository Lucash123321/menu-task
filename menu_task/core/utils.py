from django.urls import NoReverseMatch
from django.urls import reverse
import re


class URLHandler:
    def __init__(self):
        pass

    @staticmethod
    def convert_url(url, request):
        try:
            url = reverse(url)

        except NoReverseMatch:
            if f'{request.scheme}://{request.get_host()}' in url:
                url = re.sub(f'{request.scheme}://{request.get_host()}', '', url)

            elif url[0] != '/':
                url = '/' + url

            else:
                url = url

            if url[-1] != '/':
                url += '/'

        return url
