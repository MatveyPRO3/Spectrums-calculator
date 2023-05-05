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
