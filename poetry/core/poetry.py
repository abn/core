from __future__ import absolute_import
from __future__ import unicode_literals

from typing import TYPE_CHECKING
from typing import Any
from typing import Optional

from poetry.core.pyproject import PyProjectTOML
from poetry.core.utils._compat import Path  # noqa


if TYPE_CHECKING:
    from poetry.core.lock.locker import Locker
    from poetry.core.packages import ProjectPackage  # noqa
    from poetry.core.pyproject.toml import PyProjectTOMLFile  # noqa


class Poetry(object):
    def __init__(
        self, file, local_config, package, locker=None
    ):  # type: (Path, dict, "ProjectPackage", Optional["Locker"]) -> None
        self._pyproject = PyProjectTOML(file)
        self._package = package
        self._local_config = local_config
        self._locker = locker

    @property
    def pyproject(self):  # type: () -> PyProjectTOML
        return self._pyproject

    @property
    def file(self):  # type: () -> "PyProjectTOMLFile"
        return self._pyproject.file

    @property
    def package(self):  # type: () -> "ProjectPackage"
        return self._package

    @property
    def local_config(self):  # type: () -> dict
        return self._local_config

    @property
    def locker(self):  # type: () -> Optional["Locker"]
        if self._locker is None:
            from poetry.core.lock.locker import Locker

            self._locker = Locker(
                self.pyproject.file / "poetry.lock", self.local_config
            )
        return self._locker

    def get_project_config(self, config, default=None):  # type: (str, Any) -> Any
        return self._local_config.get("config", {}).get(config, default)
