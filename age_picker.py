class AgePicker:
    def __init__(self, toddler: int,child: int,teen: int,adult:int,elderly: int):
        self.age_center = {
            'toddler': toddler,
            'child': child,
            'teen': teen,
            'adult': adult,
            'elderly': elderly} 

    def add(self, age_center: str) -> None:
        if age_center == 'toddler':
            self.age_center['toddler'] = self.age_center.get('toddler') +1
        if age_center == 'child':
            self.age_center['child'] = self.age_center.get('adolescence') +1
        if age_center == 'teen':
            self.age_center['teen'] = self.age_center.get('teen') +1
        if age_center == 'adult':
            self.age_center['adult'] = self.age_center.get('adult') +1
        if age_center == 'elderly':
            self.age_center['elderly'] = self.age_center.get('elderly') +1


    def sort(self) -> str:
        score = 0
        result = ''
        for age, points in self.age_center.items():
            if points > score:
                score = points
                result = age

        return result
    

def clear(self) -> None:
    self.age_center = {
        'toddler': 0,
        'child': 0,
        'teen': 0,
        'adult': 0,
        'elderly': 0,}