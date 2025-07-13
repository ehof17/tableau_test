from registry import RegistryBase


def main():
    #request = {"datasource": "GoogleAnalyticsDataManager"}
    #request = {"datasource": "Neo4jDataManager"}
    request = {"datasource": "SalesCacheDataSource",
               "data_source_id": "a"}
    
    request = {"datasource": "DaisyDataDataSource", "dataframe":"bruh"}
    request = {"datasource": "ComplicatedRefreshesDataSource", "dataframe":"bruh"}
    
    classes = RegistryBase.get_registry().keys()
    print(f"Available datasources: {classes}")

    refresh_class = RegistryBase.get_registry().get(request["datasource"])
    if refresh_class is None:
        raise ValueError(f"Unknown datasource: {request['datasource']}")
    else:
        res = refresh_class().refresh_hyper_file(**request)
        
    


if __name__ == "__main__":
    main()