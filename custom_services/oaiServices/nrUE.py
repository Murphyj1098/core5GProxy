from typing import Dict, List

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode

class nrUE(ConfigService):
    name: str = "nrUE"
    group: str = "OpenAirInterface"
    directories: List[str] = []
    files: List[str] = ["nrUE_proxy.conf"]
    executables: List[str] = ["/home/jrmurphy/dev/openairinterface5g/cmake_targets/ran_build/build/nr-uesoftmodem"] # TODO: Don't hardcode OAI executables
    dependencies: List[str] = []
    startup: List[str] = ["nr-uesoftmodem -O nrUE_proxy.conf"]
    validate: List[str] = []
    shutdown: List[str] = []
    validation_mode: ConfigServiceMode = ConfigServiceMode.BLOCKING
    default_configs: List[Configuration] = []
    modes: Dict[str, Dict[str, str]] = {}
