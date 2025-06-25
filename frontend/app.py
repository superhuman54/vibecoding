import streamlit as st
import requests
import time
import os
import json
from typing import Dict, Any

# 페이지 설정
st.set_page_config(
    page_title="VibeCoding AI 챗봇",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 상수 설정
BACKEND_URL = "http://localhost:8000/chat/"
REQUEST_TIMEOUT = 5 if os.getenv("STREAMLIT_TESTING") else 30  # 테스트 환경에서는 짧은 타임아웃

def call_backend_api(message: str) -> str:
    """백엔드 API 호출 함수"""
    try:
        with st.spinner("AI가 상품을 검색 중입니다..."):
            response = requests.post(
                BACKEND_URL,
                json={"message": message},
                timeout=REQUEST_TIMEOUT
            )
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data.get("response", "응답을 받을 수 없습니다.")
            else:
                return f"서버 오류가 발생했습니다. (상태 코드: {response.status_code})"
                
    except requests.exceptions.ConnectionError:
        return "백엔드 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요."
    except requests.exceptions.Timeout:
        return "요청 시간이 초과되었습니다. 다시 시도해주세요."
    except requests.exceptions.RequestException as e:
        return f"요청 중 오류가 발생했습니다: {str(e)}"
    except Exception as e:
        return f"예상치 못한 오류가 발생했습니다: {str(e)}"

def display_response_with_stream(response: str):
    """응답을 스트리밍 방식으로 표시"""
    # 테스트 환경에서는 스트리밍 효과 생략
    if os.getenv("STREAMLIT_TESTING"):
        st.markdown(response)
        return response
    
    placeholder = st.empty()
    displayed_text = ""
    
    for char in response:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(0.02)  # 타이핑 효과
    
    return response

def main():
    """메인 애플리케이션"""
    st.title("🤖 VibeCoding AI 챗봇")
    st.markdown("---")
    
    # 사이드바 설정
    with st.sidebar:
        st.header("⚙️ 설정")
        
        # 새로운 기능: 응답 설정
        temperature = st.slider(
            "응답 창의성",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="높을수록 더 창의적인 응답을 생성합니다"
        )
        
        max_length = st.selectbox(
            "최대 응답 길이",
            options=[500, 1000, 1500, 2000],
            index=1,
            help="응답의 최대 길이를 설정합니다"
        )
        
        enable_search = st.checkbox(
            "웹 검색 활성화",
            value=True,
            help="실시간 웹 검색을 통한 최신 정보 제공"
        )
        
        st.markdown("---")
        if st.button("🔄 대화 초기화"):
            if "messages" in st.session_state:
                st.session_state.messages = []
                st.rerun()
    
    # 메인 채팅 영역
    chat_container = st.container()
    
    # 세션 상태 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # 환영 메시지
        welcome_msg = """안녕하세요! 👋 

저는 **VibeCoding AI 챗봇**입니다. 
실시간 웹 검색을 통해 최신 정보를 제공하고, 다양한 질문에 답변드릴 수 있습니다.

**새로운 기능:**
- 🎯 응답 창의성 조절
- 📏 응답 길이 설정  
- 🔍 실시간 웹 검색
- 💾 대화 기록 관리

궁금한 것이 있으시면 언제든 물어보세요!"""
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome_msg
        })
    
    # 이전 대화 기록 표시
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # 새 메시지 입력
    if prompt := st.chat_input("메시지를 입력하세요..."):
        # 사용자 메시지 추가
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt
        })
        
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # AI 응답 생성
            with st.chat_message("assistant"):
                with st.spinner("🤔 생각 중..."):
                    response = get_ai_response(
                        prompt, 
                        temperature=temperature,
                        max_length=max_length,
                        enable_search=enable_search
                    )
                    st.markdown(response)
                    
                    # 응답을 세션에 저장
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response
                    })

def get_ai_response(
    message: str, 
    temperature: float = 0.7,
    max_length: int = 1000,
    enable_search: bool = True
) -> str:
    """AI 응답 생성"""
    try:
        # 백엔드 API 호출
        payload = {
            "message": message,
            "settings": {
                "temperature": temperature,
                "max_length": max_length,
                "enable_search": enable_search
            }
        }
        
        # TODO: 실제 백엔드 API 연동
        # response = requests.post("http://localhost:8000/chat", json=payload)
        # if response.status_code == 200:
        #     return response.json()["response"]
        
        # 임시 응답 (백엔드 연동 전)
        return f"""**설정된 옵션으로 응답 생성 중...**

📝 **질문:** {message}
⚙️ **설정:**
- 창의성: {temperature}
- 최대 길이: {max_length}자
- 웹 검색: {'활성화' if enable_search else '비활성화'}

💡 실제 AI 응답은 백엔드 API가 연동되면 제공됩니다.
현재는 개발 중인 기능입니다! 🚀"""
        
    except Exception as e:
        st.error(f"❌ 오류가 발생했습니다: {str(e)}")
        return "죄송합니다. 일시적인 오류가 발생했습니다. 다시 시도해 주세요."

if __name__ == "__main__":
    main()

# 사이드바에 추가 정보
with st.sidebar:
    st.header("💡 사용법")
    st.markdown("""
    1. 아래 채팅창에 찾고 싶은 상품명을 입력하세요
    2. AI가 웹에서 상품 정보를 검색합니다
    3. 검색 결과와 추천 상품을 확인하세요
    
    **예시 질문:**
    - "iPhone 15 Pro 가격 알려줘"
    - "노트북 추천해줘"
    - "무선 이어폰 비교해줘"
    """)
    
    if st.button("채팅 기록 삭제"):
        st.session_state.messages = []
        st.rerun() 