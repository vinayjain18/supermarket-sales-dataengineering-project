import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = df.drop_duplicates().reset_index(drop=True)
    df.rename(columns = {'Tax(5 percent)':'Tax_5_percent'}, inplace = True)
    df["Date"] = df["Date"].str.replace("/","-")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Id"] = df.index

    branch_dim = df[['Branch']].drop_duplicates().reset_index(drop=True)
    branch_dim["branch_id"] = branch_dim.index
    branch_dim = branch_dim[["branch_id", "Branch"]]

    city_dim = df[["City"]].drop_duplicates().reset_index(drop=True)
    city_dim["city_id"] = city_dim.index
    city_dim = city_dim[["city_id", "City"]]

    customer_type_dim = df[["Customer type"]].drop_duplicates().reset_index(drop=True)
    customer_type_dim["customer_type_id"] = customer_type_dim.index
    customer_type_dim = customer_type_dim[["customer_type_id", "Customer type"]]

    gender_dim = df[["Gender"]].drop_duplicates().reset_index(drop=True)
    gender_dim["gender_id"] = gender_dim.index
    gender_dim = gender_dim[["gender_id", "Gender"]]

    product_type_dim = df[["Product line"]].drop_duplicates().reset_index(drop=True)
    product_type_dim["product_type_id"] = product_type_dim.index
    product_type_dim = product_type_dim[["product_type_id", "Product line"]]

    date_dim = df[["Date"]].drop_duplicates().reset_index(drop=True)
    date_dim["date_id"] = date_dim.index
    date_dim["purchase_day"] = date_dim["Date"].dt.day
    date_dim["purchase_month"] = date_dim["Date"].dt.month
    date_dim["purchase_year"] = date_dim["Date"].dt.year
    date_dim = date_dim[["date_id", "Date", "purchase_day", "purchase_month", "purchase_year"]]

    time_dim = df[["Time"]].drop_duplicates().reset_index(drop=True)
    time_dim["time_id"] = time_dim.index
    time_dim["purchase_hour"] = time_dim["Time"].str.split(":").str[0]
    time_dim = time_dim[["time_id", "Time", "purchase_hour"]]

    payment_type_dim = df[["Payment"]].drop_duplicates().reset_index(drop=True)
    payment_type_dim["payment_type_id"] = payment_type_dim.index
    payment_type_dim = payment_type_dim[["payment_type_id", "Payment"]]

    fact_table = df.merge(branch_dim, on='Branch')\
                .merge(city_dim, on='City')\
                .merge(customer_type_dim, on='Customer type')\
                .merge(gender_dim, on='Gender')\
                .merge(product_type_dim, on='Product line')\
                .merge(date_dim, on='Date')\
                .merge(time_dim, on='Time')\
                .merge(payment_type_dim, on='Payment')\
                [['Id', 'Invoice ID', 'branch_id', 'city_id', 'customer_type_id', 'gender_id', 'product_type_id', 'date_id', 'time_id', 
                'payment_type_id','Unit price', 'Quantity', 'Tax_5_percent', 'Total', 'cogs', 'gross margin percentage', 
                'gross income', 'Rating']]

    return {"branch_dim": branch_dim.to_dict(orient='dict'),
            "city_dim": city_dim.to_dict(orient='dict'),
            "customer_type_dim": customer_type_dim.to_dict(orient='dict'),
            "gender_dim": gender_dim.to_dict(orient='dict'),
            "product_type_dim": product_type_dim.to_dict(orient='dict'),
            "date_dim": date_dim.to_dict(orient='dict'),
            "time_dim": time_dim.to_dict(orient='dict'),
            "payment_type_dim": payment_type_dim.to_dict(orient='dict'),
            "fact_table": fact_table.to_dict(orient='dict')}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
