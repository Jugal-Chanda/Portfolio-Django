from django import forms
from blog.models import Blog

class BlogCreateForm(forms.ModelForm):
    title = forms.CharField(label='Enter the blog title', max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Blog title Here"}))
    post = forms.CharField(label='Write post here',widget = forms.Textarea(attrs={'class':'form-control','placeholder':"Blog title Here"}))

    class Meta:
        """docstring for ."""
        model = Blog
        fields = ('title','post')
