from django.shortcuts import render,get_object_or_404
from .models import Casing

# List view for casing products
def gamecase_list(request):
    casings = Casing.objects.all()
    return render(request, 'store/gamecase.html', {'casings': casings})

# def gamecase_page(request, slug):
#       casings = Casing.objects.get(slug=slug)
#       return render(request, 'store/gamecasepage.html', {'casings': casings})
    

def gamecase_page(request, slug):
    casing = get_object_or_404(Casing, slug=slug)
    return render(request, 'store/gamecasepage.html', {'casing': casing})