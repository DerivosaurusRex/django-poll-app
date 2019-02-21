from django.urls import path

from polls.views import detail, index, result, vote

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/detail', detail, name='detail'),
    path('<int:question_id>/result', result, name='result'),
    path('<int:question_id>/vote', vote, name='vote')
]