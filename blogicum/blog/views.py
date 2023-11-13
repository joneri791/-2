from django.shortcuts import get_object_or_404, get_list_or_404, render
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.select_related(
        'location', 'author', 'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=timezone.now()
    ).order_by(
        '-pub_date'
    )[0:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pk=post_id,
            pub_date__lt=timezone.now())
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    post_list = get_list_or_404(
        Post.objects.select_related(
            'location', 'author', 'category').filter(
            is_published=True,
            category__slug=category_slug,
            pub_date__lt=timezone.now()).order_by(
            '-pub_date')
    )

    category = get_object_or_404(
        Category.objects.filter(slug=category_slug, is_published=True)
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
