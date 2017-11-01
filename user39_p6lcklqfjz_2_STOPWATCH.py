# template for "Stopwatch: The Game"

import simplegui

# define global variables
k = 0
count = 0
success = 0
rate = str(success) + '/' + str(count)
runs = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    msec = t % 10
    sec1 = (t / 10)% 10
    minutes = (t / 100)/ 6
    sec2 = (t / 100)% 6
    return str(minutes) + ':' + str(sec2) + str(sec1) + '.' + str(msec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global runs
    
    timer.start()
    runs = True
    

def stop():
    global rate,success,count,runs
    
    timer.stop()
    
    if runs == True:
        count = count + 1
        if k % 10 == 0:
            success += 1
            
    rate = str(success) + '/' + str(count)
    runs = False
    

def reset():
    global k,runs,rate,count,success
    
    timer.stop()
    k = 0
    success = 0
    count = 0
    rate = str(success) + '/' + str(count)
    runs = False
    
    

# define event handler for timer with 0.1 sec interval
def time_handler():
    global k
    k = k + 1
    

# define draw handler
def draw_handler(canvas):    
    canvas.draw_text(format(k), [90, 150], 40, 'White')
    canvas.draw_text(rate, [240 ,35], 30, 'Green')


    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers

frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, time_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
