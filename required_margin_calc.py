def margin(total, absent):
    present = total - absent
    if present/total < 0.75:
        req = 3 * absent - present
        print("Required: {} hours".format(ceil(req)))
    else:
        margin = present / 3 - absent
        print("Margin: {} hours".format(int(margin)))

def ceil(x: float):
    if x*10%10 >= 5: return int(x) + 1
    else: return int(x)
