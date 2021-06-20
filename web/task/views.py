from django.shortcuts import render
from requests_html import HTMLSession
from django.http import HttpResponse
import sys
import io
import datetime
from .models import Template
# Create your views here.


def get_html():
	f = io.open('simple.txt', "w", encoding="utf-8") 
		

	sys.stdin.reconfigure(encoding='utf-8')
	sys.stdout.reconfigure(encoding='utf-8')
	session = HTMLSession()
	r = session.get('https://russia24.pro/news')

	body_link = r.html.find('div.r24_body a')[1].attrs['href']
	body_r = session.get(body_link)
	title = body_r.html.find('header h1', first=True).text
	text = body_r.html.find('div.r24_text', first=True).html
	print(title)
	element = "<div class='jumbotron'>"+'<h1>'+'Title:<br>'+title+'</h1>' +'<br><br>' + '<h1>Text:</h1> ' + '<article>'+text+ '</article>'+"</div>"
	f.write(element)
	f.close()
	return (title,element)
	# body_links = r.html.find('div.r24_body a')
	# len_of_links = len(body_links)
	# print(len_of_links)
	# contents = []
	# for i in range(1,len_of_links):
	# 	body_link = body_links[i].attrs['href']
	# 	body_r = session.get(body_link)
	# 	try:
	# 		title = body_r.html.find('header h1', first=True).text
	# 		text = body_r.html.find('div.r24_text', first=True).html

	# 		print(title)
	# 		print(text)
	# 		element = '<h1>'+'Title: '+title+'</h1>' +'<br><br>' + '\n\n<h1>Text:</h1> \n' + '<article>'+text+ '</article>' + '\n\n'
	# 		#element = title+'\n\n'
	# 		contents.append(element)
	# 		f.write(element)
		
	# 	except:
	# 		pass
    		
	# return contents



def index(request):
	title, contents = get_html()
	length = len(Template.objects.all())
	if title != Template.objects.all()[length-1].title:
		template = Template(title=title,contents=contents,pub_date=datetime.datetime.now())
		template.save()
	return  render(request, 'task/index.html', {'contents' : contents}) #HttpResponse(contents)