"""11장 · 폐루프 loop()
검출된 스파이크에 같은 채널 자극으로 반응하는 간단한 폐루프.
지터(시간 예산 초과)가 의심되면 recover_from_jitter()로 복구할 수 있다.
"""
import cl
from cl import StimDesign

def main():
    design = StimDesign(160, -1.0, 160, 1.0)
    with cl.open() as neurons:
        # 초당 1000번, 3초 동안: 스파이크에 반응해 같은 채널을 자극
        for tick in neurons.loop(ticks_per_second=1000, stop_after_seconds=3):
            for spike in tick.analysis.spikes:
                neurons.stim(spike.channel, design)
    print("폐루프 종료.")

if __name__ == "__main__":
    main()
