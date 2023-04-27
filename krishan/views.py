from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import CV

# Create your views here.

def main(request):
  return render(request, 'main.html')





from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'main.html', {'form': form})

def success(request):
    return render(request, 'main.html')




def download_cv(request):
    cv = CV.objects.get(id=1)  # replace `1` with the actual ID of your CV file
    response = HttpResponse(cv.pdf_file.read(), content_type='application/vnd.ms-word')
    response['Content-Disposition'] = 'attachment; filename=Developer_krishan_CV.pdf'  # replace `your-cv.docx` with the actual filename of your CV
    return response
