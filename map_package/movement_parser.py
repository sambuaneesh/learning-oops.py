def parse_distance(distance_str):
    if distance_str.endswith("mm"):
        d_mm = float(distance_str[:-2])
        d_cm = d_mm / 10
        return d_cm
    elif distance_str.endswith("cm"):
        d_cm = float(distance_str[:-2])
        return d_cm
    else:
        d_mm = float(distance_str)
        d_cm = d_mm / 10
        return d_cm
