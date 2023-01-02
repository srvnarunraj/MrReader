from django.shortcuts import redirect, render
import requests
def startup(request):
    return render(request,'index.html')
def search(request):
    if request.method=='POST':
        searchtxt = request.POST['x']
        url = 'https://www.googleapis.com/books/v1/volumes?q='+searchtxt
        r = requests.get(url)
        result = r.json()
        result_list = []
        try:
            for i in range(10):
                result_dict={
                'title':result['items'][i]['volumeInfo']['title'],
                'subtitle':result['items'][i]['volumeInfo'].get('subtitle'),
                'description':result['items'][i]['volumeInfo'].get('description')[:200],
                'count':result['items'][i]['volumeInfo'].get('pageCount'),
                'thumbnail':result['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':result['items'][i]['volumeInfo'].get('previewLink'),
                }
                result_list.append(result_dict)
        except:
            context={
                'results':result_list
            }
        return render(request,'index.html',context)
    else:
        return redirect('/')

    