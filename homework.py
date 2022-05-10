from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        self.duration = self.duration
        self.distance = self.distance
        self.speed = self.speed
        self.calories = self.calories
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; Ср. '
                f'скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.'
                )


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    COEFF_MINUTE: float = 60

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        mean_speed = distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> None:
        """Получить количество затраченных калорий."""
        raise NameError('Расчёт каллорий должен быть у каждого подкласса!')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        distance = self.get_distance()
        mean_speed = self.get_mean_speed()
        spent_calories = self.get_spent_calories()
        return InfoMessage(
            self.__class__.__name__, self.duration,
            distance, mean_speed, spent_calories
        )


class Running(Training):
    """Тренировка: бег."""

    MEAN_SPEED_MULTIPICATOR: float = 18
    MEAN_SPEED_DEDUCTION: float = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (
            (self.MEAN_SPEED_MULTIPICATOR * self.get_mean_speed()
             - self.MEAN_SPEED_DEDUCTION) * self.weight / self.M_IN_KM
            * self.duration * self.COEFF_MINUTE
        )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    WEIGHT_MULTIPICATOR_1: float = 0.035
    WEIGHT_MULTIPICATOR_2: float = 0.029

    def __init__(
        self, action: int,
        duration: float,
        weight: float,
        height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = self.get_mean_speed()
        spent_calories = ((self.WEIGHT_MULTIPICATOR_1 * self.weight
                          + (mean_speed**2 // self.height)
                          * self.WEIGHT_MULTIPICATOR_2 * self.weight)
                          * self.duration * self.COEFF_MINUTE)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    MEAN_SPEED_ADD: float = 1.1
    WEIGHT_MULTIPICATOR: float = 2

    def __init__(
        self, action: int,
        duration: float,
        weight: float,
        length_pool: int,
        count_pool: int
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = self.get_mean_speed()
        spent_calories = ((mean_speed + self.MEAN_SPEED_ADD)
                          * self.WEIGHT_MULTIPICATOR * self.weight)
        return spent_calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    read_workout_type: dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in read_workout_type:
        raise NameError('Данный вид тренировки отсутствует в программе!')
    return read_workout_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = Training.show_training_info(training)
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
