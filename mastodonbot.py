from mastodon import Mastodon
import time

#input secret token for bot
mastodon = Mastodon(
    access_token = 'secret token',
    api_base_url = 'https://botsin.space/'
)

#input the output file for mastodon to upload
media_file = 'output file'
media_id = mastodon.media_post(media_file, description='Out of Context Pete and Pete Clip')
try:
    mastodon.status_post('This is my video clip!', media_ids=[media_id])

#time for mastodon to catch up

except:
    print("30s delay")
    time.sleep(30)
    mastodon.status_post('This is my video clip!', media_ids=[media_id])

#toot successful!

finally:
    print("Toot posted successfully!")