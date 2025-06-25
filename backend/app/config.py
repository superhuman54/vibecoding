import os
from dotenv import load_dotenv
from functools import lru_cache
from typing import Optional

# .env 파일 로드
load_dotenv()


class Settings:
    """애플리케이션 설정 클래스"""
    
    # API 키 설정
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    langsmith_api_key: Optional[str] = os.getenv("LANGSMITH_API_KEY")
    
    # 서버 설정
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # 새로운 기능: 응답 설정
    max_response_length: int = int(os.getenv("MAX_RESPONSE_LENGTH", "1000"))
    default_temperature: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    enable_streaming: bool = os.getenv("ENABLE_STREAMING", "True").lower() == "true"
    
    # 로깅 설정
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    def validate_api_keys(self) -> bool:
        """API 키 유효성 검증"""
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY는 필수 설정입니다")
        return True

@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스 반환 (싱글톤 패턴)"""
    settings = Settings()
    settings.validate_api_keys()
    return settings 