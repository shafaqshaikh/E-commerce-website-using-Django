from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request , *args , **kwagrs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request , *args , **kwagrs)
	return  wrapper_func


def allowed_user(allowed_user=[]):
	def decorator(view_func):
		def wrapper_func(request , *args , **kwagrs):
			group=None
			if request.user.groups.exists():
				group= request.user.groups.all()[0].name
			if group in allowed_user:

				return view_func(request , *args , **kwagrs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

