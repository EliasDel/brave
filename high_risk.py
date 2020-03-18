def gitpull():
    import dataiku
    import pandas as pd
    
    client_data = dataiku.Dataset("client_data_scored")
    client_df = client_data.get_dataframe()
    
    high_risk_df = client_df.loc[client_df['score'] == 1]
    
    client_data_high_risk = dataiku.Dataset("client_data_high_risk")
    client_data_high_risk.write_with_schema(high_risk_df)
