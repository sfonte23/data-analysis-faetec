import sgs

def get_basic_basket_cost(codes, start_date, end_date):
    df = sgs.dataframe(codes, start=start_date, end=end_date)
    return df

if __name__ == "__main__":
    basket_data = get_basic_basket_cost([7491, 7493, 7482], '01/01/2023', '01/08/2023')
    print(basket_data)
