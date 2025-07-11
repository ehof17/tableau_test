from registry import RegistryBase


def main():
    #request = {"datasource": "GoogleAnalyticsDataManager"}
    request = {"datasource": "Neo4jDataManager"}

    refresh_class = RegistryBase.get_registry().get(request["datasource"])
    
    if refresh_class is None:
        raise ValueError(f"Unknown datasource: {request['datasource']}")
    else:
        refresh_class().refresh_hyper_file()
    


if __name__ == "__main__":
    main()