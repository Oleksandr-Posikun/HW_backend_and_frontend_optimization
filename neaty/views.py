from django.shortcuts import render

# Create your views here.

g_one = [
    {'title': 'neaty-g1-01', 'src': 'gallery_1/neaty-gallery-01.jpg', 'href': 'gallery_1/neaty-gallery-01.jpg', 'alt': 'neaty-gallery_1-01-img'},
    {'title': 'neaty-g1-02', 'src': 'gallery_1/neaty-gallery-02.jpg', 'href': 'gallery_1/neaty-gallery-02.jpg', 'alt': 'neaty-gallery_1-02-img'},
    {'title': 'neaty-g1-03', 'src': 'gallery_1/neaty-gallery-03.jpg', 'href': 'gallery_1/neaty-gallery-03.jpg', 'alt': 'neaty-gallery_1-03-img'},
    {'title': 'neaty-g1-04', 'src': 'gallery_1/neaty-gallery-04.jpg', 'href': 'gallery_1/neaty-gallery-04.jpg', 'alt': 'neaty-gallery_1-04-img'},
    {'title': 'neaty-g1-05', 'src': 'gallery_1/neaty-gallery-05.jpg', 'href': 'gallery_1/neaty-gallery-05.jpg', 'alt': 'neaty-gallery_1-05-img'}
]

g_second = [
    {'title': 'neaty-g2-01', 'src': 'gallery_2/neaty-gallery-01.jpg', 'href': 'gallery_2/neaty-gallery-01.jpg', 'alt': 'neaty-gallery_2-01-img'},
    {'title': 'neaty-g2-02', 'src': 'gallery_2/neaty-gallery-02.jpg', 'href': 'gallery_2/neaty-gallery-02.jpg', 'alt': 'neaty-gallery_2-02-img'},
    {'title': 'neaty-g2-03', 'src': 'gallery_2/neaty-gallery-03.jpg', 'href': 'gallery_2/neaty-gallery-03.jpg', 'alt': 'neaty-gallery_2-03-img'}
]

g_third = [
    {'title': 'neaty-g3-01', 'src': 'gallery_3/neaty-gallery-01.jpg', 'href': 'gallery_3/neaty-gallery-01.jpg', 'alt': 'neaty-gallery_3-01-img'},
    {'title': 'neaty-g3-02', 'src': 'gallery_3/neaty-gallery-02.jpg', 'href': 'gallery_3/neaty-gallery-02.jpg', 'alt': 'neaty-gallery_3-02-img'},
    {'title': 'neaty-g3-03', 'src': 'gallery_3/neaty-gallery-03.jpg', 'href': 'gallery_3/neaty-gallery-03.jpg', 'alt': 'neaty-gallery_3-03-img'},
    {'title': 'neaty-g3-04', 'src': 'gallery_3/neaty-gallery-04.jpg', 'href': 'gallery_3/neaty-gallery-04.jpg', 'alt': 'neaty-gallery_3-04-img'}
]


def index(request):
    form_data = {
        'name': request.POST.get("contact_name"),
        'mail': request.POST.get("contact_email"),
        'massage': request.POST.get("contact_message"),
    }

    params = {
        'gallery_data': [{'name': 'Gallery One', 'gallery_id': 'galleryone', 'gallery_img': g_one},
                         {'name': 'Gallery Second', 'gallery_id': 'secondgallery', 'gallery_img': g_second},
                         {'name': 'Gallery Third', 'gallery_id': 'thirdgallery', 'gallery_img': g_third}],
        'data': form_data,

    }
    return render(request, 'index.html', params)


