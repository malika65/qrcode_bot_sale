import qrcode 

def generate_qrcode(description):

    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5
    )

    data = description

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='block',back_color='white')
    
    return img

