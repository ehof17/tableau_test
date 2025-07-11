from .registry_base import BaseRegisteredClass
class GoogleAnalyticsDataManager(BaseRegisteredClass):
    @classmethod
    def generate_dataframe(cls, *args, **kwargs):
        print("GoogleAnalyticsManager Generate Dataframe")
      