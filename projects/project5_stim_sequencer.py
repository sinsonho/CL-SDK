"""[프로젝트 5] 자극 패턴 시퀀서
채널 그룹을 순서대로 돌며 버스트 자극을 흘리는 간단한 시퀀서.
"""
import cl
import time
from cl import ChannelSet, StimDesign, BurstDesign

def main(rounds=3):
    design = StimDesign(160, -1.0, 160, 1.0)
    burst  = BurstDesign(5, 50)
    groups = [ChannelSet(0, 1), ChannelSet(20, 21), ChannelSet(40, 41)]
    with cl.open() as neurons:
        for r in range(rounds):
            for i, g in enumerate(groups):
                neurons.stim(g, design, burst)
                print(f"라운드 {r+1} · 그룹 {i+1} 자극")
                time.sleep(0.2)

if __name__ == "__main__":
    main()
