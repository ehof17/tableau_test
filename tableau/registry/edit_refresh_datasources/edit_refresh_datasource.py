from ..base_data_sources.registry_base import BaseRegisteredClass
from datamodels import HyperFileWrapper
class EditRefreshDataSource(BaseRegisteredClass):
    @classmethod
    def generate_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        print("[EDIT-REFRESH DATASOURCE]-Generating dataframe for class:", cls.__name__)
        
        if 'data_source_id' not in kwargs:
            raise ValueError("EditRefreshDataSource requires 'data_source_id' argument to be passed to generate_dataframe.")
        
        data_source_id = kwargs['data_source_id']
        print("[EDIT-REFRESH DATASOURCE]-Downloading existing Hyper File ", data_source_id)
        print("[EDIT-REFRESH DATASOURCE]-Converting existing Hyper into dataframe ")
        dataframe = "PANDAS-DF"
        # add arg of dataframe to this
        kwargs['dataframe'] = dataframe
        res = cls.generate_modified_dataframe(*args, **kwargs)
        res.refreshType = 'edit'
        return res
    
    @classmethod
    def generate_modified_dataframe(cls, *args, **kwargs):
        raise NotImplementedError()