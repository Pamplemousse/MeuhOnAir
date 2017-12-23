from bs4 import BeautifulSoup
from playlist import Playlist

import unittest


class TestPlaylist(unittest.TestCase):
    def test_clean_method_remove_jingle(self):
        cleaned_playlist = Playlist.clean(self.results)
        jingle = BeautifulSoup(
            "<td class='Cell'>21:01:05<br><br/>Astrid RM.com (Jingle)</td>",
            "html.parser"
        )

        self.assertTrue(str(jingle) != str(cleaned_playlist[2]))


    def test_clean_method_remove_upcoming_title(self):
        cleaned_playlist = Playlist.clean(self.results)
        upcoming_title = BeautifulSoup(
            "<td class='Cell'>...<br>El Michels Affair - Return to the 37th Chamber<br/>Verbal Intercourse (R&B)</td>",
            "html.parser"
        )

        self.assertTrue(str(upcoming_title) != str(cleaned_playlist[0]))


    def test_clean_method_keeps_titles_containing_ellipsis(self):
        cleaned_playlist = Playlist.clean(self.results)
        ellipsis_title = BeautifulSoup(
            "<td class='Cell'>20:22:45<br>Fake title containing ...<br/>So fake</td>",
            "html.parser"
        )

        self.assertTrue(str(ellipsis_title) == str(cleaned_playlist[-1]))


    def test_clean_method_keeps_titles_containing_jingle(self):
        cleaned_playlist = Playlist.clean(self.results)
        jingle_title = BeautifulSoup(
            "<td class='Cell'>20:27:02<br>Fake title containing Jingle<br/>So fake</td>",
            "html.parser"
        )

        self.assertTrue(str(jingle_title) == str(cleaned_playlist[-2]))


    def test_clean_method_returns_rest_of_titles(self):
        cleaned_playlist = Playlist.clean(self.results)

        self.assertEqual(len(cleaned_playlist), 8)


    def test_format_method_returns_nicely_formatted_elements(self):
        formatted_playlist = Playlist.format(self.cleaned_results)
        expected_playlist = [
            { "time": "20:56:51", "artist_album": "P-Sol - Mixed Bag, Vol. 3", "track_title": "If You Let Me (Nu Disco;Re-Edits)" },
            { "time": "20:52:08", "artist_album": "Sinkane - Life & Livin' It", "track_title": "Favorite Song" },
            { "time": "20:47:02", "artist_album": "Ryo Kawasaki", "track_title": "Dreams For Radha" },
            { "time": "20:41:00", "artist_album": "4th Sign - Eloge De La Lenteur Part 2", "track_title": "02-No Trouble No Men (House)" },
            { "time": "20:35:25", "artist_album": "Free Radicals -  ", "track_title": "I Just Can't Turn It Loose (Je (House)" },
            { "time": "20:30:41", "artist_album": "DORSIA - Ghana", "track_title": "Ghana (HNNY remix) (Deep house)" },
            { "time": "20:27:02", "artist_album": "Fake title containing Jingle", "track_title": "So fake" },
            { "time": "20:22:45", "artist_album": "Fake title containing ...", "track_title": "So fake" },
        ]

        self.assertListEqual(expected_playlist, formatted_playlist)


    def setUp(self):
        self.results = BeautifulSoup("""
<!--<html>
<body class="TextCell2">
-->
<table border="0" cellpadding="3" cellspacing="0" style="border-collapse: collapse; width: 535px; border:0px;">
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>...<br>El Michels Affair - Return to the 37th Chamber<br/>Verbal Intercourse (R&B)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='TextCell'><B>21:01:07<br>DJ Prosper<br/>Prosper Show n5<BR><font style='font-size : 10px;'>temps restant: 6min 54s</font></B></td></tr>
<tr><td class='pochette'><img src='http://ilaster.radiomeuh.com/mediabox/imgtmb/1297_75.jpg'></td><td class='Cell'>21:01:05<br><br/>Astrid RM.com (Jingle)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:56:51<br>P-Sol - Mixed Bag, Vol. 3<br/>If You Let Me (Nu Disco;Re-Edits)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:52:08<br>Sinkane - Life & Livin' It<br/>Favorite Song</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:47:02<br>Ryo Kawasaki<br/>Dreams For Radha</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:41:00<br>4th Sign - Eloge De La Lenteur Part 2<br/>02-No Trouble No Men (House)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:35:25<br>Free Radicals -  <br/>I Just Can't Turn It Loose (Je (House)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:30:41<br>DORSIA - Ghana<br/>Ghana (HNNY remix) (Deep house)</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:27:02<br>Fake title containing Jingle<br/>So fake</td></tr>
<tr><td class='pochette'>&nbsp;</td><td class='Cell'>20:22:45<br>Fake title containing ...<br/>So fake</td></tr>
</table>
<!--</body>
</html>
-->"""
            , "html.parser"
        ).select("td.Cell")

        self.cleaned_results = BeautifulSoup(
"""
<td class='Cell'>20:56:51<br>P-Sol - Mixed Bag, Vol. 3<br/>If You Let Me (Nu Disco;Re-Edits)</td>
<td class='Cell'>20:52:08<br>Sinkane - Life & Livin' It<br/>Favorite Song</td>
<td class='Cell'>20:47:02<br>Ryo Kawasaki<br/>Dreams For Radha</td>
<td class='Cell'>20:41:00<br>4th Sign - Eloge De La Lenteur Part 2<br/>02-No Trouble No Men (House)</td>
<td class='Cell'>20:35:25<br>Free Radicals -  <br/>I Just Can't Turn It Loose (Je (House)</td>
<td class='Cell'>20:30:41<br>DORSIA - Ghana<br/>Ghana (HNNY remix) (Deep house)</td>
<td class='Cell'>20:27:02<br>Fake title containing Jingle<br/>So fake</td>
<td class='Cell'>20:22:45<br>Fake title containing ...<br/>So fake</td>
"""
            , "html.parser"
        ).select("td.Cell")

if __name__ == '__main__':
    unittest.main()
