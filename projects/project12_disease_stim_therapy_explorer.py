"""[프로젝트 12] 질환 모델 자극치료 탐색기 — 자극 파라미터를 바꿔 가며 효과 비교"""
import cl
from cl import ChannelSet, StimDesign

def trial(neurons, current):
    design = StimDesign(160, -current, 160, current)
    neurons.stim(ChannelSet(range(0, 16)), design)
    after = 0
    for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=1):
        after += len(tick.analysis.spikes)
    return after

def main():
    with cl.open() as neurons:
        for current in (0.5, 1.0, 1.5):
            print(f"전류 {current}uA → 이후 1초 발화:", trial(neurons, current))

if __name__ == "__main__":
    main()
