"""20장 · 실시간 폐루프 최적화
무거운 준비는 루프 '밖'에서 미리, 루프 '안'은 최대한 가볍게.
지터가 불가피하면 recover_from_jitter()로 그 tick만 넘어간다.
"""
import cl
from cl import StimDesign

def main():
    design = StimDesign(160, -1.0, 160, 1.0)   # 루프 밖에서 미리 만들기
    total = 0
    def on_recover(tick):
        print("지터 복구:", tick.iteration)
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=1000, stop_after_seconds=3):
            n = len(tick.analysis.spikes)        # 가벼운 작업만
            total += n
            if n > 0:
                neurons.stim(tick.analysis.spikes[0].channel, design)
            # 만약 무거운 작업을 했다면:
            # tick.loop.recover_from_jitter(on_recover)
    print("총 스파이크:", total)

if __name__ == "__main__":
    main()
