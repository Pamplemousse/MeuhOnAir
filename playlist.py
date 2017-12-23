import re

class Playlist():
    @staticmethod
    def clean(playlist):
        return list(
            filter(
                Playlist.__is_legit_track_title,
                playlist
            )
        )


    @staticmethod
    def __is_legit_track_title(element):
        not_current = not re.compile("^(\.\.\.)").search(element.text)
        not_jingle = not re.compile("\(Jingle\)").search(element.text)

        return not_current and not_jingle
