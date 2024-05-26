from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPagination(LimitOffsetPagination):
   default_limit=4
   # limit_query_param='mylimit'
   # offset_query_param='myoffset'
   # max_limit=4