
from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberJoinForm, LogInForm, ModifyUserInfoForm


def signup(request):
    signup_form = MemberJoinForm()
    if request.method == "POST":
        form = MemberJoinForm(request.POST)
        mem_list = Member.objects.all()
        if mem_list.filter(user_email=request.POST['user_email']).exists():
            return render(request, 'account/signup.html', {'message': '이미 존재하는 이메일 입니다.',
                                                           'signup_form': signup_form})
        if request.POST['user_pw1'] != request.POST['user_pw2']:
            return render(request, 'account/signup.html', {'message': '비밀번호가 일치하지 않습니다.',
                                                           'signup_form': signup_form})
        else:
            if form.is_valid():
                form.save()
                return redirect('/account/signup_done')

            else:
                return render(request, 'account/signup.html',
                              {'message': '회원가입 실패',
                               'signup_form': signup_form
                               })

    if request.method == "GET":
        return render(request, 'account/signup.html', {'signup_form': signup_form})


def login(request):
    login_form = LogInForm()
    if request.method == 'POST':
        input_email = request.POST['user_email']
        input_pw = request.POST['user_pw1']

        if Member.objects.filter(user_email=input_email).exists():
            member = Member.objects.get(user_email=input_email)
            if member.user_pw1 == input_pw:
                request.session['loginObj'] = member.user_email

                # group이 있고없고 조건으로 나눠야 함
                if member.user_status:
                    return redirect('/bbs/main/')
                else:
                    return redirect('/group/group_main/')
            else:
                return render(request, 'account/login.html', {
                    'message': '비밀번호가 맞지 않습니다.',
                    'login_form': login_form
                })
        else:
            return render(request, 'account/login.html', {
                'message': '존재하지 않는 이메일 입니다.',
                'login_form': login_form
            })

    if request.method == 'GET':
        return render(request, 'account/login.html', {'login_form': login_form})


def signupdone(request):
    return render(request, 'account/signup_done.html')


def modify(request):
    login_email = request.session['loginObj']
    if request.method == 'POST':
        member = Member.objects.get(user_email=login_email)
        modify_form = ModifyUserInfoForm(request.POST, instance=member)
        if request.POST['user_pw1'] != request.POST['user_pw2']:
            return render(request, 'account/modify_info.html', {
                'message': '비밀번호가 일치하지 않습니다!',
                'modify_form': modify_form
            })
        if modify_form.is_valid():
            modify_form.save()
            return render(request, 'account/modify_info.html', {
                'message': '회원정보 update 완료!',
                'modify_form': modify_form
            })
        else:
            return render(request, 'account/modify_info.html', {
                'message': '회원정보 update 실패',
                'modify_form': modify_form
            })

    if request.method == 'GET':
        member = Member.objects.get(user_email=login_email)
        modify_form = ModifyUserInfoForm(instance=member)
        return render(request, 'account/modify_info.html', {'modify_form': modify_form})

