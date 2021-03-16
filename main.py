import kivy

from kivy.config import Config 
Config.set("graphics", "width", "480")
Config.set("graphics", "height", "320")
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivy.core.window import Window
#Window.show_cursor = False
Window.softinput_mode = "below_target"

from kivy.uix.label import Label 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics.svg import Svg
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from datetime import datetime
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard 

class ImageAnchorLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self._update_img, pos=self._update_img)

        with self.canvas.before:
            self.image = Image(source="img/background.jpg", 
                size=self.size, pos=self.pos, allow_stretch=True, keep_ratio=False)
    
    def _update_img(self, instance, value):
        self.image.pos = instance.pos
        self.image.size = instance.size
    
    def change_image(self, source):
        self.image.source = source

class ImageGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self._update_img, pos=self._update_img)

        with self.canvas.before:
            self.image = Image(source="img/background.jpg", 
                size=self.size, pos=self.pos, allow_stretch=True, keep_ratio=False)
    
    def _update_img(self, instance, value):
        self.image.pos = instance.pos
        self.image.size = instance.size
    
    def change_image(self, source):
        self.image.source = source

class ImageFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self._update_img, pos=self._update_img)

        with self.canvas.before:
            self.image = Image(source="img/background.jpg", 
                size=self.size, pos=self.pos, allow_stretch=True, keep_ratio=False)
    
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

