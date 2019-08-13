def jobtime(jobs):
    epoch = 0
    rest = 2
    d = {}
    for job in jobs:
        if job in d.keys():
            delta_t = epoch - d[job]
            cool = rest + 1 - delta_t
            if cool > 0:
                epoch += cool

        d[job] = epoch
        epoch += 1

    return epoch

if __name__ == '__main__':
    assert jobtime('AAA') == 7
    assert jobtime('') == 0
    assert jobtime('ABA') == 4
