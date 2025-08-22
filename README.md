# 🎮 Arcade Fantasy Sports Display

Retro arcade-style web app displaying live sports scores and fantasy team performances.

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## Connect to ESPN Fantasy Leagues

1. **Create `.env` file**

   ```bash
   cp env_example.txt .env
   ```

2. **Add your leagues to `.env`**

   ```
   ESPN_S2=your_espn_s2_cookie_value
   ESPN_SWID=your_swid_cookie_value
   FANTASY_LEAGUES=123456789:football:2024:My NFL League
   ```

3. **Test connection**
   ```bash
   python test_real_league.py
   ```

## Dependencies

- `flask`: Web framework
- `espn_api`: ESPN Fantasy Sports API
- `python-dotenv`: Environment variables
- `requests`: HTTP library

## League Format

`league_id:sport:year:display_name`

Example: `123456789:football:2024:My NFL League`
