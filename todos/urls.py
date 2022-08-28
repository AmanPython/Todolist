from todos.views import TodosAPIView, TodoDetailAPIView
from django.urls import path

urlpatterns = [
    path("create", TodosAPIView.as_view(), name="todos"),
    path("list", TodoDetailAPIView.as_view(), name="todo")
]
