"""[프로젝트 10] 합성 신경신호 생성기
sine_source(14장)를 시뮬레이터 데이터 소스로 연결해 합성 신호를 읽는다.
(11-03 폴더에서 실행)
"""
import os, sys
# sine_source.py 가 있는 상위(교재 소스코드) 폴더를 import 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cl

def main():
    cl.sim.set_simulator_data_source("sine_source:create_source", config={"scale": 80.0})
    try:
        with cl.open() as neurons:
            for tick in neurons.loop(ticks_per_second=50, stop_after_seconds=2):
                pass
            print("합성 신호 재생 완료")
    finally:
        cl.sim.clear_simulator_data_source()

if __name__ == "__main__":
    main()
