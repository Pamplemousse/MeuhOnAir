import re

class Playlist():
    @staticmethod
    def clean(playlist):
        return list(
            filter(
                lambda x: not re.compile("Jingle").search(x.text),
                filter(
                    lambda x: not re.compile("\.\.\.").search(x.text),
                    playlist
                )
            )
        )
