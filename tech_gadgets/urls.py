from django.urls import path
from .views import (
    start_page_view,
    single_gadget_view,
    single_gadget_slug_view,
)

urlpatterns = [
    path('', start_page_view, name='start-page'),
    path(
        'gadget/<int:gadget_id>/',
        single_gadget_view,
        name='single-gadget-by-id'
    ),
    path(
        'gadget/<int:gadget_id>/<slug:gadget_slug>/',
        single_gadget_slug_view,
        name='single-gadget-by-slug'
    ),
]