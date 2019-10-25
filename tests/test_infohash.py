#!/usr/bin/env python3


import os.path
from unittest import TestCase

from infohash import infohash, infohash_alt



test_hashes = {
    # Bogus torrent file with source=ABC (https://github.com/qbittorrent/qBittorrent/issues/7965#issuecomment-348702492)
    '0001.torrent': 'd11a5d0debccb5ddbe97d3906090b5f3ae953460',

    # Debian netinstall torrent
    'debian-10.1.0-amd64-netinst.iso.torrent': '0f2a3adfe82e1c92b390cdcaaec3cdc0dd3ebfd7',

    # Same data with and without source tag
    'bogus-without-source.torrent': 'b31685bb4596ddb34e72ed5fb347f645b01f9e3c',
    'bogus-with-source.torrent': '90ff13ca09fc4f002b88e2cacaed6fa59b569e52',
}
without_source_tag = {
    'bogus-without-source.torrent': 'b31685bb4596ddb34e72ed5fb347f645b01f9e3c',
    'bogus-with-source.torrent': 'b31685bb4596ddb34e72ed5fb347f645b01f9e3c',
}



class TestInfoHash(TestCase):


    def data(self, name):
        return os.path.join('tests/data', name)


    def test_correct_value(self):
        for filename, correct_hash in test_hashes.items():
            filename = self.data(filename)
            with self.subTest(filename=filename, correct_hash=correct_hash):
                self.assertEqual(correct_hash, infohash(filename))


    def test_without_source(self):
        for filename, alt_hash in without_source_tag.items():
            filename = self.data(filename)
            with self.subTest(filename=filename, alt_hash=alt_hash):
                self.assertEqual(alt_hash, infohash_alt(filename, source=None))


    def test_replace_source(self):
        new_value = b'helloworld'
        clean = self.data('bogus-without-source.torrent')
        modified = self.data('bogus-with-source.torrent')
        self.assertEqual(infohash(modified), infohash_alt(clean, source=new_value))



if __name__ == '__main__':
    main()
