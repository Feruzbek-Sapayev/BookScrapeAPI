from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django import forms
from django.contrib import messages
from django.utils.html import format_html
from .models import Book
from .scraper import get_src
from .forms import ScrapeBookForm


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('scrape/', self.admin_site.admin_view(self.scrape_view), name="book_scrape"),
        ]
        return custom_urls + urls

    def scrape_view(self, request):
        if request.method == "POST":
            form = ScrapeBookForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']
                content = get_src(url)
                obj, created = Book.objects.get_or_create(
                    title=content[0], 
                    price=content[1],
                    image=content[2], 
                    description=content[3],
                )

                if created:
                    messages.success(request, f"Kitob saqlandi: {content[0]}")
                else:
                    messages.warning(request, f"Bu kitob allaqachon bor: {content[0]}")

                return redirect("/admin/core/book/")  # Admin panelga qaytish
        
        else:
            form = ScrapeBookForm()
        return render(request, "admin/scrape_form.html", {"form": form})


admin.site.register(Book, BookAdmin)
