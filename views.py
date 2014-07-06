#!/usr/bin/env python
# coding: utf-8

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

import utils
from blog.models import Post, Page





# reload(sys)
# sys.setdefaultencoding( "utf-8" )

def home(request):
    '''首页'''
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    return render_to_response('index.html', {
    'index': True,
    'keywords': settings.SITE_DESC,
    'posts': utils.get_page(Post.objects.all(), page),
    }, context_instance=RequestContext(request))


def archives(request):
    '''归档页面'''
    posts = [Post(**i) for i in Post.objects.values('id', 'title', 'created_at', 'slug')]
    # for i in posts:
    #     print i.title + 'content'
    page = {
    'title': 'Blog Archive',
    }
    return render_to_response('archives.html', {
    'posts': posts,
    'page': page,
    }, context_instance=RequestContext(request))


def show_page(request, page):
    '''单页面'''
    return render_to_response('page.html', {
    'no_sidebar': True,
    'page': page,
    'comments': page['allow_comment'],
    }, context_instance=RequestContext(request))


def handler404(request):
    '''所有其他页面'''
    path = request.path

    # 是否存在此页面
    if 2 < len(path) < 51 and utils.is_slug(path[1:-1]):
        try:
            page = Page.objects.values('title', 'content', 'created_at', 'allow_comment').get(slug=path[1:-1])
            return show_page(request, page)
        except Page.DoesNotExist:
            pass

    ret = render_to_response('404.html', {
    'no_sidebar': True,
    'path': request.path,
    }, context_instance=RequestContext(request))
    ret.status_code = 404

    return ret


def about(request):
    # 传递关于页面的对象
    # the_about_post = get_object_or_404(BlogPost, title="about")
    # if the_about_post:
    #     print("get about page...")
    #     print(""+the_about_post.display_html())
    # else:
    #     print("cannot get about page")
    #
    # args = {"about": the_about_post}
    # # return render(request, '../templates/about.html', args)
    return render_to_response('about.html', {})


def aliyun(request):
    return render_to_response('aliyun_verify_3c2a8c9eb497880e48d0569136c03476.html', {})


def aliyun1(request):
    return render_to_response('aliyun_verify_31d1ed977a7e1ff4f038711801722b07.html', {})


def aliyun2(request):
    return render_to_response('aliyun_verify_4e2c22d6893dd289f79a7cb4723ea72a.html', {})


def contact(request):
    return render_to_response('contact.html', {})

