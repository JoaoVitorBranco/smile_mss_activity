import pytest

from src.shared.domain.entities.speaker import Speaker
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Speaker:
    def test_speaker(self):
        Speaker(name="Briqz", bio="Daora", company="Microsoft")


    def test_speaker_invalid_name(self):
        with pytest.raises(EntityError):
            Speaker(name="B", bio="Daora", company="Microsoft")

    def test_speaker_invalid_bio(self):
        with pytest.raises(EntityError):
            Speaker(name="Briqz", bio=1, company="Microsoft")

    def test_speaker_invalid_company(self):
        with pytest.raises(EntityError):
            Speaker(name="Briqz", bio="Daora", company=1)

    def test_speaker_invalid_name_none(self):
        with pytest.raises(EntityError):
            Speaker(name=None, bio="Daora", company="Microsoft")

    def test_speaker_invalid_bio_none(self):
        with pytest.raises(EntityError):
            Speaker(name="Briqz", bio=None, company="Microsoft")

    def test_speaker_invalid_company_none(self):
        with pytest.raises(EntityError):
            Speaker(name="Briqz", bio="Daora", company=None)
