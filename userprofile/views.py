from django.shortcuts import render
from core.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import CreateUserProfileForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


# Create your views here.
@login_required(login_url="core:login")
def user_profile(request, user_id):
    user_data = UserProfile.objects.get(pk=user_id)
    user = User.objects.get(pk=user_id)
    return render(request, "userprofile/user_profile.html", {
        "user": user,
        "user_data": user_data
    })

@login_required(login_url="core:login")
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == "POST":
        #cancel the edit request
        if request.POST.get("cancel") == "clicked":
            return HttpResponseRedirect(reverse("userprofile:user_profile", args=[request.user.id]))
        
        #Edit the profile
        form = CreateUserProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            #update all profile's data with form's data
            user_profile.name = form.cleaned_data.get("name")
            user_profile.date_of_birth = form.cleaned_data.get("date_of_birth")
            user_profile.about = form.cleaned_data.get("about")
            user_profile.country = form.cleaned_data.get("country")

            #update image only if the file was uploaded
            if len(request.FILES) == 1:
                user_profile.image = request.FILES['image']
            
            user_profile.save()

            return HttpResponseRedirect(reverse("userprofile:user_profile", args=[request.user.id]))
        else:
            return render(request, "userprofile/edit_profile.html", {
                "form": form,
                "max_file_size": settings.MAX_UPLOAD_SIZE
            })
    
    return render(request, "userprofile/edit_profile.html", {
        "form": CreateUserProfileForm(instance=request.user.profile),
        "max_file_size": settings.MAX_UPLOAD_SIZE
    })