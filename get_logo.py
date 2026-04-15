import urllib.request
import ssl

url = "https://scontent-bom5-2.cdninstagram.com/v/t51.2885-19/339532397_540738681546643_8938332949018453391_n.jpg?stp=dst-jpg_s100x100_tt6&_nc_cat=102&ccb=7-5&_nc_sid=bf7eb4&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4zNDIuQzMifQ%3D%3D&_nc_ohc=PyIlJIiRoj8Q7kNvwH8tS_E&_nc_oc=Adpiw5bMECvsL8-u3fJ7I0VKEPTf5rX-gSIIymQTXOX9O5Dee9XPF4wxQjxHI6ZCzmA&_nc_zt=24&_nc_ht=scontent-bom5-2.cdninstagram.com&_nc_ss=7a30f&oh=00_Af2bHi48LPz7C87EaWHE5ZexvUEITKPmsq4r18JfV_Wcow&oe=69DC11D8"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response, open("logo.jpg", 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print("Logo downloaded to logo.jpg")
except Exception as e:
    print(f"Error: {e}")

