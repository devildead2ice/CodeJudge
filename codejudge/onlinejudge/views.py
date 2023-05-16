from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from USERS.models import User, Submission
from onlinejudge.models import Problem, TestCase
from onlinejudge.forms import CodeForm
from datetime import datetime
from time import time

# DashBoard

#@login_required(login_url='login')
def dashboardPage(request):
    total_ques_count=len(Problem.objects.all())
    easy_ques_count=len(Problem.objects.filter(difficulty="Easy"))
    medium_ques_count=len(Problem.objects.filter(difficulty="Medium"))
    tough_ques_count=len(Problem.objects.filter(difficulty="Tough"))

    user=request.user
    easy_solve_count=user.easy_solve_count
    medium_solve_count=user.medium_solve_count
    tough_solve_count=user.tough_solve_count
    total_solve_count=user.total_solve_count

    easy_progress=(easy_solve_count+easy_ques_count)*100
    medium_progress=(medium_solve_count+medium_ques_count)*100
    tough_progress=(tough_solve_count+tough_ques_count)*100
    total_progress=(total_solve_count+total_ques_count)*100

    context = {"easy_progress": easy_progress,"medium_progress" : medium_progress,
                "tough_progress" : tough_progress, "total_progress":total_progress,
                "easy_ques_count" : easy_ques_count, "medium_ques_count" : medium_ques_count,
                "tough_ques_count": tough_ques_count, "total_ques_count" : total_ques_count,
                "easy_solve_count": easy_solve_count,"medium_solve_count": medium_solve_count,
                "tough_solve_count": tough_solve_count, "total_solve_count": total_solve_count}
    
    return render(request,'onlinejudge/dashboard.html',context)



#list of Problems

@login_required(login_url='login')
def problemPage(request):
    problems=Problem.objects.all()
    Submissions=Submission.objects.filter(user=request.user,verdict="Accepted")
    accepted_problems=[]
    for submission in Submissions:
        accepted_problems.append(submission.problem_id)
    context={'problems': problems,'accepted_problems': accepted_problems}
    return render(request,'onlinejudge/problem.html',context)




#problem description
'''
@login_required(login_url='login')
def descriptionPage(request, id=problem_id):
    user_id=request.user.id
    problem=get_object_or_404(Problem,id=problem_id)
    user=User.objects.get(id=user_id)
    form=CodeForm()
    context={'problem': problem, 'user':user, 'user_id':user_id,'code_form': form}
    return render(request,'onlinejudge/description.html',context)

'''



#Verdict Page

##@login_required(login_url='login')
##def verdictPage(request, problem_id):


#LeaderBoard

@login_required(login_url='login')
def leaderboardPage(request):
    coders=User.objects.all()
    return render(request,'onlinejudge/leaderboard.html',{'coders': coders})
