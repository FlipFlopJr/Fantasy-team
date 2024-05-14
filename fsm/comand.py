from aiogram.fsm.state import StatesGroup, State


class TeamState(StatesGroup):
    point_guard = State()
    shooting_guard = State()
    small_forward = State()
    power_forward = State()
    center = State()