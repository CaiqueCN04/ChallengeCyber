from pydantic import BaseModel
from typing import Annotated
from pydantic import Field

class InputData(BaseModel):
    daily_bets: int
    avg_bet_amount: float
    sessions_per_day: int
    time_spent_minutes: float
    lost_money_days: int
    won_money_days: int
    self_exclusion_attempts: int
    account_age_days: int

               