import os

n = 1
t = '00:00'
work_dir = os.path.dirname(os.path.realpath(__file__))

class TimeStamp:
    def __init__(self, t_from, t_to):
        self.t_from = t_from
        self.t_to = t_to
    def to_sec(self, t):
        if len(t) == 5:
            m, s = t.split(':')
            return int(m) * 60 + int(s)
        elif len(t) == 8:
            h, m, s = t.split(':')
            return int(h) * 3600 + int(m) * 60 + int(s)
        else:
            print('Wrong time format')
    def add(self):
        add_time = self.to_sec(self.t_from) + self.to_sec(self.t_to)
        new_min, new_sec = divmod(add_time, 60)
        return str(new_min).zfill(2) + ':' + str(new_sec).zfill(2)
    def to_mins(self):
        new_min, new_sec = divmod(self.to_sec(self.t_to), 60)
        return str(new_min).zfill(2) + ':' + str(new_sec).zfill(2)

source_type = input('Type of source audio (single or multiple files) [S/M]: ')
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
        if source_type.upper() == 'S':
            new = TimeStamp('00:00:00', track_time)
            t = new.to_mins()
        elif source_type.upper() == 'M':
            new = TimeStamp(t, track_time)
            t = new.add()
        else:
            print('Wrong source type')
            break
        tr = t + ':00'
        file.write(f'  TRACK {tn} AUDIO\n')
        file.write(f'    PERFORMER \"{performer}\"\n')
        file.write(f'    TITLE \"{track_title}\"\n')
        file.write(f'    INDEX 01 {tr}\n')
        n += 1