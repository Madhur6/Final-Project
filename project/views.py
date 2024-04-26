from django.shortcuts import render, redirect, get_object_or_404
from project.models import Project, Post, Img, user_directory_path
from django.contrib import messages
from .forms import PostForm, ImageUploadForm

from django.conf import settings
from django.core.exceptions import ValidationError

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from django.core.signing import Signer, BadSignature
from django.utils import timezone
from datetime import timedelta

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from markdown2 import Markdown


# Create your views here.
def projects(request):
    projects = Project.objects.filter(user=request.user).all()

    paginator = Paginator(projects, 8)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'project/projects.html', {
        'projects': projects,
        "page_obj": page_obj
    })


def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('project:projects')
    else:
        return redirect('project:projects')



def post(request):
    # total_images = Images.objects.filter(post__project__user=request.user)
    
    total_images = Img.objects.filter(user=request.user)

    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            content = form.cleaned_data['content']

            if title:
                project = Project.objects.create(user=user, title=title)
                project.save()

            post = Post.objects.create(project=project, title=title, content=content)
            post.save()

            messages.info(request, 'Post created successfully!')
            return redirect('project:projects')
        else:
            return render(request, "project/post.html", {"form":form, "user_images":total_images})
        
    return render(request, 'project/post.html', {
        'form': PostForm(),
        "user_images":total_images,
    })




def upload_image(request):
    total_images = Img.objects.filter(user=request.user)
    redirect_url = reverse('project:post')

    if request.method == "POST":
        redirect_url = request.GET.get('next', reverse('project:post'))
        form = ImageUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            try:
                images = request.FILES.getlist('images')
                # Count the total number of images uploaded by the user
                total_images_count = Img.objects.filter(user=request.user).count()

                # Check if the user has exceeded the maximum limit (10 images)
                if total_images_count + len(request.FILES.getlist('images')) > 10:
                    raise ValidationError("You can upload a maximum of 10 images. Delete some previous images to add more.")
                
                images = request.FILES.getlist('images')
                # Check if the number of images exceeds 3
                if images and len(images) > 3:
                    raise ValidationError("You can upload a maximum of 3 images.")

                for image in images:
                    # Handle image uploads here
                    if image.size > settings.MAX_UPLOAD_SIZE * 1024 * 1024:
                        raise ValidationError(f"Image file {image.name} exceeds {settings.MAX_UPLOAD_SIZE} MB size limit")
                    img_instance = Img(user=request.user, img=image)  # Create Img instance
                    img_instance.save()  # Save the instance to the database

            except ValidationError as e:
                message = ''.join(e)
                return render(request, 'project/upload_image.html', {
                    "message": message,
                    "form": form,
                    "user_images": total_images,
                    "redirect": redirect_url
                })
            messages.info(request, 'Images uploaded successfully!')
            return redirect('project:upload_image')
    else:
        form = ImageUploadForm()
    return render(request, 'project/upload_image.html', {'form': form, "user_images": total_images, "redirect": redirect_url})


def detail_post(request, post_id):
    # Retrieve the post object using the post_id
    post = Post.objects.get(pk=post_id)
    total_images = Img.objects.filter(user=request.user)
    redirect_url = reverse("project:projects")
    return render(request, "project/detail_post.html", {
        "post":post,
        "post_content": markdown(post.content),
        "user_images": total_images,
        "redirect": redirect_url
    })


def edit_post(request, post_id):
    # Retrieve the post object using the post_id
    post = Post.objects.get(pk=post_id)
    total_images = Img.objects.filter(user=request.user)
    # If the request method is POST, validate the form and save changes
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post edited successfully!')
            return redirect('project:detail_post', post_id=post_id)
    # If the request method is GET, create a form populated with the post's current data
    else:
        form = PostForm(instance=post)
    # Render the form in a template
    return render(request, "project/edit_post.html", {"form":form, "post":post, "user_images": total_images})



def upload_image_edit(request, post_id):
    total_images = Img.objects.filter(user=request.user)
    redirect_url = reverse('project:edit_post', args=(post_id,))

    if request.method == "POST":
        redirect_url = request.GET.get('next', reverse('project:edit_post', args=(post_id,)))
        form = ImageUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            try:
                images = request.FILES.getlist('images')
                # Count the total number of images uploaded by the user
                total_images_count = Img.objects.filter(user=request.user).count()

                # Check if the user has exceeded the maximum limit (10 images)
                if total_images_count + len(request.FILES.getlist('images')) > 10:
                    raise ValidationError("You can upload a maximum of 10 images. Delete some previous images to add more.")
                
                images = request.FILES.getlist('images')
                # Check if the number of images exceeds 3
                if images and len(images) > 3:
                    raise ValidationError("You can upload a maximum of 3 images.")

                for image in images:
                    # Handle image uploads here
                    if image.size > settings.MAX_UPLOAD_SIZE * 1024 * 1024:
                        raise ValidationError(f"Image file {image.name} exceeds {settings.MAX_UPLOAD_SIZE} MB size limit")
                    img_instance = Img(user=request.user, img=image)  # Create Img instance
                    img_instance.save()  # Save the instance to the database

            except ValidationError as e:
                message = ''.join(e)
                return render(request, 'project/upload_image_edit.html', {
                    "message": message,
                    "form": form,
                    "user_images": total_images,
                    "redirect": redirect_url,
                    "post_id":post_id
                })
            messages.info(request, 'Images uploaded successfully!')
            return HttpResponseRedirect(reverse('project:upload_image_edit', args=(post_id,)))
    else:
        form = ImageUploadForm()
    return render(request, 'project/upload_image_edit.html', {'form': form, "user_images": total_images, "redirect": redirect_url, "post_id":post_id})


