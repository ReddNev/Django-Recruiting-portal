from django.shortcuts import render, get_object_or_404
from .models import Profile, Skill


def profiles(request):
    profiles = Profile.object.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.object.get(id=pk)
    main_skills = profile.skills.all()[:2]
    extra_skills = profile.skills.all()[2:]
    context = {'profiles': profile, 'main_skills': main_skills,
               'extra_skills': extra_skills}
    return render(request, 'users/user-profile.html', context)


def profiles_by_skill(request, skill_sluq):
    skill = get_object_or_404(Skill, slug=skill_sluq)
    profiles = Profile.object.filter(skills_in=[skill])
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)