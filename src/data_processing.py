from statsbombpy import sb
import pandas as pd

def fetch_competitions():
    """Fetches all available competitions from StatsBomb Open Data."""
    competitions = sb.competitions()
    return competitions

def fetch_matches(competition_id, season_id):
    """Fetches matches for a given competition and season."""
    matches = sb.matches(competition_id=competition_id, season_id=season_id)
    return matches

def fetch_event_data(match_id):
    """Fetches event data for a specific match by match_id."""
    events = sb.events(match_id=match_id)
    return events

def preprocess_data(df, event_type='Pass'):
    """Filters and preprocesses event data based on event type (e.g., Pass, Shot)."""
    filtered_events = df[df['type'] == event_type]
    return filtered_events