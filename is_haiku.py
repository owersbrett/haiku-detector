import sys, cmudict

def beginning():
    exception_string = ""
    args = sys.argv
    arg = args[1]
    string = str(arg).lower()
    lines = string.split(" , ")
    if (len(lines) > 3):
        raise Exception("Haiku Line Length Exceeds 3")
    if (len(lines) < 3):
        raise Exception("Haiku Line Length Falls Short of 3")
    line_index = 0
    for line in lines:
        line_index += 1
        words = line.split(" ")
        
        line_syllables = 0
        for word in words:
            line_syllables += get_syllable_count(word.strip())
            
        if (line_index == 1 and line_syllables > 5):
            exception_string += "Line 1: '" + line + "' exceeds 5 syllables\n"
        if (line_index == 1 and line_syllables < 5):
            exception_string += "Line 1: '" + line + "' is less than 5 syllables\n"
        if (line_index == 2 and line_syllables > 7):
            exception_string += "Line 2: '" + line + "' exceeds 7 syllables\n"
        if (line_index == 2 and line_syllables < 7):
            exception_string += "Line 2: '" + line + "' is less than 7 syllables\n"
        if (line_index == 3 and line_syllables > 5):
            exception_string += "Line 3: '" + line + "' exceeds 5 syllables\n"
        if (line_index == 3 and line_syllables < 5):
            exception_string += "Line 3: '" + line + "' is less than 5 syllables\n"    
            
        if (len(exception_string) == 0):
            print("there are " +  str(line_syllables) + " syllables on line " + str(line_index) + ": " + line)
        else:
            print(exception_string)
    if (len(exception_string) == 0):
        print("it's a haiku")
    else:
        print("it's not a haiku")

def get_syllable_count(word):
    map = cmudict.dict()
    syllables = map.get(word)[0]
    syllable_count = 0
    for syllable in syllables:
        if (str(syllable).endswith("0") or str(syllable).endswith("1") or str(syllable).endswith("2")):
            syllable_count += 1
    return syllable_count

beginning()