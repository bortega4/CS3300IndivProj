from django.http import HttpResponse
from django.shortcuts import redirect

#will redirect a user that is logged in - useful for registerPage function in
#views.py because a logged in user should not be able to create a new user
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
   
    return wrapper_func

#allows us to specify which role is llowed to view the page
#@allowed_user(allowed_roles=['author_role'])
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name


            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator