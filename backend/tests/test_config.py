import pytest
import os
from unittest.mock import patch
from app.config import Settings, get_settings


def test_settings_defaults():
    """기본 설정값 테스트"""
    assert settings.HOST == "0.0.0.0"
    assert settings.PORT == 8000
    assert isinstance(settings.DEBUG, bool)


def test_settings_types():
    """설정값 타입 테스트"""
    assert isinstance(settings.HOST, str)
    assert isinstance(settings.PORT, int)
    assert isinstance(settings.DEBUG, bool)


class TestSettings:
    """Settings 클래스 테스트"""
    
    def test_default_settings(self):
        """기본 설정값 테스트"""
        settings = Settings()
        
        assert settings.host == "0.0.0.0"
        assert settings.port == 8000
        assert settings.debug == False
        assert settings.max_response_length == 1000
        assert settings.default_temperature == 0.7
        assert settings.enable_streaming == True
        assert settings.log_level == "INFO"
    
    @patch.dict(os.environ, {
        "HOST": "127.0.0.1",
        "PORT": "3000",
        "DEBUG": "true",
        "MAX_RESPONSE_LENGTH": "2000",
        "DEFAULT_TEMPERATURE": "0.9",
        "ENABLE_STREAMING": "false",
        "LOG_LEVEL": "DEBUG"
    })
    def test_environment_settings(self):
        """환경변수 설정 테스트"""
        settings = Settings()
        
        assert settings.host == "127.0.0.1"
        assert settings.port == 3000
        assert settings.debug == True
        assert settings.max_response_length == 2000
        assert settings.default_temperature == 0.9
        assert settings.enable_streaming == False
        assert settings.log_level == "DEBUG"
    
    @patch.dict(os.environ, {"GOOGLE_API_KEY": ""})
    def test_api_key_validation_failure(self):
        """API 키 검증 실패 테스트"""
        settings = Settings()
        
        with pytest.raises(ValueError, match="GOOGLE_API_KEY는 필수 설정입니다"):
            settings.validate_api_keys()
    
    @patch.dict(os.environ, {"GOOGLE_API_KEY": "test-api-key"})
    def test_api_key_validation_success(self):
        """API 키 검증 성공 테스트"""
        settings = Settings()
        
        assert settings.validate_api_keys() == True
        assert settings.google_api_key == "test-api-key"
    
    @patch.dict(os.environ, {"LANGSMITH_API_KEY": "langsmith-key"})
    def test_optional_api_key(self):
        """선택적 API 키 테스트"""
        settings = Settings()
        
        assert settings.langsmith_api_key == "langsmith-key"
    
    def test_type_conversions(self):
        """타입 변환 테스트"""
        with patch.dict(os.environ, {
            "PORT": "8080",
            "MAX_RESPONSE_LENGTH": "1500",
            "DEFAULT_TEMPERATURE": "0.5"
        }):
            settings = Settings()
            
            assert isinstance(settings.port, int)
            assert isinstance(settings.max_response_length, int)
            assert isinstance(settings.default_temperature, float)
            assert isinstance(settings.debug, bool)
            assert isinstance(settings.enable_streaming, bool)


class TestGetSettings:
    """get_settings 함수 테스트"""
    
    @patch.dict(os.environ, {"GOOGLE_API_KEY": "test-key"})
    def test_get_settings_returns_same_instance(self):
        """싱글톤 패턴 테스트"""
        settings1 = get_settings()
        settings2 = get_settings()
        
        assert settings1 is settings2
    
    @patch.dict(os.environ, {"GOOGLE_API_KEY": "test-key"})
    def test_get_settings_validates_keys(self):
        """get_settings가 API 키 검증을 수행하는지 테스트"""
        settings = get_settings()
        
        assert settings.google_api_key == "test-key" 