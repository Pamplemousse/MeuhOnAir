import re


def clean(playlist):
    return list(
        filter(
            __is_legit_track_title,
            playlist
        )
    )


def format(playlist):
    return list(
        map(
            __track_element_to_dict,
            playlist
        )
    )


def __is_legit_track_title(element):
    not_upcoming = not re.compile("^(\.\.\.)").search(element.text)
    not_jingle = not re.compile("\(Jingle\)").search(element.text)

    return not_upcoming and not_jingle


def __track_element_to_dict(element):
    content = element.contents
    return {
        "time": content[0],
        "artist_album": content[2],
        "track_title": content[3].text
    }
