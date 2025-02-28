def transform_data(df: dict):
    # build data model
    df = df[[
        "id", 
        "display_name",
        "hw_address",
        "vendor",
        "model",
        "type",
        "os",
        "user_data",
        "ip_addresses",
        "open_ports",
        "names",
        ]].copy()

    # transform data
    df.loc[:, "type"] = df["type"].apply(
        lambda x: x.get("label") 
            if isinstance(x, dict) 
            and "label" in x 
            else None
    )
    df.loc[:, "names"] = df["names"].apply(
        lambda x: x.get("host")
            if isinstance(x, dict)
            and "host" in x
            else None
    )
    
    # rename columns
    df = df.rename(columns={
        'display_name': 'name',
        'vendor': 'manufacturer',
        'names': 'hostname',
        })
    
    return df