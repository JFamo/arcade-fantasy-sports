#!/usr/bin/env python3
"""
Retro Arcade Fantasy Sports Display
A Flask web application that displays live sports scores and fantasy team performances
in a retro arcade style interface.
"""

from flask import Flask, render_template, jsonify
from espn_api.football import League
from espn_api.basketball import League as BasketballLeague
from espn_api.baseball import League as BaseballLeague
import json
import os
from datetime import datetime
import time
import threading
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Global data storage
sports_data = {
    "timestamp": datetime.now().isoformat(),
    "sports": {
        "football": {"games": []},
        "basketball": {"games": []},
        "baseball": {"games": []}
    },
    "fantasy_teams": []
}

def get_sample_sports_data():
    """Generate sample sports data for demonstration"""
    return {
        "timestamp": datetime.now().isoformat(),
        "sports": {
            "football": {
                "games": [
                    {
                        "home_team": "Kansas City Chiefs",
                        "away_team": "Buffalo Bills",
                        "home_score": 24,
                        "away_score": 20,
                        "quarter": "Final",
                        "time_remaining": "0:00",
                        "status": "Final"
                    },
                    {
                        "home_team": "San Francisco 49ers",
                        "away_team": "Dallas Cowboys",
                        "home_score": 17,
                        "away_score": 14,
                        "quarter": "Q3",
                        "time_remaining": "8:45",
                        "status": "Live"
                    },
                    {
                        "home_team": "Green Bay Packers",
                        "away_team": "Chicago Bears",
                        "home_score": 28,
                        "away_score": 21,
                        "quarter": "Q4",
                        "time_remaining": "2:15",
                        "status": "Live"
                    }
                ]
            },
            "basketball": {
                "games": [
                    {
                        "home_team": "Los Angeles Lakers",
                        "away_team": "Golden State Warriors",
                        "home_score": 108,
                        "away_score": 105,
                        "quarter": "Q4",
                        "time_remaining": "2:30",
                        "status": "Live"
                    },
                    {
                        "home_team": "Boston Celtics",
                        "away_team": "Miami Heat",
                        "home_score": 95,
                        "away_score": 92,
                        "quarter": "Q3",
                        "time_remaining": "5:20",
                        "status": "Live"
                    }
                ]
            },
            "baseball": {
                "games": [
                    {
                        "home_team": "New York Yankees",
                        "away_team": "Boston Red Sox",
                        "home_score": 6,
                        "away_score": 4,
                        "inning": "8",
                        "status": "Live"
                    }
                ]
            }
        },
        "fantasy_teams": [
            {
                "name": "Team Alpha",
                "owner": "John Doe",
                "points": 145.6,
                "opponent": "Team Beta",
                "opponent_points": 132.3,
                "status": "Winning",
                "league": "NFL Fantasy"
            },
            {
                "name": "Team Beta",
                "owner": "Jane Smith",
                "points": 132.3,
                "opponent": "Team Alpha",
                "opponent_points": 145.6,
                "status": "Losing",
                "league": "NFL Fantasy"
            },
            {
                "name": "Dunk Masters",
                "owner": "Mike Johnson",
                "points": 112.8,
                "opponent": "Three Point Kings",
                "opponent_points": 108.4,
                "status": "Winning",
                "league": "NBA Fantasy"
            },
            {
                "name": "Three Point Kings",
                "owner": "Sarah Wilson",
                "points": 108.4,
                "opponent": "Dunk Masters",
                "opponent_points": 112.8,
                "status": "Losing",
                "league": "NBA Fantasy"
            }
        ]
    }

def update_sports_data():
    """Update sports data periodically"""
    global sports_data
    
    # For now, use sample data
    # In production, you would fetch real data from ESPN API
    sports_data = get_sample_sports_data()
    
    # Simulate some data changes
    import random
    if sports_data["sports"]["football"]["games"]:
        game = sports_data["sports"]["football"]["games"][1]
        if game["status"] == "Live":
            # Randomly update scores
            if random.random() < 0.3:  # 30% chance to update
                game["home_score"] += random.randint(0, 3)
                game["away_score"] += random.randint(0, 3)
    
    if sports_data["fantasy_teams"]:
        for team in sports_data["fantasy_teams"]:
            if random.random() < 0.2:  # 20% chance to update
                team["points"] += random.uniform(0.1, 2.0)
                team["opponent_points"] += random.uniform(0.1, 2.0)
                # Update status
                if team["points"] > team["opponent_points"]:
                    team["status"] = "Winning"
                else:
                    team["status"] = "Losing"

def data_update_loop():
    """Background thread to update data"""
    while True:
        update_sports_data()
        time.sleep(30)  # Update every 30 seconds

@app.route('/')
def index():
    """Main arcade display page"""
    return render_template('arcade_display.html')

@app.route('/api/sports-data')
def get_sports_data():
    """API endpoint to get current sports data"""
    return jsonify(sports_data)

@app.route('/api/fantasy-league/<int:league_id>/<int:year>')
def get_fantasy_league_data(league_id, year):
    """API endpoint to get fantasy league data from ESPN"""
    try:
        # You would need to provide your actual ESPN credentials
        # league = League(league_id=league_id, year=year)
        # return jsonify({
        #     "teams": [{"name": team.team_name, "owner": team.owner} for team in league.teams],
        #     "scoreboard": league.scoreboard()
        # })
        
        # For now, return sample data
        return jsonify({
            "message": "Fantasy league data endpoint - requires ESPN credentials",
            "league_id": league_id,
            "year": year
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start background data update thread
    update_thread = threading.Thread(target=data_update_loop, daemon=True)
    update_thread.start()
    
    # Initialize with sample data
    update_sports_data()
    
    print("🎮 Retro Arcade Fantasy Sports Display Starting...")
    print("🌐 Open your browser to: http://localhost:5000")
    print("📊 API endpoint: http://localhost:5000/api/sports-data")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
