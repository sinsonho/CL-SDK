"""[프로젝트 2] 자극-반응 테스터
한 채널을 자극하고, 직후 짧은 시간 동안 검출되는 스파이크를 센다.
(시뮬레이터는 자극에 학습/반응하지 않는 대조군이라는 점에 유의)
"""
import cl
from cl import ChannelSet, StimDesign

def main():
    design = StimDesign(160, -1.0, 160, 1.0)
    with cl.open() as neurons:
        neurons.stim(ChannelSet(8), design)
        after = 0
        for tick in neurons.loop(ticks_per_second=1000, stop_after_seconds=1):
            after += len(tick.analysis.spikes)
        print("자극 후 1초간 검출 스파이크:", after)

if __name__ == "__main__":
    main()
