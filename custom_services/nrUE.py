from typing import Dict, List

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode

class nrUE(ConfigService):
    name: str = "nrUE"
    group: str = "OpenAirInterface"
    directories: List[str] = []
    files: List[str] = ["nrUE_proxy.conf","start_ue.sh"]
    executables: List[str] = []
    dependencies: List[str] = []
    startup: List[str] = ["bash start_ue.sh"]
    validate: List[str] = []
    shutdown: List[str] = []
    validation_mode: ConfigServiceMode = ConfigServiceMode.NON_BLOCKING
    default_configs: List[Configuration] = []
    modes: Dict[str, Dict[str, str]] = {}
