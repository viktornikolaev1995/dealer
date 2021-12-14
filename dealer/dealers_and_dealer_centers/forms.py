from django import forms
from .models import DealerCenterReviews

class DealerCenterReviewForm(forms.ModelForm):
    """Отзывы дилерского центра"""

    class Meta:
        model = DealerCenterReviews
        fields = ('name', 'text', 'email')

