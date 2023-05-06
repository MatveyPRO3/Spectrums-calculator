import time_calculator
import time_parser
import os

path = input(
    "Enter full directory path with slash at the end: (put all spectrums there)"
)

first_peak, second_peak, base_line = (
    float(
        input(
            "Enter wave length for first(left) peak (you can only choose from existing in file wave lengths!):"
        )
    ),
    float(
        input(
            "Enter wave length for second(right) peak (you can only choose from existing in file wave lengths!):"
        )
    ),
    float(input("Enter wave length for base line: ")),
)


def analyzer():
    file_names = os.listdir(path)

    times = [
        time_calculator.get_time(*time_parser.speed_port_parser(f)) for f in file_names
    ]

    points = []  # for each spectrum making sublist [first peak, second peak, base line]
    for f_n in file_names:
        print("Processing", f_n, end=" ")
        try:
            with open(path + f_n, "r") as opened_file:
                lines = opened_file.readlines()
                lines = {
                    float(l.split(",")[0]): float(l.split(",")[1]) for l in lines
                }  # converting each line such '153.834,0.0' to {153.834: 0.0}
                points.append([lines[first_peak], lines[second_peak], lines[base_line]])
        except:
            print(
                "Cant get peaks in {}, make sure you entered correct input".format(f_n)
            )
        else:
            print("Succeed")

    print("Collected points:")
    print(points)
    result = [(p[1] - p[2]) / (p[0] - p[2]) for p in points]

    with open("result.txt", "w") as file:
        file.write(
            "[file name]|[reaction time]|[left peak, right peak, base line]|[ratio]\n"
        )
        for i in range(len(points)):
            file.write(
                f"{file_names[i]}|{str(times[i])}|{str(points[i])}|{result[i]} \n"
            )


if __name__ == "__main__":
    analyzer()
