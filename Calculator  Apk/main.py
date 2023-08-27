import kivy
from kivy.app  import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)
# from kivy.uix.floatlayout import FloatLayout
Builder.load_file('Main.kv')

class MyLayout (Widget):
    def clear(self):
        self.ids.calc_input.text='0'

    def button_press(self,button):
        k = self.ids.calc_input.text

        if "Error" in k:
            k = ''

        #Let If Zero Will be there
        if k == "0":
            self.ids.calc_input.text =""
            self.ids.calc_input.text =f'{button}'

        else:
            self.ids.calc_input.text = f'{k}{button}'
    #Create a Addition Function
    def add(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text
        #slap a text sign to text box
        self.ids.calc_input.text=f'{k}+'
    def substract(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text
        #slap a text sign to text box
        self.ids.calc_input.text=f'{k}-'
    def multipication(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text
        #slap a text sign to text box
        self.ids.calc_input.text=f'{k}*'
    def division(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text
        #slap a text sign to text box
        self.ids.calc_input.text=f'{k}/'
    def modulous(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text
        #slap a text sign to text box
        self.ids.calc_input.text=f'{k}%'
        # self.ids.calc_input.text=str((k),(/))
#Create  function to make text box postive or negative
    def pn(self):
        k=self.ids.calc_input.text 
        if "-" in k:
            self.ids.calc_input.text = f'{k.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{k}'


    #create a decimal function
    def dot(self):
        k = self.ids.calc_input.text
        #Add a decimaal to the end of the text
        num_list=k.split('+')

        if "+" in k and "." not in num_list[-1]:
            k=f'{k}.'
            self.ids.calc_input.text = k
        
        elif '.' in k:
            pass
        else:
            k= f'{k}.'
            self.ids.calc_input.text = k
    def remove(self):
        k = self.ids.calc_input.text
        k= k[:-1]
        self.ids.calc_input.text = k
    
    def equal(self):
        #Create a variable that contains whatever 
        k = self.ids.calc_input.text

        try:
            ans = eval(k)
            self.ids.calc_input.text = str(ans)
        except:
            self.ids.calc_input.text = "Error"
        # ans = eval(k)
        # self.ids.calc_input.text = str(ans)
        # #Addition 
        # if '+' in k:
        #     num_list=k.split('+')
        # # print(num_list)
        #     ans=0
        #     for num in num_list:
        #         ans = ans + float(num)
        #     # print(ans)
        #     self.ids.calc_input.text = f'{ans}'

        # elif '-' in k:

        #     num_list=k.split('-')
        #     # ans=0
        #     # for num in num_list:
        #     #     d =  ans  
        #     #     an =   int(num) 
        #     #     ans =  d - an
        #     # ans = int(num_list[0])  # Initialize ans with the first number in the list
        #     # for num in num_list[1:]:
        #     #   ans -= int(num)
        #     ans = eval(k.replace('-', '-')) 
        #     # print(ans)
        #     self.ids.calc_input.text = f'{ans}'

        # elif 'x' in k:
        #     num_list=k.split('x')
        #     ans=1
        #     for num in num_list:
        #         ans=ans * int(num)
        #     self.ids.calc_input.text = f'{ans}'

        # elif '/' in k:
        #     num_list:k.split('/')
        #     # ans = int(num_list[0])  # Initialize ans with the first number in the list
        #     # for num in num_list[1:]:
        #     #   ans /= int(num)
        #     ans = eval(k.replace('/', '/')) 

        #     self.ids.calc_input.text = f'{ans}'





    
class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ =='__main__':
    CalculatorApp().run()