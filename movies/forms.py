from django import forms
from .models import Movie, Rating, GenreType, RatingType
from datetime import date

INPUT_CLASSES = 'w-full mb-4 py-4 px-6 rounded-xl text-gray-800 border'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'genre', 'rating', 'release_date', 'images', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Name...',
            }),

            'genre': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Genre...',
            }),

            'rating': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Rating...',
            }),

            'release_date': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Release Date...',
                'type': 'date'
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Description...'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        release_date = cleaned_data.get('release_date')

        if release_date > date.today():
           
            self.add_error('release_date', forms.ValidationError("Future date is not accepted."))
        
        return cleaned_data
    
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'w-40 py-2 px-6 rounded-xl bg-gray-700 text-white',
                'placeholder': 'Out of 5'
            })
        }

class MovieFilterForm(forms.Form):
    genre_types = forms.MultipleChoiceField(
        choices=GenreType.choices,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'this.form.submit();'}),
        required=False,
        label="Genre Types"
    )

    rating_types = forms.MultipleChoiceField(
        choices=RatingType.choices,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'this.form.submit();'}),
        required=False,
        label="Rating Types"
    )
