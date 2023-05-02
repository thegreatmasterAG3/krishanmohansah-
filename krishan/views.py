from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import CV,IMAGE,TEXT,LINK,TITLE

# Create your views here.

def main(request):

  images = IMAGE.objects.all()
  texts = TEXT.objects.all()
  links = LINK.objects.all()
  title = TITLE.objects.all()


  context = {'images': images,
             'texts': texts,
             'links': links,
             'title': title,

             }
  return render(request, 'main.html',context)





from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ContactForm()
    return render(request, 'main.html', {'form': form})





def download_cv(request):
    cv = CV.objects.get(id=1)  # replace `1` with the actual ID of your CV file
    response = HttpResponse(cv.pdf_file.read(), content_type='application/vnd.ms-word')
    response['Content-Disposition'] = 'attachment; filename=Developer_krishan_CV.pdf'  # replace `your-cv.docx` with the actual filename of your CV
    return response


