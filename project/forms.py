from django import forms
from .models import Post, Img

from django.core.exceptions import ValidationError
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'style':'width:280px;','autofocus':'autofocus', 'autocomplete':'off', 'class':'form-control', 'id':'id_title', 'placeholder':'Doc title...'}),
            'content': forms.Textarea(attrs={'rows':18, 'cols':20, 'autocomplete':'off', 'class':'form-control', 'id':'id_content', 'placeholder':'start writing...'})
        }

# class PostFullForm(PostForm):
#     post_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
#     images = forms.FileField(widget=forms.ClearableFileInput(attrs={}),required=False)

#     def clean_images(self):
#         images = self.cleaned_data.get('images')
#         print('image type:',type(images))
                
#     class Meta(PostForm.Meta):
#         fields = PostForm.Meta.fields


class ImageUploadForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={}), required=False)

    def clean_images(self):
        images = self.cleaned_data.get('images')
        return images