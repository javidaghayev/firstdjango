from django.shortcuts import render


def exchange(request):
    answer = ''
    context = {'data': ''}
    if request.method == 'POST':
        answer = request.POST['answer']
        select1 = request.POST['select1']
        select2 = request.POST['select2']
        if select1 == "azn" and select2 == "usd":
            context = {'data': int(answer)/1.7}
        elif select1 == "usd" and select2 == "azn":
            context = {'data': int(answer)*1.7}
        else:
            context = {'data': answer}
    
    return render(request, "exchange.html", context)


def exam(request):
    count_true = 0
    count_false = 0
    if request.method == 'POST':
        sual1 = request.POST['sual1']
        sual2 = request.POST['sual2']
        sual3 = request.POST['sual3']
        sual4 = request.POST['sual4']
        sual5 = request.POST['sual5']

        if sual1 == 'c':
            count_true += 1
        elif sual1 == '':
            pass
        else:
            count_false += 1
        
        if sual2 == 'b':
            count_true += 1
        else:
            count_false += 1

        if sual3 == 'd':
            count_true += 1
        else:
            count_false += 1

        if sual4 == 'c':
            count_true += 1
        else:
            count_false += 1

        if sual5 == 'a':
            count_true += 1
        else:
            count_false += 1
        
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