def get_time(port, speed, chip_volume=0.2):
    try:
        t = ((chip_volume * (port - 1) / 8) + (0.75 if port == 9 else 0)) / (speed)*1000
        return t
    except:
        return "Failed to calculate time"