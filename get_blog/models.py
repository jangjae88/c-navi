from django.db import models

# Create your models here.

class Prouser(models.Model):
    user = models.CharField(max_length=10, verbose_name='사용자')
    password = models.CharField(max_length=10, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now=True, verbose_name='등록날짜')

    def __str__(self):
        return self.user
        
    class Meta:
        db_table = '프로사용자'
        verbose_name = '프로사용자들'
        verbose_name_plural = '프로사용자들'

class SearchResult(models.Model):
    search_keyword =  models.CharField(max_length=30)
    search_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.search_keyword

class GotBlog(models.Model):
    search_result = models.ForeignKey(SearchResult, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    content_url = models.CharField(max_length=100, null=True, blank=True)
    original_name = models.CharField(max_length=100, null=True, blank=True)
    original_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

  
    