from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition
from kivy.uix.image import Image
import sqlite3

conn=sqlite3.connect("db.db")
c=conn.cursor()


class ConnectingSigninRegister(ScreenManager):
    pass

class HomePage(Screen,BoxLayout):
    pass

class SigninWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.infologin

        uname=user.text
        passw=pwd.text
        templist=(uname,passw)
        fetchlist=list(c.execute("select username,password from logindetails"))
        if(templist in fetchlist):
            info.text='[color=#FF0000]Login Success[/color]'
            self.manager.current="homepage"
        else:
            info.text='[color=#FF0000]Wrong Username or password[/color]'


    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()

class RegisterWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def completeregister(self):
        name = self.ids.name_register.text
        email = self.ids.email_register.text
        user = self.ids.username_register.text
        pwd = self.ids.password_register.text
        info = self.ids.inforegister


        if(name=="" or email=="" or user=="" or pwd==""):
            info.text='[color=#FF0000]Please fill all the details![/color]'
        else:
            info.text='[color=#FF0000]Succesffully Succesfully Registered[/color]'
            templist=(name,email,user,pwd)
            c.execute("insert into logindetails values(?,?,?,?)",templist)


    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()


kv=Builder.load_file("signin.kv")

class SigninApp(App):
    def build(self):
        return kv

obj=SigninApp()
obj.run()
