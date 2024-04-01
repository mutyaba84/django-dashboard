# views.py

from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserProfileForm

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_update.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        # Get UserProfile for current user or create if it doesn't exist
        user = self.request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        return user_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        context['current_information'] = user_profile.get_current_information()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
