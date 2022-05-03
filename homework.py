from turtle import distance

"""Константы"""
M_IN_KM: int = 1000
coeff_calorie_1 = 18
coeff_calorie_2 = 20
LEN_STEP = 0.65
LEN_STEP_SWEEM = 1.38


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str, duration: float, 
                distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = round(distance, 3)
        self.speed = round(speed, 3)
        self.calories = round(calories, 3)

    def get_message(self) -> str:
        return ('Тип тренировки: {training_type}; Длительность: {duration} '
                'ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; '
                'Потрачено ккал: {round(calories}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self, action: int, duration: float, 
                weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = distance / self.duration
        return mean_speed

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_info = InfoMessage(self.duration, distance, mean_speed, spent_calories)
        return 

class Running(Training):
    """Тренировка: бег."""
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = ((coeff_calorie_1 * self.mean_speed - coeff_calorie_2) * 
        self.weight / M_IN_KM * self.duration)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action: int, duration: float, 
                weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (0.035 * self.weight + (self.mean_speed**2 // self.height)*
         0.029 * self.weight) * self.duration 
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self, action: int, duration: float, 
                weight: float, length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (self.length_pool * self.count_pool / M_IN_KM / 
        self.duration)
        return mean_speed
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (self.mean_speed + 1.1) * 2 * self.weight  
        return spent_calories
    
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * LEN_STEP_SWEEM / M_IN_KM
        return distance

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        workout = Swimming(data)
    elif workout_type == 'RUN':
        workout = Running(data)
    elif workout_type == 'WLK':
        workout = SportsWalking(data)
    else:
        pass
    return workout


def main(training: Training) -> None:
    """Главная функция."""
    info = InfoMessage(training)
    print (info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

