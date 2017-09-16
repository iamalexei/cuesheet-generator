import os

n = 1
t = '00:00'
work_dir = os.path.dirname(os.path.realpath(__file__))

class TimeStamp:
    def __init__(self, t_from, t_to):
        self.t_from = t_from
        self.t_to = t_to
    def to_sec(self, t):
        mins = int(t.split(':')[0])
        seconds = int(t.split(':')[1])
        return mins * 60 + seconds
    def add(self):
        add_time = self.to_sec(self.t_from) + self.to_sec(self.t_to)
        new_min, new_sec = divmod(add_time, 60)
        return str(new_min).zfill(2) + ':' + str(new_sec).zfill(2)

file_name = input('File name: ')
performer = input('Performer: ')
title = input('Title: ')
cue_name = file_name + '.cue'    

with open(os.path.join(work_dir, cue_name), 'a') as file:
    file.write(f'PERFORMER \"{performer}\"\n')
    file.write(f'TITLE \"{title}\"\n')
    file.write(f'FILE \"{file_name}.opus\" WAVE\n')
    while True:
        tn = str(n).zfill(2)    
        track_title = input(f'{n} Track title: ')
        if track_title == '':
            break
        track_time = input(f'{n} Track time: ')
        new = TimeStamp(t, track_time)
        t = new.add()
        tr = t + ':00'
        file.write(f'  TRACK {tn} AUDIO\n')
        file.write(f'    PERFORMER \"{performer}\"\n')
        file.write(f'    TITLE \"{track_title}\"\n')
        file.write(f'    INDEX 01 {tr}\n')
        tn += 1