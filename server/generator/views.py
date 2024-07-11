from django.http import JsonResponse


def get_image(request):
    if request.method == 'POST':
        data = request.POST.get('image')
        print(data)
        return JsonResponse({'success': data})
