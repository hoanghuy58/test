import kivy
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.core import window
from kivy.core.window import Window
from kivy.properties import StringProperty, BooleanProperty, Clock, NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import Property
#class GridLayoutExample(GridLayout):
#    pass

class CanvasExample5(Widget):

    diem_x = NumericProperty(0)
    diem = NumericProperty(0)
    vecxin_x = NumericProperty(Window.width/2)
    vecxin_y = NumericProperty(Window.height*0.9)
    meo_y = NumericProperty(Window.height/16)
    meo_x = NumericProperty(0)
    #diem_x = NumericProperty(0)
    diem_y = NumericProperty(0)
    def __init__(self, **kwargs):
        super(CanvasExample5, self).__init__(**kwargs)
        self.ball_size = 50

        self.width = 900
        self.height = 1600

        self.ball_x = Window.width / 2
        self.ball_y = Window.height /2
        self.ball_size = 1

        self.ball1_x = Window.width / 2
        self.ball1_y = Window.height /2
        self.ball1_size = 1

        self.ball2_x = Window.width / 2
        self.ball2_y = Window.height /2
        self.ball2_size = 1

        self.inx, self.iny = 4,6
        self.inx2, self.iny2 = 2,3
        self.inx1, self.iny1 = 5, 3

        self.size_meo_x = Window.width/10
        self.size_meo_y = Window.width/10 * 1.2

       # self.choilai = Button(text = "CHƠI LẠI ")
       # self.add_widget(self.choilai)

        self.vecxin = Image(source = "images\covid-19-5358852_640.png",size =(40,64),pos =(self.vecxin_x, self.vecxin_y))
        self.add_widget(self.vecxin)
        self.thanh_dichuyen = Slider(pos=(0,0), min=0, max= Window.width-40, width=Window.width, height = 60, value = 100,on_touch_move =self.dichuyen,on_touch_down= self.test_nhay) #,on_touch_down= self.test_nhay
        self.add_widget(self.thanh_dichuyen)
        self.meo = Image(source = "images\cd1.gif",pos = (self.meo_x,self.meo_y), size = (self.size_meo_x,self.size_meo_y))
        self.add_widget(self.meo)
        self.ball = Image(source = "images\do.png",pos = (self.ball_x,self.ball_y),size=(self.ball_size, self.ball_size))
        self.add_widget(self.ball)
        self.ball1 = Image(source="images\green.png", pos = (self.ball1_x,self.ball1_y),size=(self.ball1_size, self.ball1_size))
        self.add_widget(self.ball1)
        self.ball2 = Image(source="images\cut.png", pos = (self.ball2_x,self.ball2_y),size=(self.ball2_size, self.ball2_size))
        self.add_widget(self.ball2)
        self.event4 = Clock.schedule_interval(self.update4, 1 / 40)
        self.event1=Clock.schedule_interval(self.update1, 1 / 40)
        self.event=Clock.schedule_interval(self.update, 1/40)
        self.event2=Clock.schedule_interval(self.update2, 1/40)
        self.event3=Clock.schedule_interval(self.update3, 1/200)
        #cứ thười gian 0.5 lại thực hiện 1 hàm
    def choilai(self):
        self.ball.source = "images\do.png"
        self.ball1.source ="images\green.png"
        self.ball2.source = "images\cut.png"
        self.thanh_dichuyen.disabled = False
        self.diem = 0
        self.meo.source = "images\h1.gif"


    def on_size(self,*args):
        self.diem_x = self.width
        self.diem_y = self.height
       # print("on_size : ", str(self.width)," ",str(self.height))
       # print(self.ball.pos


    def dichuyen(self,*args):
        print(Window.width, Window.height)
        self.thanh_dichuyen.width = self.width
        self.thanh_dichuyen.max = self.width-self.size_meo_x*0.8
        if self.thanh_dichuyen.disabled == False:
            if self.meo_x > self.thanh_dichuyen.value and self.meo_y < self.height*0.15:
                self.meo.source = "images\cd2.gif"
            if self.meo_x < self.thanh_dichuyen.value and self.meo_y < self.height*0.15:
                self.meo.source = "images\cd1.gif"
            self.meo_x = self.thanh_dichuyen.value


    def test_nhay(self,*args):
       #self.meo.source = "images\cccc.gif"
       if self.meo_y < self.height*0.25 and self.thanh_dichuyen.disabled == False :
           self.meo_y +=self.height*0.08
           self.meo.pos = (self.meo_x,self.meo_y)

    def update4(self, dt):
        self.size_meo_x = self.width/10
        self.size_meo_y = self.width/10 * 1.2
        self.meo.size = (self.size_meo_x, self.size_meo_y)
        self.vecxin.size = (self.width/10,self.width/10)
        self.vecxin_y-=3
        if self.vecxin_y <= self.height/18 :
            self.vecxin_x = random.randint(50,self.width-50)
            self.vecxin_y = self.height*0.9
        if self.meo_x - self.size_meo_x/2 - self.width/16 < self.vecxin_x < self.meo_x + self.size_meo_x/2 + self.width/16 and self.meo_y < self.vecxin_y < self.meo_y+self.size_meo_y*0.8:
            self.diem +=1
            self.vecxin_x = random.randint(50, self.width-50)
            self.vecxin_y = self.height * 0.9
        self.vecxin.pos = (self.vecxin_x,self.vecxin_y)


    def update3(self,dt):
        if self.meo_y > self.height/16 :
            self.meo_y = self.meo_y - 3
            if  self.thanh_dichuyen.disabled == False:
                self.meo.source = "images\h1.gif"
        self.meo.pos = (self.meo_x,self.meo_y)


    def update2(self,dt):
        if self.meo_x - self.size_meo_x/2 - self.ball2_size  < self.ball2_x < self.meo_x + self.size_meo_x/2 + self.ball2_size/4 and self.meo_y - self.ball2_size/4 < self.ball2_y < self.meo_y + self.size_meo_y*0.8:
            self.ball2.source = "images\cut_ac.png"
            self.meo.source = "images\Anim.gif"
            self.thanh_dichuyen.disabled = True
            #self.event2.cancel()
        self.ball2_x +=self.inx2
        self.ball2_y +=self.iny2
        self.ball2.pos = (self.ball2_x,self.ball2_y)
        self.ball2_size = self.width /8
        self.ball2.size = (self.ball2_size,self.ball2_size)
        if self.ball2_x + self.ball2_size  >= self.width or self.ball2_x <= 0 :
            self.inx2 = -self.inx2
        if self.ball2_y + self.ball2_size >= self.height*0.8 or self.ball2_y <= 0:
            self.iny2 = -self.iny2

    def update1(self, dt):
        if self.meo_x - self.size_meo_x/2 - self.ball1_size < self.ball1_x < self.meo_x + self.size_meo_x/2 + self.ball1_size/4 and self.meo_y - self.ball1_size/4 < self.ball1_y < self.meo_y + self.size_meo_y*0.8:
            self.ball1.source = "images\green_ac.png"
            self.meo.source = "images\Anim.gif"
            self.thanh_dichuyen.disabled = True
            #self.event1.cancel()
        self.ball1_x +=self.inx1
        self.ball1_y +=self.iny1
        self.ball1.pos = (self.ball1_x,self.ball1_y)
        self.ball1_size = self.width / 15
        self.ball1.size = (self.ball1_size,self.ball1_size)
        if self.ball1_x + self.ball1_size  >= self.width or self.ball1_x <= 0 :
            self.inx1 = -self.inx1
        if self.ball1_y + self.ball1_size >= self.height*0.8 or self.ball1_y <= 0:
            self.iny1 = -self.iny1

    def update(self,dt):
        if self.meo_x - self.size_meo_x/2 - self.ball_size < self.ball_x < self.meo_x + self.size_meo_x/2 + self.ball_size/4 and self.meo_y - self.ball_size/4 < self.ball_y < self.meo_y + self.size_meo_y*0.8:
            self.ball.source = "images\do_ac.png"
            self.meo.source = "images\Anim.gif"
            self.thanh_dichuyen.disabled = True
            #self.event.cancel()
        self.ball_x +=self.inx
        self.ball_y +=self.iny
        self.ball.pos = (self.ball_x,self.ball_y)
        self.ball_size = self.width/10
        self.ball.size = (self.ball_size,self.ball_size)
        if self.ball_x + self.ball_size  >= self.width or self.ball_x <= 0 :
            self.inx = -self.inx
        if self.ball_y + self.ball_size >= self.height*0.8 or self.ball_y <= 0:
            self.iny = -self.iny

class TheLabApp(App):
    def build(self):
        return CanvasExample5()

TheLabApp().run()