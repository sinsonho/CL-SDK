"""[프로젝트 4] 채널별 발화율 히트맵 뷰어
3초간 채널별 스파이크 수를 모아 8x8 격자로 출력한다(텍스트 히트맵).
"""
import cl

def main(seconds=3):
    counts = [0] * 64
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=seconds):
            for spike in tick.analysis.spikes:
                counts[spike.channel] += 1
    print("채널별 발화 수 (8x8):")
    for row in range(8):
        line = " ".join(f"{counts[row*8+col]:3d}" for col in range(8))
        print(line)

if __name__ == "__main__":
    main()
