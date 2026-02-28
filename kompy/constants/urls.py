from typing import Final


class KomootUrl:
    USER_LOGIN_URL: Final[str] = 'https://api.komoot.de/v006/account/email/{email_address}/'
    LIST_TOURS_URL: Final[str] = 'https://api.komoot.de/v007/users/{user_identifier}/tours/'
    TOUR_URL: Final[str] = 'https://api.komoot.de/v007/tours/{tour_identifier}'
    UPLOAD_TOUR_URL: Final[str] = 'https://api.komoot.de/v007/tours/?data_type={object_type}'
    LIST_RELATION_URL: Final[str] = 'https://api.komoot.de/v007/users/{user_identifier}/relations/{relation_identifier}/'
    LIST_FOLLOWER_URL: Final[str] = 'https://komoot.com/user/{user_identifier}/followers/'
    PROFILE_URL: Final[str] = 'https://api.komoot.de/v007/users/{user_identifier}/'

    testing = "lol"
