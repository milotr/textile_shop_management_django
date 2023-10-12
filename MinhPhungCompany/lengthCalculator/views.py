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
            length = (1000/((form.cleaned_data['weight_10cm'] * 100)*form.cleaned_data['height']))*form.cleaned_data['weight']   
        context = {
            "length" : length
        }
        return render(request, "lengthCalculator/results.html", context)
