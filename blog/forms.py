from django import forms
from blog.models import Comment
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment#defines model used
        fields = ["content"]#defines wht field of model is required in form

    def __init__(self, *args, **kwargs):#*args gets variable length positional args, **kwargs gets variable length dictionary of keywords args
        super(CommentForm, self).__init__(*args, **kwargs)#calls parent constructor
        self.helper = FormHelper()#creates a Formhelper instance for effective form layout and styling
        self.helper.add_input(Submit('submit', 'Submit'))