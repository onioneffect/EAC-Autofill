"""
    main.py: Entry point
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

import discogs_client
import cddb_sdf

def clean_leave():
    pass

def main():
    fp = open("token.txt", "r")
    token_s = fp.read()
    fp.close()

    d = discogs_client.Client('Autofill/0.1', user_token=token_s)
    artist = d.artist(2427937)
    print(artist)

    return

if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        clean_leave()
