from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import FormView
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Image
from .forms import ImageUploadForm, UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, TemplateView
from django.views.generic.edit import UpdateView

#This acts as the home page view for the app.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        #Checks if the user is authenticated and redirects accordingly
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('appsec:list'))
        else:
            return HttpResponseRedirect(reverse('appsec:hl_login'))

#This view is used to upload the images. Django CBV along with Django braces are used for checking authenticity and simplicity
class GetImage(LoginRequiredMixin, FormView):
    form_class = ImageUploadForm
    template_name = 'imageupload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            formdata = form.cleaned_data # Here we collect all the form data and store it to the Image Object
            image = Image()
            image.caption = formdata['caption']
            obj = self.request.FILES['uploadimage']
            image.uploadimage = obj
            owner = User.objects.get(id=request.user.id)
            image.user = owner
            image.save()
            return HttpResponseRedirect(reverse('appsec:list')) #After saving the image object we riderect back to the list view
        return render(request, self.template_name, {'form': form})

#This view is used to update the images caption. Django CBV along with Django braces are used for checking authenticity and simplicity

class ImageUpdate(LoginRequiredMixin, UpdateView):
    model = Image
    fields = ['caption']
    template_name = 'imageupload_update_form.html'

    def get_object(self):
        object = get_object_or_404(Image, pk=self.kwargs['image_id'])
        return object

    def get_success_url(self):
        return reverse('appsec:list')

#This view is used to list the images. Django CBV along with Django braces are used for checking authenticity and simplicity
class ListImage(LoginRequiredMixin, TemplateView):
    template_name = "imageslist.html"
    title = "List of Images"

    def get_context_data(self, **kwargs):
        context = super(ListImage, self).get_context_data(**kwargs)
        imgs = Image.objects.all().order_by('-pub_date') #We filter the images to view the most recent images first
        if imgs.count() > 0:
            paginator = Paginator(imgs, settings.PAGINATION_LIMIT) #Access the PAGE limit set in settings file i.e 10/page
            page = self.request.GET.get('imagepage')
            try:
                final_images = paginator.page(page) #
            except PageNotAnInteger:
                final_images = paginator.page(1)
            except EmptyPage:#return rest of the remaining images
                final_images = paginator.page(paginator.num_pages)
            context['images'] = final_images
        return context

#This view is used to delete the images. Django CBV along with Django braces are used for checking authenticity and simplicity
class Delete(LoginRequiredMixin, View):
    def post(self, request, format=None):
        print "In delete", request.POST['image_id']
        image_id = int(request.POST['image_id'])
        user_id = int(request.user.id)
        if Image.objects.filter(user_id=user_id, pk=image_id).count() > 0:
            i = Image.objects.filter(user_id=user_id, pk=image_id)
            i.delete()
        return HttpResponseRedirect(reverse('appsec:list'))

#View to logout from the app with a decorator to check that logout takes place only when user is logged in
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return HttpResponseRedirect(reverse('appsec:hl_login')) #redirects to the login page

#View to register new users
class Register(CreateView):
    template_name = 'register.html'
    form_class = UserForm
    success_url = reverse_lazy('appsec:list')  #redirects to the list view page
    model = User

    def get_success_url(self):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if self.object:# Here we collect all the form data and store it to the User Object
                self.object.set_password(form.cleaned_data['password'])
                self.object.save()
                username = self.object.username
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(self.request, user)
        return super(Register, self).get_success_url()

#View to login existing users
class LoginView(CreateView):
    form_class = LoginForm
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            formdata = form.cleaned_data # Here we collect all the form data and store it to the Image Object
            username = formdata['username']
            password = formdata['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                return HttpResponseRedirect(reverse('appsec:list')) #redirects to the list view page after authenticating
        return render(request, self.template_name, {'form': self.form_class})
