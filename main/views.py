from django.shortcuts import render
import requests

def exchange(request):
    context = {'data': ''}
    
    if request.method == 'POST':
        answer = request.POST['answer']
        select1 = request.POST['select1']
        select2 = request.POST['select2']
        amount = float(answer)
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        rates = response.json().get('rates', {})

        if select1 in rates and select2 in rates:
            rate1 = rates[select1]
            rate2 = rates[select2]
            result = (amount / rate1) * rate2
            context = {'data': round(result, 2)}
        else:
            context = {'data': amount}            
        
    return render(request, "exchange.html", context)

# def exchange(request):
#     answer = ''
#     context = {'data': ''}
#     if request.method == 'POST':
#         answer = request.POST['answer']
#         select1 = request.POST['select1']
#         select2 = request.POST['select2']
#         if select1 == "azn" and select2 == "usd":
#             context = {'data': int(answer)/1.7}
#         elif select1 == "usd" and select2 == "azn":
#             context = {'data': int(answer)*1.7}
#         else:
#             context = {'data': answer}
    
#     return render(request, "exchange.html", context)


def exam(request):
    count_true = 0
    count_false = 0
    if request.method == 'POST':

        if 'sual1' in request.POST:
            if request.POST['sual1'] == 'c':
                count_true += 1

            else:
                count_false += 1
        else:
            pass
        

        if 'sual2' in request.POST:
            if request.POST['sual2'] == 'b':
                count_true += 1
            else:
                count_false += 1
        else:
            pass
        
        if 'sual3' in request.POST:
            if request.POST['sual3'] == 'd':
                count_true += 1
            else:
                count_false += 1
        else:
            pass

        if 'sual4' in request.POST:
            if request.POST['sual4'] == 'c':
                count_true += 1
            else:
                count_false += 1
        else:
            pass
        if 'sual5' in request.POST:
            if request.POST['sual5'] == 'a':
                count_true += 1
            else:
                count_false += 1
        else:
            pass

       
    context = {
        'true_': count_true,
        'false_': count_false,
        'point_': count_true * 20
        }
        
    return render(request, 'exam.html', context)

def calc(request):
    context = {'data': ''}
    if request.method == 'POST':
        first = request.POST['first']
        second = request.POST['second']
        operation = request.POST['operation']

        if operation == 'topla':
            context = {'data': int(first) + int(second)}
        elif operation == 'cix':
            context = {'data': int(first) - int(second)}
        elif operation == 'vur':
            context = {'data': int(first) * int(second)}
        elif operation == 'bol':
            context = {'data': int(first) / int(second)}
            
    return render(request, 'calc.html', context)