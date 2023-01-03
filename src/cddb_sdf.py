# TODO

"""
    cddb_sdf.py: constants defining the CDDB schema used by EAC
	Copyright (C) 2023  onioneffect
	This file is part of EAC-Autofill.
	EAC-Autofill is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	EAC-Autofill is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	You should have received a copy of the GNU General Public License
	along with EAC-Autofill.  If not, see <https://www.gnu.org/licenses/>.
"""

class Eac_cddb_schema:
    cddbid : int
    cdplayerini : int
    artist : str
    title : str
    musictype : int
    numtracks : int
    year : int
    revision : int
    mp3type : int
    leadout : int
    track = None
    startpos : str
    extdisc : str
    exttrack : str
    mp3v2type : str
    crcs : str
    cdcode = None
    picture = "0x0" # IF WRITING A SQL PLAINTEXT DO NOT WRAP BETWEEN QUOTES
    firsttracknumber : int = 1
    composer : str
    conductor : str
    orchestra : str
    publisher : str
    albuminterpreter : str
    trackcomposer : str
    cdnumber : int = 1
    numtotalcds : int = 1
    comment : str
    trackartist : str
    tracktitle : str
    lyrics : str
    coverimageurl : str
