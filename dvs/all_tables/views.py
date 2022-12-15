from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products


from django.views.generic.edit import CreateView
from django.views.generic import ListView

def Page(request):
    users_list = User.objects.all()
    return render(request, 'temp/UserList.html', locals())


class Add_product(CreateView):
    model = Products
    template_name = 'temp/addProduct.html'
    fields = ['title', 'price', 'count']

def Edit_Product(request):
    pass



class Prod(ListView):
    model = Products
    template_name = 'temp/index.html'


@login_required
def delete_product(request, prod_id: int) -> HttpResponse:

    if request.method == "POST":
        task = get_object_or_404(Products, pk=prod_id)
        task.delete()

        messages.success(request, "Product '{}' has been deleted".format(Products.title))
        return redirect('/temp/index.html')

    else:
        raise PermissionDenied


# @login_required
# def add_list(request) -> HttpResponse:
#
#     if request.POST:
#         form = AddTaskListForm(request.user, request.POST)
#         if form.is_valid():
#             try:
#                 newlist = form.save(commit=False)
#                 newlist.slug = slugify(newlist.name, allow_unicode=True)
#                 newlist.save()
#                 messages.success(request, "A new list has been added.")
#                 return redirect("todo:lists")
#
#             except IntegrityError:
#                 messages.warning(
#                     request,
#                     "There was a problem saving the new list. "
#                     "Most likely a list with the same name in the same group already exists.",
#                 )
#     else:
#         if request.user.groups.all().count() == 1:
#             form = AddTaskListForm(request.user, initial={"group": request.user.groups.all()[0]})
#         else:
#             form = AddTaskListForm(request.user)
#
#     context = {"form": form}
#
#     return render(request, "todo/add_list.html", context)