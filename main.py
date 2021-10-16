from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFont, ImageDraw


class GUI:

    def __init__(self, window):
        # Set paths as empty strings.
        self.path1 = ""
        self.path2 = ""
        # Set images as an blank png so it doesnt crash.
        self.image1 = Image.open('vacio.png')
        self.image2 = Image.open('vacio.png')
        # Set label as variable so you can change it later.
        self.img_label1 = Label()
        # Set the user input to a StringVar so you can get the value later.
        self.user_input = StringVar()

        # Change window title.
        window.title("Automatic Watermarking Program")
        window.geometry("+50+50")

        # Create welcome label.
        Label(text='Welcome to the automatic watermarking program.').grid(column=0,
                                                                          row=0,
                                                                          pady=20,
                                                                          padx=10,
                                                                          columnspan=3)

        # Create button to select image.
        Button(text='Select Image', command=self.select_img1).grid(column=0, row=1, pady=20, columnspan=3)

    def select_img1(self):
        """This function opens a search box to select the image you want to watermark."""
        self.path1 = askopenfilename()
        self.image1 = Image.open(self.path1)
        selected_img = ImageTk.PhotoImage(self.image1)

        self.set_label(selected_img)
        # Create buttons to select what to do.
        Button(text='Watermark with PNG', command=self.png_watermark).grid(column=0, row=3, pady=20)
        Button(text="Save Image", command=self.save_image).grid(column=1, row=3, pady=20)
        Button(text='Watermark with text', command=self.text_watermark).grid(column=2, row=4)
        Entry(text='Watermark with text', textvariable=self.user_input).grid(column=2, row=3)
        self.set_label(selected_img)

    def png_watermark(self):
        """This function watermarks the image with a png and calls the save_image and set_label functions."""
        self.path2 = askopenfilename()
        self.image2 = Image.open(self.path2).resize((100, 50))
        self.image1.paste(self.image2, (1800, 1030), self.image2)

        png_watermark_img = ImageTk.PhotoImage(self.image1)
        self.set_label(png_watermark_img)

    def text_watermark(self):
        """This function takes input text from entry and watermarks the image with it."""
        text = self.user_input.get()
        fnt = ImageFont.truetype("arial.ttf", 28, encoding="unic")
        draw = ImageDraw.Draw(self.image1)
        draw.text((1750, 1030), text, fill=(255, 255, 255), font=fnt)
        text_watermark_img = ImageTk.PhotoImage(self.image1)
        self.set_label(text_watermark_img)

    def set_label(self, img):
        """This function changes the label with the actual image."""
        self.img_label1 = Label(image=img)
        self.img_label1.grid(column=0, row=2, columnspan=3)
        self.img_label1.photo = img

    def save_image(self):
        """This function saves the image where you want it with the name you want."""
        result = asksaveasfilename(filetypes=(
            ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')),
            ('PNG', '*.png'),
            ('GIF', '*.gif')))
        self.image1.save(str(result) + '.png', 'PNG')
        print("Image Saved")


if __name__ == '__main__':
    """Initialize the class passing the window and create the mainloop"""
    window = Tk()
    gui = GUI(window)
    window.mainloop()
