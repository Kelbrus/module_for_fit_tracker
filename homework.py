from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, List


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    TRAINING_TYPE_STR: ClassVar[str] = 'Тип тренировки: {}; '
    DURATION_STR: ClassVar[str] = 'Длительность: {:.3f} ч.; '
    DISTANCE_STR: ClassVar[str] = 'Дистанция: {:.3f} км; '
    SPEED_STR: ClassVar[str] = 'Ср. скорость: {:.3f} км/ч; '
    CALORIES_STR: ClassVar[str] = 'Потрачено ккал: {:.3f}.'
    INFO_MESSAGE: ClassVar[str] = (
        TRAINING_TYPE_STR
        + DURATION_STR
        + DISTANCE_STR
        + SPEED_STR
        + CALORIES_STR
    )

    def get_message(self) -> str:
        """Выводит сообщение пользователю."""
        return self.INFO_MESSAGE.format(*asdict(self).values())


@dataclass
class Training:
    """Базовый класс тренировки."""

    action: int
    duration: float
    weight: float

    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    COEFF_HOURS_IN_MIN: ClassVar[int] = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            'В подклассе должен быть определен метод get_spent_calories!'
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        result_for_message = InfoMessage(self.__class__.__name__,
                                         self.duration,
                                         self.get_distance(),
                                         self.get_mean_speed(),
                                         self.get_spent_calories()
                                         )
        return result_for_message


class Running(Training):
    """Тренировка: бег."""

    COEFF_CALORIE_RUN_1: ClassVar[int] = 18
    COEFF_CALORIE_RUN_2: ClassVar[int] = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.COEFF_CALORIE_RUN_1 * self.get_mean_speed()
                    - self.COEFF_CALORIE_RUN_2) * self.weight / self.M_IN_KM
                    * self.duration * self.COEFF_HOURS_IN_MIN)
        return calories


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    height: float

    COEFF_CALORIE_WLK_1: ClassVar[float] = 0.035
    COEFF_CALORIE_WLK_2: ClassVar[int] = 2
    COEFF_CALORIE_WLK_3: ClassVar[float] = 0.029

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.COEFF_CALORIE_WLK_1 * self.weight
                    + (self.get_mean_speed() ** self.COEFF_CALORIE_WLK_2
                     // self.height) * self.COEFF_CALORIE_WLK_3 * self.weight)
                    * self.duration * self.COEFF_HOURS_IN_MIN)
        return calories


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    length_pool: float
    count_pool: int

    COEFF_CALORIE_SWM_1: ClassVar[float] = 1.1
    COEFF_CALORIE_SWM_2: ClassVar[int] = 2
    LEN_STEP: ClassVar[float] = 1.38

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в бассейне."""
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий в бассейне."""
        calories = ((self.get_mean_speed() + self.COEFF_CALORIE_SWM_1)
                    * self.COEFF_CALORIE_SWM_2 * self.weight)
        return calories

    def get_distance(self) -> float:
        """Получить дистанцию для бассейна в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    sports_dictionary: Dict[str, Training] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    sports_dictionary_data = sports_dictionary.get(workout_type)(*data)
    return sports_dictionary_data


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
