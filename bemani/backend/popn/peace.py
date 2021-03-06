# vim: set fileencoding=utf-8
from typing import Optional

from bemani.backend.popn.base import PopnMusicBase
from bemani.backend.popn.usaneko import PopnMusicUsaNeko
from bemani.common import VersionConstants


class PopnMusicPeace(PopnMusicBase):

    name = "Pop'n Music peace"
    version = VersionConstants.POPN_MUSIC_PEACE

    def previous_version(self) -> Optional[PopnMusicBase]:
        return PopnMusicUsaNeko(self.data, self.config, self.model)
