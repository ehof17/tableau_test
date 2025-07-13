from managers import TableauServerManager
class RegistryBase(type):
    REGISTRY = {}
    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls
    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)
    
    

class BaseRegisteredClass(metaclass=RegistryBase):
    def __init__(self):
        self.servermanager = TableauServerManager()
        

    def refresh_hyper_file(self, *args, **kwargs):
        """
        Refresh a hyper file
        """
        hf = self.generate_dataframe(*args, **kwargs)
        self.servermanager.refresh_hyper_file(hf)
        print(hf)

