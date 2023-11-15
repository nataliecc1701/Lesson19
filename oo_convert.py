'''uses python's object-oriented functions convert
between arbitrary temperature scales'''

class Temperature_Scale:
    '''Defines a temperature scale by the boiling and freezing points of water'''
    def __init__(self, freezing_point, boiling_point, name):
        self.freezing_point = freezing_point
        self.boiling_point = boiling_point
        self.name = name
        
    def __repr__(self):
        return f"<{self.name} Temperature Scale: water freezes at {self.freezing_point} and boils at {self.boiling_point}>"
        
    def get_conversion(self, other_scale):
        '''returns a 2-tuple with the conversion factors from self to the other scale
        of form other_scale_temperature = return[0] * this_scale_temperature + return[1]'''
        ratio = ((other_scale.boiling_point - other_scale.freezing_point)
                 /(self.boiling_point - self.freezing_point))
        offset = other_scale.freezing_point - (self.freezing_point * ratio)
        return (ratio, offset)

# this is the general data structure that holds all of our temperature scales
temperature_scales = {
    "c" : Temperature_Scale(0, 100, "Celsius"),
    "f" : Temperature_Scale(32, 212, "Fahrenheit"),
    "d" : Temperature_Scale(150, 0, "Delisle"),
    "k" : Temperature_Scale(273.15, 373.15, "Kelvin"),
    "n" : Temperature_Scale(0, 33, "Newton"),
}

def convert_temp(from_scale, to_scale, temp):
    '''uses our handy data structures to convert a temperature from from_scale to to_scale'''
    
    # check to see that we have our scales
    if not temperature_scales[from_scale]:
        return f"unrecognized scale {from_scale}"
    if not temperature_scales[to_scale]:
        return f"unrecognized scale {to_scale}"
    
    # and then let the magic happen
    factors = temperature_scales[from_scale].get_conversion(temperature_scales[to_scale])
    return temp * factors[0] + factors[1]

def add_scale(freezing_point, boiling_point, name, initial = None, overwrite = False):
    if initial == None:
        initial = name[0].lower()
    
    if initial in temperature_scales and not overwrite:
        print(f"scale not added, initial {initial} already in use")
        print(f"add again with overwrite=True to replace existing scale {temperature_scales[initial].name}")
    
    temperature_scales[initial] = Temperature_Scale(freezing_point, boiling_point, name)
    print(f"scale added successfully with initial {initial}")
    
# main loop
while True:
    print('enter command ("quit" to end, "help" for more info)')
    cmd = input().split()
    if cmd[0] == "quit":
        break
    if cmd[0] == "help":
        if cmd[1] == "quit":
            print("the 'quit' command ends the program and returns you to the console")
        elif cmd[1] == "convert":
            print('''convert [from_scale], [to_scale], temp
                  from_scale and to_scale should be provided as initials
                  Converts the provided temperature from from_scale to to_scale''')
        elif cmd[1] == "add":
            print('''add [freezing_point], [boiling_point], [name], [initial]
                  initial is optional; defaults to lowercase first character of name
                  adds a temperature scale to be available for conversions with the specified parameters
                  if the chosen initial is already in use, warns and does not add unless followed with
                  overwrite=True''')
        else:
            print('available commands: quit, convert, add. type "help [command]" for syntax')
    elif cmd[0] == "convert":
        print (f"{cmd[3]} degrees {temperature_scales[cmd[1]].name} is " +
               f"{round(convert_temp(cmd[1], cmd[2], float(cmd[3])), 2)} degrees " 
               + f"{temperature_scales[cmd[2]].name}")
    elif cmd[0] == "add":
        while len(cmd) < 6:
            cmd.append(None) # ugly kludge to avoid some errors
        if cmd[5] == "overwrite=True":
            add_scale(float(cmd[1]), float(cmd[2]), cmd[3], cmd[4], True)
        else:
            add_scale(float(cmd[1]), float(cmd[2]), cmd[3], cmd[4])
        
    