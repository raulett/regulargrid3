from qgis.core import QgsProject


def get_vector_layers(layer_class_type, field_names=None):
    layers_list = []
    qgs_project = QgsProject.instance()
    for layer in qgs_project.mapLayers().values():
        try:
            is_visible = qgs_project.layerTreeRoot().findLayer(layer.id()).isVisible()
        except:
            is_visible = False
        if isinstance(layer, layer_class_type) and (field_names is None) and is_visible:
            layers_list.append(layer)
    layers_list = sorted(layers_list, key=lambda layer: layer.name().lower())
    return layers_list
