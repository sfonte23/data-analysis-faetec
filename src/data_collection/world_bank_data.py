import pandas_datareader.data as web

def get_world_bank_data(codes, start_year, end_year):
    df = web.DataReader(codes, 'wb', start=start_year, end=end_year)
    return df

if __name__ == "__main__":
    world_data = get_world_bank_data(['SP.DYN.LE00.IN', 'EN.ATM.CO2E.PC'], 2010, 2023)
    print(world_data)
