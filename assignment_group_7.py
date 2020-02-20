'''
Registration A
'''

from pathlib import Path

PATH = Path(r'C:\Users\saski\Desktop\KT\Master\TM10002_(Python)\Assignment\DataFiles-20180227-Registration-A\Reference')
DICTIONARY = dict()


def read_xyz(landmark):
    '''
    Reading floats from a string
    '''
    lijst_float = []
    lijst = landmark.strip().split()
    for i in lijst:
        lijst_float.append(float(i))
    return lijst_float


for subpath in PATH.iterdir():
    print(f'{subpath!r}')
    if subpath.is_dir():
        print(f'{subpath} is a directory')
        for obs in subpath.iterdir():
            print(f'{obs!r}')
            if obs.is_dir():
                print(f'{obs} is a directory')
                for patient in obs.iterdir():
                    print(f'{patient!r}')
                    with open(patient, "r") as landmarks:
                        xyz = read_xyz(landmarks.read())
                        DICTIONARY = {'obs': subpath.name,
                                      'patient': obs.name,
                                      'landmarks': patient.name,
                                      'x': xyz[0],
                                      'y': xyz[1],
                                      'z': xyz[2]}
                        print(DICTIONARY)
