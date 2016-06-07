import pytest

from ..utils import create_test_image


@pytest.mark.django_db
def test_create_test_image():
    width = 150
    height = 150

    result = create_test_image(width, height)

    assert result.width == height
    assert result.height == height
