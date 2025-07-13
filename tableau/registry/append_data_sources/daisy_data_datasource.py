from .append_refresh_datasource import AppendRefreshDataSource
from datamodels import HyperFileWrapper
class DaisyDataDataSource(AppendRefreshDataSource):
    @classmethod
    def generate_partial_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        print("[DAISY-DATA-DATASOURCE] -> Generating partial dataframe")
        path_to_hyper = "daisy.to.hyper"
        res = HyperFileWrapper(path_to_hyper=path_to_hyper)
        return res