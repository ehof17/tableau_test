from .registry_base import BaseRegisteredClass
class Neo4jDataManager(BaseRegisteredClass):
    @classmethod
    def generate_dataframe(cls, *args, **kwargs):
        print("Neo4jDataManager Generate Dataframe")
      