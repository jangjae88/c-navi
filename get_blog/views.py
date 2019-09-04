import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.parse import quote

from .models import SearchResult, GotBlog

# Create your views here.

def get_blog(request, search_keyword=None):
    #POST형식일때 키워드를 받아옵니다.
    if request.method == "POST":
        search_keyword = request.POST['keyword']
        if not search_keyword:
            return redirect('get_blog')
    #키워드 인코딩
        search_keyword_incoded = quote(search_keyword)
    #키워드(SearchResult) 모델 객체생성
        search_result = SearchResult.objects.create(
            search_keyword = search_keyword
        )
    #인코딩된 키워드로 검색
        search_url = 'https://m.search.naver.com/search.naver?where=m_view&query={}'.format(search_keyword_incoded)
    #beautifulsoup 가동위한 작업    
        source_code_from_URL = urllib.request.urlopen(search_url)
        soup = bs(source_code_from_URL, 'lxml', from_encoding='utf-8')     
    #크롤링중
        contents = soup.find_all('li', class_='_svp_item')
        for content in contents:
            #GotBlog모델 객체생성
            GotBlog.objects.create(
                title =  content.find('a', class_='api_txt_lines').text,
                content_url = content.find('a' , class_='api_txt_lines').get('href'),
                original_name = content.find('a', class_='sub_txt').text,
                original_url = content.find('a' , class_='sub_thumb').get('href'),
                search_result = search_result
            )
        return redirect('search_result', search_keyword = search_keyword)
    if search_keyword:
        result = SearchResult.objects.filter(search_keyword = search_keyword).order_by('-search_date')
        if result[0].gotblog_set.all():
            return render(request,'get_blog/result_search.html', {'result': result[0]})
        else:
            return render(request,'get_blog/result_search.html', {'result': False})
    #GET메소드
    return render(request,'get_blog/get_blog.html')