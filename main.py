import kivy

from kivy.config import Config 
Config.set("graphics", "width", "480")
Config.set("graphics", "height", "320")
Config.set('kivy', 'keyboard_mode', 'systemanddock')
screen_width = 480
screen_height = 320

from kivy.core.window import Window
Window.show_cursor = False
Window.softinput_mode = "below_target"

from kivy.uix.label import Label 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.textinput import TextInput

from server_communication import ServerCommunication


class ImageGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.image = Image(source="img/background.jpg", 
                size=self.size, pos=self.pos, allow_stretch=True, keep_ratio=False)
        
        self.bind(size=self._update_img, pos=self._update_img)
    
    def _update_img(self, instance, value):
        self.image.pos = instance.pos
        self.image.size = instance.size
    
    def change_image(self, source):
        self.image.source = source

class ImageFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            self.image = Image(source="img/background.jpg", 
                size=self.size, pos=self.pos, allow_stretch=True, keep_ratio=False)

        self.bind(size=self._update_img, pos=self._update_img)
    
    def _update_img(self, instance, value):
        self.image.pos = instance.pos
        self.image.size = instance.size
    
    def change_image(self, source):
        self.image.source = source

# Utils
def to_string(value):
    if value < 10:
        return '0' + str(value)    
    return str(value)

def minutes_border(minutes):
    if minutes < 0:
        minutes = 59
    if minutes > 59:
        minutes = 0
    return minutes

def hours_border(hour):
    if hour < 0:
        hour = 23
    if hour > 23:
        hour = 0
    return hour

def month_number_border(month_number):
    if month_number < 0:
        month_number = 11
    if month_number > 11:
        month_number = 0
    return month_number

def day_of_month_border(day_of_month):
    pass

def year_border(year):
    if year < 0:
        year = 0
    return year

def day_of_week_border(day_of_week):
    if day_of_week < 0:
        day_of_week = 6
    if day_of_week > 6:
        day_of_week = 0
    return day_of_week

def time_interval_border(time_interval):
    if time_interval < 0:
        time_interval = 3
    if time_interval > 3:
        time_interval = 0
    return time_interval
    

Builder.load_string(''' 
<ImageTopButtonText>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.25, .25, .25 ,1)
    border_radius: 35
    border_width: 2

    font_size: 0.16*self.height
    color: (.25,.25,.25,1)
    bold: True
    text_size: self.size     
    halign: 'center'
    valign: 'bottom'
    padding_y: 10

    canvas.before:
        Color:
            rgba: self.back_color
        Line:
            rounded_rectangle: ( self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
            width: 2
    
    Image:
        id: btn_image
        height: self.parent.height * 0.5
        center_x: self.parent.center_x
        center_y: self.parent.center_y - 15

<ImageButton>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.25, .25, .25 ,1)
    border_radius: 10
    border_width: 2

    canvas.before:
        Color:
            rgba: self.back_color
        Line:
            rounded_rectangle: ( self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
            width: 2
    
    Image:
        id: btn_image
        height: self.parent.height * 0.5
        center_x: self.parent.center_x
        center_y: self.parent.center_y

<ImageLeftButtonText>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.25, .25, .25 ,1)
    border_radius: 20
    border_width: 2

    font_size: 0.1*self.width
    color: (.25,.25,.25,1)
    bold: True
    text_size: self.size     
    halign: 'right'
    valign: 'center'
    padding_x: 15

    canvas.before:
        Color:
            rgba: self.back_color
        Line:
            rounded_rectangle: ( self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
            width: 2
    
    Image:
        id: btn_image
        height: self.parent.height * 0.7
        center_x: self.parent.x + self.width / 2 - 5
        center_y: self.parent.center_y

<ImageRightButtonText>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.25, .25, .25 ,1)
    border_radius: 20
    border_width: 2

    font_size: 0.1*self.width
    color: (.25,.25,.25,1)
    bold: True
    text_size: self.size     
    halign: 'left'
    valign: 'center'
    padding_x: 15

    canvas.before:
        Color:
            rgba: self.back_color
        Line:
            rounded_rectangle: ( self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
            width: 2
    
    Image:
        id: btn_image
        height: self.parent.height * 0.7
        center_x: self.parent.x + self.parent.width - self.width / 2
        center_y: self.parent.center_y

<TextButton>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.25, .25, .25 ,1)
    border_radius: 10
    border_width: 2

    color: (.25,.25,.25,1)
    bold: True
    text_size: self.size     
    halign: 'center'
    valign: 'center'

    canvas.before:
        Color:
            rgba: self.back_color
        Line:
            rounded_rectangle: ( self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
            width: 2
''')

