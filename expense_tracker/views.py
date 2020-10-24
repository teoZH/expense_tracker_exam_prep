from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from expense_tracker.models import Profile, Expense
from expense_tracker.forms import CreateUser, CreateExpense


# Create your views here.


def homepage(request):
    context = {}
    profiles = Profile.objects.all()
    if profiles:
        expenses = profiles[0].expense_set.all()
        left = profiles[0].budget - sum([e.price for e in expenses])
        context.update({'profile': profiles[0], 'expenses': expenses, 'left': left})
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == "POST":
            form = CreateUser(request.POST, label_suffix='')
            if form.is_valid():
                form.save()
                return homepage(request)

        else:
            form = CreateUser(label_suffix='')
        context.update({'form': form})
        return render(request, 'home-no-profile.html', context)


def create_expense(request):
    context = {}
    profiles = Profile.objects.all()
    if not profiles:
        return redirect('home')
    if request.method == 'POST':
        form = CreateExpense(request.POST, label_suffix='', instance=Expense(profile=profiles[0]))
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpense(label_suffix='')
    context.update({'form': form})
    return render(request, 'expense-create.html', context)


def edit_expense(request, exp_id):
    profiles = Profile.objects.all()
    try:
        expense = Expense.objects.get(pk=exp_id)
    except ObjectDoesNotExist:
        return redirect('home')
    if not profiles:
        return redirect('home')
    if request.method == 'POST':
        form = CreateExpense(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = CreateExpense(initial=expense.get_values_dict())
    return render(request, 'expense-edit.html', {'form': form})


def delete_expense(request, exp_id):
    profiles = Profile.objects.all()
    if not profiles:
        return redirect('home')
    try:
        expense = Expense.objects.get(pk=exp_id)
    except ObjectDoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    else:
        form = CreateExpense(initial=expense.get_values_dict())
        for x in form.fields:
            form.fields[x].disabled = True
    return render(request, 'expense-delete.html', {'form': form})


def profile_page(request):
    context = {}
    profiles = Profile.objects.all()
    expenses = profiles[0].expense_set.all()
    left = profiles[0].budget - sum([e.price for e in expenses])
    if not profiles:
        return redirect('home')
    context.update({'profile': profiles[0], 'left': left})
    return render(request, 'profile.html', context)


def profile_edit(request):
    profiles = Profile.objects.all()
    if not profiles:
        return redirect('home')
    if request.method == 'POST':
        form = CreateUser(request.POST, instance=profiles[0])
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreateUser(initial=profiles[0].get_values_dict())
    return render(request, 'profile-edit.html', {'form': form})


def profile_delete(request):
    profiles = Profile.objects.all()

    if not profiles:
        return redirect('home')
    if request.method == 'POST':
        profiles.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')
