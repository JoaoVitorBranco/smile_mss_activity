import datetime

import pytest
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError


class Test_CreateActivityUsecase:

    def test_create_activity_user(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        activitiesLenBefore = len(repo.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305),
                           stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305),
                           speakers=[{
                               "name": "Robert Cecil Martin",
                               "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               "company": "Clean Architecture Company"
                           }], responsible_professors_user_id=["12mf"])

        activitiesLenAfter = activitiesLenBefore + 1

        assert len(repo.activities) == activitiesLenAfter
        assert repo.activities[activitiesLenBefore].code == "CodigoNovo"
        assert repo.activities[activitiesLenBefore].title == "Atividade da ECM 2345"
        assert repo.activities[activitiesLenBefore].description == "Isso é uma atividade"
        assert repo.activities[activitiesLenBefore].activity_type == ACTIVITY_TYPE.LECTURES
        assert repo.activities[activitiesLenBefore].delivery_model == DELIVERY_MODEL.HYBRID
        assert repo.activities[activitiesLenBefore].duration == 120
        assert repo.activities[activitiesLenBefore].link == None
        assert repo.activities[activitiesLenBefore].place == "H332"
        assert repo.activities[activitiesLenBefore].total_slots == 4
        assert repo.activities[activitiesLenBefore].is_extensive == True
        assert repo.activities[activitiesLenBefore].taken_slots == 4
        assert repo.activities[activitiesLenBefore].accepting_new_enrollments == True
        assert repo.activities[activitiesLenBefore].start_date == datetime.datetime(2022, 12, 22, 19, 16, 52, 998305)
        assert repo.activities[activitiesLenBefore].stop_accepting_new_enrollments_before == datetime.datetime(2022, 12,
                                                                                                               22, 18,
                                                                                                               16, 52,
                                                                                                               998305)
        assert repo.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo.activities[activitiesLenBefore].speakers[
                   0].bio == "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design"
        assert repo.activities[activitiesLenBefore].speakers[0].company == "Clean Architecture Company"
        assert repo.activities[activitiesLenBefore].responsible_professors[0].name == "Rafael Santos"
        assert repo.activities[activitiesLenBefore].responsible_professors[0].role == ROLE.PROFESSOR
        assert repo.activities[activitiesLenBefore].responsible_professors[0].user_id == "12mf"

    def test_create_activity_usecase_two_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        activitiesLenBefore = len(repo.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305),
                           stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305),
                           speakers=[{
                                   "name": "Robert Cecil Martin",
                                   "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                   "company": "Clean Architecture Company"
                           },
                                 {
                                    "name": "Vitor Soller",
                                    "bio": "SOCORRRO ALGUEM ME AJUDA",
                                    "company": "Clean Architecture Company"
                                 }
                           ], responsible_professors_user_id=["12mf"])

        assert len(repo.activities) == activitiesLenBefore + 1
        assert len(repo.activities[activitiesLenBefore].speakers) == 2
        assert repo.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo.activities[activitiesLenBefore].speakers[1].name == "Vitor Soller"




    def test_create_activity_usecase_invalid_code_int(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code=00000, title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305),
                    stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305),
                    speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                    responsible_professors_user_id=["12mf"])

    def test_create_activity_usecase_not_str(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code=123, title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305),
                    stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305),
                    speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                    responsible_professors_user_id=["12mf"])
