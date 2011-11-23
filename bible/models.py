from django.db import models
from managers import BookManager

class Book(models.Model):
    """
    Book of the Bible
    """
    number = models.PositiveIntegerField(primary_key=True, unique=True,
            db_index=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64, db_index=True)
    is_new_testament = models.BooleanField()
    
    objects = BookManager()

    @models.permalink
    def get_absolute_url(self):
        """
        Returns the absolute url
        """
        return ('book_detail', [self.slug,])
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['number',]
    
class Chapter(models.Model):
    """
    Chapter of the Bible
    """
    book = models.ForeignKey(Book, related_name='chapters')
    number = models.PositiveIntegerField(db_index=True)
    
    def __unicode__(self):
        return '%s %s' % (self.book.name, self.number)
    
    def get_next_chapter(self):
        try:
            return Chapter.objects.filter(
                book=self.book,number__gt=self.number).order_by(
                'number')[0]
        except IndexError:
            return None
        
    def get_previous_chapter(self):
        try:
            return Chapter.objects.filter(
                book=self.book,number__lt=self.number).order_by(
                '-number')[0]
        except IndexError:
            return None
    
    @models.permalink
    def get_absolute_url(self):
        """
        Returns the absolute url
        """
        return ('chapter_detail', [self.book.slug, self.number])
    
    class Meta:
        ordering = ['number',]
        unique_together=(('book','number',),)
    
class Verse(models.Model):
    """
    Bible Verse
    """
    chapter = models.ForeignKey(Chapter, related_name='verses')
    number = models.PositiveIntegerField(db_index=True)
    text = models.TextField()
    
    class Meta:
        ordering = ['number']
        unique_together=(('chapter','number'),)

    def __unicode__(self):
        return '%s %s:%s' % (self.chapter.book.name, self.chapter.number,
            self.number)
        
    def get_absolute_url(self):
        return '%s#%s' % (self.chapter.get_absolute_url(), self.number)

