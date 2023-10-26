from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound

class GetActivityWithEnrollmentsUsecase:

    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability

    def __call__(self, user: User, code: str) -> dict:
        self.observability.log_usecase_in()
        if user.role != ROLE.PROFESSOR and user.role != ROLE.ADMIN:
            raise ForbiddenAction("user: only responsible professors and admin can do that")

        if not Activity.validate_activity_code(code):
            raise EntityError("code")
        activity, all_enrollments = self.repo_activity.get_activity_with_enrollments(code=code)

        if activity is None:
            raise NoItemsFound('activity')

        if user.role == ROLE.PROFESSOR:
            if user.user_id not in [professor.user_id for professor in activity.responsible_professors]:
                raise ForbiddenAction('user')

        enrollments = [enrollment for enrollment in all_enrollments if enrollment.state in [ENROLLMENT_STATE.ENROLLED, ENROLLMENT_STATE.IN_QUEUE, ENROLLMENT_STATE.COMPLETED]]
        user_id_list = list()
        for enrollment in enrollments:
            user_id_list.append(enrollment.user_id)

        users = self.repo_user.get_users_info(user_id_list)

        users_dict = {user.user_id: user for user in users}

        activity_dict = dict()

        activity_dict = {

            "activity": activity,
            "enrollments": [
                (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]

            }
        self.observability.log_usecase_out()
        return activity_dict
