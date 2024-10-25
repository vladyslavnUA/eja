from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import *
from .models import *
from django.utils.text import slugify

def homepage(request): 
    context = {}
    
    return render(request, 'app/index.html', context)

def about(request): 
    context = {}
    
    return render(request, 'app/about.html', context)

def projects(request): 
    projects = Project.objects.all()
    
    context = {'projects': projects, }
    return render(request, 'app/projects.html', context)

def project(request, pk): 
    project = get_object_or_404(Project, pk=pk)

    context = {'project': project, }
    return render(request, 'app/project.html', context)

def shop(request):
    context = {}
    
    return render(request, 'app/shop.html', context)

def shopDetail(request): 
    context = {}
    
    return render(request, 'app/shop-details.html', context)

def save_images(images, folder_name, project_name):
    """Helper function to save multiple images under a folder named after the project."""
    saved_image_paths = []
    project_folder = slugify(project_name)  # Convert project name to URL-safe format
    for image in images:
        # Create a directory that includes the project name
        directory = os.path.join(settings.MEDIA_ROOT, folder_name, project_folder)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save each image in the specific project folder
        image_path = os.path.join(directory, image.name)
        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        # Append the relative image path to be saved in the model (use forward slashes)
        saved_image_paths.append(os.path.join(folder_name, project_folder, image.name).replace("\\", "/"))
    
    return saved_image_paths

def addProject(request):
    # def add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save()
            additional_images = request.FILES.getlist('additional_images')  # Get the list of uploaded files
            for image in additional_images:
                AdditionalProjectImage.objects.create(project=project, image=image)  # Create a new AdditionalImage instance
            return redirect('project_list')  # Redirect after saving
    else:
        project_form = ProjectForm()
        additional_image_form = AdditionalProjectImageForm()

    return render(request, 'app/newproject.html', {'form': project_form,
'additional_image_form': additional_image_form})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES, instance=project)

        if project_form.is_valid():
            project = project_form.save()

            # Handle additional images
            existing_images = request.POST.getlist('existing_images')
            for index, image_id in enumerate(existing_images):
                AdditionalProjectImage.objects.filter(id=image_id).update(position=index)

            additional_images = request.FILES.getlist('additional_images')
            for image in additional_images:
                AdditionalProjectImage.objects.create(project=project, image=image)

            return redirect('project_detail', pk=project.pk)
    else:
        project_form = ProjectForm(instance=project)

    return render(request, 'app/pedit.html', {'project_form': project_form, 'project': project})

def addProduct(request):
    # def add_project(request):
    if request.method == 'POST':
        project_form = ProductForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save()
            additional_images = request.FILES.getlist('additional_images')  # Get the list of uploaded files
            for image in additional_images:
                AdditionalProjectImage.objects.create(project=project, image=image)  # Create a new AdditionalImage instance
            return redirect('project_list')  # Redirect after saving
    else:
        project_form = ProductForm()
        additional_image_form = AdditionalProductImageForm()
    return render(request, 'app/newproduct.html', {'form': project_form,
'additional_image_form': additional_image_form})

# def addProduct(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()

#             # Handle multiple additional images
#             for f in request.FILES.getlist('additional_images'):
#                 print('file: ', f)
#                 product.additional_images.save(f.name, f)

#             # return redirect('product_list')  # Redirect to a list view
#     else:
#         form = ProductForm()

#     return render(request, 'app/newproduct.html', {'form': form})

def contact(request): 
    context = {}
    
    return render(request, 'app/contact.html', context)