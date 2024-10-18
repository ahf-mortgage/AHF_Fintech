# views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import MLO
from .forms import BookForm  # Assume you have a BookForm defined

class BookView(View):
    template_name = 'book_list.html'

    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(MLO, pk=pk)
            return render(request, 'book_detail.html', {'book': book})
        else:
            books = MLO.objects.all()
            return render(request, self.template_name, {'books': books})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, self.template_name, {'form': form})

    def put(self, request, pk):
        book = get_object_or_404(MLO, pk=pk)
        form = BookForm(request.PUT, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
        return render(request, 'book_form.html', {'form': form, 'book': book})

    def delete(self, request, pk):
        book = get_object_or_404(MLO, pk=pk)
        book.delete()
        return redirect('book-list')