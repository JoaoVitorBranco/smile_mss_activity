from .get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from .get_enrollments_by_user_id_viewmodel import \
    GetEnrollmentsByUserIdViewmodel

from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetEnrollmentsByUserIdController:

    def __init__(self, usecase: GetEnrollmentsByUserIdUsecase):
        self.GetEnrollmentsByUserIdUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            enrollments = self.GetEnrollmentsByUserIdUsecase(
                user_id=request.data.get('user_id')
            )

            viewmodel = GetEnrollmentsByUserIdViewmodel(enrollments)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
