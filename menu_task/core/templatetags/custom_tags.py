from django import template
from django.utils.html import format_html
from menu.models import ListItems
from core.utils import URLHandler


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu):
    items = ListItems.objects.filter(menu=menu)
    request = context['request']
    url = request.path_info

    current_path = None

    for item in items:

        item_url = URLHandler.convert_url(item.url, request)

        if url == item_url:
            current_path = item.path.split('/')
            break

    if not current_path:
        return ''

    menu_html = []

    def recursion(path, level=0):
        menu_html.append('<ul>')
        for item in items:

            item_path = item.path.split('/')
            slice = len(item_path) - 1

            if item_path[:slice] == path[:level]:

                item_url = URLHandler.convert_url(item.url, request)

                menu_html.append(f'<li><a href={item_url}>{item.name}</a></li>')

                if '/'.join(item_path) in '/'.join(path):
                    recursion(path, level + 1)

        menu_html.append('</ul>')
        return menu_html

    menu_html = recursion(current_path)
    return format_html(''.join(menu_html))
