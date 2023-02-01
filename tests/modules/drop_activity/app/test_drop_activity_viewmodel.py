from src.modules.drop_activity.app.drop_activity_viewmodel import DropActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityViewmodel:

    def test_drop_activity_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[8]

        drop_activity_viewmodel = DropActivityViewmodel(enrollment, enrollment.user).to_dict()

        expected = {'activity_code': "COD1468",
                    'user': {'name': 'Pedro Marcelino', 'user_id': '0355573c-a110-11ed-a8fc-0242ac120002', 'role': 'INTERNATIONAL_STUDENT'},
                    'state': 'DROPPED', 'date_subscribed': 1671488212000,
                    'message': 'the enrollment was dropped'}

        assert drop_activity_viewmodel == expected
