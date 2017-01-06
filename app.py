from flask import Flask, render_template,request
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#dir = "directory"
print("APP_ROOT = ", os.path.abspath(__file__))
images_folder = APP_ROOT + "/images/"
print(images_folder)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("upload.html")


class Unit:
    def __init__(self, img_url, name, desc):
        self.img_url = img_url
        self.name = name
        self.desc = desc

unit = []
@app.route('/upload', methods = ["POST"])
def upload():
    images_folder = os.path.join(APP_ROOT, 'static/images/')
    print(images_folder)

    if not os.path.isdir(images_folder):
        os.mkdir(images_folder) #mkdir = makedirectory

    name = request.form["name"]
    desc = request.form["desc"]
    print(name)
    print(desc)

    for image in request.files.getlist("file"):
        image_name = image.filename
        image_dir = "/".join([images_folder,image_name])
        #them 1 doi tuong vao csdl
        image.save(image_dir)
        unit.append(Unit(img_url=image_name, name=name, desc=desc))

    return render_template("loadimage.html", unit = unit )

@app.route("/loadimage")
def loadimage():
    return render_template("loadimage.html", unit = unit)

if __name__ == '__main__':
    app.run(debug=True)
