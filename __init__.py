#
import os, shutil
import folder_paths

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = os.path.dirname(folder_paths.__file__)
from .cd_tuner import CDTuner
from .negpip import Negpip

NODE_CLASS_MAPPINGS = {
    "CDTuner": CDTuner,
    "Negapip": Negpip,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CDTuner": "Apply CDTuner",
    "Negapip": "Apply Negapip",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
