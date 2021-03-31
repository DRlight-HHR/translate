from django.http import HttpResponse
from django.shortcuts import render
from .forms import my_form


def change(request):
    if request.method == "POST":
        try:
            b = request.POST.get("number")
            b = int(b)
            print(b)
            if b is None:
                assert 10 / 0
        except:
            return render(request, 'tem_changing.html')

        if request.POST.get("select") == "Celsius to Fahrenheit":
            c = b * 1.8 + 32
            d = dict(value=c)
            return render(request, "tem_changing.html", d)
        else:
            c = (b - 32) / 1.8
            d = dict(value=c)
            return render(request, "tem_changing.html", d)

    return render(request, "tem_changing.html")


def login(request):
    My = my_form()
    a = dict(my_form=My)
    return render(request, "login_forms.html", a)

 
def translate(request):
    import goslate
    t = goslate.Goslate()
    bb = request.POST.get("text1")
    aa = request.POST.get("text2")
    if request.method == "POST":
        a = request.POST.get('leagues')
        if a == "English to Farsi":
            result = t.translate(aa, "fa")
            origin = aa
            end = dict(text_t=result, text_t1=origin)
            return render(request, "translate.html", end)
        else:
            result = t.translate(bb, "en")
            origin = bb
            end = dict(text_t=origin, text_t1=result)
            return render(request, "translate.html", end)

    return render(request, "translate.html")
