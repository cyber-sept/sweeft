from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404

from .models import Short
from .utils import random_hash
from .forms import ShortForm


def home(request):
    template = 'urlshortener/index.html'
    context = {}
    # Empty form
    context['form'] = ShortForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
    	form = ShortForm(request.POST)
    	if form.is_valid():
    		code = random_hash()
    		full = form.cleaned_data["full_url"]

    		url = Short(full_url=full, short_url=code)
    		url.save()

    		shorten = request.build_absolute_uri('/') + code
    		context['url']  = shorten
    		return render(request, template, context)

    	context['errors'] = form.errors
    	return render(request, template, context)


def urlRedirect(request, slug):
	try:
		data = Short.objects.get(short_url=slug)
		data.use_counter += 1
		data.save()
		return redirect(data.full_url)
	except:
		raise Http404('Try another URL')