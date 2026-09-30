class Video:
    def __init__(self, title: str, duration: float, position: float):
        if duration <= 0:
            raise ValueError("Duration is invalid and must be greater than 0")
        if not (0 <= position <= duration):
            raise ValueError("Position is invalid and must be between 0 and duration")
        
        self.title = title
        self.duration = duration
        self.position = position


    def play(self) -> None:
        print(f"Now Playing {self.title}")

    def advance(self, minutes: float) -> None:
        if minutes < 0:
            raise ValueError("Minutes is invalid and must be greater than 0")
        self.position = min(self.position + minutes, self.duration)

    def is_finished(self) -> bool:
        return self.position >= self.duration

    def restart(self) -> None:
        self.position = 0


