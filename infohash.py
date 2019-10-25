from hashlib import sha1
from bencoder import bencode, bdecode


INFO = b'info'
SOURCE = b'source'


def _parse_torrent(filename):
    with open(filename, 'rb') as f:
        torrent = bdecode(f.read())
    info = torrent[INFO]
    return torrent, info


def infohash(filename):
    '''Read infohash from the torrent file'''
    torrent, info = _parse_torrent(filename)
    return sha1(bencode(info)).hexdigest()


def infohash_alt(filename, source=None):
    '''Calculate infohash for the same torrent with different source tag'''
    torrent, info = _parse_torrent(filename)
    if source is None:  # delete source tag
        if SOURCE in info:
            del info[SOURCE]
    else:
        info[SOURCE] = source
    return sha1(bencode(info)).hexdigest()


