import investpy

def index_hist(startdate, enddate, index): 
  df = investpy.get_index_historical_data(index=index, country='Bangladesh', from_date=startdate, to_date=enddate)
  df = df.reset_index().sort_values(by="Date", ascending=False)
  return (df)