Builder.load_string(''' 
<CustomButton>:
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

<IconButton>:
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

    font_size: 0.1*self.width
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

class CustomButton(Button):
    def __init__(self, text, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.ids.btn_image.source = image_url

class IconButton(Button):
    def __init__(self, image_url="img/png/default.png", **kwargs):
        super().__init__(**kwargs)
        self.ids.btn_image.source = image_url

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

class ImageButton(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


############################################################
# Clock page
############################################################

class ClockPage(ImageAnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.anchor_x = "center"
        self.anchor_y = "center"

        self.change_image("img/background2.jpg")

        self.on_touch_down = self.clicked

        self.label = Label(text="17:26", font_size=60, color=(0,0,0,1))
        self.add_widget(self.label)

        self.update_clock_interval = Clock.schedule_interval(self._update_clock, 30)

    def _update_clock(self, *args):
        now = datetime.now()
        self.label.text = now.strftime("%H:%M")

    def clicked(self, instance):
        smart_medical_box_ui.screen_manager.current = "MainMenu"


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

        self.back = CustomButton(text="BACK", image_url="img/png/long_arrow_alt_left.png")
        self.fill_box = CustomButton(text="FILL BOX", image_url="img/png/pills.png")
        self.fill_insulin = CustomButton(text="FILL INSULIN", image_url="img/png/pills.png")
        self.set_clock = CustomButton(text="CLOCK", image_url="img/png/clock.png")
        self.set_intervals = CustomButton(text="INTERVALS", image_url="img/png/user_md.png")
        self.settings = CustomButton(text="SETTINGS", image_url="img/png/cog.png")

        self.back.bind(on_press=self.function_back)
        self.fill_box.bind(on_press=self.function_fill_box)
        self.fill_insulin.bind(on_press=self.function_fill_insulin)
        self.set_clock.bind(on_press=self.function_set_clock)
        self.set_intervals.bind(on_press=self.function_set_intervals)
        self.settings.bind(on_press=self.function_settings)

        self.add_widget(self.back)
        self.add_widget(self.fill_box)
        self.add_widget(self.fill_insulin)
        self.add_widget(self.set_clock)
        self.add_widget(self.set_intervals)
        self.add_widget(self.settings)

    def function_back(self, instance):
        smart_medical_box_ui.screen_manager.current = "Clock"

    def function_fill_box(self, instance):
        smart_medical_box_ui.screen_manager.current = "FillBox"

    def function_fill_insulin(self, instance):
        smart_medical_box_ui.screen_manager.current = "FillInsulin"

    def function_set_clock(self, instance):
        smart_medical_box_ui.screen_manager.current = "SetClockTime"

    def function_set_intervals(self, instance):
        smart_medical_box_ui.screen_manager.current = "SetIntervals"

    def function_settings(self, instance):
        smart_medical_box_ui.screen_manager.current = "Settings"

    def log(self, instance):
        print("-------------------")
        print("Clicked")
        print(instance)
        print("-------------------")


############################################################
# Clock Settings Pages
############################################################

class SetClockTime(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.hours = 15
        self.minutes = 47

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Selection Buttons
        self.button_right = ImageRightButtonText(text="NEXT", image_url="img/png/long_arrow_alt_right.png", size_hint=(.4, .12), pos_hint={'x':0.58, 'y':0.02})
        self.button_right.bind(on_press=self.set_clock_date_page)
        self.add_widget(self.button_right)

        # Hour Buttons
        self.plus_hour = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_hour = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_hour.bind(on_press=self.add_one_hour)
        self.minus_hour.bind(on_press=self.subtract_one_hour)
        self.add_widget(self.plus_hour)
        self.add_widget(self.minus_hour)

        # Minute Buttons
        self.plus_minute = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.minus_minute = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
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
            text="Clock Setup", 
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

    def subtract_one_hour(self, instance):
        self.hours = hours_border(self.hours - 1)
        self.hours_label.text = to_string(self.hours)

    def add_one_minute(self, instance):
        self.minutes = minutes_border(self.minutes + 1)
        self.minutes_label.text = to_string(self.minutes)

    def subtract_one_minute(self, instance):
        self.minutes = minutes_border(self.minutes - 1)
        self.minutes_label.text = to_string(self.minutes)

    def set_clock_date_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "SetClockDate"

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"


class SetClockDate(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.month_names = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

        self.day = 1
        self.month_number = 0

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
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
        self.plus_day = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_day = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_day.bind(on_press=self.add_one_day)
        self.minus_day.bind(on_press=self.subtract_one_day)
        self.add_widget(self.plus_day)
        self.add_widget(self.minus_day)

        # Month Buttons
        self.next_month = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.previous_month = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
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
            text="Clock Setup", 
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

    def subtract_one_day(self, instance):
        self.day = self.day - 1
        self.day_label.text = to_string(self.day)

    def add_one_month(self, instance):
        self.month_number = month_number_border(self.month_number + 1)
        self.month_label.text = self.month_names[self.month_number]

    def subtract_one_month(self, instance):
        self.month_number = month_number_border(self.month_number - 1)
        self.month_label.text = self.month_names[self.month_number]

    def set_clock_time_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "SetClockTime"

    def set_clock_weekday_year_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "SetClockWeekdayYear"
    
    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"

class SetClockWeekdayYear(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.day_names = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]

        self.day_of_week_number = 0
        self.year = 2021

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Selection Buttons
        self.button_left = ImageLeftButtonText(text="PREVIOUS", image_url="img/png/long_arrow_alt_left.png", size_hint=(.4, .12), pos_hint={'x':0.02, 'y':0.02})
        self.button_left.bind(on_press=self.set_clock_date_page)
        self.add_widget(self.button_left)

        # Day Buttons
        self.plus_day_of_week = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.55})
        self.minus_day_of_week = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.25, 'y':.25})
        self.plus_day_of_week.bind(on_press=self.add_one_day_of_week)
        self.minus_day_of_week.bind(on_press=self.subtract_one_day_of_week)
        self.add_widget(self.plus_day_of_week)
        self.add_widget(self.minus_day_of_week)

        # Year Buttons
        self.plus_year = IconButton(image_url="img/png/arrow_up.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.55})
        self.minus_year = IconButton(image_url="img/png/arrow_down.png", size_hint=(.2, .15), pos_hint={'x':.55, 'y':.25})
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
            text="Clock Setup", 
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

    def subtract_one_day_of_week(self, instance):
        self.day_of_week_number = day_of_week_border(self.day_of_week_number - 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]

    def add_one_year(self, instance):
        self.year = year_border(self.year + 1)
        self.year_label.text = str(self.year)

    def subtract_one_year(self, instance):
        self.year = year_border(self.year - 1)
        self.year_label.text = str(self.year)

    def set_clock_date_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "SetClockDate"
    
    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"


############################################################
# Set Intervals Page
############################################################

class SetIntervals(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.interval_names = ["Morning", "Midday", "Evening", "Night"]
        self.current_interval = 0

        self.inactive_active = ["Inactive", "Active"]
        self.use_interval       = [0, 0, 0, 0]
        self.interval_start_hh  = [0, 0, 0, 0]
        self.interval_start_mm  = [0, 0, 0, 0]
        self.interval_end_hh    = [0, 0, 0, 0]
        self.interval_end_mm    = [0, 0, 0, 0]

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Title
        self.title = Label(
            text=self.interval_names[self.current_interval] + " interval", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .1), 
            pos_hint={'x':.22, 'y':.88})
        self.add_widget(self.title)

        # Start Interval Title
        self.start_title = Label(
            text="START", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.1, 'y':.65})
        self.add_widget(self.start_title)

        # End Interval Title
        self.end_title = Label(
            text="END", 
            color=(.25,.25,.25,1),
            font_size="20",
            size_hint=(.3, .1), 
            pos_hint={'x':.5, 'y':.65})
        self.add_widget(self.end_title)

        # Start interval hour label
        self.start_interval_hour_label = Label(
            text=to_string(self.interval_start_hh[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.1, 'y':.3})
        self.add_widget(self.start_interval_hour_label)

        # Start interval minutes label
        self.start_interval_minutes_label = Label(
            text= to_string(self.interval_start_mm[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.3, 'y':.3})
        self.add_widget(self.start_interval_minutes_label)

        # End interval hour label
        self.end_interval_hour_label = Label(
            text= to_string(self.interval_end_hh[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.5, 'y':.3})
        self.add_widget(self.end_interval_hour_label)

        # End interval minutes label
        self.end_interval_minutes_label = Label(
            text= to_string(self.interval_end_mm[self.current_interval]), 
            color=(.25,.25,.25,1),
            font_size="30",
            size_hint=(.1, .2), 
            pos_hint={'x':.7, 'y':.3})
        self.add_widget(self.end_interval_minutes_label)

        # Start interval hour buttons
        self.start_interval_hour_button_plus = IconButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.07, 'y':.47})
        self.start_interval_hour_button_minus = IconButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.07, 'y':.18})

        self.start_interval_hour_button_plus.bind(on_press=self.start_interval_add_hour)
        self.start_interval_hour_button_minus.bind(on_press=self.start_interval_subtract_hour)

        self.add_widget(self.start_interval_hour_button_plus)
        self.add_widget(self.start_interval_hour_button_minus)

        # Start interval minutes buttons
        self.start_interval_minutes_button_plus = IconButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.27, 'y':.47})
        self.start_interval_minutes_button_minus = IconButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.27, 'y':.18})

        self.start_interval_minutes_button_plus.bind(on_press=self.start_interval_add_minute)
        self.start_interval_minutes_button_minus.bind(on_press=self.start_interval_subtract_minute)

        self.add_widget(self.start_interval_minutes_button_plus)
        self.add_widget(self.start_interval_minutes_button_minus)

        # End interval hour buttons
        self.end_interval_hour_button_plus = IconButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.47, 'y':.47})
        self.end_interval_hour_button_minus = IconButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.47, 'y':.18})

        self.end_interval_hour_button_plus.bind(on_press=self.end_interval_add_hour)
        self.end_interval_hour_button_minus.bind(on_press=self.end_interval_subtract_hour)

        self.add_widget(self.end_interval_hour_button_plus)
        self.add_widget(self.end_interval_hour_button_minus)

        # End interval minutes buttons
        self.end_interval_minutes_button_plus = IconButton(image_url="img/png/arrow_up.png", size_hint=(.16, .15), pos_hint={'x':.67, 'y':.47})
        self.end_interval_minutes_button_minus = IconButton(image_url="img/png/arrow_down.png", size_hint=(.16, .15), pos_hint={'x':.67, 'y':.18})

        self.end_interval_minutes_button_plus.bind(on_press=self.end_interval_add_minute)
        self.end_interval_minutes_button_minus.bind(on_press=self.end_interval_subtract_minute)

        self.add_widget(self.end_interval_minutes_button_plus)
        self.add_widget(self.end_interval_minutes_button_minus)

        # Active / Inactive interval
        self.active_inactive_button = TextButton(text=self.inactive_active[self.use_interval[self.current_interval]], size_hint=(.4, .1), pos_hint={'x':.4, 'y':.75})
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

    def start_interval_subtract_hour(self, instance):
        self.interval_start_hh[self.current_interval] = hours_border(self.interval_start_hh[self.current_interval] - 1)
        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])


    def start_interval_add_minute(self, instance):
        self.interval_start_mm[self.current_interval] = minutes_border(self.interval_start_mm[self.current_interval] + 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])

    def start_interval_subtract_minute(self, instance):
        self.interval_start_mm[self.current_interval] = minutes_border(self.interval_start_mm[self.current_interval] - 1)
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])


    def end_interval_add_hour(self, instance):
        self.interval_end_hh[self.current_interval] = hours_border(self.interval_end_hh[self.current_interval] + 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])

    def end_interval_subtract_hour(self, instance):
        self.interval_end_hh[self.current_interval] = hours_border(self.interval_end_hh[self.current_interval] - 1)
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])

    
    def end_interval_add_minute(self, instance):
        self.interval_end_mm[self.current_interval] = minutes_border(self.interval_end_mm[self.current_interval] + 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])

    def end_interval_subtract_minute(self, instance):
        self.interval_end_mm[self.current_interval] = minutes_border(self.interval_end_mm[self.current_interval] - 1)
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])

    
    def change_interval_state(self, instance):
        if self.use_interval[self.current_interval] == 1:
            self.use_interval[self.current_interval] = 0
        else:
            self.use_interval[self.current_interval] = 1
        
        self.active_inactive_button.text = self.inactive_active[self.use_interval[self.current_interval]]


    def next_interval(self, instance):
        self.current_interval = self.current_interval + 1
        if self.current_interval > 3:
            self.current_interval = 0

        self.title.text = self.interval_names[self.current_interval] + " interval"
        self.active_inactive_button.text = self.inactive_active[self.use_interval[self.current_interval]]

        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])

    def previous_interval(self, instance):
        self.current_interval = self.current_interval - 1
        if self.current_interval < 0:
            self.current_interval = 3

        self.title.text = self.interval_names[self.current_interval] + " interval"
        self.active_inactive_button.text = self.inactive_active[self.use_interval[self.current_interval]]

        self.start_interval_hour_label.text = to_string(self.interval_start_hh[self.current_interval])
        self.start_interval_minutes_label.text = to_string(self.interval_start_mm[self.current_interval])
        self.end_interval_hour_label.text = to_string(self.interval_end_hh[self.current_interval])
        self.end_interval_minutes_label.text = to_string(self.interval_end_mm[self.current_interval])

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"


############################################################
# Filll Box Page
############################################################

class FillBox(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.day_names = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]
        self.day_of_week_number = 0

        self.interval_names = ["Morning", "Midday", "Evening", "Night"]
        self.current_interval = 0

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="Fill Box", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Day Of Week Label
        self.day_of_week_label = Label(
            text=self.day_names[self.day_of_week_number], 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.4, .15), 
            pos_hint={'x':.3, 'y':.37})
        self.add_widget(self.day_of_week_label)

        # Time Interval Label
        self.time_interval_label = Label(
            text=self.interval_names[self.current_interval], 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.4, .15), 
            pos_hint={'x':.3, 'y':.22})
        self.add_widget(self.time_interval_label)

        # Control Buttons
        self.button_up = IconButton(image_url="img/png/arrow_up.png", size_hint=(.4, .2), pos_hint={'x':.3, 'y':.52})
        self.button_down = IconButton(image_url="img/png/arrow_down.png", size_hint=(.4, .2), pos_hint={'x':.3, 'y':.02})
        self.button_left = IconButton(image_url="img/png/arrow_left.png", size_hint=(.15, .3), pos_hint={'x':.15, 'y':.22})
        self.button_right = IconButton(image_url="img/png/arrow_right.png", size_hint=(.15, .3), pos_hint={'x':.7, 'y':.22})

        self.button_up.bind(on_press=self.next_interval)
        self.button_down.bind(on_press=self.previous_interval)
        self.button_left.bind(on_press=self.subtract_one_day_of_week)
        self.button_right.bind(on_press=self.add_one_day_of_week)

        self.add_widget(self.button_up)
        self.add_widget(self.button_down)
        self.add_widget(self.button_left)
        self.add_widget(self.button_right)

    def add_one_day_of_week(self, instance):
        self.day_of_week_number = day_of_week_border(self.day_of_week_number + 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]

    def subtract_one_day_of_week(self, instance):
        self.day_of_week_number = day_of_week_border(self.day_of_week_number - 1)
        self.day_of_week_label.text = self.day_names[self.day_of_week_number]

    def next_interval(self, instance):
        self.current_interval = self.current_interval + 1
        if self.current_interval > 3:
            self.current_interval = 0

        self.time_interval_label.text = self.interval_names[self.current_interval]
        
    def previous_interval(self, instance):
        self.current_interval = self.current_interval - 1
        if self.current_interval < 0:
            self.current_interval = 3

        self.time_interval_label.text = self.interval_names[self.current_interval]

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"


############################################################
# Filll Box Page
############################################################

class FillInsulin(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        self.day_insulin_state = 1
        self.night_insulin_state = 1
        self.close_open = ["Close", "Open"]

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
        self.button_back.bind(on_press=self.main_menu_page)
        self.add_widget(self.button_back)

        # Page Title
        self.page_title_label = Label(
            text="Fill Insulin", 
            color=(.25,.25,.25,1),
            font_size="35",
            size_hint=(.8, .23), 
            pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.page_title_label)

        # Open / Close insulin day
        self.open_close_insulin_day = TextButton(text=self.close_open[self.day_insulin_state] + " Insulin Day", size_hint=(.96, .3), pos_hint={'x':.02, 'y':.37})
        self.open_close_insulin_day.bind(on_press=self.invert_insulin_day_state)
        self.add_widget(self.open_close_insulin_day)

        # Open / Close insulin night
        self.open_close_insulin_night = TextButton(text=self.close_open[self.night_insulin_state] + " Insulin Night", size_hint=(.96, .3), pos_hint={'x':.02, 'y':.02})
        self.open_close_insulin_night.bind(on_press=self.invert_insulin_night_state)
        self.add_widget(self.open_close_insulin_night)

    def invert_insulin_day_state(self, instance):
        if self.day_insulin_state == 1:
            self.day_insulin_state = 0
        else:
            self.day_insulin_state = 1 

        self.open_close_insulin_day.text = self.close_open[self.day_insulin_state] + " Insulin Day"

    def invert_insulin_night_state(self, instance):
        if self.night_insulin_state == 1:
            self.night_insulin_state = 0
        else:
            self.night_insulin_state = 1 

        self.open_close_insulin_night.text = self.close_open[self.night_insulin_state] + " Insulin Night"

    def main_menu_page(self, instance):
        print("Next Page")
        smart_medical_box_ui.screen_manager.current = "MainMenu"


############################################################
# Settings Page
############################################################

class Settings(ImageFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.change_image("img/background2.jpg")

        # Button Back
        self.button_back = IconButton(image_url="img/png/long_arrow_alt_left.png", size_hint=(.2, .23), pos_hint={'x':.02, 'y':.75})
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
        smart_medical_box_ui.screen_manager.current = "MainMenu"


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

        self.settings = Settings()
        screen = Screen(name="Settings")
        screen.add_widget(self.settings)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    smart_medical_box_ui = SmartMedicalBoxUi()
    smart_medical_box_ui.run()
        
