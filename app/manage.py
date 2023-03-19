from sqlalchemy import update
from errors.user_error import CreateUserError, ChangeUserDataError
from models.database import session
from models.user import User
from utils import user_settings


def main():
    """

    """
    user: User | None
    while True:
        u = user_settings.get_user_settings()
        if not u:
            return

        try:
            is_user: User = session.query(User).where(User.token == u.token).first()  # if user exists
            if not is_user:
                user = User(token=u.token, language=u.lang)
                session.add(user)
                session.commit()
            else:
                user = is_user
        except Exception as e:
            session.rollback()
            print(CreateUserError(e))
            continue

        u.__setattr__("id", user.id)
        break

    index: str = ""
    while index not in ["exit", 'выход']:
        print("Выбор действия: \n"
              "exit или выход - выход из программы\n"
              "1 - изменить данные(token, language) \n"
              "2 - получить координаты адреса\n")
        index = input("Действие: ")
        if index == "1":
            try:
                if u.change_data():
                    stmt = (update(User).where(User.id == u.id)).values(
                        {User.token: u.token, User.language: u.lang}).returning(User)
                    session.execute(stmt)
                    session.commit()
                    print("Изменения были успешно добавлены")
            except Exception as e:
                print(ChangeUserDataError(e))
        elif index == "2":
            places = {}
            place = input("Введите место, у которого вы ходите найти координаты: ")
            res = u.execute_places(place)
            if res:
                print("Выберите подходящее для вас место")
                for index, values in enumerate(res):
                    value = values.get("value", "")
                    print(f"{index} - {value}")
                    places[f'{index}'] = value
            else:
                print("Заданные вами место не найдено")
                continue
            current_place = input("Место: ")
            if current_place not in places.keys():
                print("В списке нет выбранного вами места")
            geolocate: dict = u.get_geolocate(places[current_place])
            lat, lon = geolocate.get("data").get("geo_lat"), geolocate.get("data").get("geo_lon")
            if lat and lon:
                print(f"Ваши координаты: \nШирота: {lat}; Долгота: {lon}")
        elif index not in ["exit", 'выход']:
            print("Неправильный ввод действия")


if __name__ == '__main__':
    main()
