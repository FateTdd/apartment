from django import forms


class FormMixin(object):
    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}


class User(forms.Form, FormMixin):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(max_length=20, min_length=6)


class ChangeInfo(forms.Form, FormMixin):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)
    address = forms.CharField(max_length=200)
