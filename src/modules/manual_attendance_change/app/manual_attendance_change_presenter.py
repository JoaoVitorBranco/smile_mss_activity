from src.modules.manual_attendance_change.app.manual_attendance_change_controller import \
    ManualAttendanceChangeController
from src.modules.manual_attendance_change.app.manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
controller = ManualAttendanceChangeController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
