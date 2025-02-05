# Python2 and Python 3 compatibility:
from __future__ import absolute_import, division, print_function, unicode_literals

from copy import deepcopy

from src.models.configuration_manager import ConfigurationManager
from src.models.otml_configuration import OtmlConfiguration


class OtmlConfigurationManager(ConfigurationManager):
    configurations: OtmlConfiguration

    def __init__(self, config_path):
        ConfigurationManager.__init__(
            self,
            config_type=OtmlConfiguration,
            config_loader=OtmlConfiguration.from_json,
            config_path=config_path,
        )
        self.initial_configurations = deepcopy(self.configurations)

    def __str__(self):
        return repr(self.configurations)
