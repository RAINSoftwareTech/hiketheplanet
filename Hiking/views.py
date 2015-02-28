# from django.contrib.auth.models import User
# from django.contrib import auth
#
# def register(request):
#     if request.method == "POST":
#         User.objects.create_user(request.POST["username"], None, request.POST["password"])
#     return render(request, 'hikes/register.html')
#
#
# def login(request):
#     if request.method == "POST":
#         user = auth.authenticate(username=request.POST['username'],
#                                  password=request.POST['password'])
#         if user is not None:
#             if user.is_active:
#                 print("user is valid, active and authenticated")
#                 return redirect('index')
#             else:
#                 print("the password is valid, but the account has been disabled!")
#
#         else:
#             print("the username and password were incorrect")
#     return render(request, 'hikes/login.html')

