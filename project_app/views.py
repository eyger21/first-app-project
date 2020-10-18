from django.shortcuts import render
from project_app.models import Mem
from project_app.forms import MemeForm
from django.views.generic import DetailView, ListView


def Memes_view(request):
    memes_query = Mem.objects.all()
    return render(request, "list.html", {"memes": memes_query})

class detail_view(DetailView):
    model = Mem
    template_name = 'post_detail.html'

def new_meme(request):
    form = MemeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'add.html', {'form': form})

class HomeView(ListView):
    model = Mem
    template_name = 'list.html'
