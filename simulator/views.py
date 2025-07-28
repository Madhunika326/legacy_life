from django.shortcuts import render

def simulator_home(request):
    if request.method == 'POST':
        organs = request.POST.getlist('organs')
        lives_saved = len(organs) * 3  # Pedicted logic : each organ can help 3 people
        return render(request, 'simulator_result.html', {
            'organs': organs,
            'lives_saved': lives_saved
        })
    return render(request, 'simulator.html')

