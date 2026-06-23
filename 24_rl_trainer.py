"""24장 · 폐루프 강화학습 트레이너 (DishBrain식 골격)
'좋은 행동'에는 예측 가능한(규칙적) 자극을, '나쁜 행동'에는 예측 불가능한(무작위) 자극을 준다.
자유에너지 원리: 놀라움을 줄이려는 성질이 학습을 유도한다(실제 학습은 CL1에서).
"""
import cl, random
from cl import ChannelSet, StimDesign

def main():
    regular = StimDesign(160, -1.0, 160, 1.0)
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=10):
            up = sum(1 for s in tick.analysis.spikes if s.channel < 32)
            good = up > (len(tick.analysis.spikes) - up)      # 행동 평가(예시 규칙)
            if good:
                neurons.stim(ChannelSet(0, 1), regular)        # 예측 가능 = 보상
            else:
                ch = random.randint(0, 63)
                neurons.stim(ChannelSet(ch), regular)          # 예측 불가능 = 벌

if __name__ == "__main__":
    main()
