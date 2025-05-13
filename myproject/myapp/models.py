from django.db import models

class Workout(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тренировки")
    description = models.TextField(verbose_name="Описание тренировки", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название группы мышц")
    description = models.TextField(verbose_name="Описание группы мышц", blank=True, null=True)
    workouts = models.ManyToManyField(Workout, related_name="muscle_groups", verbose_name="Тренировки")

    def __str__(self):
        return self.name

 
class Statistic(models.Model):
    user = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="statistics", verbose_name="Пользователь")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="statistics", verbose_name="Тренировка")
    regularity = models.FloatField(verbose_name="Регулярность тренировок")
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"{self.user.username} - {self.workout.name} - {self.date}"

class RegularityStatistic(models.Model):
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, related_name="regularity_statistics", verbose_name="Группа мышц")
    average_regularity = models.FloatField(verbose_name="Средняя регулярность")
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"{self.muscle_group.name} - {self.average_regularity}"

