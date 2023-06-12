import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control

전달함수 G(s) 정의
num = [100] # 분자 계수
den = [1, 5, 6] # 분모 계수: s^2 + 5s + 6
G = control.TransferFunction(num, den)

폐루프 전달함수 T(s) 계산
H = 1  # 피드백 루프의 전달함수 (1이면 피드백이 없는 상태)
T = control.series(G, H)
T = control.minreal(T)  # 최소 실수화

출력 값 출력
st.write('전달함수:')
st.latex(r"\frac{100}{{(s+2)(s+3)+100}}")

시간 벡터 생성
t = np.linspace(0, 10, 1000)

Unit step 입력 생성
u = np.ones_like(t)

시스템 응답 계산
t, y = control.step_response(T, T=t, input=u)

응답곡선 그리기
fig1, ax1 = plt.subplots()
ax1.plot(t, y)
ax1.set_xlabel('Time')
ax1.set_ylabel('Output')
ax1.set_title('Step Response')
ax1.grid(True)

주파수 응답 계산
omega, mag, phase = control.bode(T)

보드선도 그리기
fig2, (ax2, ax3) = plt.subplots(2, 1)
ax2.semilogx(omega, mag)  # 주파수 응답의 크기
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Magnitude (dB)')
ax2.set_title('Bode Plot - Magnitude')
ax2.grid(True)

ax3.semilogx(omega, phase)  # 주파수 응답의 위상
ax3.set_xlabel('Frequency')
ax3.set_ylabel('Phase (degrees)')
ax3.set_title('Bode Plot - Phase')
ax3.grid(True)

그래프를 Streamlit 앱에 출력
st.write('Step Response:')
st.pyplot(fig1)

st.write('Bode Plot:')
st.pyplot(fig2)

시스템 응답 계산
t, y = control.step_response(T, T=t, input=u)

응답곡선 그리기
fig1, ax1 = plt.subplots()
ax1.plot(t, y)
ax1.set_xlabel('Time')
ax1.set_ylabel('Output')
ax1.set_title('Step Response')
ax1.grid(True)

그래프를 Streamlit 앱에 출력
st.write('Step Response:')
st.pyplot(fig1)
