"""27장 — 지터(jitter)와 회복.

폐루프 한 틱의 시간 예산은 25kHz 기준 40µs.
이 예산을 넘기면 '실제 CL1'은 TimeoutError 를 던진다(시뮬레이터는 경고만).
특정 틱에서 의도적으로 느린 작업을 했다면 recover_from_jitter() 로 회복할 수 있다.
"""
import cl
import time


def on_recovery(tick):
    # 회복 중 건너뛴 틱마다 호출되는 선택적 콜백
    print(f"  회복 중: iteration={tick.iteration}")


def main():
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_ticks=10):
            print(f"정상 틱: iteration={tick.iteration}")

            if tick.iteration == 1:
                # 이 틱에서만 일부러 느린 작업(50ms) → 예산 초과
                time.sleep(50 / 1000)
                # 회복 요청: 밀린 틱을 건너뛰고 따라잡는다(없으면 지터 오류)
                tick.loop.recover_from_jitter(on_recovery)


if __name__ == "__main__":
    main()