def get_temporary_image_url(request, image_id):
    try:
        image = Img.objects.get(id=image_id)
        image_url = image.img.url
        signer = Signer()
        timestamp = int(timezone.now().timestamp())
        signed_value = signer.sign(f'{image_id}-{timestamp}')
        return JsonResponse({'image_url': f'get-image/{signed_value}/'})
    except Img.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)
    
def get_image(request, signed_value):
    signer = Signer()
    try:
        image_id, timestamp = signer.unsign(signed_value).split('-')
        image = Img.objects.get(id=image_id)
        return redirect(image.img.url)
    
        # Check if the request is made within a certain time window (e.g., 5 minutes)
        # if int(timezone.now().timestamp()) - int(timestamp) <= 300:  
        #     return redirect(image.image.url)
        # else:
        #     return HttpResponse('Link expired.', status=403)

    except (BadSignature, ValueError, Img.DoesNotExist):
        return HttpResponse('Invalid link.', status=403)
    
    
def get_temporary_image_url_edit(request, image_id, post_id):
    return get_temporary_image_url(request, image_id)

def get_image_edit(request, signed_value, post_id):
    return get_image(request, signed_value)

def get_image_detail_post(request, signed_value, post_id):
    return get_image(request, signed_value)

def delete_images(request):
    if request.method == "POST":
        selected_image_ids = request.POST.getlist('selected_image_ids')

        # Delete selected Img
        Img.objects.filter(id__in=selected_image_ids).delete()

    return redirect('project:upload_image')


def markdown(content):
    markdowner = Markdown()
    return markdowner.convert(content)





























# def post(request):
#     # total_images = Images.objects.filter(post__project__user=request.user)
#     total_images = Img.objects.filter(user=request.user)
#     if request.method == "POST":
#         form = PostFullForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             try:
#                 user = request.user
#                 title = form.cleaned_data.get('title')
#                 content = form.cleaned_data['content']

#                 if title:
#                     project = Project.objects.create(user=user, title=title)
#                     project.save()

#                 post = Post.objects.create(project=project, title=title, content=content)
#                 post.save()

#                 # Count the total number of images uploaded by the user
#                 total_images_count = Images.objects.filter(post__project__user=user).count()

#                 # Check if the user has exceeded the maximum limit (10 images)
#                 if total_images_count + len(request.FILES.getlist('images')) > 20:
#                     raise ValidationError("You can upload a maximum of 10 images. Delete some previous images to add more.")
                
#                 images = request.FILES.getlist('images')
#                 # Check if the number of images exceeds 3
#                 if images and len(images) > 3:
#                     raise ValidationError("You can upload a maximum of 3 images.")
            
#                 for image in images:
#                     if image.size > settings.MAX_UPLOAD_SIZE*1024*1024:
#                         raise ValidationError(f"Image file {image.name} exceeds {settings.MAX_UPLOAD_SIZE} MB size limit")
#                     Images.objects.create(post=post, image=image)

#             except ValidationError as e:
#                 message = ''.join(e)
#                 return render(request, 'project/post.html', {
#                     'message':message,
#                     'form': form
#                     })

#             messages.info(request, 'Post created successfully!')
#             return redirect('project:post')
#         else:
#             return render(request, "project/post.html", {"form":form})
        
#     return render(request, 'project/post.html', {
#         'form': PostForm(),
#         "user_images": total_images,
#     })

# def get_image_url(request, image_id):
#     try:
#         image = Images.objects.get(id=image_id)
#         image_url = image.image.url
#         return JsonResponse({'image_url': image_url})
#     except Images.DoesNotExist:
#         return JsonResponse({'error': 'Image not found'}, status=404)
    

# def get_temporary_image_url(request, image_id):
#     try:
#         image = Images.objects.get(id=image_id)
#         image_url = image.image.url
#         signer = Signer()
#         timestamp = int(timezone.now().timestamp())
#         signed_value = signer.sign(f'{image_id}-{timestamp}')
#         return JsonResponse({'image_url': f'get-image/{signed_value}/'})
#     except Images.DoesNotExist:
#         return JsonResponse({'error': 'Image not found'}, status=404)

# def get_image(request, signed_value):
#     signer = Signer()
#     try:
#         image_id, timestamp = signer.unsign(signed_value).split('-')
#         image = Images.objects.get(id=image_id)
#         return redirect(image.image.url)
    
#         # Check if the request is made within a certain time window (e.g., 5 minutes)
#         # if int(timezone.now().timestamp()) - int(timestamp) <= 300:  
#         #     return redirect(image.image.url)
#         # else:
#         #     return HttpResponse('Link expired.', status=403)

#     except (BadSignature, ValueError, Images.DoesNotExist):
#         return HttpResponse('Invalid link.', status=403)
    

# def delete_images(request):
#     if request.method == "POST":
#         selected_image_ids = request.POST.getlist('selected_image_ids')

#         # Delete selected images
#         Images.objects.filter(id__in=selected_image_ids).delete()

#     return redirect('project:post')]

