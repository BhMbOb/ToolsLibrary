import os
import abc
from abc import ABC

import tools_library.utilities.pathing as pathutils

import asset_library


class _Asset(ABC):
    """Base class for all AssetLibrary Asset Types"""
    def __init__(self, real_path):

        # the asset library relative path to this asset
        self.path = real_path.lower()

        # dict containing extra user defined metadata
        self.metadata = {}

        self.paths = lambda: None
        setattr(self.paths, "unreal", self.unreal_path)

    @property
    def name(self):
        return os.path.basename(self.real_path).split(".")[0]

    @abc.abstractproperty
    def unreal_path(self):
        """Returns the unreal relative path for this asset"""
        pass

    @property
    def asset_library_path(self):
        """Returns the asset library relative path for this asset"""
        return asset_library.paths.map_path(self.path)

    @property
    def real_path(self):
        """Returns the real path to this asset on the hard drive"""
        return self.path

    @property
    def has_metadata(self):
        """Returns true if the asset has a valid .meta file associated with it"""
        return os.path.isfile(pathutils.set_path_file_type(self.real_path, "meta"))

    @abc.abstractmethod
    def import_to_unreal(self):
        """Abstract function for importing the current asset into unreal"""
        pass

    def add_metadata(self, key, val):
        """Adds a metadata key/value to the current Asset object
        NOTE: This doesn't add data to the final .meta file, only to the current instance of this python object"""
        self.metadata[key] = val

    def get_metadata(self, key):
        """Search the current Python Object for metadata and return if found"""
        if(key in self.metadata):
            return self.metadata[key]
        return None

