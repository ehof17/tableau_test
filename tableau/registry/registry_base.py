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
    def generate_dataframe(self, *args, **kwargs):
        """
        Iterate over all documents in the document storage system
        and add/update/delete documents as needed.
        """
        raise NotImplementedError()

    def generate_partial_dataframe(self, *args, **kwargs):
        """
        Assemble and return the schema (map of field names to data types)
        """
        raise NotImplementedError()
    
    def refresh_hyper_file(self):
        """
        Refresh the data in the document storage system.
        """
        df = self.generate_dataframe()
        print("Converting to hyper_file")
        print("Calling tableau server manager to refresh")
        print("Completed refresh")

