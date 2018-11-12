from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    phone = forms.CharField(label='Телефон', max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    citizenship = forms.CharField(label='Гражданство', max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Гражданство'}))
    consent_personal_data = forms.BooleanField(label='Согласие на обработку персональных данных')
    address = forms.CharField(label='Адрес', max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Адрес'}))
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'placeholder': 'Комментарий'}))
