from django.shortcuts import render


def index(request):
	context = {
		'judul':'contexTerbuka',
		'kontributor':'name',
		'nav':[
			['/','Home'],
			['/blog','Blog'],
			['/news','News'],
			['/contact','Contact'],
		]
	}
	return render (request,'index.html', context)