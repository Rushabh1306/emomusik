from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for : {username} ! ')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    context = {}
    context['form']=form
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form =  ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile Updated!')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form =  ProfileUpdateForm(instance=request.user.profile)

    context = {}
    context['u_form']=u_form
    context['p_form']=p_form

    return render(request,'users/profile.html',context)




