#!/usr/bin/env python3
"""
Test script to explore ESPN API functionality with real league data
Reads configuration from .env file and tests connections to each league
"""

from espn_api.football import League
from espn_api.basketball import League as BasketballLeague
from espn_api.baseball import League as BaseballLeague
import json
from datetime import datetime
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_football_league(league_id, year=2024, espn_s2=None, swid=None):
    """Test NFL/Football API with real league data"""
    print(f"=== NFL/Football API Test - League ID: {league_id}, Year: {year} ===")
    try:
        league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
        print(f"✅ Successfully connected to league: {league.settings.name}")
        
        # Print all available league attributes
        print(f"\n📋 League Object Attributes:")
        for attr in dir(league):
            if not attr.startswith('_'):
                try:
                    value = getattr(league, attr)
                    if not callable(value):
                        print(f"  {attr}: {value}")
                except Exception as e:
                    print(f"  {attr}: [Error accessing: {e}]")
        
        # Print settings attributes
        if hasattr(league, 'settings'):
            print(f"\n⚙️  League Settings Attributes:")
            for attr in dir(league.settings):
                if not attr.startswith('_'):
                    try:
                        value = getattr(league.settings, attr)
                        if not callable(value):
                            print(f"  settings.{attr}: {value}")
                    except Exception as e:
                        print(f"  settings.{attr}: [Error accessing: {e}]")
        
        # Print teams information
        if hasattr(league, 'teams'):
            print(f"\n👥 Teams Information:")
            print(f"  Number of teams: {len(league.teams)}")
            for i, team in enumerate(league.teams, 1):
                print(f"\n  Team {i}:")
                for attr in dir(team):
                    if not attr.startswith('_'):
                        try:
                            value = getattr(team, attr)
                            if not callable(value):
                                print(f"    {attr}: {value}")
                        except Exception as e:
                            print(f"    {attr}: [Error accessing: {e}]")
        
        return league
        
    except Exception as e:
        print(f"❌ Football API error: {e}")
        return None