class ImageTopButtonText(Button):
    def __init__(self, text, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.ids.btn_image.source = image_url

class ImageButton(Button): #ImageButton
    def __init__(self, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.ids.btn_image.source = image_url

    def update_image(self, new_image):
        self.ids.btn_image.source = new_image
        self.ids.btn_image.reload()

class ImageLeftButtonText(Button):
    def __init__(self, text, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.ids.btn_image.source = image_url

class ImageRightButtonText(Button):
    def __init__(self, text, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.ids.btn_image.source = image_url

class TextButton(Button):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text


############################################################
# Clock page
############################################################

class ClockPage(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")
        self.on_touch_down = self.clicked
        self.month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.date_str = str(server.getClockDayOfMonth()) + " " + self.month_names[server.getClockMonth()] + " " + str(server.getClockYear())
        self.dots = 1

        # Hours Label
        self.hours_label = Label(
            text=to_string(server.getClockHour()), 
            color=(.25,.25,.25,1),
            font_size="100",
            size_hint=(.2, .2), 
            pos_hint={'x':.25, 'y':.5})
        self.add_widget(self.hours_label)

        # Hours Label
        self.minutes_label = Label(
            text=to_string(server.getClockMinutes()), 
            color=(.25,.25,.25,1),
            font_size="100",
            size_hint=(.2, .2), 
            pos_hint={'x':.55, 'y':.5})
        self.add_widget(self.minutes_label)

        # Dots ":"
        self.dots_label = Label(
            text=":", 
            halign="center",
            color=(.25,.25,.25,1),
            font_size="100",
            size_hint=(.04, .2), 
            pos_hint={'x':.48, 'y':.52})
        self.add_widget(self.dots_label)

        # Date
        self.date_label = Label(
            text=self.date_str, 
            color=(.25,.25,.25,1),
            font_size="50",
            size_hint=(.8, .2), 
            pos_hint={'x':.1, 'y':.25})
        self.add_widget(self.date_label)

        # Title
        self.title = Label(
            text="SMART MEDICAL BOX", 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(1, .2), 
            pos_hint={'x':.0, 'y':.8})
        self.add_widget(self.title)
        
        with self.canvas:
            Color(.25,.25,.25)
            Line(points=[0, screen_height*0.8, screen_width, screen_height*0.8], width=2)


        self.update_clock_interval = Clock.schedule_interval(self._update_clock, 1)

    def _update_clock(self, *args):
        self.date_str = str(server.getClockDayOfMonth()) + " " + self.month_names[server.getClockMonth()] + " " + str(server.getClockYear())
        self.date_label.text = self.date_str
        self.hours_label.text = to_string(server.getClockHour())
        self.minutes_label.text = to_string(server.getClockMinutes())

        if self.dots:   
            self.dots_label.text = ""
            self.dots = 0
        else:
            self.dots_label.text = ":"
            self.dots = 1

    def clicked(self, instance):
        smart_medical_box_ui.main_menu_page.change_page()


############################################################
# Main Menu page
############################################################

class MainMenuPage(ImageGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.cols = 3
        self.padding = [20, 40]
        self.spacing = 20

        self.back = ImageTopButtonText(text="BACK", image_url="img/png/long_arrow_alt_left.png")
        self.back.bind(on_press=self.function_back)
        self.add_widget(self.back)

        self.fill_box = ImageTopButtonText(text="FILL BOX", image_url="img/png/pills.png")
        self.fill_box.bind(on_press=self.function_fill_box)
        self.add_widget(self.fill_box)

        self.fill_insulin = ImageTopButtonText(text="FILL INSULIN", image_url="img/png/syringe.png")
        self.fill_insulin.bind(on_press=self.function_fill_insulin)
        self.add_widget(self.fill_insulin)

        self.set_clock = ImageTopButtonText(text="SET CLOCK", image_url="img/png/clock_cog.png")
        self.set_clock.bind(on_press=self.function_set_clock)
        self.add_widget(self.set_clock)

        self.set_intervals = ImageTopButtonText(text="SET BOX", image_url="img/png/pill_cog.png")
        self.set_intervals.bind(on_press=self.function_set_intervals)
        self.add_widget(self.set_intervals)

        self.settings = ImageTopButtonText(text="SET INSULIN", image_url="img/png/syringe_cog.png")
        self.settings.bind(on_press=self.function_settings)
        self.add_widget(self.settings)

    def function_back(self, instance):
        server.enableAutomaticBox()
        smart_medical_box_ui.screen_manager.current = "Clock"

    def function_fill_box(self, instance):
        smart_medical_box_ui.fill_box.change_page()

    def function_fill_insulin(self, instance):
        smart_medical_box_ui.fill_insulin.change_page()

    def function_set_clock(self, instance):
        smart_medical_box_ui.set_clock_time.change_page()

    def function_set_intervals(self, instance):
        smart_medical_box_ui.set_intervals.change_page()

    def function_settings(self, instance):
        smart_medical_box_ui.set_insulin_intervals_day.change_page()

    def change_page(self):
        server.disableAutomaticBox()
        smart_medical_box_ui.screen_manager.current = "MainMenu"



############################################################
# Clock Settings Pages
############################################################

class SetClockTime(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.hours = server.getClockHour()
        self.minutes = server.getClockMinutes()

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Selection Buttons
        self.button_right = ImageRightButtonText(text="NEXT", image_url="img/png/long_arrow_alt_right.png", size_hint=(.4, .12), pos_hint={'x':0.58, 'y':0.02})
        self.button_right.bind(on_press=self.set_clock_date_page)
        self.add_widget(self.button_right)

        # Hour Buttons
        self.plus_hour = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_hour = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_hour.bind(on_press=self.add_one_hour)
        self.minus_hour.bind(on_press=self.subtract_one_hour)
        self.add_widget(self.plus_hour)
        self.add_widget(self.minus_hour)

        # Minute Buttons
        self.plus_minute = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.minus_minute = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
        self.plus_minute.bind(on_press=self.add_one_minute)
        self.minus_minute.bind(on_press=self.subtract_one_minute)
        self.add_widget(self.plus_minute)
        self.add_widget(self.minus_minute)

        # Hours Label
        self.hours_label = Label(
            text=to_string(self.hours), 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.25, 'y':.4})
        self.add_widget(self.hours_label)

        # Dots ":"
        self.dots = Label(
            text=":", 
            color=(.25,.25,.25,1),
            font_size="60",
            size_hint=(.10, .15), 
            pos_hint={'x':.45, 'y':.4})
        self.add_widget(self.dots)

        # Minutes Label
        self.minutes_label = Label(
            text=to_string(self.minutes), 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.55, 'y':.4})
        self.add_widget(self.minutes_label)

        # Page Title
        self.page_title_label = Label(
            text="CLOCK SETUP", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Hours Name Label
        self.hours_name_label = Label(
            text="HOURS", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.25, 'y':.15})
        self.add_widget(self.hours_name_label)

        # Minutes Name Label
        self.minutes_name_label = Label(
            text="MINUTES", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.55, 'y':.15})
        self.add_widget(self.minutes_name_label)

    def add_one_hour(self, instance):
        self.hours = hours_border(self.hours + 1)
        self.hours_label.text = to_string(self.hours)
        server.setClockHour(self.hours)

    def subtract_one_hour(self, instance):
        self.hours = hours_border(self.hours - 1)
        self.hours_label.text = to_string(self.hours)
        server.setClockHour(self.hours)

    def add_one_minute(self, instance):
        self.minutes = minutes_border(self.minutes + 1)
        self.minutes_label.text = to_string(self.minutes)
        server.setClockMinutes(self.minutes)

    def subtract_one_minute(self, instance):
        self.minutes = minutes_border(self.minutes - 1)
        self.minutes_label.text = to_string(self.minutes)
        server.setClockMinutes(self.minutes)

    def set_clock_date_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.set_clock_date.change_page()

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.hours = server.getClockHour()
        self.minutes = server.getClockMinutes()
        self.hours_label.text = to_string(self.hours)
        self.minutes_label.text = to_string(self.minutes)

        smart_medical_box_ui.screen_manager.current = "SetClockTime"

class SetClockDate(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.month_names = ["JAN.", "FEB.", "MAR.", "APR.", "MAY.", "JUN.", "JUL.", "AUG.", "SEP.", "OCT.", "NOV.", "DEC."]

        self.day = server.getClockDayOfMonth()
        self.month_number = server.getClockMonth()

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Selection Buttons
        self.button_left = ImageLeftButtonText(text="PREVIOUS", image_url="img/png/long_arrow_alt_left.png", size_hint=(.4, .12), pos_hint={'x':0.02, 'y':0.02})
        self.button_right = ImageRightButtonText(text="NEXT", image_url="img/png/long_arrow_alt_right.png", size_hint=(.4, .12), pos_hint={'x':0.58, 'y':0.02})
        self.button_left.bind(on_press=self.set_clock_time_page)
        self.button_right.bind(on_press=self.set_clock_weekday_year_page)
        self.add_widget(self.button_left)
        self.add_widget(self.button_right)

        # Day Buttons
        self.plus_day = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_day = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_day.bind(on_press=self.add_one_day)
        self.minus_day.bind(on_press=self.subtract_one_day)
        self.add_widget(self.plus_day)
        self.add_widget(self.minus_day)

        # Month Buttons
        self.next_month = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.previous_month = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
        self.next_month.bind(on_press=self.add_one_month)
        self.previous_month.bind(on_press=self.subtract_one_month)
        self.add_widget(self.next_month)
        self.add_widget(self.previous_month)

        # Day Label
        self.day_label = Label(
            text=to_string(self.day), 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.25, 'y':.4})
        self.add_widget(self.day_label)

        # Month Label
        self.month_label = Label(
            text=self.month_names[self.month_number], 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.55, 'y':.4})
        self.add_widget(self.month_label)

        # Page Title
        self.page_title_label = Label(
            text="CLOCK SETUP", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Day Name Label
        self.day_name_label = Label(
            text="DAY", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.25, 'y':.15})
        self.add_widget(self.day_name_label)

        # Month Name Label
        self.month_name_label = Label(
            text="MONTH", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.55, 'y':.15})
        self.add_widget(self.month_name_label)

    def add_one_day(self, instance):
        self.day = self.day + 1
        self.day_label.text = to_string(self.day)
        server.setClockDayOfMonth(self.day)

    def subtract_one_day(self, instance):
        self.day = self.day - 1
        self.day_label.text = to_string(self.day)
        server.setClockDayOfMonth(self.day)

    def add_one_month(self, instance):
        self.month_number = month_number_border(self.month_number + 1)
        self.month_label.text = self.month_names[self.month_number]
        server.setClockMonth(self.month_number)

    def subtract_one_month(self, instance):
        self.month_number = month_number_border(self.month_number - 1)
        self.month_label.text = self.month_names[self.month_number]
        server.setClockMonth(self.month_number)

    def set_clock_time_page(self, instance):
        smart_medical_box_ui.set_clock_time.change_page()

    def set_clock_weekday_year_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.set_clock_weekday_year.change_page()
    
    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.day = server.getClockDayOfMonth()
        self.month_number = server.getClockMonth()

        self.day_label.text = to_string(self.day)
        self.month_label.text = self.month_names[self.month_number]

        smart_medical_box_ui.screen_manager.current = "SetClockDate"

class SetClockWeekdayYear(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.day_names = ["MON.", "TUE.", "WED.", "THU.", "FRI.", "SAT.", "SUN."]

        self.day_of_week_number = server.getClockDayOfWeek()
        self.year = server.getClockYear()

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Selection Buttons
        self.button_left = ImageLeftButtonText(text="PREVIOUS", image_url="img/png/long_arrow_alt_left.png", size_hint=(.4, .12), pos_hint={'x':0.02, 'y':0.02})
        self.button_left.bind(on_press=self.set_clock_date_page)
        self.add_widget(self.button_left)

        # Day Buttons
        self.plus_day_of_week = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_day_of_week = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_day_of_week.bind(on_press=self.add_one_day_of_week)
        self.minus_day_of_week.bind(on_press=self.subtract_one_day_of_week)
        self.add_widget(self.plus_day_of_week)
        self.add_widget(self.minus_day_of_week)

        # Year Buttons
        self.plus_year = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.minus_year = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
        self.add_widget(self.plus_year)
        self.add_widget(self.minus_year)
        self.plus_year.bind(on_press=self.add_one_year)
        self.minus_year.bind(on_press=self.subtract_one_year)

        # Day Of Week Label
        self.day_of_week_label = Label(
            text=self.day_names[self.day_of_week_number], 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.25, 'y':.4})
        self.add_widget(self.day_of_week_label)

        # Year Label
        self.year_label = Label(
            text=str(self.year), 
            color=(.25,.25,.25,1),
            font_size="40",
            size_hint=(.2, .15), 
            pos_hint={'x':.55, 'y':.4})
        self.add_widget(self.year_label)

        # Page Title Label
        self.page_title_label = Label(
            text="CLOCK SETUP", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Day Of Week Name Label
        self.day_of_week_name_label = Label(
            text="DAY", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.25, 'y':.15})
        self.add_widget(self.day_of_week_name_label)

        # Year Name Label
        self.year_name_label = Label(
            text="YEAR", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.2, .1), 
            pos_hint={'x':0.55, 'y':.15})        
        self.add_widget(self.year_name_label)

    def add_one_day_of_week(self, instance):
        self.day_of_week_number = day_of_week_border(self.day_of_week_number + 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        server.setClockDayOfWeek(self.day_of_week_number)

    def subtract_one_day_of_week(self, instance):
        self.day_of_week_number = day_of_week_border(self.day_of_week_number - 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        server.setClockDayOfWeek(self.day_of_week_number)

    def add_one_year(self, instance):
        self.year = year_border(self.year + 1)
        self.year_label.text = str(self.year)
        server.setClockYear(self.year)

    def subtract_one_year(self, instance):
        self.year = year_border(self.year - 1)
        self.year_label.text = str(self.year)
        server.setClockYear(self.year)

    def set_clock_date_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.set_clock_date.change_page()
    
    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.day_of_week_number = server.getClockDayOfWeek()
        self.year = server.getClockYear()

        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        self.year_label.text = str(self.year)

        smart_medical_box_ui.screen_manager.current = "SetClockWeekdayYear"


############################################################
# Set Intervals Page
############################################################

class SetIntervals(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.interval_names = ["MORNING", "MIDDAY", "EVENING", "NIGHT"]
        self.interval_icons = ["img/png/sunrise.png", "img/png/sun.png", "img/png/moon_rotated.png", "img/png/bed_stars.png"]
        self.current_interval = 0
        self.inactive_active = ["INACTIVE", "ACTIVE"]

        self.use_interval       = [0, 0, 0, 0]
        self.interval_start_hh  = [0, 0, 0, 0]
        self.interval_start_mm  = [0, 0, 0, 0]
        self.interval_end_hh    = [0, 0, 0, 0]
        self.interval_end_mm    = [0, 0, 0, 0]

        self.fill_intervals()

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Title
        self.title = Label(
            text=self.interval_names[self.current_interval] + " INTERVAL", 
            color=(.25,.25,.25,1),
            font_size="27",
            size_hint=(.56, .1), 
            pos_hint={'x':.44, 'y':.88})
        self.add_widget(self.title)

        # Interval Icon
        self.icon = Image(
            source = self.interval_icons[self.current_interval],
            size_hint=(.2, .2), 
            pos_hint={'x':.22, 'y':.78})
        self.add_widget(self.icon)

        # Start Interval Title
        self.start_title = Label(
            text="START", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.15, 'y':.65})
        self.add_widget(self.start_title)

        # End Interval Title
        self.end_title = Label(
            text="END", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.55, 'y':.65})
        self.add_widget(self.end_title)

        # Start interval hour label
        self.start_interval_hour_label = Label(
            text=to_string(self.interval_start_hh[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.15, 'y':.3})
        self.add_widget(self.start_interval_hour_label)

        # Start interval minutes label
        self.start_interval_minutes_label = Label(
            text= to_string(self.interval_start_mm[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.35, 'y':.3})
        self.add_widget(self.start_interval_minutes_label)

        # End interval hour label
        self.end_interval_hour_label = Label(
            text= to_string(self.interval_end_hh[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.55, 'y':.3})
        self.add_widget(self.end_interval_hour_label)

        # End interval minutes label
        self.end_interval_minutes_label = Label(
            text= to_string(self.interval_end_mm[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.75, 'y':.3})
        self.add_widget(self.end_interval_minutes_label)

        # Start interval hour buttons
        self.start_interval_hour_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.12, 'y':.47})
        self.start_interval_hour_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.12, 'y':.18})

        self.start_interval_hour_button_plus.bind(on_press=self.start_interval_add_hour)
        self.start_interval_hour_button_minus.bind(on_press=self.start_interval_subtract_hour)

        self.add_widget(self.start_interval_hour_button_plus)
        self.add_widget(self.start_interval_hour_button_minus)

        # Start interval minutes buttons
        self.start_interval_minutes_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.32, 'y':.47})
        self.start_interval_minutes_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.32, 'y':.18})

        self.start_interval_minutes_button_plus.bind(on_press=self.start_interval_add_minute)
        self.start_interval_minutes_button_minus.bind(on_press=self.start_interval_subtract_minute)

        self.add_widget(self.start_interval_minutes_button_plus)
        self.add_widget(self.start_interval_minutes_button_minus)

        # End interval hour buttons
        self.end_interval_hour_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.52, 'y':.47})
        self.end_interval_hour_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.52, 'y':.18})

        self.end_interval_hour_button_plus.bind(on_press=self.end_interval_add_hour)
        self.end_interval_hour_button_minus.bind(on_press=self.end_interval_subtract_hour)

        self.add_widget(self.end_interval_hour_button_plus)
        self.add_widget(self.end_interval_hour_button_minus)

        # End interval minutes buttons
        self.end_interval_minutes_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.72, 'y':.47})
        self.end_interval_minutes_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.72, 'y':.18})

        self.end_interval_minutes_button_plus.bind(on_press=self.end_interval_add_minute)
        self.end_interval_minutes_button_minus.bind(on_press=self.end_interval_subtract_minute)

        self.add_widget(self.end_interval_minutes_button_plus)
        self.add_widget(self.end_interval_minutes_button_minus)

        # Active / Inactive interval
        self.active_inactive_button = TextButton(
            text=self.inactive_active[self.use_interval[self.current_interval]],
            font_size="20",
            size_hint=(.4, .1), 
            pos_hint={'x':.5, 'y':.75})
        self.active_inactive_button.bind(on_press=self.change_interval_state)
        self.add_widget(self.active_inactive_button)

        # Interval select buttons
        self.previous = ImageLeftButtonText(text="PREVIOUS", image_url="img/png/long_arrow_alt_left.png", size_hint=(.4, .12), pos_hint={'x':0.02, 'y':0.02})
        self.next = ImageRightButtonText(text="NEXT", image_url="img/png/long_arrow_alt_right.png", size_hint=(.4, .12), pos_hint={'x':0.58, 'y':0.02})
        self.previous.bind(on_press=self.previous_interval)
        self.next.bind(on_press=self.next_interval)
        self.add_widget(self.previous)
        self.add_widget(self.next)


    def start_interval_add_hour(self, instance):
        self.interval_start_hh[self.current_interval] = hours_border(self.interval_start_hh[self.current_interval] + 1)
        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])
        self.setInterval()

    def start_interval_subtract_hour(self, instance):
        self.interval_start_hh[self.current_interval] = hours_border(self.interval_start_hh[self.current_interval] - 1)
        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])
        self.setInterval()


    def start_interval_add_minute(self, instance):
        self.interval_start_mm[self.current_interval] = minutes_border(self.interval_start_mm[self.current_interval] + 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])
        self.setInterval()

    def start_interval_subtract_minute(self, instance):
        self.interval_start_mm[self.current_interval] = minutes_border(self.interval_start_mm[self.current_interval] - 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])
        self.setInterval()


    def end_interval_add_hour(self, instance):
        self.interval_end_hh[self.current_interval] = hours_border(self.interval_end_hh[self.current_interval] + 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])
        self.setInterval()

    def end_interval_subtract_hour(self, instance):
        self.interval_end_hh[self.current_interval] = hours_border(self.interval_end_hh[self.current_interval] - 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])
        self.setInterval()

    
    def end_interval_add_minute(self, instance):
        self.interval_end_mm[self.current_interval] = minutes_border(self.interval_end_mm[self.current_interval] + 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])
        self.setInterval()

    def end_interval_subtract_minute(self, instance):
        self.interval_end_mm[self.current_interval] = minutes_border(self.interval_end_mm[self.current_interval] - 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])
        self.setInterval()

    
    def change_interval_state(self, instance):
        if self.use_interval[self.current_interval] == 1:
            self.use_interval[self.current_interval] = 0
        else:
            self.use_interval[self.current_interval] = 1
        
        self.active_inactive_button.text = self.inactive_active[self.use_interval[self.current_interval]]

        self.setInterval()


    def next_interval(self, instance):
        self.current_interval = self.current_interval + 1
        if self.current_interval > 3:
            self.current_interval = 0

        self.update_labels()

    def previous_interval(self, instance):
        self.current_interval = self.current_interval - 1
        if self.current_interval < 0:
            self.current_interval = 3

        self.update_labels()

    def update_labels(self):
        self.title.text = self.interval_names[self.current_interval] + " INTERVAL"
        self.active_inactive_button.text = self.inactive_active[self.use_interval[self.current_interval]]
        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])
        self.icon.source = self.interval_icons[self.current_interval]
        self.icon.reload()

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def fill_intervals(self):
        morning_interval = server.getNormalIntervalByName("morning")
        midday_interval = server.getNormalIntervalByName("midday")
        evening_interval = server.getNormalIntervalByName("evening")
        night_interval = server.getNormalIntervalByName("night")

        self.use_interval       = [morning_interval["active"], midday_interval["active"], evening_interval["active"], night_interval["active"]]
        self.interval_start_hh  = [morning_interval["time_start_h"], midday_interval["time_start_h"], evening_interval["time_start_h"], night_interval["time_start_h"]]
        self.interval_start_mm  = [morning_interval["time_start_m"], midday_interval["time_start_m"], evening_interval["time_start_m"], night_interval["time_start_m"]]
        self.interval_end_hh    = [morning_interval["time_end_h"], midday_interval["time_end_h"], evening_interval["time_end_h"], night_interval["time_end_h"]]
        self.interval_end_mm    = [morning_interval["time_end_m"], midday_interval["time_end_m"], evening_interval["time_end_m"], night_interval["time_end_m"]]
    
    def setInterval(self):
        server.setOrUpdateNormalInterval(
            self.interval_names[self.current_interval].lower(), 
            self.interval_start_hh[self.current_interval], 
            self.interval_start_mm[self.current_interval], 
            self.interval_end_hh[self.current_interval], 
            self.interval_end_mm[self.current_interval], 
            self.use_interval[self.current_interval]
        )
    
    def change_page(self):
        self.current_interval = 0
        self.fill_intervals()
        self.update_labels()
        smart_medical_box_ui.screen_manager.current = "SetIntervals"
        

