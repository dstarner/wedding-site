from django import forms


BOOL_CHOICES = (
    (True, 'Joyfully Accept(s)'),
    (False, 'No')
)


class PartyRSVPForm(forms.Form):

    accepts = forms.IntegerField(label="Joyfully Accepts", initial=0, required=True)
