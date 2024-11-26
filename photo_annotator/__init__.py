# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoAn
                                 A QGIS plugin
 Annotate TIFF files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-26
        copyright            : (C) 2024 by Matthew Wiecking
        email                : matthew@gentian.team
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeoAn class from file GeoAn.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .photo_annotator import GeoAn
    return GeoAn(iface)
