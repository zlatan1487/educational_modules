from django import forms
from education_modules.models import EducationalModule, Review


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EducationModuleForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = EducationalModule
        fields = '__all__'


class ReviewForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Текст отзыва')
