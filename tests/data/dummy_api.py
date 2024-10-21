from fild.sdk import Dictionary, Int, String

from fildapi.method import ApiMethod
from fildapi.schema import HttpMethod


SERVICE = 'dummy'
BASE_URL = 'http://baseurl'
API_URL = 'dummyurl/'


class CheckCallReq(Dictionary):
    Id = Int(name='id')
    Name = String(name='name')


class CheckCall(ApiMethod):
    method = HttpMethod.POST
    url = 'api/check_call'
    req_body = CheckCallReq
    resp_body = Dictionary


class PathParams(Dictionary):
    Id = Int(name='id')
    Param = String(name='param')


class CheckParamsCall(ApiMethod):
    method = HttpMethod.GET
    url = 'api/{id}/get/{param}'
