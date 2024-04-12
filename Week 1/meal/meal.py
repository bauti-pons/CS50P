def main():

    time = input("What time is it? ")
    float_time = convert(time)
    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")

def convert(time):

    if "p.m" in time:
        time = time.replace(" p.m", "")
        hours, minutes = time.split(":")
        float_time = float(hours) + 12 + float(minutes) / 60
        return float_time
    else:
        hours, minutes = time.split(":")
        float_time = float(hours) + float(minutes) / 60
        return float_time

if __name__ == "__main__":
    main()
