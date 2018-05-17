

def month_info():
    import datetime
    import calendar

    pubholys = {4: [30], 5: [3, 4, 5], 7: [16], 8: [11],
                9: [17, 24], 10: [8], 11: [3, 23], 12: [24]}
    nextmonth = int(datetime.date.today().month + 1)        # シフトを作る月を取得
    daysinthemonth = []                                 # 月の日にちのリスト
    dates = []
    datesDic = {0: "月", 1: "火", 2: "水", 3: "木", 4: "金",
                5: "土", 6: "日"}
    satlist = []                                            # 土曜日のリスト
    holydaylist = []                                        # 日祝のリスト
    weekdays = []                                           # 平日のリスト

    if nextmonth in pubholys:
        holydaylist.extend(pubholys[nextmonth])

    (a, b) = calendar.monthrange(2018, nextmonth)           # 月の最初の曜日と日数を取得

    for day in range(1, b+1):
        daysinthemonth.append(day)                          # 月の日にちをリストに突っ込む

    if (0 <= a) and (a <= 5):                               # 月の最初の曜日でパターン分け
        sat = 6 - a
        sun = sat + 1

    elif a == 6:
        sat = 7
        sun = 1

    thismonth = calendar.Calendar(firstweekday=a)
    dateslist = list(thismonth.iterweekdays()) * 5

    for datenum in dateslist:
        if len(dates) <= b-1:
            dates.append(datesDic[datenum])

    for i in range(0, 6):                                   # 土曜と日祝をリストに突っ込む
        if (sat + 7 * i) <= b and (sat + 7 * i) not in satlist:
            satlist.append(sat + 7 * i)
            satlist = list(set(satlist) - set(holydaylist))
            satlist.sort()
        if (sun + 7 * i) <= b:
            holydaylist.append(sun + 7 * i)
            holydaylist.sort()

    weekdays = list(set(daysinthemonth) - set(satlist) - set(holydaylist))

    return {"nextmonth": nextmonth,
            "daysinthemonth": daysinthemonth,
            "dates": dates,
            "satlist": satlist,
            "holydaylist": holydaylist,
            "weekdays": weekdays,
            "a": a,
            "b": b}