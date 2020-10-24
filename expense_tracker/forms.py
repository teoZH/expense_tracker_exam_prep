from django import forms
from expense_tracker.models import Profile, Expense


class CreateUser(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name')
        widgets = {
            'budget': forms.NumberInput(attrs={
                'step': 'any',
                'name': 'budget',
                'id': 'id_budget'
            }),
            'first_name': forms.TextInput(attrs={
                'name': 'first_name',
                'id': 'id_first_name',

            }),
            'last_name': forms.TextInput(attrs={
                'name': 'first_name',
                'id': 'id_last_name',

            })
        }

        labels = {
            'budget': "Budget",
            'first_name': 'First Name',
            'last_name': "Last Name"
        }


class CreateExpense(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image_url', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image_url': 'Link to Image',
            'price': 'Price'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'name': 'title',
                'id': 'id_title'
            }),
            'description': forms.Textarea(attrs={
                'name': 'description',
                'rows': '10',
                'cols': '40',
                'id': 'id_description'
            }),
            'image_url': forms.URLInput(attrs={
                'name': 'image_url',
                'id': 'id_image_url'
            }),
            'price': forms.NumberInput(attrs={
                'step': 'any',
                'name': 'price',
                'id': 'id_price'
            })

        }