############################################################
# Filll Box Page
############################################################

class FillBox(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.day_names = ["MON.", "TUE.", "WED.", "THU.", "FRI.", "SAT.", "SUN."]
        self.day_of_week_number = 0

        self.interval_names = ["MORNING", "MIDDAY", "EVENING", "NIGHT"]
        self.interval_icons = ["img/png/sunrise.png", "img/png/sun.png", "img/png/moon_rotated.png", "img/png/bed_stars.png"]
        self.current_interval = 0

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="FILL BOX", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Day Of Week Label
        self.day_of_week_label = Label(
            text=self.day_names[self.day_of_week_number], 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.2, .2), 
            pos_hint={'x':.5, 'y':.27})
        self.add_widget(self.day_of_week_label)

        # Time Interval Label
        # self.time_interval_label = Label(
        #     text=self.interval_names[self.current_interval], 
        #     color=(.25,.25,.25,1),
        #     font_size="35",
        #     size_hint=(.4, .15), 
        #     pos_hint={'x':.3, 'y':.22})
        # self.add_widget(self.time_interval_label)

        self.icon = Image(
            source = self.interval_icons[self.current_interval],
            size_hint=(.2, .2), 
            pos_hint={'x':.3, 'y':.27})
        self.add_widget(self.icon)

        # Control Buttons
        self.button_up = ImageButton(
            image_url=self.interval_icons[time_interval_border(self.current_interval - 1)], 
            size_hint=(.4, .2), 
            pos_hint={'x':.3, 'y':.52})
        self.button_down = ImageButton(
            image_url=self.interval_icons[time_interval_border(self.current_interval + 1)], 
            size_hint=(.4, .2), 
            pos_hint={'x':.3, 'y':.02})

        self.button_left = ImageButton(
            image_url="img/png/long_arrow_alt_left.png", 
            size_hint=(.2, .3), 
            pos_hint={'x':.1, 'y':.22})
        self.button_right = ImageButton(
            image_url="img/png/long_arrow_alt_right.png", 
            size_hint=(.2, .3), 
            pos_hint={'x':.7, 'y':.22})

        self.button_up.bind(on_press=self.previous_interval)
        self.button_down.bind(on_press=self.next_interval)
        self.button_left.bind(on_press=self.subtract_one_day_of_week)
        self.button_right.bind(on_press=self.add_one_day_of_week)

        self.add_widget(self.button_up)
        self.add_widget(self.button_down)
        self.add_widget(self.button_left)
        self.add_widget(self.button_right)

    def add_one_day_of_week(self, instance):
        server.closeBox(self.day_of_week_number, self.current_interval)
        self.day_of_week_number = day_of_week_border(self.day_of_week_number + 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        server.openBox(self.day_of_week_number, self.current_interval)

    def subtract_one_day_of_week(self, instance):
        server.closeBox(self.day_of_week_number, self.current_interval)
        self.day_of_week_number = day_of_week_border(self.day_of_week_number - 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        server.openBox(self.day_of_week_number, self.current_interval)

    def next_interval(self, instance):
        server.closeBox(self.day_of_week_number, self.current_interval)
        self.current_interval = time_interval_border(self.current_interval + 1)
        self.change_interval_label_and_icons()
        server.openBox(self.day_of_week_number, self.current_interval)
        
    def previous_interval(self, instance):
        server.closeBox(self.day_of_week_number, self.current_interval)
        self.current_interval = time_interval_border(self.current_interval - 1)
        self.change_interval_label_and_icons()
        server.openBox(self.day_of_week_number, self.current_interval)

    def change_interval_label_and_icons(self):
        #self.time_interval_label.text = self.interval_names[self.current_interval]
        self.button_up.update_image(self.interval_icons[time_interval_border(self.current_interval - 1)])
        self.button_down.update_image(self.interval_icons[time_interval_border(self.current_interval + 1)])
        self.icon.source = self.interval_icons[self.current_interval]
        self.icon.reload()

    def main_menu_page(self, instance):
        print("Next Page")
        server.closeBoxAll()
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.day_of_week_number = 0
        self.current_interval = 0

        self.day_of_week_label.text = self.day_names[self.day_of_week_number]
        self.change_interval_label_and_icons()
        #self.time_interval_label.text = self.interval_names[self.current_interval]

        server.openBox(self.day_of_week_number, self.current_interval)
        smart_medical_box_ui.screen_manager.current = "FillBox"


############################################################
# Filll Insulin Page
############################################################

class FillInsulin(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.day_insulin_state = 1
        self.night_insulin_state = 1
        self.close_open = ["CLOSE", "OPEN"]

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="FILL INSULIN", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Open / Close insulin day
        self.open_close_insulin_day = TextButton(
            text=self.close_open[self.day_insulin_state] + " INSULIN DAY", 
            font_size="40",
            size_hint=(.96, .3), 
            pos_hint={'x':.02, 'y':.37})
        self.open_close_insulin_day.bind(on_press=self.invert_insulin_day_state)
        self.add_widget(self.open_close_insulin_day)

        # Open / Close insulin night
        self.open_close_insulin_night = TextButton(
            text=self.close_open[self.night_insulin_state] + " INSULIN NIGHT", 
            font_size="40",
            size_hint=(.96, .3), 
            pos_hint={'x':.02, 'y':.02})
        self.open_close_insulin_night.bind(on_press=self.invert_insulin_night_state)
        self.add_widget(self.open_close_insulin_night)

    def invert_insulin_day_state(self, instance):
        if self.day_insulin_state == 1:
            self.day_insulin_state = 0
            server.openInsulinDay()
        else:
            self.day_insulin_state = 1 
            server.closeInsulinDay()

        self.open_close_insulin_day.text = self.close_open[self.day_insulin_state] + " INSULIN DAY"

    def invert_insulin_night_state(self, instance):
        if self.night_insulin_state == 1:
            self.night_insulin_state = 0
            server.openInsulinNight()
        else:
            self.night_insulin_state = 1 
            server.closeInsulinNight()

        self.open_close_insulin_night.text = self.close_open[self.night_insulin_state] + " INSULIN NIGHT"

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.day_insulin_state = 1
        self.night_insulin_state = 1
        self.open_close_insulin_day.text = self.close_open[self.day_insulin_state] + " INSULIN DAY"
        self.open_close_insulin_night.text = self.close_open[self.night_insulin_state] + " INSULIN NIGHT"
        smart_medical_box_ui.screen_manager.current = "FillInsulin"


############################################################
# Settings Page
############################################################

class Settings(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="Settings", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()


############################################################
# Set Insulin Intervals Page
############################################################

class InsulinIntervalSettingsPage(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.insulin_type = 0 # 0-day 1-night
        self.interval_number = 0

        self.interval_start_h = 0
        self.interval_start_m = 0
        self.interval_end_h = 0
        self.interval_end_m = 0

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.back)
        self.add_widget(self.button_back)

        # Title
        self.title = Label(
            text="SET INSULIN", 
            color=(.25,.25,.25,1),
            font_size="27",
            size_hint=(.56, .1), 
            pos_hint={'x':.44, 'y':.88})
        self.add_widget(self.title)

        # Interval Icon
        self.icon = Image(
            source = "img/png/default.png",
            size_hint=(.2, .2), 
            pos_hint={'x':.22, 'y':.78})
        self.add_widget(self.icon)

        # Start Interval Title
        self.start_title = Label(
            text="START", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.15, 'y':.65})
        self.add_widget(self.start_title)

        # End Interval Title
        self.end_title = Label(
            text="END", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.55, 'y':.65})
        self.add_widget(self.end_title)

        # Start interval hour label
        self.start_interval_hour_label = Label(
            text=to_string(self.interval_start_h), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.15, 'y':.3})
        self.add_widget(self.start_interval_hour_label)

        # Start interval minutes label
        self.start_interval_minutes_label = Label(
            text= to_string(self.interval_end_h), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.35, 'y':.3})
        self.add_widget(self.start_interval_minutes_label)

        # End interval hour label
        self.end_interval_hour_label = Label(
            text= to_string(self.interval_start_m), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.55, 'y':.3})
        self.add_widget(self.end_interval_hour_label)

        # End interval minutes label
        self.end_interval_minutes_label = Label(
            text= to_string(self.interval_end_m), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.75, 'y':.3})
        self.add_widget(self.end_interval_minutes_label)


        # Start interval hour buttons
        self.start_interval_hour_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.12, 'y':.47})
        self.start_interval_hour_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.12, 'y':.18})

        self.start_interval_hour_button_plus.bind(on_press=self.start_interval_add_hour)
        self.start_interval_hour_button_minus.bind(on_press=self.start_interval_subtract_hour)

        self.add_widget(self.start_interval_hour_button_plus)
        self.add_widget(self.start_interval_hour_button_minus)

        # Start interval minutes buttons
        self.start_interval_minutes_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.32, 'y':.47})
        self.start_interval_minutes_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.32, 'y':.18})

        self.start_interval_minutes_button_plus.bind(on_press=self.start_interval_add_minute)
        self.start_interval_minutes_button_minus.bind(on_press=self.start_interval_subtract_minute)

        self.add_widget(self.start_interval_minutes_button_plus)
        self.add_widget(self.start_interval_minutes_button_minus)

        # End interval hour buttons
        self.end_interval_hour_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.52, 'y':.47})
        self.end_interval_hour_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.52, 'y':.18})

        self.end_interval_hour_button_plus.bind(on_press=self.end_interval_add_hour)
        self.end_interval_hour_button_minus.bind(on_press=self.end_interval_subtract_hour)

        self.add_widget(self.end_interval_hour_button_plus)
        self.add_widget(self.end_interval_hour_button_minus)

        # End interval minutes buttons
        self.end_interval_minutes_button_plus = ImageButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.72, 'y':.47})
        self.end_interval_minutes_button_minus = ImageButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.72, 'y':.18})

        self.end_interval_minutes_button_plus.bind(on_press=self.end_interval_add_minute)
        self.end_interval_minutes_button_minus.bind(on_press=self.end_interval_subtract_minute)

        self.add_widget(self.end_interval_minutes_button_plus)
        self.add_widget(self.end_interval_minutes_button_minus)

        # Delete Interval
        self.delete_interval_button = TextButton(
            text="DELETE INTERVAL",
            font_size="20",
            size_hint=(.4, .1), 
            pos_hint={'x':.5, 'y':.75})
        self.delete_interval_button.bind(on_press=self.delete_interval)
        self.add_widget(self.delete_interval_button)


    def start_interval_add_hour(self, instance):
        self.interval_start_h = hours_border(self.interval_start_h + 1)
        self.start_interval_hour_label.text = to_string(self.interval_start_h)
        self.set_insulin_interval()

    def start_interval_subtract_hour(self, instance):
        self.interval_start_h = hours_border(self.interval_start_h - 1)
        self.start_interval_hour_label.text = to_string(self.interval_start_h)
        self.set_insulin_interval()


    def start_interval_add_minute(self, instance):
        self.interval_start_m = minutes_border(self.interval_start_m + 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_m)
        self.set_insulin_interval()

    def start_interval_subtract_minute(self, instance):
        self.interval_start_m = minutes_border(self.interval_start_m - 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_m)
        self.set_insulin_interval()


    def end_interval_add_hour(self, instance):
        self.interval_end_h = hours_border(self.interval_end_h + 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_h)
        self.set_insulin_interval()

    def end_interval_subtract_hour(self, instance):
        self.interval_end_h = hours_border(self.interval_end_h - 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_h)
        self.set_insulin_interval()

    
    def end_interval_add_minute(self, instance):
        self.interval_end_m = minutes_border(self.interval_end_m + 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_m)
        self.set_insulin_interval()

    def end_interval_subtract_minute(self, instance):
        self.interval_end_m = minutes_border(self.interval_end_m - 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_m)
        self.set_insulin_interval()

    def delete_interval(self, instance):
        print(self.interval_number)
        print(self.insulin_type)
        server.deleteInsulinIntervalByNumberAndType(self.interval_number, self.insulin_type)

        if self.insulin_type == 0:
            smart_medical_box_ui.set_insulin_intervals_day.change_page()
        else:
            smart_medical_box_ui.set_insulin_intervals_night.change_page()

    def back(self, instance):
        if self.insulin_type == 0:
            smart_medical_box_ui.set_insulin_intervals_day.change_page()
        else:
            smart_medical_box_ui.set_insulin_intervals_night.change_page()

    def change_page(self, interval_number, insulin_type, icon):
        self.interval_number = interval_number
        self.insulin_type = insulin_type

        insulin_interval = server.getInsulinIntervalByNumberAndType(self.interval_number, self.insulin_type)
        self.interval_start_h = insulin_interval["time_start_h"]
        self.interval_start_m = insulin_interval["time_start_m"]
        self.interval_end_h = insulin_interval["time_end_h"]
        self.interval_end_m = insulin_interval["time_end_m"]

        self.start_interval_hour_label.text = to_string(self.interval_start_h)
        self.start_interval_minutes_label.text = to_string(self.interval_start_m)
        self.end_interval_hour_label.text = to_string(self.interval_end_h)
        self.end_interval_minutes_label.text = to_string(self.interval_end_m)

        self.icon.source = icon
        self.icon.reload()

        smart_medical_box_ui.screen_manager.current = "InsulinIntervalSettingsPage"
    
    def set_insulin_interval(self):
        server.setOrUpdateInsulinInterval(
            self.interval_number, 
            self.insulin_type, 
            self.interval_start_h, 
            self.interval_start_m, 
            self.interval_end_h, 
            self.interval_end_m
        )
        
