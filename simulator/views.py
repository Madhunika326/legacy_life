from django.shortcuts import render

def simulator_home(request):
    if request.method == 'POST':
        organs = request.POST.getlist('organs')  # Get organs from the form
        lives_saved = len(organs) * 3  #  Simple logic: each organ helps 3 people
        return render(request, 'simulator_result.html', {
            'organs': organs,
            'lives_saved': lives_saved
        })
    
    #  If not POST, show the simulator form
    return render(request, 'simulator.html')
