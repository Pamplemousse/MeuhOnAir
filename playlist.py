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
    def format(playlist):
        return list(
            map(
                Playlist.__track_element_to_dict,
                playlist
            )
        )


    @staticmethod
    def __is_legit_track_title(element):
        not_upcoming = not re.compile("^(\.\.\.)").search(element.text)
        not_jingle = not re.compile("\(Jingle\)").search(element.text)

        return not_upcoming and not_jingle


    @staticmethod
    def __track_element_to_dict(element):
        content = element.contents
        return {
            "time": content[0],
            "artist_album": content[2],
            "track_title": content[3].text
        }
