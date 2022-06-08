from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul':'Blog Kita',
		'kontributor':'siape jak',
	}
	return render(request,'blog/index.html', context)

def cerita(request):
	context = {
		'judul':'cerita Kita',
		'kontributor':'siape jak',
	}
	return render(request,'blog/index.html', context)


def news(request):
	context = {
		'judul':'news Kita',
		'kontributor':'siape jak',
	}
	return render(request,'blog/index.html', context)
