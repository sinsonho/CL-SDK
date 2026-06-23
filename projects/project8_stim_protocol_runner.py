"""[프로젝트 8] 자극 프로토콜 실험 러너
미리 짜 둔 자극 계획(stim plan)을 기록과 함께 실행한다.
"""
import cl
from cl import ChannelSet, StimDesign, BurstDesign

def main():
    with cl.open() as neurons:
        plan = neurons.create_stim_plan()
        plan.stim(ChannelSet(8, 9), StimDesign(160, -1.0, 160, 1.0), BurstDesign(10, 40))
        plan.stim(ChannelSet(20, 21), StimDesign(100, -1.5, 100, 1.5), BurstDesign(10, 40))
        rec = neurons.record(stop_after_seconds=2)
        plan.run()
        rec.wait_until_stopped()
        print("프로토콜 실행·기록 완료:", rec.file["path"])

if __name__ == "__main__":
    main()
