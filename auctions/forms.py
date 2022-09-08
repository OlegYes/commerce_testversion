from .models import Lots, Category
from django import forms

#class CreatelotForm(forms.Form):





class LotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = Lots
        #fields = "__all__"
        fields = [
            'title',
            'text_lot',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6',
            'image7',
            'category',
            'cost_initial',
            'close_lot_date',
            'close_lot_time'
        ]
        category = forms.ModelChoiceField(queryset=Category.objects.all())
        main_image = forms.ImageField()
        image1 = forms.ImageField()
        image2 = forms.ImageField()
        image3 = forms.ImageField()
        image4 = forms.ImageField()
        image5 = forms.ImageField()
        image6 = forms.ImageField()
        image7 = forms.ImageField()

        cost_initial = forms.DecimalField(max_digits=19, decimal_places=10)
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name lot"
            }),
            "text_lot": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Lot description"
            }),
            'close_lot_time': forms.TimeInput(attrs={
                "class": "front-control",
                'type': "time"
            }),
            'close_lot_date': forms.DateInput(attrs={
                "class": "front-contro",
                'type': "date"
            })

        }