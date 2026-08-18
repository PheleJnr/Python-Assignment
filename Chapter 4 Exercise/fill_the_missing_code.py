def seconds_since_midnight(hours, minutes, seconds):

    hour_in_seconds = hours * 60 * 60

    minute_in_seconds = minutes * 60

    sum_of_seconds = hour_in_seconds + minute_in_seconds + seconds 

    return sum_of_seconds


print(seconds_since_midnight(hours, minutes, seconds))


