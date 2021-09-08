from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'Message from {name} with email {from_email}:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg,from_email

    def send(self):

        subject, msg,from_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=from_email,
            recipient_list=[settings.EMAIL_HOST_USER,]
        )