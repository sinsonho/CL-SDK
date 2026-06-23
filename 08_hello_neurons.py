"""8장 · Hello, Neurons — 첫 코드
1초 동안 폐루프를 돌며 검출된 스파이크를 출력한다.
"""
import cl

def main():
    with cl.open() as neurons:
        print("뉴런에 연결되었습니다. 스파이크를 기다립니다...")
        # 1초 동안 초당 100번(tick) 돌면서 스파이크를 출력
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=1):
            for spike in tick.analysis.spikes:
                print(spike)   # 예) Spike(timestamp=..., channel=52)
    print("완료.")

if __name__ == "__main__":
    main()
