from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .forms import CommandForm
from .models import Animal, Commands
# Create your views here.

def animals(request, page_number=1):

    all_articles = Animal.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response('animals.html', {'animals': current_page.page(page_number),
                                                'username': auth.get_user(request).username})


def animal(request, animal_id=1):
    command_form = CommandForm
    args = {}
    args.update(csrf(request))
    args['animal'] = Animal.objects.get(id=animal_id)
    args['comments'] = Commands.objects.filter(comments_article_id=animal_id)
    args['form'] = command_form
    args['username'] = auth.get_user(request).username
    return render_to_response('animal.html', args)

def addcomment(request, animal_id):
    if request.POST and ("pause" not in request.session):
        form = CommandForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Animal.objects.get(id=animal_id)
            form.save()
            request.session.set_expiry(60) # session exists 60 seconds
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % animal_id)
