from age_picker import AgePicker

def test_age_picker():
    pass
def age_picker():
    age_picker = AgePicker(0, 0, 0, 0, 0)
    age_picker.add('toddler')
    age_picker.add('child')
    age_picker.add('teen')
    age_picker.add('adult')
    age_picker.add('elderly')

    assert age_picker.sort() == 'elderly'

def age_picker():
    age_picker = AgePicker(0, 0, 0, 0, 0)
    age_picker.add('toddler')
    age_picker.add('child')
    age_picker.add('teen')
    age_picker.add('adult')
    age_picker.add('elderly')

    assert AgePicker.sort() == 'elderly'
