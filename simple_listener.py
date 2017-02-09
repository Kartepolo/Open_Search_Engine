from tweepy import StreamListener, OAuthHandler, Stream
import time, json


class SimpleListener(StreamListener):
    def __init__(self, time_limit):
        StreamListener.__init__(self)

        self.start_time = time.time()
        self.limit = time_limit


    def on_data(self, raw_data):
        while time.time() - self.start_time < self.limit:
            try:
                print(json.loads(raw_data))
                return True
            except BaseException as e:
                print("Failed on fetching data due to", e)
                time.sleep(5)
                pass
    def on_status(self, status):
        print("on_status",status)

    def on_disconnect(self, notice):
        print("on_notice",notice)

    def on_error(self, status_code):
        print("on_error", status_code)

if __name__ == '__main__':
    listener = SimpleListener(180)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(locations = (42.268880, -71.772836))