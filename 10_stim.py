"""10장 · 자극(Stim)
ChannelSet(어디) + StimDesign(어떻게) + BurstDesign(얼마나)를 조합한다.
주의: 안전 한계(위상당 3nC, 3uA, 채널당 200Hz)는 SDK가 자동 검사한다.
"""
import cl
from cl import ChannelSet, StimDesign, BurstDesign

def main():
    with cl.open() as neurons:
        channels = ChannelSet(8, 9, 10)                  # 어디에
        design   = StimDesign(160, -1.0, 160, 1.0)        # 어떻게(이상성·음극 선행)

        # 단발 자극
        neurons.stim(channels, design)
        print("단발 자극 전달")

        # 버스트 자극: 10회를 40Hz로
        burst = BurstDesign(10, 40)                       # 얼마나
        neurons.stim(channels, design, burst)
        print("버스트 자극 전달")

if __name__ == "__main__":
    main()
