"""12장 · 데이터 스트림
내가 만든 데이터(예: 점수)를 시간순으로 기록/시각화에 함께 싣는다.
"""
import cl

def main():
    with cl.open() as neurons:
        stream = neurons.create_data_stream(
            name="game_state",
            attributes={"score": 0},
        )
        recording = neurons.record(stop_after_seconds=1)

        t = neurons.timestamp()
        stream.append(t + 0, {"ball_x": 10, "ball_y": 5})
        stream.append(t + 1, {"ball_x": 11, "ball_y": 6})
        stream.set_attribute("score", 1)

        recording.wait_until_stopped()
    print("데이터 스트림 기록 완료.")

if __name__ == "__main__":
    main()
