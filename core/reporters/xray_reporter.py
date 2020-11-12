from enum import Enum

from requests import get, put

from core import ParamError


class XRayEndpoint(Enum):
    TEST_RUN = 'testrun/{}'
    TEST_EXEC = 'testexec/{}/test'


class TestStatus(Enum):
    PASS = 'PASS'
    FAIL = 'FAIl'
    TODO = 'TODO'


class XRayReporter:
    def __init__(self):
        self.headers = None
        self.base_url = None

    def set_auth(self, token: str):
        self.headers = {'Authorization': f'Basic {token}'}
        return self

    def set_base_url(self, url: str):
        self.base_url = url
        return self

    def __check_required_parameters(self):
        if self.base_url is not None and self.headers is not None:
            return True
        else:
            raise ParamError('set_base_url', 'set_auth')

    def __get(self, endpoint: str, params={}):
        return get(f'{self.base_url}{endpoint}', headers=self.headers, params=params)

    def __put(self, endpoint: str, body):
        return put(f'{self.base_url}{endpoint}', headers=self.headers, json=body)

    def __run_id(self, test_name: str, execution_id: str):
        '''
        :param test_name: Jira id of the test case (e.g. PATHTEST-309)
        :param execution_id: Jira id of the test execution (e.g. PATHTEST-511)
        :return: run id of the test
        '''
        return [test for test in self.__execution(execution_id) if test['key'] == test_name][0]['id']

    def __execution(self, execution_id: str):
        '''
        :param execution_id: Jira id of the test execution (e.g. PATHTEST-511)
        :return: json representation of test execution
        '''
        page1 = self.__get(XRayEndpoint.TEST_EXEC.value.format(execution_id), params={'limit': 200, 'page': 1}).json()
        page2 = self.__get(XRayEndpoint.TEST_EXEC.value.format(execution_id), params={'limit': 200, 'page': 2}).json()
        return page1 + page2

    def test_run(self, test_name: str, execution_id: str, status: TestStatus, comment: str = ""):
        '''
        :param test_name: Jira id of the test case (e.g. PATHTEST-309)
        :param execution_id: Jira id of the test execution (e.g. PATHTEST-511)
        :param status: test outcome status
        :param comment: optional comment
        :return: requests.Response
        '''
        self.__check_required_parameters()

        body = {
            "status": f"{status.value}",
            "comment": f"{comment}"
        }

        run_id = self.__run_id(test_name, execution_id)
        return self.__put(XRayEndpoint.TEST_RUN.value.format(run_id), body=body)
