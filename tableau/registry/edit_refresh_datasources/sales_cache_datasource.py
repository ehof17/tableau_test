from .edit_refresh_datasource import EditRefreshDataSource
from datamodels import HyperFileWrapper
class SalesCacheDataSource(EditRefreshDataSource):
    @classmethod
    def generate_modified_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        print(kwargs)
        print(f"[SALES-CACHE-DATASOURCE] -> Modifying this dataframe-> {kwargs['dataframe']}")   
           
        path_to_hyper= "Sales_cache.hyper"
        res = HyperFileWrapper(path_to_hyper=path_to_hyper)
        return res
        