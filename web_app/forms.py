from .models import contectus,profile,aaddimage,maddimage,laddimage

from django import forms

class contectform(forms.ModelForm):
    class Meta:
        model = contectus
        fields = '__all__'


class profileform(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'


class maddimgform(forms.ModelForm):
    class Meta:
        model = maddimage
        fields = '__all__'



class laddimgform(forms.ModelForm):
    class Meta:
        model = laddimage
        fields = '__all__'



class aaddimgform(forms.ModelForm):
    class Meta:
        model = aaddimage
        fields = '__all__'