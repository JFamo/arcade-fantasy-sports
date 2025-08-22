#!/usr/bin/env python3
"""
Configuration file for Arcade Fantasy Sports Display
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'arcade-fantasy-sports-secret-key'
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # ESPN API Authentication
    ESPN_S2 = os.environ.get('ESPN_S2')
    ESPN_SWID = os.environ.get('ESPN_SWID')
    
    # ESPN API Configuration
    ESPN_LEAGUE_ID = os.environ.get('ESPN_LEAGUE_ID')
    ESPN_YEAR = int(os.environ.get('ESPN_YEAR', '2024'))
    ESPN_SPORT = os.environ.get('ESPN_SPORT', 'football')  # football, basketball, baseball
    
    # Display Configuration
    UPDATE_INTERVAL = int(os.environ.get('UPDATE_INTERVAL', '30'))  # seconds
    SCROLL_SPEED = int(os.environ.get('SCROLL_SPEED', '30'))  # seconds for full scroll
    
    # Sample Data Configuration
    ENABLE_SAMPLE_DATA = os.environ.get('ENABLE_SAMPLE_DATA', 'True').lower() == 'true'
    SAMPLE_DATA_UPDATE_CHANCE = float(os.environ.get('SAMPLE_DATA_UPDATE_CHANCE', '0.3'))
    
    # Sports to Display
    ENABLED_SPORTS = {
        'football': True,
        'basketball': True,
        'baseball': True
    }
    
    # Fantasy Leagues Configuration
    # Format: "league_id:sport:year:display_name"
    # Example: "123456789:football:2024:My NFL League"
    FANTASY_LEAGUES_RAW = os.environ.get('FANTASY_LEAGUES', '')
    
    @classmethod
    def get_fantasy_leagues(cls):
        """Parse fantasy leagues from environment variable"""
        leagues = []
        if cls.FANTASY_LEAGUES_RAW:
            for league_str in cls.FANTASY_LEAGUES_RAW.split(','):
                league_str = league_str.strip()
                if ':' in league_str:
                    parts = league_str.split(':')
                    if len(parts) >= 4:
                        leagues.append({
                            'league_id': int(parts[0]),
                            'sport': parts[1],
                            'year': int(parts[2]),
                            'name': parts[3]
                        })
        return leagues
    
    # Visual Configuration
    COLORS = {
        'primary': '#00ff00',      # Green
        'secondary': '#0066ff',    # Blue
        'accent': '#ff6600',       # Orange
        'warning': '#ff0000',      # Red
        'success': '#00ff00',      # Green
        'text': '#ffffff'          # White
    }
    
    # Animation Configuration
    ANIMATIONS = {
        'scroll_duration': 30,     # seconds
        'pulse_duration': 2,       # seconds
        'rainbow_duration': 3      # seconds
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENABLE_SAMPLE_DATA = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENABLE_SAMPLE_DATA = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
