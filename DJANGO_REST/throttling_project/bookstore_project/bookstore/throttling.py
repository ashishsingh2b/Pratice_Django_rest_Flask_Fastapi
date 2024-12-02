from rest_framework.throttling import UserRateThrottle


class Jackratethrottel(UserRateThrottle):
    scope= 'jack'