from google.appengine.ext import ndb

class Work(ndb.Model):
    title = ndb.StringProperty()
    subtitle = ndb.StringProperty()
    release_date = ndb.DateProperty()
    duration = ndb.IntegerProperty()    # seconds
    festivals = ndb.StringProperty()
    type = ndb.StringProperty()
    director = ndb.StringProperty()
    assistant_director = ndb.StringProperty()
    editor = ndb.StringProperty()
    cinematographer = ndb.StringProperty()
    camera_assistant = ndb.StringProperty()
    sound_recorder = ndb.StringProperty()
    productor = ndb.StringProperty()
    link = ndb.StringProperty()
    source = ndb.StringProperty()
