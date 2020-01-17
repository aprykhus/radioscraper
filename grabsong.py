from songengine import get_song
import sched, time
s = sched.scheduler(time.time, time.sleep)
def run_script(sc): 
    currentsong = get_song('https://www.radio.com/wogl-vinyltap/listen')
    print(currentsong)
    s.enter(5, 1, run_script, (sc,))

s.enter(5, 1, run_script, (s,))
s.run()