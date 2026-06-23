"""[프로젝트 15] 뇌전증 발작 탐지·중재 시스템 (23장 골격의 실행 버전)"""
import cl
from cl import ChannelSet, StimDesign

def main(threshold=40):
    therapy = StimDesign(160, -1.0, 160, 1.0)
    window = 0
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=10):
            window += len(tick.analysis.spikes)
            if tick.iteration % 10 == 9:
                if window > threshold:
                    neurons.stim(ChannelSet(range(0, 16)), therapy)
                    print(f"과활동({window}) → 중재")
                window = 0

if __name__ == "__main__":
    main()
