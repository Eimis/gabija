from django.shortcuts import render


def main(request):
    '''Main app view
    '''

    return render(request, 'main.html', {})
