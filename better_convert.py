UNITS_LIST = "cdfk"

TEMP_TABLE = {
    "cf" : {"ratio" : 9/5, "offset" : 32},
    "ck" : {"ratio" : 1, "offset" : 273.15},
    "cd" : {"ratio" : -3/2, "offset" : 150},

    "dc" : {"ratio" : -2/3, "offset" : 100},
    "df" : {"ratio" : -6/5, "offset" : 212},
    "dk" : {"ratio" : -2/3, "offset" : 373.15},

    "fc" : {"ratio" : 5/9, "offset" : -160/9},
    "fk" : {"ratio" : 5/9, "offset" : 459.67},
    "fd" : {"ratio" : -5/6, "offset" : -530/3},

    "kc" : {"ratio" : 1, "offset" : -273.15},
    "kf" : {"ratio": 9/5, "offset" : -459.67},
    "kd" : {"ratio" : -3/2, "offset" : 559.725},
}

def convert_temp(unit_in, unit_out, temp):
    """converts temperatures from unit_in to unit_out.
    covers temperature scales defined in TEMP_TABLE
    
    should help you with the puzzle in chapter 6 of Exit/Corners"""

    ratio = TEMP_TABLE["unit_in" + "unit_out"]["ratio"]
    offset = TEMP_TABLE["unit_in" + "unit_out"]["offset"]

    if ratio and offset:
        return temp * ratio + offset
    else:
        unrecognized = []
        unrec_string = ""
        if unit_in not in UNITS_LIST:
            unrecognized.push(unit_in)
        if unit_out not in UNITS_LIST:
            unrecognized.push(unit_out)
        
        if unrecognized:
            if len(unrecognized) == 1:
                unrec_string = f"Unknown unit {unrecognized[0]}"
            else:
                unrec_string = f"Unknown units {unrecognized[0], unrecognized[1]}"
            return unrec_string
        else: return f"cannot convert {unit_in} to {unit_out}"
