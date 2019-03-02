from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapSource
from kivy.app import App

root = Builder.load_string("""
#:import MapSource kivy.garden.mapview.MapSource
<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'
    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

RelativeLayout:
    MapView:
        id: mapview
        lat: 50.6394
        lon: 3.057
        zoom: 8

        MapMarker:
            lat: 50.6394
            lon: 3.057
        MapMarker:
            lat: -33.867
            lon: 151.206

    Toolbar:
        Label:
            id: 'pratham'
            text: "Longitude: {}".format(mapview.lon)
        Label:
            text: "Latitude: {}".format(mapview.lat)
    """)
#print(mapview.lon)
class main(App,BoxLayout):
    def build(self):
        self.jinchuriki()
        return root
    def jinchuriki(self,BoxLayout):
        print(self.current.ids.pratham.text)

obj=main()
obj.run()
