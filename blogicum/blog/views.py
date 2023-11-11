from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request, 'blog/index.html', {'posts_list': posts[::-1]})


def post_detail(request, post_id):
    if post_id not in posts_dict:
        raise Http404(f"Поста под номером {post_id} не существует")

    return render(request, 'blog/detail.html', {'post': posts_dict[post_id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})



