from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def not_active_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_active == True:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func