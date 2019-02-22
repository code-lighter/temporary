from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import sqlite3
conn=sqlite3.connect("db.db")
c=conn.cursor()
class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname=user.text
        passw=pwd.text
        templist=(uname,passw)
        fetchlist=list(c.execute("select * from logindetails"))
        if(templist in fetchlist):
            info.text='[color=#FF0000]Login Success[/color]'
        else:
            info.text='[color=#FF0000]username and/ or password required[/color]'



class SigninApp(App):
    def build(self):
        return SigninWindow()

obj=SigninApp()
obj.run()
