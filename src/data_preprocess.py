import re
import datetime

def choose_columns(df, cols):
    return df[cols]

def remove_punc(df, cols):
    spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
    for col in cols:
        for char in spec_chars:
            df[col] = df[col].str.replace(char, ' ')
        df[col] = df[col].str.split().str.join(" ")
    return df

def cal_delta_days(ytb):
    # 转化trending_date格式
    trd = ytb['trending_date']
    trd_new = []
    for x in trd:
        l = x.split('.')
        trd_new.append(int(l[1]) + int(l[2])*100 + (2000+int(l[0]))*10000)
    ytb['trending_date'] = trd_new

    # 得到publish_date规范格式
    publish_time_dateform = []
    for i, x in ytb.iterrows():
        s = x['publish_time']
        match = re.search('\d{4}-\d{2}-\d{2}', s)
        date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
        publish_time_dateform.append(date)

    # 得到trending_date规范格式
    trending_date_dateform = []
    for i, x in ytb.iterrows():
        s = str(x['trending_date'])
        match = re.search('\d{4}\d{2}\d{2}', s)
        date = datetime.datetime.strptime(match.group(), '%Y%m%d').date()
        trending_date_dateform.append(date)

    # 得到距离天数
    delta_days = []
    for i in range(len(publish_time_dateform)):
        delta = trending_date_dateform[i] - publish_time_dateform[i]
        delta_days.append(delta.days)

    ytb['delta_days'] = delta_days
    return ytb
