from django.forms import forms

from fileupload.models import FileUpload


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('title', 'file')

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False