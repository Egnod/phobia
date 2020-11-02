from sitri import Sitri
from sitri.contrib.system import SystemConfigProvider
from sitri.contrib.yaml import YamlConfigProvider
from sitri.strategy.index_priority import IndexPriorityStrategy

from phobia import __project__

configurator = Sitri(
    IndexPriorityStrategy(
        SystemConfigProvider(prefix=__project__), YamlConfigProvider(default_separator="_", yaml_path="./config.yaml")
    )
)
