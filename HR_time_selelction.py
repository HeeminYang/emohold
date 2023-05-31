def HR_time_selection(data, date, start, end):
    thedate = data['date']== date
    l = data.loc[thedate, ['time', 'value']]
    c1=l['time'] > start
    c2=l['time'] < end
    result = l.loc[c1 & c2, :]
    return result