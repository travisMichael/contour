

def get_color_from_magnitude(mag, max_mag):
    m = min(mag, max_mag)

    red = round((m/max_mag) * 255)
    blue = 255 - red

    return blue, 0, red