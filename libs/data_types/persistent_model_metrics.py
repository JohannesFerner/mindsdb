from libs.data_types.persistent_object import PersistentObject

class PersistentModelMetrics(PersistentObject):

    _entity_name = 'model_metrics'
    _pkey = ['model_name', 'submodel_name']

    def setup(self):

        self.model_name = None
        self.submodel_name = None
        self.status = None
        self.r_squared = None
        self.confusion_matrix = None
        self.error_msg = None

