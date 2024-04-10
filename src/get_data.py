import requests 
import pandas as pd 

'''
Download presidential polls
'''
def get_csv():
    url = "https://projects.fivethirtyeight.com/polls/data/president_polls.csv"
    df = pd.read_csv(url)
    df.to_csv('data.csv')

'''
Clean data
'''
def clean_data():
    df = pd.read_csv("data.csv")

    df['start'] = df['start_date'].astype("string")
    print(df.shape)

    series = df['start']
 
    index = series[series == "12/28/23"].index

    df = df.loc[:index[0] - 1, ["poll_id", "pollster", "end_date", "candidate_id", "candidate_name", "pct"]]
    gk = df.groupby('poll_id')

    result = {'id': '','biden': 'NULL', 'trump': 'NULL', 'kennedy': '', 'pollster': '', 'end_date': ''}

    "poll_id, candidate_id, candidate_name, pct"
    l = []
    for i, frame in gk.__iter__():
        for index, row in frame.iterrows():
            if row['candidate_id'] == 19368 and result['biden'] != "NULL" and result['trump'] != 'NULL':
                print(result)
                l.append(result)
                result = {'id': '', 'biden': 'NULL', 'trump': 'NULL', 'kennedy': '', 'pollster': '', 'end_date': ''}
            
            result['id'] = row['poll_id']
            result['pollster'] = row['pollster']
            result['end_date'] = row['end_date']

            if row['candidate_id'] == 19368:
                result['biden'] = row['pct']
            elif row['candidate_id'] == 16651:
                result['trump'] = row['pct']
            elif row['candidate_id'] == 31042:
                result['kennedy'] = row['pct']

        if (result['biden'] != 'NULL' and result['trump'] != 'NULL'):
            l.append(result)
        result = {'id': '', 'biden': 'NULL', 'trump': 'NULL', 'kennedy': '',  'pollster': '', 'end_date': ''}

    df.to_csv("pct.csv")
    final = pd.DataFrame(l)
    final.to_csv("final.csv")
    print(final)

get_csv()
clean_data()