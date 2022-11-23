from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                         'aria-describedby': 'Hint2',
                                                         'aria-errormessage': 'Error2'
                                                         }),
                           label='Имя *', required=True)

    phone = forms.CharField(widget=forms.TextInput({'required': True,
                                                    'aria-describedby': 'Hint6',
                                                    'aria-errormessage': 'Error6'
                                                    }),
                            label='Телефон *', required=True)

    guests = forms.CharField(widget=forms.TextInput({'required': False,
                                                    'aria-describedby': 'Hint8',
                                                    'aria-errormessage': 'Error8'
                                                    }),
                             label='Количество гостей', required=False)

    message = forms.CharField(widget=forms.Textarea({'required': True,
                                                     'aria-describedby': 'Hint7',
                                                     'aria-errormessage': 'Error7'
                                                     }),
                              label='В какой день и время Вас ожидать? *', required=True)
