from django.shortcuts import render
from lengthCalculator.forms import LengthCalculatorForm
from django.views import View

# -------------------------------------------------------------------------------------------
# LENGTH CALCULATOR VIEWS
# -------------------------------------------------------------------------------------------
class length_calculator(View):
    def get(self, request):
        form = LengthCalculatorForm()
        context = {
            "form": form,
        }
        return render(request, "lengthCalculator/calculator.html", context)

    def post(self, request):
        form = LengthCalculatorForm(request.POST)

        if form.is_valid():
            chiều_dài = (1000/((form.cleaned_data['cân_nặng_mẫu_vải'] * 100)*form.cleaned_data['chiều_cao']))*form.cleaned_data['cân_nặng_cả_cây']   
        context = {
            "chiều_dài" : chiều_dài
        }
        return render(request, "lengthCalculator/results.html", context)
