"""[프로젝트 6] 뉴런 Pong (폐루프 학습 데모, 단순화 버전)
게임 상태를 data_stream에 남기며, 스파이크로 패들을 움직이는 폐루프 골격.
(시뮬레이터는 학습하지 않는 대조군이므로 '점수가 오르는' 학습은 CL1에서)
"""
import cl

def main():
    with cl.open() as neurons:
        state = neurons.create_data_stream(name="pong", attributes={"score": 0})
        paddle_y, ball_y, score = 0, 0, 0
        for tick in neurons.loop(ticks_per_second=100, stop_after_seconds=5):
            # 위/아래 채널의 발화로 패들을 움직인다
            up = sum(1 for s in tick.analysis.spikes if s.channel < 32)
            paddle_y += (up - (len(tick.analysis.spikes) - up))
            ts = neurons.timestamp()
            state.append(ts, {"paddle_y": paddle_y, "ball_y": ball_y})
        print("최종 패들 위치:", paddle_y)

if __name__ == "__main__":
    main()
