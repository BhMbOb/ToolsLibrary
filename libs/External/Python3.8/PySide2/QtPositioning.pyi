# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtPositioning, except for defaults which are replaced by "...".
"""

# Module PySide2.QtPositioning
import PySide2
try:
    import typing
except ImportError:
    from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtPositioning


class QGeoAddress(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoAddress): ...

    @staticmethod
    def __copy__(): ...
    def city(self) -> str: ...
    def clear(self): ...
    def country(self) -> str: ...
    def countryCode(self) -> str: ...
    def county(self) -> str: ...
    def district(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def isTextGenerated(self) -> bool: ...
    def postalCode(self) -> str: ...
    def setCity(self, city:str): ...
    def setCountry(self, country:str): ...
    def setCountryCode(self, countryCode:str): ...
    def setCounty(self, county:str): ...
    def setDistrict(self, district:str): ...
    def setPostalCode(self, postalCode:str): ...
    def setState(self, state:str): ...
    def setStreet(self, street:str): ...
    def setText(self, text:str): ...
    def state(self) -> str: ...
    def street(self) -> str: ...
    def text(self) -> str: ...


class QGeoAreaMonitorInfo(Shiboken.Object):

    @typing.overload
    def __init__(self, name:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoAreaMonitorInfo): ...

    @staticmethod
    def __copy__(): ...
    def __lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def area(self) -> PySide2.QtPositioning.QGeoShape: ...
    def expiration(self) -> PySide2.QtCore.QDateTime: ...
    def identifier(self) -> str: ...
    def isPersistent(self) -> bool: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def notificationParameters(self) -> typing.Dict: ...
    def setArea(self, newShape:PySide2.QtPositioning.QGeoShape): ...
    def setExpiration(self, expiry:PySide2.QtCore.QDateTime): ...
    def setName(self, name:str): ...
    def setNotificationParameters(self, parameters:typing.Dict): ...
    def setPersistent(self, isPersistent:bool): ...


class QGeoAreaMonitorSource(PySide2.QtCore.QObject):
    AnyAreaMonitorFeature    : QGeoAreaMonitorSource = ... # -0x1
    AccessError              : QGeoAreaMonitorSource = ... # 0x0
    InsufficientPositionInfo : QGeoAreaMonitorSource = ... # 0x1
    PersistentAreaMonitorFeature: QGeoAreaMonitorSource = ... # 0x1
    UnknownSourceError       : QGeoAreaMonitorSource = ... # 0x2
    NoError                  : QGeoAreaMonitorSource = ... # 0x3

    class AreaMonitorFeature(object):
        AnyAreaMonitorFeature    : QGeoAreaMonitorSource.AreaMonitorFeature = ... # -0x1
        PersistentAreaMonitorFeature: QGeoAreaMonitorSource.AreaMonitorFeature = ... # 0x1

    class AreaMonitorFeatures(object): ...

    class Error(object):
        AccessError              : QGeoAreaMonitorSource.Error = ... # 0x0
        InsufficientPositionInfo : QGeoAreaMonitorSource.Error = ... # 0x1
        UnknownSourceError       : QGeoAreaMonitorSource.Error = ... # 0x2
        NoError                  : QGeoAreaMonitorSource.Error = ... # 0x3

    def __init__(self, parent:PySide2.QtCore.QObject): ...

    @typing.overload
    def activeMonitors(self) -> typing.List: ...
    @typing.overload
    def activeMonitors(self, lookupArea:PySide2.QtPositioning.QGeoShape) -> typing.List: ...
    @staticmethod
    def availableSources() -> typing.List: ...
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.Error: ...
    def positionInfoSource(self) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def requestUpdate(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo, signal:bytes) -> bool: ...
    def setPositionInfoSource(self, source:PySide2.QtPositioning.QGeoPositionInfoSource): ...
    def sourceName(self) -> str: ...
    def startMonitoring(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool: ...
    def stopMonitoring(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool: ...
    def supportedAreaMonitorFeatures(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeatures: ...


class QGeoCircle(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, center:PySide2.QtPositioning.QGeoCoordinate, radius:float=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoCircle): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...

    @staticmethod
    def __copy__(): ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def extendCircle(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def radius(self) -> float: ...
    def setCenter(self, center:PySide2.QtPositioning.QGeoCoordinate): ...
    def setRadius(self, radius:float): ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoCircle: ...


class QGeoCoordinate(Shiboken.Object):
    Degrees                  : QGeoCoordinate = ... # 0x0
    InvalidCoordinate        : QGeoCoordinate = ... # 0x0
    Coordinate2D             : QGeoCoordinate = ... # 0x1
    DegreesWithHemisphere    : QGeoCoordinate = ... # 0x1
    Coordinate3D             : QGeoCoordinate = ... # 0x2
    DegreesMinutes           : QGeoCoordinate = ... # 0x2
    DegreesMinutesWithHemisphere: QGeoCoordinate = ... # 0x3
    DegreesMinutesSeconds    : QGeoCoordinate = ... # 0x4
    DegreesMinutesSecondsWithHemisphere: QGeoCoordinate = ... # 0x5

    class CoordinateFormat(object):
        Degrees                  : QGeoCoordinate.CoordinateFormat = ... # 0x0
        DegreesWithHemisphere    : QGeoCoordinate.CoordinateFormat = ... # 0x1
        DegreesMinutes           : QGeoCoordinate.CoordinateFormat = ... # 0x2
        DegreesMinutesWithHemisphere: QGeoCoordinate.CoordinateFormat = ... # 0x3
        DegreesMinutesSeconds    : QGeoCoordinate.CoordinateFormat = ... # 0x4
        DegreesMinutesSecondsWithHemisphere: QGeoCoordinate.CoordinateFormat = ... # 0x5

    class CoordinateType(object):
        InvalidCoordinate        : QGeoCoordinate.CoordinateType = ... # 0x0
        Coordinate2D             : QGeoCoordinate.CoordinateType = ... # 0x1
        Coordinate3D             : QGeoCoordinate.CoordinateType = ... # 0x2

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, latitude:float, longitude:float): ...
    @typing.overload
    def __init__(self, latitude:float, longitude:float, altitude:float): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoCoordinate): ...

    @staticmethod
    def __copy__(): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def altitude(self) -> float: ...
    def atDistanceAndAzimuth(self, distance:float, azimuth:float, distanceUp:float=...) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def azimuthTo(self, other:PySide2.QtPositioning.QGeoCoordinate) -> float: ...
    def distanceTo(self, other:PySide2.QtPositioning.QGeoCoordinate) -> float: ...
    def isValid(self) -> bool: ...
    def latitude(self) -> float: ...
    def longitude(self) -> float: ...
    def setAltitude(self, altitude:float): ...
    def setLatitude(self, latitude:float): ...
    def setLongitude(self, longitude:float): ...
    def toString(self, format:PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat=...) -> str: ...
    def type(self) -> PySide2.QtPositioning.QGeoCoordinate.CoordinateType: ...


class QGeoLocation(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoLocation): ...

    @staticmethod
    def __copy__(): ...
    def address(self) -> PySide2.QtPositioning.QGeoAddress: ...
    def boundingBox(self) -> PySide2.QtPositioning.QGeoRectangle: ...
    def coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def extendedAttributes(self) -> typing.Dict: ...
    def isEmpty(self) -> bool: ...
    def setAddress(self, address:PySide2.QtPositioning.QGeoAddress): ...
    def setBoundingBox(self, box:PySide2.QtPositioning.QGeoRectangle): ...
    def setCoordinate(self, position:PySide2.QtPositioning.QGeoCoordinate): ...
    def setExtendedAttributes(self, data:typing.Dict): ...


class QGeoPath(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPath): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, path:typing.Sequence, width:float=...): ...

    @staticmethod
    def __copy__(): ...
    def addCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def clearPath(self): ...
    def containsCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index:int) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def insertCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def length(self, indexFrom:int=..., indexTo:int=...) -> float: ...
    def path(self) -> typing.List: ...
    @typing.overload
    def removeCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def removeCoordinate(self, index:int): ...
    def replaceCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setPath(self, path:typing.Sequence): ...
    def setVariantPath(self, path:typing.Sequence): ...
    def setWidth(self, width:float): ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoPath: ...
    def variantPath(self) -> typing.List: ...
    def width(self) -> float: ...


class QGeoPolygon(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPolygon): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, path:typing.Sequence): ...

    @staticmethod
    def __copy__(): ...
    def addCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def addHole(self, holePath:typing.Sequence): ...
    @typing.overload
    def addHole(self, holePath:typing.Any): ...
    def containsCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index:int) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def hole(self, index:int) -> typing.List: ...
    def holePath(self, index:int) -> typing.List: ...
    def holesCount(self) -> int: ...
    def insertCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def length(self, indexFrom:int=..., indexTo:int=...) -> float: ...
    def path(self) -> typing.List: ...
    def perimeter(self) -> typing.List: ...
    @typing.overload
    def removeCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def removeCoordinate(self, index:int): ...
    def removeHole(self, index:int): ...
    def replaceCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setPath(self, path:typing.Sequence): ...
    def setPerimeter(self, path:typing.Sequence): ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoPolygon: ...


class QGeoPositionInfo(Shiboken.Object):
    Direction                : QGeoPositionInfo = ... # 0x0
    GroundSpeed              : QGeoPositionInfo = ... # 0x1
    VerticalSpeed            : QGeoPositionInfo = ... # 0x2
    MagneticVariation        : QGeoPositionInfo = ... # 0x3
    HorizontalAccuracy       : QGeoPositionInfo = ... # 0x4
    VerticalAccuracy         : QGeoPositionInfo = ... # 0x5

    class Attribute(object):
        Direction                : QGeoPositionInfo.Attribute = ... # 0x0
        GroundSpeed              : QGeoPositionInfo.Attribute = ... # 0x1
        VerticalSpeed            : QGeoPositionInfo.Attribute = ... # 0x2
        MagneticVariation        : QGeoPositionInfo.Attribute = ... # 0x3
        HorizontalAccuracy       : QGeoPositionInfo.Attribute = ... # 0x4
        VerticalAccuracy         : QGeoPositionInfo.Attribute = ... # 0x5

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, coordinate:PySide2.QtPositioning.QGeoCoordinate, updateTime:PySide2.QtCore.QDateTime): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPositionInfo): ...

    @staticmethod
    def __copy__(): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def attribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> float: ...
    def coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def hasAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> bool: ...
    def isValid(self) -> bool: ...
    def removeAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute): ...
    def setAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute, value:float): ...
    def setCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setTimestamp(self, timestamp:PySide2.QtCore.QDateTime): ...
    def timestamp(self) -> PySide2.QtCore.QDateTime: ...


class QGeoPositionInfoSource(PySide2.QtCore.QObject):
    NonSatellitePositioningMethods: QGeoPositionInfoSource = ... # -0x100
    AllPositioningMethods    : QGeoPositionInfoSource = ... # -0x1
    AccessError              : QGeoPositionInfoSource = ... # 0x0
    NoPositioningMethods     : QGeoPositionInfoSource = ... # 0x0
    ClosedError              : QGeoPositionInfoSource = ... # 0x1
    UnknownSourceError       : QGeoPositionInfoSource = ... # 0x2
    NoError                  : QGeoPositionInfoSource = ... # 0x3
    SatellitePositioningMethods: QGeoPositionInfoSource = ... # 0xff

    class Error(object):
        AccessError              : QGeoPositionInfoSource.Error = ... # 0x0
        ClosedError              : QGeoPositionInfoSource.Error = ... # 0x1
        UnknownSourceError       : QGeoPositionInfoSource.Error = ... # 0x2
        NoError                  : QGeoPositionInfoSource.Error = ... # 0x3

    class PositioningMethod(object):
        NonSatellitePositioningMethods: QGeoPositionInfoSource.PositioningMethod = ... # -0x100
        AllPositioningMethods    : QGeoPositionInfoSource.PositioningMethod = ... # -0x1
        NoPositioningMethods     : QGeoPositionInfoSource.PositioningMethod = ... # 0x0
        SatellitePositioningMethods: QGeoPositionInfoSource.PositioningMethod = ... # 0xff

    class PositioningMethods(object): ...

    def __init__(self, parent:PySide2.QtCore.QObject): ...

    @staticmethod
    def availableSources() -> typing.List: ...
    def backendProperty(self, name:str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parameters:typing.Dict, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName:str, parameters:typing.Dict, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly:bool=...) -> PySide2.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    def preferredPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def requestUpdate(self, timeout:int=...): ...
    def setBackendProperty(self, name:str, value:typing.Any) -> bool: ...
    def setPreferredPositioningMethods(self, methods:PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods): ...
    def setUpdateInterval(self, msec:int): ...
    def sourceName(self) -> str: ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def updateInterval(self) -> int: ...


class QGeoPositionInfoSourceFactory(Shiboken.Object):

    def __init__(self): ...

    def areaMonitor(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    def positionInfoSource(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def satelliteInfoSource(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...


class QGeoRectangle(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, center:PySide2.QtPositioning.QGeoCoordinate, degreesWidth:float, degreesHeight:float): ...
    @typing.overload
    def __init__(self, coordinates:typing.Sequence): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoRectangle): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, topLeft:PySide2.QtPositioning.QGeoCoordinate, bottomRight:PySide2.QtPositioning.QGeoCoordinate): ...

    @staticmethod
    def __copy__(): ...
    def __ior__(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def __or__(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def bottomLeft(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def bottomRight(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    @typing.overload
    def contains(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    @typing.overload
    def contains(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> bool: ...
    def extendRectangle(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def height(self) -> float: ...
    def intersects(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> bool: ...
    def setBottomLeft(self, bottomLeft:PySide2.QtPositioning.QGeoCoordinate): ...
    def setBottomRight(self, bottomRight:PySide2.QtPositioning.QGeoCoordinate): ...
    def setCenter(self, center:PySide2.QtPositioning.QGeoCoordinate): ...
    def setHeight(self, degreesHeight:float): ...
    def setTopLeft(self, topLeft:PySide2.QtPositioning.QGeoCoordinate): ...
    def setTopRight(self, topRight:PySide2.QtPositioning.QGeoCoordinate): ...
    def setWidth(self, degreesWidth:float): ...
    def toString(self) -> str: ...
    def topLeft(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def topRight(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoRectangle: ...
    def united(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def width(self) -> float: ...


class QGeoSatelliteInfo(Shiboken.Object):
    Elevation                : QGeoSatelliteInfo = ... # 0x0
    Undefined                : QGeoSatelliteInfo = ... # 0x0
    Azimuth                  : QGeoSatelliteInfo = ... # 0x1
    GPS                      : QGeoSatelliteInfo = ... # 0x1
    GLONASS                  : QGeoSatelliteInfo = ... # 0x2

    class Attribute(object):
        Elevation                : QGeoSatelliteInfo.Attribute = ... # 0x0
        Azimuth                  : QGeoSatelliteInfo.Attribute = ... # 0x1

    class SatelliteSystem(object):
        Undefined                : QGeoSatelliteInfo.SatelliteSystem = ... # 0x0
        GPS                      : QGeoSatelliteInfo.SatelliteSystem = ... # 0x1
        GLONASS                  : QGeoSatelliteInfo.SatelliteSystem = ... # 0x2

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoSatelliteInfo): ...

    @staticmethod
    def __copy__(): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def attribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> float: ...
    def hasAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> bool: ...
    def removeAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute): ...
    def satelliteIdentifier(self) -> int: ...
    def satelliteSystem(self) -> PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem: ...
    def setAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute, value:float): ...
    def setSatelliteIdentifier(self, satId:int): ...
    def setSatelliteSystem(self, system:PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem): ...
    def setSignalStrength(self, signalStrength:int): ...
    def signalStrength(self) -> int: ...


class QGeoSatelliteInfoSource(PySide2.QtCore.QObject):
    UnknownSourceError       : QGeoSatelliteInfoSource = ... # -0x1
    AccessError              : QGeoSatelliteInfoSource = ... # 0x0
    ClosedError              : QGeoSatelliteInfoSource = ... # 0x1
    NoError                  : QGeoSatelliteInfoSource = ... # 0x2

    class Error(object):
        UnknownSourceError       : QGeoSatelliteInfoSource.Error = ... # -0x1
        AccessError              : QGeoSatelliteInfoSource.Error = ... # 0x0
        ClosedError              : QGeoSatelliteInfoSource.Error = ... # 0x1
        NoError                  : QGeoSatelliteInfoSource.Error = ... # 0x2

    def __init__(self, parent:PySide2.QtCore.QObject): ...

    @staticmethod
    def availableSources() -> typing.List: ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parameters:typing.Dict, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName:str, parameters:typing.Dict, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoSatelliteInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def requestUpdate(self, timeout:int=...): ...
    def setUpdateInterval(self, msec:int): ...
    def sourceName(self) -> str: ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def updateInterval(self) -> int: ...


class QGeoShape(Shiboken.Object):
    UnknownType              : QGeoShape = ... # 0x0
    RectangleType            : QGeoShape = ... # 0x1
    CircleType               : QGeoShape = ... # 0x2
    PathType                 : QGeoShape = ... # 0x3
    PolygonType              : QGeoShape = ... # 0x4

    class ShapeType(object):
        UnknownType              : QGeoShape.ShapeType = ... # 0x0
        RectangleType            : QGeoShape.ShapeType = ... # 0x1
        CircleType               : QGeoShape.ShapeType = ... # 0x2
        PathType                 : QGeoShape.ShapeType = ... # 0x3
        PolygonType              : QGeoShape.ShapeType = ... # 0x4

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...

    @staticmethod
    def __copy__(): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def boundingGeoRectangle(self) -> PySide2.QtPositioning.QGeoRectangle: ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def contains(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def extendShape(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def toString(self) -> str: ...
    def type(self) -> PySide2.QtPositioning.QGeoShape.ShapeType: ...


class QNmeaPositionInfoSource(PySide2.QtPositioning.QGeoPositionInfoSource):
    RealTimeMode             : QNmeaPositionInfoSource = ... # 0x1
    SimulationMode           : QNmeaPositionInfoSource = ... # 0x2

    class UpdateMode(object):
        RealTimeMode             : QNmeaPositionInfoSource.UpdateMode = ... # 0x1
        SimulationMode           : QNmeaPositionInfoSource.UpdateMode = ... # 0x2

    def __init__(self, updateMode:PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def device(self) -> PySide2.QtCore.QIODevice: ...
    def error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly:bool=...) -> PySide2.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    def parsePosInfoFromNmeaData(self, data:bytes, size:int, posInfo:PySide2.QtPositioning.QGeoPositionInfo) -> typing.Tuple: ...
    def requestUpdate(self, timeout:int=...): ...
    def setDevice(self, source:PySide2.QtCore.QIODevice): ...
    def setUpdateInterval(self, msec:int): ...
    def setUserEquivalentRangeError(self, uere:float): ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def updateMode(self) -> PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode: ...
    def userEquivalentRangeError(self) -> float: ...

# eof
