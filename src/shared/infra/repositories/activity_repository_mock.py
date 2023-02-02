import datetime
from typing import List, Tuple

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    speakers: List[Speaker]
    users: List[User]
    activities: List[Activity]
    enrollments: List[Enrollment]

    def __init__(self):
        self.users = [
            User(name="João Vilas", role=ROLE.ADMIN, user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002"),
            User(name="Bruno Soller", role=ROLE.STUDENT, user_id="0355535e-a110-11ed-a8fc-0242ac120002"),
            User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002"),
            User(name="Pedro Marcelino", role=ROLE.INTERNATIONAL_STUDENT, user_id="0355573c-a110-11ed-a8fc-0242ac120002"),
            User(name="Hector Guerrini", role=ROLE.EXTERNAL, user_id="03555872-a110-11ed-a8fc-0242ac120002"),
            User(name="Ricardo Soller", role=ROLE.EMPLOYEE, user_id="2f0df47e-a110-11ed-a8fc-0242ac120002"),
            User(name="Marcos Romanato", role=ROLE.STUDENT, user_id="38c3d7fe-a110-11ed-a8fc-0242ac120002"),
            User(name="Marco Briquez", role=ROLE.STUDENT, user_id="452a5f9a-a110-11ed-a8fc-0242ac120002"),
            User(name="Simone Romanato", role=ROLE.EXTERNAL, user_id="4d1d64ae-a110-11ed-a8fc-0242ac120002"),
            User(name="Viviani Soller", role=ROLE.EXTERNAL, user_id="5a49ad2c-a110-11ed-a8fc-0242ac120002"),
            User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
            User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="62cafdd4-a110-11ed-a8fc-0242ac120002"),
            User(name="Rodrigo Santos", role=ROLE.PROFESSOR, user_id="71f06f24-a110-11ed-a8fc-0242ac120002"),
        ]

        self.activities = [
            Activity(
                code="ECM2345",
                title="Atividade da ECM 2345",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671747413000,
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=4,
                taken_slots=4,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671743812000
            ),
            Activity(
                code="ELET355",
                title="Atividade da ELET 355",
                description="Isso é uma atividade, sério.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1671661013000,
                duration=400,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="COD1468",
                title="Atividade da COD 1468",
                description="Isso definitivamente é uma atividade",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1671661013000,
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2], self.users[10]],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=50,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CODIGO",
                title="Atividade da CÓDIGO",
                description="Isso DEFINITIVAMENTE é uma atividade!",
                activity_type=ACTIVITY_TYPE.TECHNICAL_VISITS,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1672006613000,
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                          Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671747413000
            ),
            Activity(
                code="AC000",
                title="Atividade de competição",
                description="Isso é uma guerra",
                activity_type=ACTIVITY_TYPE.ACADEMIC_COMPETITIONS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671661013000,
                duration=190,
                link=None,
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=50,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671574613000
            ),
            Activity(
                code="ECM251",
                title="Atividade da ECM251",
                description="Se o professor chegar vai ter atividade...",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1671733013000,
                duration=40,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=20,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="SC456",
                title="Atividade da SC456",
                description="Sem criatividade para descrição",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1671563813000,
                duration=80,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CAFE",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671661013000,
                duration=20,
                link=None,
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CODE",
                title="Atividade da CODE",
                description="O mesmo speaker pela 50° vez",
                activity_type=ACTIVITY_TYPE.PROFESSORS_ACADEMY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1671488213000,
                duration=120,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="PRF246",
                title="Atividade da PRF246",
                description="Um único professor pra tudo",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1672006613000,
                duration=140,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="2468",
                title="Atividade da 2468",
                description="Atividade com números pares",
                activity_type=ACTIVITY_TYPE.GCSP,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1672006613000,
                duration=60,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=25,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="ULTIMA",
                title="Última atividade",
                description="Atividade pra acabar",
                activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671733013000,
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671733012000
            ),
            Activity(
                code="PINOQ1",
                title="Atividade da PINOQ1",
                description="Não era a última....",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1670005013000,
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=1669918612000
            ),

        ]

        self.enrollments = [
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[0], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671229013000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671315413000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[2], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671401813000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[3], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[4], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[5], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574673000),
            Enrollment(activity_code=self.activities[0].code, user_id=self.users[6], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574733000),
            Enrollment(activity_code=self.activities[1].code, user_id=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[2].code, user_id=self.users[3], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488212000),
            Enrollment(activity_code=self.activities[2].code, user_id=self.users[4], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[3].code, user_id=self.users[4], state=ENROLLMENT_STATE.REJECTED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[3].code, user_id=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[3].code, user_id=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671661013000),
            Enrollment(activity_code=self.activities[4].code, user_id=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671481013000),
            Enrollment(activity_code=self.activities[4].code, user_id=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[5].code, user_id=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[6].code, user_id=self.users[7], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[7].code, user_id=self.users[8], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671401813000),
            Enrollment(activity_code=self.activities[7].code, user_id=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[7].code, user_id=self.users[2], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[8].code, user_id=self.users[9], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671315413000),
            Enrollment(activity_code=self.activities[9].code, user_id=self.users[0], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[10].code, user_id=self.users[1], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[11].code, user_id=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710613000),
            Enrollment(activity_code=self.activities[11].code, user_id=self.users[2], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710614000),
            Enrollment(activity_code=self.activities[11].code, user_id=self.users[3], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1670710615000),
            Enrollment(activity_code=self.activities[11].code, user_id=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710616000),
            Enrollment(activity_code=self.activities[11].code, user_id=self.users[4], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671661013000),
            Enrollment(activity_code=self.activities[12].code, user_id=self.users[1], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1668896213000),
            Enrollment(activity_code=self.activities[12].code, user_id=self.users[2], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1668982612000),
            Enrollment(activity_code=self.activities[12].code, user_id=self.users[3], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1669069013000),
            Enrollment(activity_code=self.activities[12].code, user_id=self.users[4], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1669760213000),
        ]

    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        for enrollment in self.enrollments:
            if enrollment.user.user_id == user_id and enrollment.activity_code == code and enrollment.state != ENROLLMENT_STATE.DROPPED and enrollment.state != ENROLLMENT_STATE.ACTIVITY_CANCELLED:
                return enrollment
        return None

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        self.enrollments.append(enrollment)
        activity = self.get_activity(code=enrollment.activity_code)
        if enrollment.state == ENROLLMENT_STATE.ENROLLED:
            self.update_activity(code=enrollment.activity_code, new_taken_slots=activity.taken_slots + 1)

        return enrollment

    def get_user(self, user_id: str) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_activity(self, code: str) -> Activity:
        for activity in self.activities:
            if activity.code == code:
                return activity
        return None

    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:
        for enrollment in self.enrollments:
            if enrollment.user.user_id == user_id and enrollment.activity_code == code:
                activity = self.get_activity(code=code)
                if new_state == ENROLLMENT_STATE.DROPPED:
                    self.update_activity(code=code, new_taken_slots=activity.taken_slots - 1)
                elif new_state == ENROLLMENT_STATE.ENROLLED:
                    self.update_activity(code=code, new_taken_slots=activity.taken_slots + 1)

                enrollment.state = new_state
                return enrollment
        return None

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        for activity in self.activities:
            if activity.code == code:
                enrollments = [enrollment for enrollment in self.enrollments if enrollment.activity_code == code]
                return activity, enrollments
        return None, None

    def update_activity(self, code: str, new_title: str = None, new_description: str = None,
                        new_activity_type: ACTIVITY_TYPE = None, new_is_extensive: bool = None,
                        new_delivery_model: DELIVERY_MODEL = None, new_start_date: int = None,
                        new_duration: int = None, new_link: str = None, new_place: str = None,
                        new_responsible_professors: List[User] = None, new_speakers: List[Speaker] = None,
                        new_total_slots: int = None, new_taken_slots: int = None,
                        new_accepting_new_enrollments: bool = None,
                        new_stop_accepting_new_enrollments_before: int = None) -> Activity:
        for activity in self.activities:
            if activity.code == code:
                if new_title is not None:
                    activity.title = new_title
                if new_description is not None:
                    activity.description = new_description
                if new_activity_type is not None:
                    activity.activity_type = new_activity_type
                if new_is_extensive is not None:
                    activity.is_extensive = new_is_extensive
                if new_delivery_model is not None:
                    activity.delivery_model = new_delivery_model
                if new_start_date is not None:
                    activity.start_date = new_start_date
                if new_duration is not None:
                    activity.duration = new_duration
                if new_link is not None:
                    activity.link = new_link
                if new_place is not None:
                    activity.place = new_place
                if new_responsible_professors is not None:
                    activity.responsible_professors = new_responsible_professors
                if new_speakers is not None:
                    activity.speakers = new_speakers
                if new_total_slots is not None:
                    activity.total_slots = new_total_slots
                if new_taken_slots is not None:
                    activity.taken_slots = new_taken_slots
                if new_accepting_new_enrollments is not None:
                    activity.accepting_new_enrollments = new_accepting_new_enrollments
                if new_stop_accepting_new_enrollments_before is not None:
                    activity.stop_accepting_new_enrollments_before = new_stop_accepting_new_enrollments_before
                return activity

        return None

    def get_all_activities_admin(self) -> List[Tuple[Activity, List[Enrollment]]]:
        activities_with_enrollments = list()
        for activity in self.activities:
            activity, enrollments = self.get_activity_with_enrollments(code=activity.code)
            activities_with_enrollments.append((activity, enrollments))
        return activities_with_enrollments

    def get_all_activities(self) -> List[Activity]:
        activities = list()
        for activity in self.activities:
            activities.append(activity)
        return activities

    def delete_activity(self, code: str) -> Activity:
        for idx, activity in enumerate(self.activities):
            if activity.code == code:
                return self.activities.pop(idx)
        return None

    def batch_update_enrollment(self, enrollments: List[Enrollment], state: ENROLLMENT_STATE) -> List[Enrollment]:
        new_enrollments = []
        for enrollment in enrollments:
            new_enrollment = self.update_enrollment(user_id=enrollment.user.user_id, code=enrollment.activity_code,
                                                    new_state=state)
            new_enrollments.append(new_enrollment)

        return new_enrollments

    def create_activity(self, activity: Activity) -> Activity:
        self.activities.append(activity)

        return activity

    def get_users(self, user_ids: List[str]) -> List[User]:
        users = list()
        for user in self.users:
            if user.user_id in user_ids:
                users.append(user)
        return users

    def get_enrollments_by_user_id(self, user_id: str) -> List[Enrollment]:
        enrollments = list()
        for enrollment in self.enrollments:
            if enrollment.user.user_id == user_id and enrollment.state == ENROLLMENT_STATE.ENROLLED:
                enrollments.append(enrollment)
        return enrollments
