"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
"""


def timeConversion(s):
    """
    :param s: string of time(must be in format hh:mm:ssAM or hh:mm:ssPM)
    :return:string of time in military time hh:mm:ss
    """
    # Checking if last two elements of time is AM and first two elements are 12
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    # remove the AM
    elif s[-2:] == "AM":
        return s[:-2]
    # Checking if last two elements of time is PM and first two elements are 12
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(s[:2]) + 12) + s[2:8]


s = "08:40:22PM"
print(timeConversion(s))
