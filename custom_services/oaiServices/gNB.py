from typing import List, Dict

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode

class gNB(ConfigService):
    name: str = "gNB"
    group: str = "OpenAirInterface"
    directories: List[str] = []
    files: List[str] = ["gNB_proxy.conf"]
    executables: List[str] = ["/home/jrmurphy/dev/openairinterface5g/cmake_targets/ran_build/build/nr-softmodem"] # TODO: Don't hardcode OAI executables
    dependencies: List[str] = ["nr-softmodem -O gNB_proxy.conf"]
    startup: List[str] = []
    validate: List[str] = []
    shutdown: List[str] = []
    validation_mode: ConfigServiceMode = ConfigServiceMode.BLOCKING
    default_configs: List[Configuration] = []
    modes: Dict[str, Dict[str, str]] = {}