def test_basketball_league(league_id, year=2024, espn_s2=None, swid=None):
    """Test NBA/Basketball API with real league data"""
    print(f"\n=== NBA/Basketball API Test - League ID: {league_id}, Year: {year} ===")
    try:
        league = BasketballLeague(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
        print(f"✅ Successfully connected to league: {league.settings.name}")
        
        # Print all available league attributes
        print(f"\n📋 League Object Attributes:")
        for attr in dir(league):
            if not attr.startswith('_'):
                try:
                    value = getattr(league, attr)
                    if not callable(value):
                        print(f"  {attr}: {value}")
                except Exception as e:
                    print(f"  {attr}: [Error accessing: {e}]")
        
        # Print settings attributes
        if hasattr(league, 'settings'):
            print(f"\n⚙️  League Settings Attributes:")
            for attr in dir(league.settings):
                if not attr.startswith('_'):
                    try:
                        value = getattr(league.settings, attr)
                        if not callable(value):
                            print(f"  settings.{attr}: {value}")
                    except Exception as e:
                        print(f"  settings.{attr}: [Error accessing: {e}]")
        
        # Print teams information
        if hasattr(league, 'teams'):
            print(f"\n👥 Teams Information:")
            print(f"  Number of teams: {len(league.teams)}")
            for i, team in enumerate(league.teams, 1):
                print(f"\n  Team {i}:")
                for attr in dir(team):
                    if not attr.startswith('_'):
                        try:
                            value = getattr(team, attr)
                            if not callable(value):
                                print(f"    {attr}: {value}")
                        except Exception as e:
                            print(f"    {attr}: [Error accessing: {e}]")
        
        return league
        
    except Exception as e:
        print(f"❌ Basketball API error: {e}")
        return None

def test_baseball_league(league_id, year=2024, espn_s2=None, swid=None):
    """Test MLB/Baseball API with real league data"""
    print(f"\n=== MLB/Baseball API Test - League ID: {league_id}, Year: {year} ===")
    try:
        league = BaseballLeague(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
        print(f"✅ Successfully connected to league: {league.settings.name}")
        
        # Print all available league attributes
        print(f"\n📋 League Object Attributes:")
        for attr in dir(league):
            if not attr.startswith('_'):
                try:
                    value = getattr(league, attr)
                    if not callable(value):
                        print(f"  {attr}: {value}")
                except Exception as e:
                    print(f"  {attr}: [Error accessing: {e}]")
        
        # Print settings attributes
        if hasattr(league, 'settings'):
            print(f"\n⚙️  League Settings Attributes:")
            for attr in dir(league.settings):
                if not attr.startswith('_'):
                    try:
                        value = getattr(league.settings, attr)
                        if not callable(value):
                            print(f"  settings.{attr}: {value}")
                    except Exception as e:
                        print(f"  settings.{attr}: [Error accessing: {e}]")
        
        # Print teams information
        if hasattr(league, 'teams'):
            print(f"\n👥 Teams Information:")
            print(f"  Number of teams: {len(league.teams)}")
            for i, team in enumerate(league.teams, 1):
                print(f"\n  Team {i}:")
                for attr in dir(team):
                    if not attr.startswith('_'):
                        try:
                            value = getattr(team, attr)
                            if not callable(value):
                                print(f"    {attr}: {value}")
                        except Exception as e:
                            print(f"    {attr}: [Error accessing: {e}]")
        
        return league
        
    except Exception as e:
        print(f"❌ Baseball API error: {e}")
        return None

def parse_fantasy_leagues():
    """Parse fantasy leagues from environment variable"""
    leagues = []
    fantasy_leagues_raw = os.environ.get('FANTASY_LEAGUES', '')
    
    if fantasy_leagues_raw:
        for league_str in fantasy_leagues_raw.split(','):
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

def main():
    print("🎮 ESPN Fantasy League API Tester")
    print("=" * 50)
    
    # Read ESPN authentication credentials from environment
    espn_s2 = os.environ.get('ESPN_S2')
    swid = os.environ.get('ESPN_SWID')
    
    if not espn_s2 or not swid:
        print("⚠️  ESPN_S2 or ESPN_SWID not found in .env file.")
        print("   This may not work for private leagues.")
        print("   Add these to your .env file:")
        print("   ESPN_S2=your_espn_s2_cookie_value")
        print("   ESPN_SWID=your_swid_cookie_value")
        espn_s2 = None
        swid = None
    else:
        print("✅ ESPN authentication credentials found in .env file")
    
    # Parse fantasy leagues from environment
    fantasy_leagues = parse_fantasy_leagues()
    
    if not fantasy_leagues:
        print("\n❌ No fantasy leagues configured in .env file.")
        print("   Add FANTASY_LEAGUES to your .env file:")
        print("   FANTASY_LEAGUES=123456789:football:2024:My NFL League,987654321:basketball:2024:My NBA League")
        return
    
    print(f"\n📋 Found {len(fantasy_leagues)} configured fantasy leagues:")
    for i, league in enumerate(fantasy_leagues, 1):
        print(f"  {i}. {league['name']} ({league['sport']} - {league['year']})")
    
    print(f"\n🔍 Testing connections to all configured leagues...")
    
    successful_leagues = []
    failed_leagues = []
    
    for league_config in fantasy_leagues:
        league_id = league_config['league_id']
        sport = league_config['sport']
        year = league_config['year']
        name = league_config['name']
        
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"League ID: {league_id}, Sport: {sport}, Year: {year}")
        print(f"{'='*60}")
        
        # Test based on sport type
        league = None
        if sport == "football":
            league = test_football_league(league_id, year, espn_s2, swid)
        elif sport == "basketball":
            league = test_basketball_league(league_id, year, espn_s2, swid)
        elif sport == "baseball":
            league = test_baseball_league(league_id, year, espn_s2, swid)
        else:
            print(f"❌ Unknown sport: {sport}")
            failed_leagues.append(league_config)
            continue
        
        if league:
            successful_leagues.append({
                'config': league_config,
                'league': league
            })
        else:
            failed_leagues.append(league_config)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"🎯 CONNECTION TEST SUMMARY")
    print(f"{'='*60}")
    print(f"✅ Successful connections: {len(successful_leagues)}")
    print(f"❌ Failed connections: {len(failed_leagues)}")
    
    if successful_leagues:
        print(f"\n✅ Successfully connected leagues:")
        for i, league_data in enumerate(successful_leagues, 1):
            config = league_data['config']
            league = league_data['league']
            print(f"  {i}. {config['name']} ({config['sport']}) - {league.settings.name}")
    
    if failed_leagues:
        print(f"\n❌ Failed to connect to leagues:")
        for i, league_config in enumerate(failed_leagues, 1):
            print(f"  {i}. {league_config['name']} ({league_config['sport']}) - League ID: {league_config['league_id']}")
        print(f"\n💡 Troubleshooting tips:")
        print(f"  - Check if league IDs are correct")
        print(f"  - Verify years are correct")
        print(f"  - Ensure leagues are public or you have access")
        print(f"  - Add ESPN_S2 and ESPN_SWID to .env for private leagues")
    
    if successful_leagues:
        print(f"\n🎉 Successfully connected to {len(successful_leagues)} leagues!")
        print(f"   Review the output above to see all available data for each league.")

if __name__ == "__main__":
    main()
