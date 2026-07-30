def temperature_value(value, unit):

    default_celsius_threshold = 0

    default_fahrenheit_threshold = 32

    if unit == "C":
        converted = (value * 9 / 5) + 32
        threshold = default_fahrenheit_threshold

    elif unit == "F":
        converted = (value - 32) * 5 / 9
        threshold = default_celsius_threshold

    else:
        return ValueError("unit must be 'C' or 'F'")

    if converted < threshold:

        return "Cold advisory"

    else:

        return "Heat alert"





