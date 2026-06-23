"""[프로젝트 1] 실시간 스파이크 모니터
초당 발화 수를 1초 간격으로 출력하는 가장 단순한 모니터.
"""
import cl

def main(seconds=5):
    with cl.open() as neurons:
        counts = {}
        for tick in neurons.loop(ticks_per_second=10, stop_after_seconds=seconds):
            sec = tick.iteration // 10
            counts.setdefault(sec, 0)
            counts[sec] += len(tick.analysis.spikes)
            if tick.iteration % 10 == 9:
                print(f"{sec+1}초: {counts[sec]} 스파이크")

if __name__ == "__main__":
    main()
