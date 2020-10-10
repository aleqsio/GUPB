from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller import myawesome

# KEYBOARD_CONTROLLER = keyboard.KeyboardController()
MY_AWESOME_CONTROLLER = myawesome.MyAwesomeController()
CONFIGURATION = {
    'arenas': [
        'island',
    ],
    'controllers': [
        # KEYBOARD_CONTROLLER,
        MY_AWESOME_CONTROLLER,
        random.RandomController("Alice"),
        # random.RandomController("Bob"),
        # random.RandomController("Cecilia"),
    ],
    'visualise': True,
    'show_sight': MY_AWESOME_CONTROLLER,
    'runs_no': 1,
}
