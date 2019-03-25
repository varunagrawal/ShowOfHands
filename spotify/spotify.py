"""
https://developer.spotify.com/discover/
    https://developer.spotify.com/documentation/general/guides/authorization-guide/
https://developer.spotify.com/documentation/general/guides/scopes/
https://developer.spotify.com/documentation/web-api/reference/player/start-a-users-playback/
https://developer.spotify.com/documentation/web-playback-sdk/quick-start/#
https://developer.spotify.com/documentation/web-api/guides/using-connect-web-api/#viewing-active-device-list
"""

import spotipy
import spotipy.util as util
import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("search")
    args = parser.parse_args()
    return args


def get_credentials(file="client_cred.json"):
    credentials = json.load(open("client_cred.json"))
    return credentials["username"], credentials["scopes"], credentials["client_id"], credentials["client_secret"], credentials["redirect_uri"]


def main():
    username, scopes, client_id, client_secret, redirect_uri = get_credentials()

    track_uris = []

    token = util.prompt_for_user_token(username, scopes,
                                       client_id=client_id, client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    spotify = spotipy.Spotify(auth=token)

    args = parse_args()
    results = spotify.search(q=args.search)
    track_uris.extend(map(lambda x: x['uri'], results['tracks']['items']))
    print(track_uris)
    # print(json.dumps(results['tracks']['items'][0]['uri']))

    #TODO fork spotipy since the PyPI version is outdated
    devices = spotify.devices()
    device_id = devices['devices'][0]['id']
    spotify.start_playback(device_id=device_id, uris=track_uris)

main()
