from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller import ihavenoideawhatimdoing

# KEYBOARD_CONTROLLER = keyboard.KeyboardController()
I_HAVE_NO_IDEA_WHAT_IM_DOING_CONTROLLER = ihavenoideawhatimdoing.IHaveNoIdeaWhatImDoingController()
CONFIGURATION = {
    'arenas': [
        'island',
    ],
    'controllers': [
        # KEYBOARD_CONTROLLER,
        I_HAVE_NO_IDEA_WHAT_IM_DOING_CONTROLLER,
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
         random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
         random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
         random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
         random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
    ],
    'visualise': True,
    'show_sight': I_HAVE_NO_IDEA_WHAT_IM_DOING_CONTROLLER,
    'runs_no': 1,
}
