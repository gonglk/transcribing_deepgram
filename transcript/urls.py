from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transript_interact/',views.process_transcript,name ='transcript_interact'),
    path('transcript/',views.get_data_from_post, name='transcript'),
    path('wiki-interaction/',views.Process_Wiki_Request,name = 'wiki-interaction'),
    path('gpt-interaction/',views.Process_GPT_Request,name = 'gpt-interaction'),
]
