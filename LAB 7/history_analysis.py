"""
Lab 7 Docstring
"""
def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    """
    sites = []
    for elem in visits:
        if date == elem[2]:
            if elem[0] not in sites:
                sites.append(elem[0])
    sites = set(sites)
    return sites

def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    """
    status = False
    frequency_visit = {}
    for elem in visits:
        name = elem[0]
        if len(frequency_visit) > 0:
            keys = []
            for key in frequency_visit:
                keys.append(key)
            for key_num in keys:
                if status is False:
                    if name in frequency_visit[key_num]:
                        value = frequency_visit[key_num]
                        value.remove(name)
                        if value == set():
                            frequency_visit.pop(key_num)
                        else:
                            frequency_visit[key_num] = value
                        try:
                            value = frequency_visit[key_num + 1]
                            value.add(name)
                            frequency_visit[key_num + 1] = value
                        except (KeyError, IndexError, ValueError):
                            value = set()
                            value.add(name)
                            frequency_visit[key_num + 1] = value
                        status = True
            if status is False:
                try:
                    value = frequency_visit[1]
                    value.add(name)
                    frequency_visit[1] = value
                except KeyError:
                    value = set()
                    value.add(name)
                    frequency_visit[1] = value
            status = False
        else:
            value = set()
            value.add(name)
            frequency_visit[1] = value

    sorted_keys = sorted(frequency_visit.keys(), reverse = True)
    print(sorted_keys)
    most_frequent = []
    while number > 0:
        try:
            urls = frequency_visit[sorted_keys[0]]
            random_url = urls.pop()
            most_frequent.append(random_url)
            if urls == set():
                frequency_visit.pop(sorted_keys[0])
                sorted_keys.pop(0)
            else:
                frequency_visit[sorted_keys[0]] = urls
            print(urls)
        except IndexError:
            pass
        number-=1
    most_frequent = set(most_frequent)

    return most_frequent

def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('url','topic','2021-12-07','12:05:36.66',100), ('url','topic',\
    '2021-11-07','12:05:36.66',522)], "url")
    ('topic', '2021-12-07', '12:05:36.66', 2, 311.0)
    """
    count_visit = 0
    dates_of_attendance = []
    time_spent = []
    for elem in visits:
        if elem[0] == url:
            title = elem[1]
            count_visit += 1
            dates_of_attendance.append((elem[2], elem[3]))
            time_spent.append(elem[4])
    if dates_of_attendance == []:
        return ("", "", "", 0, 0)
    last_date = dates_of_attendance[0]
    for elem in dates_of_attendance:
        local_last_date = last_date[0].split("-")
        date = elem[0].split("-")
        if local_last_date[0] < date[0]:
            last_date = elem
            continue
        elif local_last_date[0] > date[0]:
            continue
        else:
            if local_last_date[1] < date[1]:
                last_date = elem
                continue
            elif local_last_date[1] > date[1]:
                continue
            else:
                if local_last_date[2] < date[2]:
                    last_date = elem
                    continue
                elif local_last_date[2] > date[2]:
                    continue
                else:
                    local_last_time = last_date[1].split(":")
                    time = elem[1].split(":")
                    if local_last_time[0] < date[0]:
                        last_date = elem
                        continue
                    elif local_last_time[0] > date[0]:
                        continue
                    else:
                        if local_last_time[1] < date[1]:
                            last_date = elem
                            continue
                        elif local_last_time[1] > date[1]:
                            continue
                        else:
                            if local_last_time[2] < date[2]:
                                last_date = elem
                                continue
                            elif local_last_time[2] > date[2]:
                                continue
                            else:
                                pass
    last_date, last_time = last_date[0], last_date[1]
    time = 0
    for elem in time_spent:
        time += elem
    average_time_spent = time / count_visit
    return (title, last_date, last_time, count_visit, average_time_spent)

print(get_url_info([('url','topic','2021-11-07','12:05:36.66',522), ('url','topic','2021-11-28','12:05:36.66',522), ('url','topic','2021-11-07','12:05:36.66',522), ('url','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('url1','topic','2021-11-07','12:05:36.66',522), ('w','topic','2021-11-07','12:05:36.66',522), ('url2','topic','2021-11-07','12:05:36.66',522)], "url"))