"""23장 · 발작 유사 과활동 탐지 → 자극 중재 (폐루프)
짧은 구간의 발화 수가 임계치를 넘으면 '과활동'으로 보고 중재 자극을 보낸다.
신경 활동 자체를 바이오마커로 쓰는 폐루프 중재의 골격.
"""
import cl
from cl import ChannelSet, StimDesign

def main(threshold=40):
    therapy = StimDesign(160, -1.0, 160, 1.0)
    window = 0
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=10):
            window += len(tick.analysis.spikes)
            if tick.iteration % 10 == 9:          # 0.1초마다 점검
                if window > threshold:             # 과활동 탐지
                    neurons.stim(ChannelSet(range(0, 16)), therapy)  # 중재 자극
                    print(f"과활동({window}) 감지 → 중재 자극")
                window = 0

if __name__ == "__main__":
    main()
