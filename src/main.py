from data_processing import fetch_competitions, fetch_matches, fetch_event_data, preprocess_data
from visualizations import create_visualizations

if __name__ == '__main__':
    # Step 1: Fetch and display competitions
    competitions = fetch_competitions()
    print(competitions.head())  # Display available competitions
    
    # Step 2: Fetch matches for a specific competition and season
    competition_id = 43 
    season_id = 3 
    matches = fetch_matches(competition_id=competition_id, season_id=season_id)
    print(matches.head()) 

    # Step 3: Fetch event data for a specific match (e.g., match_id=3889182)
    match_id = 3889182
    events = fetch_event_data(match_id=match_id)

    # Step 4: Preprocess event data (filtering passes in this case)
    passes_data = preprocess_data(events, event_type='Pass')

    # Step 5: Create and show visualizations based on the passes data
    create_visualizations(passes_data)