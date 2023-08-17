
class Gun:
    def __init__(self, color, size, number_of_bullet, length, type, weight):
        self.color = color
        self.size = size
        self.number_of_bullet = number_of_bullet
        self.length = length
        self.type = type
        self.weight = weight

    def __str__(self) -> str:
        stars = "*" * 20
        return f"{stars}" \
               f"\nColor: {self.color} \nSize: {self.size}" \
               f"\nBullet Capacity: {self.number_of_bullet} Bullets" \
               f"\nThe length is: {self.length}Inches \nType: {self.type} \nWeight: {self.weight}Kg\n{stars}"

if __name__ == '__main__':
    ak_47 = Gun("Black", 23, 599, 40.9, "Ak-47 Super", 30)
    shot_gun = Gun("White", 29, 1, 35.5, "Shot Gun Alpha", 20)

    print(ak_47)
    print()
    print(shot_gun)