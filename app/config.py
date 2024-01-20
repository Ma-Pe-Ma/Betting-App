class Default(object):
    # the supported lanugages on the site
    SUPPORTED_LANGUAGES = {'en' : ['English', 'Angol'], 'hu' : ['Hungarian', 'Magyar']}
    # secret key for session handling
    SECRET_KEY = 'dev'
    # upload folder's name in the instance folder
    UPLOAD_FOLDER = 'upload'
    # allowed extensions to upload by the user
    ALLOWED_EXTENSIONS = ['csv']

    SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.sqlite'
    MATCH_URL = 'https://path.fixture'

    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
    SCHEDULER_TIMEZONE = 'utc'

    # 0 - not using, 1 - email, 2 - browser notification
    DIRECT_MESSAGING = 0

    SESSION_TIMEOUT = 15

    INVITATION_KEYS = {
      'user' : 'registration',
      'admin' : 'admin'
    }

    DEADLINE_TIMES = {
      'register' : '2022-11-20 18:00',
      'group_evaluation' : '2022-11-29 19:00',
      'tournament_end' : '2022-12-22 23:59'
    }

    MATCH_TIME_LENGTH = {
      'base_time' : 2,
      'extra_time' : 2.5
    }

    BET_VALUES = {
      'starting_bet_amount' : 2000,
	    'max_group_bet_value' : 50,
	    'max_tournament_bet_value' : 200,
	    'default_max_bet_per_match' : 50
    }

    GROUP_BET_HIT_MAP = [0, 1.5, 2.5, 0, 4]

    BONUS_MULTIPLIERS = {
      "bullseye" : 4,
      "difference" : 1
    }