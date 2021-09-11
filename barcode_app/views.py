from django.shortcuts import render
import qrcode
from PIL import Image
# Create your views here.


def home(request):
    context = {}
    text = request.GET.get('text')
    if text is not None:
        path = generate_barcode(text)
        context['text'] = text
        context['path'] = path
    return render(request, "barcode_app/index.html", context)


def generate_barcode(text):
    # taking image which user wants
    # in the QR code center
    Logo_link = 'user.jpg'

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    url = text

    # addingg URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Green'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    file_path = "media/barcode.png"
    QRimg.save(file_path)
    return file_path

    """

        When you run the program then it will take the input image and the base width. After that, the image will be reshaped and a QRcode object will be created. 
        Using the QRcode object various attributes will be assigned such as data or URL will be linked to the QR code using add_data() method, color of the QR code will be assigned using the make_image() method and the reshaped image will be placed in the QR code using the paste() method. 
        Finally, the generated QR code will be saved in a given location using the save() method.
    """
