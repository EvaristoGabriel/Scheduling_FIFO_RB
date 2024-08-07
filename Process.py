class Process:
    def __init__(self, name, start_time, execution_time, priority):
        self.name = name
        self.execution_time = float(execution_time)
        self.start_time = float(start_time)
        self.priority = int(priority)
        self.tempo_sobrando = self.execution_time
        self.start = []
        self.end = []

    def start_t(self,tempo_atual):
        self.start.append(tempo_atual)

    def end_t(self,tempo_atual):
        self.end.append(tempo_atual)

    def quantum(self,quantum):
        self.tempo_sobrando -= quantum
    
    def get_tempo(self):
        return self.tempo_sobrando
    
    def __str__(self):
        return f"{self.name}, {self.start_time}, {self.execution_time}, {self.tempo_sobrando}, {self.start}, {self.end}"