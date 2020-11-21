from django.shortcuts import render

posts = [
    {
        'author': 'JSON',
        'title': 'post 1',
        'content': 'this is first post',
        'date_posted': '19 Nov 2020'
    },
    {
        'author': 'mast071',
        'title': 'post 2',
        'content': 'this is second post',
        'date_posted': '20 Nov 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
