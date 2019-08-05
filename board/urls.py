from django.urls import path
from .views import topview, detail, list, make_board, contact, board_ascertain, finish_board_make, terms, policy

urlpatterns = [
    path('',topview, name='top'),
    path('detail/<int:pk>', detail, name='detail'),
    path('create/', make_board, name='create'),
    path('list/', list, name='new_list'),
    path('contact/', contact, name='contact'),
    path('ascertain/', board_ascertain,  name='board_ascertain'),
    path('finish_board_make/', finish_board_make, name='finish_board_make'),
    path('terms/', terms, name='terms'),
    path('policy/', policy, name='policy'),
]