class InsulinIntervalRow(FloatLayout):
    def __init__(self, size_hint, pos_hint, insulin_type, interval_number, icon, **kwargs):
        super().__init__(**kwargs)
        self.size_hint=size_hint[0], size_hint[1]
        self.pos_hint={'x':pos_hint["x"], 'y':pos_hint["y"]}

        self.insulin_type = insulin_type # 0-day 1-night
        self.interval_number = interval_number

        self.insulin_open_h = 0
        self.insulin_open_m = 0
        self.insulin_close_h = 0
        self.insulin_close_m = 0
        self.is_empty = 1

        self.update_values()

        if self.is_empty:
            self.from_string = "__:__"
            self.to_string = "__:__"
        else:
            self.from_string = to_string(self.insulin_open_h) + ":" + to_string(self.insulin_open_m)
            self.to_string = to_string(self.insulin_close_h) + ":" + to_string(self.insulin_close_m)

        with self.canvas.before:
            self.color = Color(.25,.25,.25,1, mode='rgba')
            self.line = Line(rounded_rectangle=( screen_width * pos_hint["x"], screen_height * pos_hint["y"], screen_width * size_hint[0], screen_height*size_hint[1], 15), width=1.5)

        # Interval Icon
        self.icon = Image(
            source = icon,
            size_hint=(.1, 1), 
            pos_hint={'x':.02, 'y':.0})
        self.add_widget(self.icon)

        self.open_time = Label(
            text="FROM: " + self.from_string, 
            color=(.25,.25,.25,1),
            font_size="27",
            size_hint=(.32, 1), 
            pos_hint={'x':.16, 'y':.0}
        )
        self.add_widget(self.open_time)

        self.close_time = Label(
            text="TO: " + self.to_string, 
            color=(.25,.25,.25,1),
            font_size="27",
            size_hint=(.32, 1), 
            pos_hint={'x':.48, 'y':.0}
        )
        self.add_widget(self.close_time)

        self.change_button = ImageButton(
            image_url='img/png/cog.png', 
            size_hint=(.18, .8), 
            pos_hint={'x':.8, 'y':.1}
        )
        self.change_button.bind(on_press=self.change_values)
        self.add_widget(self.change_button)

    def update_values(self):
        insulin_interval = server.getInsulinIntervalByNumberAndType(self.interval_number, self.insulin_type)
        self.insulin_open_h = insulin_interval["time_start_h"]
        self.insulin_open_m = insulin_interval["time_start_m"]
        self.insulin_close_h = insulin_interval["time_end_h"]
        self.insulin_close_m = insulin_interval["time_end_m"]
        self.is_empty = insulin_interval["is_empty"]

    def update_values_and_change_labels(self):
        self.update_values()

        if self.is_empty:
            self.from_string = "__:__"
            self.to_string = "__:__"
        else:
            self.from_string = to_string(self.insulin_open_h) + ":" + to_string(self.insulin_open_m)
            self.to_string = to_string(self.insulin_close_h) + ":" + to_string(self.insulin_close_m)

        self.open_time.text = "FROM: " + self.from_string
        self.close_time.text = "TO: " + self.to_string

    def change_values(self, instance):
        smart_medical_box_ui.insulin_interval_settings.change_page(self.interval_number, self.insulin_type, self.icon.source)
        

