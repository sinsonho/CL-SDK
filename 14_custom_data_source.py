"""14장 · 시뮬레이터에 커스텀 소스를 연결해 읽어 본다.
(이 파일이 있는 폴더에서 실행해야 sine_source 모듈이 import 된다)
"""
import cl

def main():
    cl.sim.set_simulator_data_source("sine_source:create_source", config={"scale": 50.0})
    try:
        with cl.open() as neurons:
            frames = neurons.read(250)
            print("커스텀 소스 프레임:", frames.shape)   # (250, 64)
    finally:
        cl.sim.clear_simulator_data_source()   # 기본 소스로 복원

if __name__ == "__main__":
    main()
