# [논문리뷰]High-Resolution Image Synthesis with Latent Diffusion Models
> [PDF](https://arxiv.org/pdf/2112.10752) / [GitHub](https://github.com/CompVis/latent-diffusion)

---

### 1. Introduction

최근 몇 년 간 생성형 AI의 많은 발전이 되고 있다. 그 중 Diffusion Model은 노이즈를 활용하여 학습을 하고 있다. 고정된 가우시안 분포로 생성된 노이즈를 더한 후 점차 노이즈를 제거해 원본 이미지와 유사한 이미지를 생성한다. 

평균적인 Diffusion Model은 pixel space에서 작동하기 때문에 비용적으로도, 시간 적으로도 많은 노력이 소요된다. 

해당 모델은 pixel space가 아닌 latent space기반으로 학습하게 된다. latent space은 데이터를 압축하여 저차원 표현(벡터)으로 바꾸는 공간으로, 계산량을 줄이면서도 데이터의 중요한 특성을 유지할 수 있다. 사전 학습 된 autoencoder를 사용하여 이미지를 잠재 공간으로 변환하는 것이다. 이렇게 하면 연산량이 크게 줄어들고, 효율적이면서도 고품질 이미지를 생성할 수 있다.

cross-attention layer를 통해 다양한 조건 입력를 효과적으로 통합 할 수 있다.이를 통해 모델은 유연하고 사용자 지정 가능한 이미지 생성이 가능하다.

따라서 LDMs을 사용하게 되면 비용 절감과 생성 속도가 향상되고, 무조건부 이미지 생성, 텍스트-이미지 합성, 초해상도(super-resolution), 이미지 인페인팅(image inpainting), 클래스 조건부 이미지 생성 등 여러 작업에서 우수한 성능을 보여주며, 시각적 품질도 우수하다.


### 2. Related Work

#### 기존 생성모델


**1. Generative Adversarial Networks (GANs)**

작동 원리
- 두 개의 신경망(Generator와 Discriminator)을 이용해 훈련
- Generator는 이미지를 생성하고, Discriminator는 진짜와 가짜 이미지를 구별
- 두 모델이 경쟁하며 점점 더 자연스러운 이미지를 생성하도록 학습

장점
- GAN은 고해상도 이미지를 생성하는 데 매우 뛰어난 성능
- 자연스럽고 세밀한 이미지 합성에서 최상의 품질 제공

한계
- 훈련이 불안정하며, 모드 붕괴(mode collapse)라는 문제가 자주 발생. 이는 Generator가 소수의 데이터 분포만 잘 학습하고 다양한 데이터를 생성하지 못하는 현상 때문
- 데이터 분포를 정확히 학습하기 어려움

**2. Variational Autoencoders (VAEs)**

작동 원리
- 입력 데이터를 잠재 공간(latent space)에 압축(encoding)한 후, 이를 다시 복원(decoding)함
- 생성 과정에서 데이터의 확률 분포를 학습하며, 데이터 샘플링과 생성 가능

장점
- 훈련 과정이 안정적이며, 잠재 공간을 명확하게 정의할 수 있음
- 복잡한 데이터 분포를 다룰 때 유용

한계
- 생성된 이미지의 품질이 낮아, 이미지가 흐릿하거나 디테일 부족

**3. Autoregressive Models (ARMs)**

작동 원리
- 데이터를 순차적으로 생성
- 텍스트 생성, 오디오 합성, 이미지 합성 등 여러 분야에서 사용

장점
- 각 데이터 포인트가 이전 데이터와 조건부 관계를 형성하므로, 밀도 추정이 매우 정확

한계
- 순차적으로 데이터를 생성하기 때문에 계산 속도가 느리고, 고해상도 이미지를 생성하는 데 적합하지 않음

---

#### Diffusion Model

작동 원리
- 노이즈를 추가하는 단계(Forward process)와 이를 제거하며 데이터를 복원하는 단계(Reverse process)로 작동
- 데이터에 점진적으로 노이즈를 추가하며 분포를 단순화한 뒤, 역과정을 통해 데이터를 복원하며 학습

장점
- 안정적인 훈련이 가능하며, 모드 붕괴 문제를 피할 수 있음
- 복잡한 데이터 분포를 효과적으로 학습

한계
- 픽셀 공간에서 작업하기 때문에 계산 비용이 큼
- 추론 속도가 느려, 고해상도 이미지를 생성하는 데 시간이 많이 걸림


#### Latent Space