class SetInsulinIntervalsDay(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.15, .15), pos_hint={'x':.02, 'y':.83})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="DAY INSULIN", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .15), 
            pos_hint={'x':.17, 'y':.85})
        self.add_widget(self.page_title_label)

        self.rowa = InsulinIntervalRow(size_hint=(0.9, .15), pos_hint={'x':.05, 'y':.6}, interval_number=0, insulin_type=0, icon="img/png/sunrise.png")
        self.rowb = InsulinIntervalRow(size_hint=(0.9, .15), pos_hint={'x':.05, 'y':.4}, interval_number=1, insulin_type=0, icon="img/png/sun.png")
        self.rowc = InsulinIntervalRow(size_hint=(0.9, .15), pos_hint={'x':.05, 'y':.2}, interval_number=2, insulin_type=0, icon="img/png/moon_rotated.png")

        self.add_widget(self.rowa)
        self.add_widget(self.rowb)
        self.add_widget(self.rowc)

        self.night = ImageRightButtonText(text="NIGHT", image_url="img/png/long_arrow_alt_right.png", size_hint=(.4, .12), pos_hint={'x':0.58, 'y':0.02})
        self.night.bind(on_press=self.set_night)
        self.add_widget(self.night)

    def set_night(self, instance):
        print("Next Page")
        smart_medical_box_ui.set_insulin_intervals_night.change_page()

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.rowa.update_values_and_change_labels()
        self.rowb.update_values_and_change_labels()
        self.rowc.update_values_and_change_labels()
        smart_medical_box_ui.screen_manager.current = "SetInsulinIntervalsDay"

