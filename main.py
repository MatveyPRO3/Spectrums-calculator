import os


def speed_port_parser(file_name: str):
    try:
        f_name = file_name.split("_")
        total_speed = sum(list(map(float, f_name[0].split("-"))))
        port = int(f_name[1].split("-")[1].replace(".txt", ""))
        return port, total_speed
    except:
        print(
            f"Cant parse speed or port for file {file_name}. Format - [speed1]-[speed2]-[speed3]_port-[port number].txt Example: '2-2-2_port-1.txt'"
        )
        return 0, 0


def get_time(port, speed, chip_volume=0.2):
    try:
        t = (
            ((chip_volume * (port - 1) / 8) + (0.75 if port == 9 else 0))
            / (speed)
            * 1000
        )
        return t
    except:
        return "Failed to calculate time"


path = input(
    "Enter full directory path with slash at the end: (put all spectrums there)"
)

first_peak, second_peak, base_line, result_calculation_way, normalization_number = (
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
    int(
        input(
            """Enter how to calculate result value for each spectrum:
            1 - peaks ratio  (divide right peak to second) 
            2 - left peak (take just value of the left peak)
            3 - right peak (take just value of the right peak)
            4 - base line (for base line calibration)\n"""
        )
    ),
    int(
        input(
            "Enter how many values to take for normalization: (enter 0 for avoiding it)"
        )
    ),
)


def analyzer():
    file_names = os.listdir(path)

    times = [get_time(*speed_port_parser(f)) for f in file_names]

    points = []  # for each spectrum making sublist [first peak, second peak, base line]
    for f_n in file_names:
        print("Processing:", f_n, end=" ")
        try:
            with open(path + f_n, "r") as opened_file:
                lines = opened_file.readlines()
                if not normalization_number:
                    lines = {
                        float(l.split(",")[0]): float(l.split(",")[1]) for l in lines
                    }  # converting each line such '153.834,0.0' to {153.834: 0.0}
                    points.append(
                        [lines[first_peak], lines[second_peak], lines[base_line]]
                    )
                else:
                    wave_lengths = [float(l.split(",")[0]) for l in lines]
                    intensities = [float(l.split(",")[1]) for l in lines]
                    first_peak_values = intensities[
                        wave_lengths.index(first_peak)
                        - normalization_number : wave_lengths.index(first_peak)
                        + normalization_number
                    ]
                    second_peak_values = intensities[
                        wave_lengths.index(second_peak)
                        - normalization_number : wave_lengths.index(second_peak)
                        + normalization_number
                    ]
                    base_line_values = intensities[
                        wave_lengths.index(base_line)
                        - normalization_number : wave_lengths.index(base_line)
                        + normalization_number
                    ]
                    points.append(
                        [
                            sum(first_peak_values) / len(first_peak_values),
                            sum(second_peak_values) / len(second_peak_values),
                            sum(base_line_values) / len(base_line_values),
                        ]
                    )
        except:
            print(
                "Cant get peaks in {}, make sure you entered correct input".format(f_n)
            )
            points.append([float("inf")] * 3)
        else:
            print("Succeed")

    print("Collected points:")
    print(points)
    if result_calculation_way == 1:
        result = [(p[1] - p[2]) / (p[0] - p[2]) for p in points]
    elif result_calculation_way == 2:
        result = [p[0] for p in points]
    elif result_calculation_way == 3:
        result = [p[1] for p in points]
    elif result_calculation_way == 4:
        result = [p[2] for p in points]

    with open("result.txt", "w") as file:
        file.write(
            "[file name]|[reaction time]|[left peak, right peak, base line]|[result value (depends on way it was calculated!)]\n"
        )
        for i in range(len(points)):
            file.write(
                f"{file_names[i]}|{str(times[i])}|{str(points[i])}|{result[i]} \n"
            )


analyzer()
