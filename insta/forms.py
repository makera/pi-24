from django import forms

from insta.models import Post


def my_validator(value):
    raise forms.ValidationError("You should no pass!!")


# class PostForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea(), validators=[my_validator])
#     image = forms.ImageField()
#
#     def clean(self):
#         raise forms.ValidationError("Oh no!")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'profile')
