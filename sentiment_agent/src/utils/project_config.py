import os
import yaml

from dotenv import load_dotenv; load_dotenv()

from src.utils.logger_config import log
from src.utils.exception_config import ProjectException

class ProjectConfig:
    def __init__(self):
        self._env = os.getenv('ENVIRONMENT', 'dev')
        self._config_dir = os.getenv('CONFIG_DIR')
        self._config = {}

        try:
            config_file = f'{self._config_dir}\config.{self._env}.yaml'
            with open(config_file, 'r') as file:
                self.config = yaml.safe_load(file)
            log.info("Load project configuration.")
        except Exception as e:
            ProjectException(
                e,
                context={
                    "operation": "log project config.",
                    "message": "Error while loading project config."
                }
            )

    @property
    def get_config(self) -> dict:
        return self._config


config = ProjectConfig()
project_config = config.get_config
print(f"type: {type(project_config)}, project_config: {project_config}")


