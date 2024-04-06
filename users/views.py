# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile



def update_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', user_id=user_id)  # Redirect to a view showing user profile details
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'update_user_profile.html', {'form': form})

def delete_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    if request.method == 'POST':
        user_profile.delete_user()
        return redirect('profile_list')  # Redirect to a view showing all user profiles
    return render(request, 'delete_user_profile.html', {'user_profile': user_profile})

def disable_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    if request.method == 'POST':
        user_profile.disable_user()
        return redirect('profile_list')  # Redirect to a view showing all user profiles
    return render(request, 'disable_user_profile.html', {'user_profile': user_profile})

def reactivate_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    if request.method == 'POST':
        user_profile.reactivate_user()
        return redirect('profile_list')  # Redirect to a view showing all user profiles
    return render(request, 'reactivate_user_profile.html', {'user_profile': user_profile})
  
  

  