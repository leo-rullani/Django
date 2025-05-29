from django.shortcuts import redirect
from django.http import (
    HttpResponse,
    JsonResponse,
    Http404,
    HttpResponseNotAllowed
)
from django.utils.text import slugify
from django.urls import reverse
from .dummy_data import gadgets


def start_page_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return HttpResponse("hey das hat doch gut funktioniert!")


def single_gadget_view(request, gadget_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    try:
        gadget = gadgets[gadget_id]
    except (IndexError, TypeError, ValueError):
        raise Http404("Gadget nicht gefunden")

    new_slug = slugify(gadget["name"])
    # reverse benötigt beide Parameter: gadget_id und gadget_slug
    new_url = reverse('single-gadget-by-slug', args=[gadget_id, new_slug])
    return redirect(new_url, permanent=True)


def single_gadget_slug_view(request, gadget_id, gadget_slug):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    try:
        gadget = gadgets[gadget_id]
    except (IndexError, TypeError, ValueError):
        raise Http404("Gadget nicht gefunden")

    if slugify(gadget['name']) != gadget_slug:
        raise Http404("Gadget nicht gefunden")

    return JsonResponse(gadget)