from django.forms import ClearableFileInput
from django.template.loader import render_to_string


class PreviewImageFileWidget(ClearableFileInput):

    def render(self, name, value, attrs=None, renderer=None):
        if value is not None:
            context = {
                'value': value,
                'name': name,
                'id': attrs['id']
            }
        else:
            context = {
                'name': name,
                'id': attrs['id']
            }

        html = render_to_string(
            'group/preview_imagefield.html', context)

        return html