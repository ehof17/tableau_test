from .append_refresh_datasource import AppendRefreshDataSource, FullRefreshMixin
from datamodels import HyperFileWrapper
class ComplicatedRefreshesDataSource(AppendRefreshDataSource, FullRefreshMixin):
    """
    This is an example of a datasource that requires a full refresh defined as well
    """
    @classmethod
    def generate_partial_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        print("[COMPLICATED-REFRESH-DATASOURCE] -> Generating partial dataframe")
        path_to_hyper = "complicated.to.hyper"
        res = HyperFileWrapper(path_to_hyper=path_to_hyper)
        return res
    
    def generate_full_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        print("[COMPLICATED-REFRESH-DATASOURCE] -> Generating FULL dataframe")
        path_to_hyper = "complicated_full.to.hyper"
        res = HyperFileWrapper(path_to_hyper=path_to_hyper)
        return res