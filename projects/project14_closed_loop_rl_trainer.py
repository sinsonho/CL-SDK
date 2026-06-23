"""[프로젝트 14] 폐루프 강화학습 트레이너 (24장 골격의 실행 버전)"""
import cl, random
from cl import ChannelSet, StimDesign

def main():
    reward = StimDesign(160, -1.0, 160, 1.0)
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=10):
            up = sum(1 for s in tick.analysis.spikes if s.channel < 32)
            if up > (len(tick.analysis.spikes) - up):
                neurons.stim(ChannelSet(0, 1), reward)          # 보상(예측 가능)
            else:
                neurons.stim(ChannelSet(random.randint(0, 63)), reward)  # 벌(무작위)

if __name__ == "__main__":
    main()