class SetInsulinIntervalsNight(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = ImageButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.15, .15), pos_hint={'x':.02, 'y':.83})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="NIGHT INSULIN", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .15), 
            pos_hint={'x':.17, 'y':.85})
        self.add_widget(self.page_title_label)

        self.rowa = InsulinIntervalRow(size_hint=(0.9, .15), pos_hint={'x':.05, 'y':.5}, interval_number=0, insulin_type=1, icon="img/png/bed_stars.png")

        self.add_widget(self.rowa)

        self.day = ImageLeftButtonText(text="DAY", image_url="img/png/long_arrow_alt_left.png", size_hint=(.4, .12), pos_hint={'x':0.02, 'y':0.02})
        self.day.bind(on_press=self.set_day)        
        self.add_widget(self.day)

    def set_day(self, instance):
        print("Next Page")
        smart_medical_box_ui.set_insulin_intervals_day.change_page()

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.main_menu_page.change_page()

    def change_page(self):
        self.rowa.update_values_and_change_labels()
        smart_medical_box_ui.screen_manager.current = "SetInsulinIntervalsNight"


############################################################
# Smart Medical Box App
############################################################

class SmartMedicalBoxUi(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.clock_page = ClockPage()
        screen = Screen(name="Clock")
        screen.add_widget(self.clock_page)
        self.screen_manager.add_widget(screen)

        self.main_menu_page = MainMenuPage()
        screen = Screen(name="MainMenu")
        screen.add_widget(self.main_menu_page)
        self.screen_manager.add_widget(screen)

        self.set_clock_time = SetClockTime()
        screen = Screen(name="SetClockTime")
        screen.add_widget(self.set_clock_time)
        self.screen_manager.add_widget(screen)

        self.set_clock_date = SetClockDate()
        screen = Screen(name="SetClockDate")
        screen.add_widget(self.set_clock_date)
        self.screen_manager.add_widget(screen)

        self.set_clock_weekday_year = SetClockWeekdayYear()
        screen = Screen(name="SetClockWeekdayYear")
        screen.add_widget(self.set_clock_weekday_year)
        self.screen_manager.add_widget(screen)

        self.set_intervals = SetIntervals()
        screen = Screen(name="SetIntervals")
        screen.add_widget(self.set_intervals)
        self.screen_manager.add_widget(screen)

        self.fill_box = FillBox()
        screen = Screen(name="FillBox")
        screen.add_widget(self.fill_box)
        self.screen_manager.add_widget(screen)

        self.fill_insulin = FillInsulin()
        screen = Screen(name="FillInsulin")
        screen.add_widget(self.fill_insulin)
        self.screen_manager.add_widget(screen)

        self.set_insulin_intervals_day = SetInsulinIntervalsDay()
        screen = Screen(name="SetInsulinIntervalsDay")
        screen.add_widget(self.set_insulin_intervals_day)
        self.screen_manager.add_widget(screen)

        self.set_insulin_intervals_night = SetInsulinIntervalsNight()
        screen = Screen(name="SetInsulinIntervalsNight")
        screen.add_widget(self.set_insulin_intervals_night)
        self.screen_manager.add_widget(screen)

        self.insulin_interval_settings = InsulinIntervalSettingsPage()
        screen = Screen(name="InsulinIntervalSettingsPage")
        screen.add_widget(self.insulin_interval_settings)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    server = ServerCommunication()
    smart_medical_box_ui = SmartMedicalBoxUi()
    smart_medical_box_ui.run()
        
