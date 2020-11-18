from django.http import HttpResponse
from django.shortcuts import render
from news.models import Post

# Create your views here.

# def index(request):
#     return HttpResponse('Hello World!')

# def index(request):
#     context = {
#         'news_list': [
#             {
#                 "title": "Django 简介",
#                 "content": "这个是简介",
#             },
#             {
#                 "title": "Django 实践",
#                 "content": "这个是实践",
#             },
#         ]
#     }
#
#     return render(request, 'news/index.html', context=context)



def index(request):
    context = { 'news_list': Post.objects.all() }
    return render(request, 'news/index.html', context=context)