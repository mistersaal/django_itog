

from django.shortcuts import render, redirect

from .models import Couple, Groups, Teachers, Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CoupleForm, AuthUserForm, RegisterUserForm, GroupForm, StudentForm, CoupleFormAdmin, TeacherForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def CoupleView(request, name):
    list_couple = Couple.objects.filter(group_id = name)
    context = {
        'list_couple' : list_couple
    }
    template = 'couple.html'
    return render(request, template, context)

def IndexView(request):
    template = 'index.html'
    context = {
        'list_groups' : Groups.objects.all(),

    }
    return render(request, template, context)



class CreateCoupleView(CreateView):
    model = Couple
    template_name = 'addcouple.html'
    form_class = CoupleForm
    success_url = reverse_lazy('AddCouple')

    def get_context_data(self, **kwargs):
        kwargs['list_couple'] = Couple.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher_id = Teachers.objects.get(user_id=self.request.user)
        self.object.save()
        return super().form_valid(form)

class CreateTeacherView(CreateView):
    model = Teachers
    template_name = 'addteacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('AddTeacher')

    def get_context_data(self, **kwargs):
        kwargs['list_teacher'] = Teachers.objects.all()
        return super().get_context_data(**kwargs)

class CreateCoupleViewAdmin(CreateView):
    model = Couple
    template_name = 'addcouple.html'
    form_class = CoupleFormAdmin
    success_url = reverse_lazy('AddCoupleAdmin')

    def get_context_data(self, **kwargs):
        kwargs['list_couple'] = Couple.objects.all()
        return super().get_context_data(**kwargs)

class CreateGroupView(CreateView):
    model = Groups
    template_name = 'addgroup.html'
    form_class = GroupForm
    success_url = reverse_lazy('AddGroup')

    def get_context_data(self, **kwargs):
        kwargs['list_group'] = Groups.objects.all()
        return super().get_context_data(**kwargs)

class CreateStudentView(CreateView):
    model = Student
    template_name = 'addstudent.html'
    form_class = StudentForm
    success_url = reverse_lazy('AddStudent')

    def get_context_data(self, **kwargs):
        kwargs['list_student'] = Student.objects.all()
        return super().get_context_data(**kwargs)



def delete_student(request, pk):
    get_couple = Student.objects.get(pk=pk)
    get_couple.delete()

    return redirect(reverse('AddStudent'))

def delete_teacher(request, pk):
    get_couple = Teachers.objects.get(pk=pk)
    get_couple.delete()

    return redirect(reverse('AddTeacher'))

def delete_group(request, pk):
    get_couple = Groups.objects.get(pk=pk)
    get_couple.delete()

    return redirect(reverse('AddGroup'))

def delete_couple(request, pk):
    get_couple = Couple.objects.get(pk=pk)
    get_couple.delete()

    return redirect(reverse('AddCouple'))

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('IndexView')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('IndexView')
    success_msg = 'Пользователь успешно создан'
    # def form_valid(self,form):
    #     form_valid = super().form_valid(form)
    #     username = form.cleaned_data["username"]
    #     password = form.cleaned_data["password"]
    #     aut_user = authenticate(username=username,password=password)
    #     login(self.request, aut_user)
    #     return form_valid

class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('IndexView')

class CoupleUpdateView(UpdateView):
    model = Couple
    template_name = 'addcouple.html'
    form_class = CoupleForm
    success_url = reverse_lazy('AddCouple')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class CoupleUpdateViewAdmin(UpdateView):
    model = Couple
    template_name = 'addcouple.html'
    form_class = CoupleFormAdmin
    success_url = reverse_lazy('AddCouple')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class UpdateStudentView(UpdateView):
    model = Student
    template_name = 'addstudent.html'
    form_class = StudentForm
    success_url = reverse_lazy('AddStudent')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class TeacherUpdateView(UpdateView):
    model = Teachers
    template_name = 'addteacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('AddTeacher')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class UpdateGroupView(UpdateView):
    model = Groups
    template_name = 'addgroup.html'
    form_class = GroupForm
    success_url = reverse_lazy('AddGroup')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

# def updateCouple(request, pk):
#     success_update = False
#     get_couple = Couple.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = Couple(request.POST, instance=get_couple)
#         if form.is_valid():
#             form.save()
#             success_update = True
#     template = 'addcouple.html'
#     context = {
#         'get_couple': get_couple,
#         'update': True,
#         'form': CoupleFormAdmin(instance=get_couple),
#         'success_update': success_update
#
#     }
#     return render(request, template, context)



# def AddCouple(request):
#     success = False
#     if request.method == 'POST':
#         form = CoupleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True
#
#     template = 'addcouple.html'
#     context = {
#         'list_couple': Couple.objects.all(),
#         'form': CoupleForm(),
#         'success': success
#     }
#     return render(request, template, context)