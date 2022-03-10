from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from .form import NameForm
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ 返回最近时间的五个问题 """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # print(question, question.pub_date)
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    print(question, question.pub_date)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print('request:')
    print(request)
    print('question_id:')
    print(question_id)
    print('question:')
    print(question)
    print('question.choice_set:')
    print( question.choice_set)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print('selected_choice: ')
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # 重新显示问题的投票表单
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        print('selected_choice.votes: ')
        print(selected_choice.votes)
        selected_choice.save()
        print('selected_choice.votes: ')
        print(selected_choice.votes)
        # 成功处理之后 POST 数据之后，总是返回一个 HttpResponseRedirect 。防止因为用户点击了后退按钮而提交了两次。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def titles(request):
    print(request)
    return render(request, "polls/titles.html")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})
    
def thanks(request):
    print(request)
    return render(request, "polls/thanks.html")

