from datamodels import HyperFileWrapper
class TableauServerManager:
    """
    Interacts with Tableau Server to manage data source refreshes.
    """
    def refresh_hyper_file(self, hfw: HyperFileWrapper):
        match(hfw.refreshType):
            case 'append':
                print("[TableauServerManager] - Appending")
            case 'edit' | 'overwrite': 
                print("[TableauServerManager] - Editing or Overwriting")
            case _:
                raise ValueError(f"Unknown refresh type: {hfw.refreshType}")
        
        hfw.refreshType
        
    