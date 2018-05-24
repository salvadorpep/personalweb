from google.appengine.ext import ndb

class Work(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    quote = ndb.StringProperty()
    quote_author = ndb.StringProperty()

    format = ndb.StringProperty()
    genre = ndb.StringProperty()
    duration = ndb.IntegerProperty()
    languages = ndb.StringProperty()
    country = ndb.StringProperty()
    year = ndb.IntegerProperty()
    release_festival = ndb.StringProperty()
    release_date = ndb.IntegerProperty()
    festivals = ndb.StringProperty()

    cast = ndb.StringProperty()
    directed_by = ndb.StringProperty()
    written_by = ndb.StringProperty()
    produced_by = ndb.StringProperty()
    co_produced_by = ndb.StringProperty()
    director_producer = ndb.StringProperty()
    executive_producer = ndb.StringProperty()
    cinematographer = ndb.StringProperty()
    sound = ndb.StringProperty()
    editing = ndb.StringProperty()
    sound_design = ndb.StringProperty()
    sound_mixing = ndb.StringProperty()
    music = ndb.StringProperty()
    assistant_director = ndb.StringProperty()
    assistant_producer = ndb.StringProperty()
    assistant_editor = ndb.StringProperty()
    animation = ndb.StringProperty()
    vfx = ndb.StringProperty()
    digital_composer = ndb.StringProperty()
    colorist = ndb.StringProperty()
    graphic_design = ndb.StringProperty()
    subtitles = ndb.StringProperty()
    sound_studio = ndb.StringProperty()
    image_postproduction_and_dcp = ndb.StringProperty()
    international_sales_and_festivals = ndb.StringProperty()

    image_top = ndb.StringProperty()
    image_one = ndb.StringProperty()
    image_one_subtext = ndb.StringProperty()
    image_two = ndb.StringProperty()
    image_two_subtext = ndb.StringProperty()
    link_video = ndb.StringProperty()
    # source = ndb.StringProperty()
