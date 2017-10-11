from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # recommender = models.ForeignKey(
    #     Idol,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='recommended_membership_set',
    # )
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommended_membership_set'
    )
    joined_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        is_active = '활동 중' if self.is_active else '비활동'
        return f'{self.idol.name} ({self.group.name} | {is_active})'
