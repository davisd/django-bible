from models import Book, Chapter, Verse
from django.shortcuts import get_object_or_404

def context_processor(target):
    """
    Decorator that allows context processors with parameters to be assigned
    (and executed properly) in a RequestContext

    Example::

      return render_to_response(
        template_name,
        context_instance=RequestContext(
          request,
          processors=[
            test_processor1,
            test_processor2(val1=test_val1, val2=test_val2),
          ]
        )
      )
      
    """
    def cp_wrapper(*args, **kwargs):
        if (len(args) == 1 and len(kwargs) == 0) \
        or (len(args) == 0 and len(kwargs) == 1 and 'request' in kwargs):
            return target(*args, **kwargs)
        else:
            def get_processor(request):
                return target(request, *args, **kwargs)
            return get_processor
    return cp_wrapper

@context_processor
def books_processor(request, context_name='books'):
    return {context_name: Book.objects}

@context_processor
def book_processor(request, slug, context_name='book'):
    return {context_name: get_object_or_404(Book, slug=slug)}

@context_processor
def chapter_processor(request, book_slug, number, context_name='chapter'):
    return {context_name: get_object_or_404(
        Chapter, book__slug=book_slug, number=number)}

