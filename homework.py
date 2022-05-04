class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str, duration: float, 
                distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = ("{:.3f}".format(duration))
        self.distance = ("{:.3f}".format(distance))
        self.speed = ("{:.3f}".format(speed))
        self.calories = ("{:.3f}".format(calories))

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} '
                f'ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000

    def __init__(self, action: int, duration: float, 
                weight: float) -> None:
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
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        distance = self.get_distance()
        mean_speed = self.get_mean_speed()
        spent_calories = self.get_spent_calories()
        info = InfoMessage(self.__class__.__name__, self.duration, 
        distance, mean_speed, spent_calories)
        return info

class Running(Training):
    """Тренировка: бег."""
    
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = Training.get_mean_speed(self)
        spent_calories = ((self.coeff_calorie_1 * mean_speed - 
        self.coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration*60)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029
    def __init__(self, action: int, duration: float, 
                weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = self.get_mean_speed()
        spent_calories = (self.coeff_calorie_1 * self.weight + (mean_speed**2 // 
        self.height)* self.coeff_calorie_2 * self.weight) * self.duration * 60 
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    def __init__(self, action: int, duration: float, 
                weight: float, length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (self.length_pool * self.count_pool / self.M_IN_KM / 
        self.duration)
        return mean_speed
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = self.get_mean_speed()
        spent_calories = (mean_speed + 1.1) * 2 * self.weight  
        return spent_calories
    
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    read_workout_type = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
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

