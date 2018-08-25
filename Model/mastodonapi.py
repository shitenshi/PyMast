from mastodon import Mastodon, StreamListener
import yaml

Mastodon.create_app(
        'otome',
        api_base_url = 'https://mstdn.maud.io',
        to_file='c_token.secret'
        )
with open('p.yaml') as passfile:
    info = yaml.load(passfile)
mstdn = Mastodon(
        client_id = 'c_token.secret',
        api_base_url = 'https://mstdn.maud.io')
mstdn.log_in(username = info['address'],
        password = info['password'],
        scopes=['read', 'write'],
        to_file ='access_token.secret'
        )
mstdn = Mastodon(
        access_token = 'access_token.secret',
        api_base_url = 'https://mstdn.maud.io'
        )

class MstdnStreamListener(StreamListener):
    def on_update(self, status):
        print(status['content'])
mstdn.stream_user(MstdnStreamListener())


