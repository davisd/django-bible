from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from context_processors import books_processor, book_processor, \
        chapter_processor

def book_index(request, template_name="bible/book/index.html"):
    """
    Book Index
    """
    return render_to_response(
        template_name,
        context_instance=RequestContext(
            request,
            processors=[books_processor,]
        )
    )

def book_detail(request, slug, template_name="bible/book/detail.html"):
    """
    Book Detail
    """
    return render_to_response(
        template_name,
        context_instance=RequestContext(
            request,
            processors=[book_processor(slug=slug),]
        )
    )

def chapter_detail(request, book_slug, chapter,
        template_name="bible/chapter/detail.html"):
    """
    Chapter Detail
    """
    return render_to_response(
        template_name,
        context_instance=RequestContext(
            request,
            processors=[chapter_processor(
                book_slug=book_slug, number=chapter),]
        )
    )

