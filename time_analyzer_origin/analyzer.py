import time_calculator
import time_parser
import os

file_names = os.listdir(r"C:\Users\matveyP\MegaSync\MEGAsync\Programming\Other\SFEDU\Spectrums")
times = [
    time_calculator.get_time(*time_parser.speed_port_parser(f)) for f in file_names
]
points = []
for f_n in file_names:
    try:
        with open(f_n, "r") as opened_file:
            lines = opened_file.readlines()
            points.append(
                [
                    min(list(map(lambda x: float(x.split(",")[1]), lines[837:1134]))),
                    max(
                        list(map(lambda x: float(x.split(",")[1]), lines[691:837]))
                    ),  # first peak
                    max(
                        list(map(lambda x: float(x.split(",")[1]), lines[1134:1833]))
                    ),  # second peak
                ]
            )
    except:
        print("Cant get peaks from file {}".format(f_n))

result = [(p[2]-p[0])/(p[1]-p[0]) for p in points]

with open ("result.txt","w") as file:
    for i in range(len(points)):
        file.write(f"{file_names[i]}  |  {str(times[i])}  |  {str(points[i])}| {result[i]} \n")

