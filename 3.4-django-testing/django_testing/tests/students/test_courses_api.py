import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


# фикстура для api-client
@pytest.fixture
def client():
    return APIClient()


# фикстура для фабрики курсов
@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# фикстура для фабрики студентов
@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения первого курса (retrieve-логика):
@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    # создаем курс через фабрику;
    course = courses_factory(_quantity=1)
    # строим урл и делаем запрос через тестовый клиент;
    response = client.get('/api/v1/courses/')
    data = response.json()
    # проверяем, что вернулся именно тот курс, который запрашивали;
    assert response.status_code == 200
    assert data[0]['name'] == course[0].name


# проверка получения списка курсов (list-логика):
@pytest.mark.django_db
def test_get_course_list(client, courses_factory):
    # аналогично — сначала вызываем фабрики, затем делаем запрос и проверяем результат;
    courses = courses_factory(_quantity=5)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


# проверка фильтрации списка курсов по id:
@pytest.mark.django_db
def test_filter(client, courses_factory):
    # создаем курсы через фабрику, передать ID одного курса в фильтр, проверить результат запроса с фильтром;
    courses = courses_factory(_quantity=20)
    id = courses[9].id
    response = client.get(f'/api/v1/courses/{id}/')
    data = response.json()
    assert response.status_code == 200
    # проверка фильтрации списка курсов по name;
    assert data['name'] == courses[9].name


# тест успешного создания курса:
@pytest.mark.django_db
def test_create(client):
    # здесь фабрика не нужна, готовим JSON-данные и создаём курс;
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Основы мемов'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# тест успешного обновления курса:
@pytest.mark.django_db
def test_patch(client, courses_factory):
    # сначала через фабрику создаём, потом обновляем JSON-данными;
    courses = courses_factory(_quantity=5)
    id = courses[4].id
    response = client.patch(f'/api/v1/courses/{id}/', data={'name': 'ТММ'}, format='json')
    assert response.status_code == 200
    response_new = client.get(f'/api/v1/courses/{id}/')
    assert response_new.status_code == 200
    data = response_new.json()
    assert data['name'] == 'ТММ'


# тест успешного удаления курса.
@pytest.mark.django_db
def test_delete(client, courses_factory):
    courses = courses_factory(_quantity=5)
    id = courses[4].id
    count = Course.objects.count()
    response = client.delete(f'/api/v1/courses/{id}/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
