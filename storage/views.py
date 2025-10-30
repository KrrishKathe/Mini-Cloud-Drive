from django.shortcuts import render

def dashboard(request):
    return render(request, 'storage/dashboard.html')

def document_list(request):
    return render(request, 'storage/document_list.html')

def upload_document(request):
    return render(request, 'storage/upload_document.html')

def login_view(request):
    return render(request, 'storage/login.html')
