from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.core.window import Window
import requests, shutil
from PIL import Image

Window.size = (500,600)

class thing(App):
    index = 0

    def reload_img(self):
        headers = {'User-Agent': 'Chrome/41.0.2228.0'}
        image_url = "https://thispersondoesnotexist.com/image"
        local_name = "i_"+  str(self.index) + ".jpg"
        with open(local_name, 'wb') as f:
            i = requests.get(image_url, headers=headers).content
            f.write(i)
        ii = Image.open(local_name)
        ii = ii.resize((400,400))
        ii.save(local_name)
        self.im.source=local_name
        self.im.size=(500,500)
    
    im = AsyncImage()

    def close(self, insrance):
        shutil.os.remove("i_"+  str(self.index) + ".jpg")
        exit(0)

    def rate(self, instance):
        f = open("r_"+str(self.index)+".txt", "w")
        f.write(str(instance.text))
        f.close()
        self.index += 1
        self.reload_img()
        return

    def build(self):
        hook = BoxLayout(size=(500,100), pos_hint=(0,0))
        ihook = BoxLayout(size=(500,Window.height), pos_hint={'left':0, 'top':Window.height}, size_hint=(1,5/6), padding=[0,0,0,100])
        root = Widget()
        root.add_widget(hook)
        root.add_widget(ihook)

        self.reload_img()
        ihook.add_widget(self.im)

        b0 = Button(text="0",size_hint=(1,1))
        b0.bind(on_release=self.rate)
        hook.add_widget(b0)

        b1 = Button(text="1",size_hint=(1,1))
        b1.bind(on_release=self.rate)
        hook.add_widget(b1)

        b2 = Button(text="2",size_hint=(1,1))
        b2.bind(on_release=self.rate)
        hook.add_widget(b2)

        b3 = Button(text="3",size_hint=(1,1))
        b3.bind(on_release=self.rate)
        hook.add_widget(b3)

        b4 = Button(text="4")
        b4.bind(on_release=self.rate)
        hook.add_widget(b4)

        b5 = Button(text="5")
        b5.bind(on_release=self.rate)
        hook.add_widget(b5)

        b6 = Button(text="End")
        b6.bind(on_release=self.close)
        hook.add_widget(b6)


        return root

thing().run()