from django import forms
from . import models

class GuardianForm(forms.ModelForm):
    curriculum= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=models.Curriculums)
    class Meta:
        model = models.Guardian
        fields = ['first_name','last_name','email','phone','hear','lesson_type','curriculum']
        widgets = {
            'lesson_type':forms.RadioSelect,
        }

class AboutChildForm(forms.ModelForm):
    subject =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=models.subjects)
    class Meta:
        model = models.AboutChild
        fields = ('child_class','goal','subject','about')
                                          
class LocationForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = ('state','street_address')

class LessonForm(forms.ModelForm):
    days =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=models.days)
    class Meta:
        model = models.Lesson
        fields = ('days','start','weeks','hour_per_day','start_time') 
        widgets = {
            'start':forms.DateInput(attrs={'type':'date'}),
            'start_time':forms.TimeInput(attrs={'type':'time'}),
            'hour_per_day':forms.NumberInput({'type':'number'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('name','phone_number', 'email','message')
