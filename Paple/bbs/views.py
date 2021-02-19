from django.shortcuts import render, redirect, get_object_or_404

from bbs.models import Question, Post, Comment
from account.models import Group, Member
from django.core.paginator import Paginator
from .forms import PostForm
import datetime


def main(request):
    try:
        user_email = request.session['loginObj']
    except:
        return redirect('/')

    if user_email:
        # 달력 질문 리스트
        questions = Question.objects.all().order_by('q_date')
        q_list = [q.as_dict() for q in questions]

        # 올라온 질문
        member = Member.objects.get(user_email=user_email)
        group_code = member.group_code
        posts = Post.objects.filter(group_code=group_code).order_by('-post_id')[0:2]

        # 오늘의 질문
        today_date = datetime.date.today().isoformat()
        try:
            today_q = Question.objects.get(q_date=today_date)
        except Question.DoesNotExist:
            today_q = None

        return render(request, 'bbs/main.html', {
            'q_list': q_list,
            'posts': posts,
            'today_q': today_q,
        })
    else:
        return redirect('/')


def logout(request):
    if request.session['loginObj']:
        del (request.session['loginObj'])
    return redirect('/')


def board(request):
    # 해당 그룹의 게시판 글을 DB에서 불러옴
    user_email = request.session['loginObj']
    member = Member.objects.get(user_email=user_email)
    group_code = member.group_code
    posts = Post.objects.select_related('user_id').filter(group_code=group_code).order_by('-post_id')

    page = request.GET.get('page', '1')

    # 페이지 당 게시물 개수 지정
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {'posts': page_obj}

    return render(request, 'bbs/board.html', context)


def detail(request, post_id):
    post = Post.objects.select_related('user_id').get(post_id=post_id)

    user_email = request.session['loginObj']
    member = Member.objects.get(user_email=user_email)
    group_code = member.group_code
    comments = Comment.objects.filter(group_code=group_code, post_id=post_id).select_related('user_id')

    return render(request, 'bbs/detail.html', {
        'post': post,
        'comments': comments
    })


def post_register(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group_code = member.group_code

            # member가 아닌 user_email인지 확인 필요
            post.user_id = member
            post.group_code = group_code
            post.post_date = datetime.datetime.now()
            post.save()
            return redirect('bbs:board')
    else:
        form = PostForm()

    return render(request, 'bbs/post_register.html', {
        'form': form
    })


def post_register2(request, q_id):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group_code = member.group_code

            # member가 아닌 user_email인지 확인 필요
            post.user_id = member
            post.group_code = group_code
            post.post_date = datetime.datetime.now()
            post.save()
            return redirect('bbs:board')
    else:
        question = Question.objects.get(q_id=q_id)
        form = PostForm(initial={'post_name': question.q_content})

    return render(request, 'bbs/post_register.html', {
        'form': form
    })


def post_update(request, post_id):
    post = Post.objects.get(post_id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group_code = member.group_code
            post.user_id = member
            post.group_code = group_code
            post.post_date = datetime.datetime.now()
            post.save()

            return redirect('bbs:detail', post_id=post_id)
    else:
        form = PostForm(instance=post)

    return render(request, 'bbs/post_update.html', {
        'form': form
    })


def post_delete(request, post_id):
    post = Post.objects.get(post_id=post_id)
    post.delete()
    return redirect('bbs:board')


def comment_register(request, post_id):
    if request.method == 'POST':
        val = request.POST.get("comment")
        user_email = request.session['loginObj']
        member = Member.objects.get(user_email=user_email)
        group_code = member.group_code
        post = Post.objects.get(post_id=post_id)

        comment = Comment()
        comment.user_id = member
        comment.group_code = group_code
        comment.c_content = val
        comment.post_id = post
        comment.save()

        return redirect('bbs:detail', post_id=post_id)


def question_register(request, q_id):
    question = Question.objects.get(q_id=q_id)

    user_email = request.session['loginObj']
    member = Member.objects.get(user_email=user_email)
    group_code = member.group_code

    try:
        post = Post.objects.get(post_name=question.q_content, group_code=group_code)
    except Post.DoesNotExist:
        post = None

    if post is None:
        return redirect('bbs:post_register2', q_id=question.q_id)
    else:
        return redirect('bbs:detail', post_id=post.post_id)


def question_register2(request, q_date):
    try:
        question = Question.objects.get(q_date=q_date)
    except Question.DoesNotExist:
        return redirect('bbs:main')

    user_email = request.session['loginObj']
    member = Member.objects.get(user_email=user_email)
    group_code = member.group_code

    try:
        post = Post.objects.get(post_name=question.q_content, group_code=group_code)
    except Post.DoesNotExist:
        post = None

    if post is None:
        return redirect('bbs:post_register2', q_id=question.q_id)
    else:
        return redirect('bbs:detail', post_id=post.post_id)
