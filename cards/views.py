from django.shortcuts import render
from django.views.generic import ListView
from .forms import CardsForm
from .models import Cards
# Create your views here.
class HomeView(ListView):
    #model = Item
    #paginate_by = 10
    template_name = "welcome.html"
    queryset = Cards.objects.all()

def product_create_view(request):
    form = CardsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "todo.html", context)
