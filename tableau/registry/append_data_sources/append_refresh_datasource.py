from ..base_data_sources import BaseRegisteredClass
from datamodels import HyperFileWrapper


class FullRefreshMixin:
    """
    For some datasources that support an append refresh, they also may need to support a full refresh.
    This ensures the method is defined
    """
    @classmethod
    def generate_full_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        raise NotImplementedError("generate_full_dataframe must be implemented.")
    
    

class AppendRefreshDataSource(BaseRegisteredClass):
    """
    Base class for append-refresh datasources. These datasource only need to generate a partial data frame
    
    
    This won't work if we want to generate full dataframe as well as append refresh
    Decorator may be nice
    Or in the args
    
    """
    @classmethod
    def generate_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        """
        This method is called to funnel to generate_partial_dataframe.
        """
        print("[APPEND-REFRESH-DATASOURCE] Generating dataframe for class:", cls.__name__)
        
        refresh_type = "full"
        
        if refresh_type == "full":
            if hasattr(cls, "generate_full_dataframe"):
                return cls.generate_full_dataframe(cls, *args, **kwargs)
            else:
                raise NotImplementedError(f"{cls.__name__} does not support full refresh.")
        elif refresh_type == "append":
            if hasattr(cls, "generate_partial_dataframe"):
                obj = generate_partial_dataframe(cls, *args, **kwargs)
                obj.refreshType = "append"
                return obj
            else:
                raise NotImplementedError(f"{cls.__name__} must implement generate_partial_dataframe.")
        else:
            raise ValueError(f"Unknown refresh type: {refresh_type}")
    
    @classmethod
    def generate_partial_dataframe(cls, *args, **kwargs) -> HyperFileWrapper:
        """
        This method must be overwritten by an append-refresh datasource subclass.
        """
        raise NotImplementedError()