import pytest
from src.modules.confirm_attendance.app.confirm_attendance_usecase import ConfirmAttendanceUsecase
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ConfirmAttendanceUsecase:

    def test_confirm_attendance_usecase(self):
        activity_repo = ActivityRepositoryMock()
        users_repo = UserRepositoryMock()
        usecase = ConfirmAttendanceUsecase(activity_repo)

        user_id = users_repo.users[5].user_id
        code = activity_repo.activities[11].code
        confirmation_code = activity_repo.activities[11].confirmation_code

        resp = usecase(
            user_id=user_id,
            code=code,
            confirmation_code=confirmation_code
        )

        assert resp is True
        assert activity_repo.enrollments[26].state == ENROLLMENT_STATE.COMPLETED
        assert activity_repo.enrollments[26].activity_code == code
        assert activity_repo.enrollments[26].user_id == user_id
    
    def test_confirm_attendance_usecase_invalid_user_id(self):
        activity_repo = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(activity_repo)

        user_id = "invalid_user_id" 
        code = activity_repo.activities[11].code
        confirmation_code = activity_repo.activities[11].confirmation_code

        with pytest.raises(ForbiddenAction):
            resp = usecase(
                user_id=user_id,
                code=code,
                confirmation_code=confirmation_code
            )

    def test_confirm_attendance_usecase_invalid_code(self):
        activity_repo = ActivityRepositoryMock()
        users_repo = UserRepositoryMock()
        usecase = ConfirmAttendanceUsecase(activity_repo)

        user_id = users_repo.users[5].user_id
        code = "invalid_code"
        confirmation_code = activity_repo.activities[11].confirmation_code

        with pytest.raises(ForbiddenAction):
            resp = usecase(
                user_id=user_id,
                code=code,
                confirmation_code=confirmation_code
            )
        
    def test_confirm_attendance_usecase_invalid_confirmation_code(self):
        activity_repo = ActivityRepositoryMock()
        users_repo = UserRepositoryMock()
        usecase = ConfirmAttendanceUsecase(activity_repo)

        user_id = users_repo.users[5].user_id
        code = activity_repo.activities[11].code
        confirmation_code = "invalid_confirmation_code"

        
        with pytest.raises(ForbiddenAction):
            resp = usecase(
                user_id=user_id,
                code=code,
                confirmation_code=confirmation_code
            )
