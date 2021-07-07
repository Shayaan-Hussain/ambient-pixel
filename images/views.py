from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import ImageForm
from .models import Image

# Create your views here.
def homeUpload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm
    images = Image.objects.all()
    if request.method == 'POST':
        return render(request, 'homeBase.html', {'images':images})
    return render(request, 'home.html', {'images':images})

def home(request):
    images = Image.objects.all()
    return render(request, 'homeBase.html', {'images':images})

def delete(request, image_id):
    item = Image.objects.get(pk=image_id)
    item.delete()
    return redirect('home')

def download(request, image_id):
    image = Image.objects.get(id=image_id)
    filename = image.photo.path
    response = FileResponse(open(filename, 'rb'))
    return response