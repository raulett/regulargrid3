from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer


def get_layers_list(layer_class_type, vector_layer_type=None, field_names=None, visible_only=True):
    layers_list = []
    qgs_project = QgsProject.instance()
    for layer in qgs_project.mapLayers().values():
        if visible_only:
            try:
                visible = qgs_project.layerTreeRoot().findLayer(layer.id()).isVisible()
            except:
                visible = False
        else:
            visible = True
        if visible:
            if isinstance(layer, layer_class_type):
                if isinstance(layer, QgsRasterLayer):
                    layers_list.append(layer)
                if isinstance(layer, QgsVectorLayer):

                    if layer.geometryType() == vector_layer_type:
                        if field_names is None:
                            layers_list.append(layer)
                        else:
                            attr_name_list = list(layer.attributeAliases())
                            field_names_len = len(field_names)
                            fieldnames_equality_counter = 0
                            for field_name in field_names:
                                if field_name in attr_name_list:
                                    fieldnames_equality_counter += 1
                            if fieldnames_equality_counter == field_names_len:
                                layers_list.append(layer)

    layers_list = sorted(layers_list, key=lambda layer_member: layer_member.name().lower())
    return layers_list
