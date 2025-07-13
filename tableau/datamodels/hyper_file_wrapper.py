class HyperFileWrapper:
    """
    Dataclass to encapsulate pathToHyper
    """
    def __init__(self, path_to_hyper: str, refreshType: str = 'overwrite', **kwargs):
        self.path_to_hyper = path_to_hyper
        self.refreshType = refreshType
        self.kwargs = kwargs

    def __repr__(self):
        return f"HyperFileWrapper(path_to_hyper='{self.path_to_hyper}', refreshType='{self.refreshType}', kwargs={self.kwargs})"

    def to_dict(self):
        return {
            'path_to_hyper': self.path_to_hyper,
            'refreshType': self.refreshType,
            **self.kwargs
        }

    @classmethod
    def from_dict(cls, data: dict):
        path_to_hyper = data.pop('path_to_hyper', None)
        refreshType = data.pop('refreshType', 'overwrite')
        return cls(path_to_hyper=path_to_hyper, refreshType=refreshType, **data)