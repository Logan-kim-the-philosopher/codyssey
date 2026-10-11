# 리소스 정리 완료 기록

이 실습의 저장된 리소스 ID만 정리했다. 실행 원본은 `evidence/cleanup-result.json`이다.

| 대상 | 결과 | 근거 |
|---|---|---|
| EC2 | terminated | evidence/terminated-instance.json |
| EBS | 실습 태그 볼륨 없음, 루트 DeleteOnTermination 적용 | evidence/remaining-volumes.json / instance.json |
| Elastic IP | 미생성, 실습 할당 주소 없음 | evidence/resources.json / remaining-addresses.json |
| Internet Gateway | 분리·삭제 완료, 실습 IGW 없음 | evidence/cleanup-result.json / remaining-igws.json |
| VPC | 삭제 완료, 실습 VPC 없음 | evidence/cleanup-result.json / remaining-vpcs.json |
| Subnet / Route Table / SG / 등록 키페어 | 저장된 ID 삭제 성공 | evidence/cleanup-result.json |
| 실습 IAM 역할 및 인라인 정책 | 삭제 명령 성공 | codyssey-b3-1-deployer / B3-1-Ec2VpcOnly |
| NAT Gateway / ALB / RDS | 생성하지 않음 | infra/provision.py / evidence/resources.json |

EC2 종료와 함께 Nginx/Caddy 컨테이너 및 루트 EBS의 인증서 저장 볼륨도 제거됐다. SSH 개인키는 저장소에 포함하지 않았다.
접속 URL은 검증 당시 증빙이며 리소스 정리 후에는 서비스되지 않는다.
무료 플랜과 크레딧은 확인했지만 Billing 최종 비용은 지연 반영될 수 있으므로 0으로 단정하지 않는다. AWS Settings > Billing에서 후속 청구 상태를 확인할 수 있다.
