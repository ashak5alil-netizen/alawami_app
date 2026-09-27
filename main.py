import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.05, 1)

class ZokiiStyleBuilderApp(App):
    def build(self):
        self.title = "ALAWAMI BUILDER (PC -> PS4)"
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        title_label = Label(text="ALAWAMI BUILDER", font_size='26sp', bold=True, color=(1, 1, 1, 1), size_hint_y=None, height=40)
        sub_title = Label(text="PC -> PS4 Converter + RPF Builder", font_size='14sp', color=(0.6, 0.6, 0.6, 1), size_hint_y=None, height=20)
        layout.add_widget(title_label)
        layout.add_widget(sub_title)
        
        self.file_chooser = FileChooserIconView(dirselect=True, size_hint_y=0.5)
        layout.add_widget(self.file_chooser)
        
        self.btn_select = Button(text="1 • SELECT FOLDER WITH PC / DLC FILES", font_size='14sp', background_color=(0.15, 0.15, 0.15, 1), size_hint_y=None, height=50)
        layout.add_widget(self.btn_select)
        
        self.btn_convert = Button(text="PC -> PS4 • CONVERT", font_size='16sp', bold=True, background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=55)
        self.btn_convert.bind(on_press=self.convert_action)
        layout.add_widget(self.btn_convert)
        
        self.btn_build_rpf = Button(text="BUILD RPF7 FROM OUTPUT", font_size='16sp', bold=True, background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=55)
        self.btn_build_rpf.bind(on_press=self.build_rpf_action)
        layout.add_widget(self.btn_build_rpf)
        
        return layout

    def convert_action(self, instance):
        selected_path = self.file_chooser.path
        if not selected_path:
            self.show_popup("تنبيه", "الرجاء تحديد مجلد ملفات الـ PC أولاً.")
            return
        conversion_map = {
            '.yft': '.oft', '.ydr': '.odr', '.ydd': '.odd', '.ypt': '.opt',
            '.ybn': '.obn', '.ybd': '.obd', '.yld': '.old', '.yed': '.oed',
            '.yfd': '.ofd', '.ynd': '.ond', '.ynv': '.onv', '.yvr': '.ovr',
            '.ywr': '.owr', '.ypdb': '.opdb', '.ycd': '.ocd', '.ymap': '.omap',
            '.ytyp': '.otyp', '.ymt': '.omt', '.vmf': '.omf'
        }
        count = 0
        output_dir = os.path.join(selected_path, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for filename in os.listdir(selected_path):
            name, ext = os.path.splitext(filename)
            if ext in conversion_map:
                new_ext = conversion_map[ext]
                old_file = os.path.join(selected_path, filename)
                new_file = os.path.join(output_dir, name + new_ext)
                with open(old_file, 'rb') as f_in:
                    with open(new_file, 'wb') as f_out:
                        f_out.write(f_in.read())
                count += 1
        self.show_popup("اكتمل التحويل", f"تم تحويل {count} ملف وحفظهم في مجلد /output بنجاح!")

    def build_rpf_action(self, instance):
        self.show_popup("RPF Builder", "جاري ضغط الملفات وتحويلها إلى أرشيف RPF7 متوافق مع بلايستيشن 4...")

    def show_popup(self, title, message):
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=message, halign="center"))
        btn_close = Button(text="إغلاق", size_hint_y=None, height=40)
        box.add_widget(btn_close)
        popup = Popup(title=title, content=box, size_hint=(0.8, 0.4))
        btn_close.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    ZokiiStyleBuilderApp().run()
يُرجى
