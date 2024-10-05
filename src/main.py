from data_collection.finance_data import get_stock_data
from data_collection.sgs_data import get_basic_basket_cost
from data_collection.world_bank_data import get_world_bank_data

if __name__ == "__main__":
    # Chamada das funções
    stock_data = get_stock_data(["PETR4.SA"], "2023-01-01", "2023-08-01")
    basket_data = get_basic_basket_cost([7491], '01/01/2023', '01/08/2023')
    world_data = get_world_bank_data(['SP.DYN.LE00.IN'], 2010, 2023)

    print(stock_data)
    print(basket_data)
    print(world_data)
