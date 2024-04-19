from django.shortcuts import render


def index_page(request):
    context = {
        'test_list': [1,2,3,4,5]
    }
    return render(request, 'index.html', context=context)
