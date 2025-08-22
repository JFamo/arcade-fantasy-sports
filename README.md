# 🎮 Arcade Fantasy Sports Display

A retro arcade-style web application that displays live sports scores and fantasy team performances with classic arcade aesthetics, scrolling animations, and real-time updates.

## ✨ Features

- **Retro Arcade Design**: Classic CRT monitor effects, scanlines, and neon colors
- **Live Sports Scores**: Real-time display of NFL, NBA, and MLB games
- **Fantasy Team Performance**: Live fantasy sports team scores and matchups
- **Scrolling Animations**: Continuous vertical scrolling display
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: Automatic data refresh every 30 seconds
- **ESPN API Integration**: Ready to connect to real ESPN Fantasy League data

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/arcade-fantasy-sports.git
   cd arcade-fantasy-sports
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎯 Usage

### Current Demo Mode

The application currently runs in demo mode with sample data that includes:
- Live NFL games with realistic scores and game states
- NBA basketball games with quarter information
- MLB baseball games with inning details
- Fantasy team matchups with points and win/loss status

### Connecting to Real ESPN Data

To connect to your actual ESPN Fantasy League:

1. **Get your League ID**
   - Log into your ESPN Fantasy League
   - The league ID is in the URL: `https://fantasy.espn.com/football/league?leagueId=YOUR_LEAGUE_ID`

2. **Update the configuration**
   ```python
   # In app.py, uncomment and update these lines:
   league = League(league_id=YOUR_LEAGUE_ID, year=2024)
   ```

3. **Restart the application**

## 🎨 Design Features

### Visual Effects
- **CRT Monitor Simulation**: Scanlines and screen curvature effects
- **Neon Color Scheme**: Green, blue, and orange neon colors
- **Rainbow Header**: Animated gradient header
- **Pulsing Animations**: Live games pulse with red borders
- **Hover Effects**: Interactive card scaling and glow effects

### Typography
- **Orbitron Font**: Futuristic monospace font for authentic arcade feel
- **Text Shadows**: Glowing text effects
- **Uppercase Styling**: Bold, arcade-style text formatting

### Animations
- **Continuous Scrolling**: Vertical scrolling of content
- **Pulse Effects**: Live games and status indicators
- **Rainbow Animation**: Animated header gradient
- **Hover Transitions**: Smooth scaling and glow effects

## 📊 API Endpoints

### `/api/sports-data`
Returns current sports and fantasy data in JSON format.

**Response Example:**
```json
{
  "timestamp": "2024-08-22T01:06:17.123456",
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
    }
  ]
}
```

### `/api/fantasy-league/<league_id>/<year>`
Returns fantasy league data for a specific ESPN league.

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask web framework
- **Data Updates**: Background thread updates data every 30 seconds
- **API Integration**: ESPN API for fantasy sports data
- **Sample Data**: Realistic sample data for demonstration

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Mobile-friendly layout
- **Real-time Updates**: AJAX calls to update display
- **CSS Animations**: Pure CSS animations for performance
- **Modern JavaScript**: ES6+ features and async/await

### Dependencies
- `flask`: Web framework
- `espn_api`: ESPN Fantasy Sports API
- `python-dotenv`: Environment variable management
- `requests`: HTTP library

## 🎮 Customization

### Adding New Sports
1. Update the `get_sample_sports_data()` function in `app.py`
2. Add new sport section to the HTML template
3. Update the JavaScript rendering logic

### Changing Colors
Modify the CSS variables in `templates/arcade_display.html`:
```css
:root {
  --primary-color: #00ff00;
  --secondary-color: #0066ff;
  --accent-color: #ff6600;
}
```

### Adjusting Animation Speed
Change the scroll animation duration in the CSS:
```css
.scrolling-content {
  animation: scroll-up 30s linear infinite; /* 30s = 30 seconds */
}
```

## 🔧 Development

### Project Structure
```
arcade-fantasy-sports/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── test_espn_api.py      # ESPN API testing script
├── templates/
│   └── arcade_display.html  # Main HTML template
└── README.md             # This file
```

### Running Tests
```bash
python test_espn_api.py
```

### Development Server
```bash
python app.py
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:
- **Gunicorn**: WSGI server
- **Nginx**: Reverse proxy
- **Docker**: Containerization
- **Environment Variables**: Secure configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- ESPN API for fantasy sports data
- Google Fonts for the Orbitron font
- Flask community for the web framework
- Retro gaming community for design inspiration

## 🆘 Support

If you encounter any issues:
1. Check the console for error messages
2. Verify your ESPN league ID is correct
3. Ensure all dependencies are installed
4. Check that port 5000 is available

---

**🎮 Ready to display your fantasy sports data in retro arcade style! 🎮**

