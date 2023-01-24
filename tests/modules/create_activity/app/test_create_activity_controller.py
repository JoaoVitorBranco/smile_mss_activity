from src.modules.create_activity.app.create_activity_controller import CreateActivityController
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_CreateActivityController:
    def test_create_activity_controller(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000000,
                                    "duration": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["12mf", "d7f1"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000000, })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['code'] == 'ZYX321'
        assert response.body['title'] == 'Clean Architecture code review!'
        assert response.body['description'] == "Reviewing IMT student's codes"
        assert response.body['activity_type'] == 'LECTURES'
        assert response.body['is_extensive'] == False
        assert response.body['delivery_model'] == 'IN_PERSON'
        assert response.body['start_date'] == 1669141012000000
        assert response.body['place'] == 'H331'
        assert response.body['duration'] == 90
        assert response.body['responsible_professors'][1]['user_id'] == '12mf'
        assert response.body['speakers'][0]['name'] == "Robert Cecil Martin"
        assert response.body['total_slots'] == 100
        assert response.body['taken_slots'] == 0
        assert response.body['accepting_new_enrollments'] == True
        assert response.body['stop_accepting_new_enrollments_before'] == 1666451811000000

    def test_create_activity_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field code is missing"

    def test_create_activity_controller_duplicated_code(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ECM2345",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'The item alredy exists for this code'

    def test_create_activity_controller_missing_title(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field title is missing"

    def test_create_activity_controller_missing_description(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"

    def test_create_activity_controller_missing_activity_type(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field activity_type is missing"

    def test_create_activity_controller_invalid_activity_type(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "INVALID_TYPE",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000000,
                                    "duration": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["12mf", "d7f1"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000000, })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field activity_type is not valid"

    def test_create_activity_controller_missing_is_extensive(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field is_extensive is missing"

    def test_create_activity_controller_missing_delivery_model(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field delivery_model is missing"

    def test_create_activity_controller_invalid_delivery_model(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "INVALID_TYPE",
                                    "start_date": 1669141012000000,
                                    "duration": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["12mf", "d7f1"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000000, })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field delivery_model is not valid"

    def test_create_activity_controller_missing_start_date(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": "1",
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field start_date isn't in the right type.\n Received: type.\n Expected: int"

    def test_create_activity_controller_invalid_start_date(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field start_date is missing"

    def test_create_activity_controller_missing_duration(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field duration is missing"

    def test_create_activity_controller_missing_responsible_professors(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field responsible_professors is missing"

    def test_create_activity_controller_missing_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field speakers is missing"

    def test_create_activity_controller_missing_total_slots(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000000,

            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field total_slots is missing"

    def test_create_activity_controller_missing_accepting_new_enrollments(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000000,
                "duration": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["12mf", "d7f1"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "stop_accepting_new_enrollments_before": 1666451811000000,
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field accepting_new_enrollments is missing"

    def test_create_activity_controller_invalid_stop_accepting_new_enrollments_before(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000000,
                                    "duration": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["12mf", "d7f1"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": "1666451811000000", })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field stop_accepting_new_enrollments_before isn't in the right type.\n Received: type.\n Expected: int"
