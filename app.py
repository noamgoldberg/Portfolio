from typing import Dict, Optional
import streamlit as st
import streamlit.components.v1 as components


PROJECTS = {
    "Music Downloader": {
        "icon" : "🎵",
        "url" : "https://music-downloader.streamlit.app/",
        "description": (
            "Download songs or playlists from Spotify, YouTube, "
            "and SoundCloud. Input a list of URLs and download songs individually "
            "or in a single zip file. Manage everything in a single, convenient interface."
        ),
    },
    "Stock Portfolio Performance Simulator": {
        "icon": "📈",
        "url": "https://stocks-portfolio-optimization.streamlit.app",
        "description": (
            "The Stock Portfolio Performance Simulator helps users evaluate a set of stocks "
            "and generate an optimized portfolio with the highest Sharpe Ratio. Users can input "
            "stock tickers and set a date range for analysis, extracting and analyzing historical "
            "data to compute risk-adjusted returns. The tool uses Sequential Least Squares "
            "Programming to determine optimal portfolio weights and uses a Monte Carlo simulation "
            "to visualize projected performance, allowing users to assess Value at Risk (VaR) and "
            "Conditional Value at Risk (CVaR) at different confidence levels."
        ),
    }
}


def display_embed_iframe(
    embed_url: Optional[str] = None,
    height: int = 450,
    width_pct: float = 1
):
    if embed_url is not None:
        iframe = f"""<iframe
            src="{embed_url}"
            style="height: {height}px; width: {width_pct * 100}%;"
        ></iframe>
        """
        components.html(iframe)

def display_project(
    project_name: str,
    project_config: Dict[str, str]
):
    project_name = project_name.strip()
    num_words_title = len(project_name.split())
    with st.container(border=True):
        icon = project_config["icon"]
        url = project_config["url"]
        description = project_config["description"]
        header_str = f"{icon} [{project_name}]({url})"
        if num_words_title > 2:
            st.header(header_str)
        col1, col2 = st.columns([1,1])
        with col1:
            if num_words_title <= 2:
                st.header(header_str)
            st.write(description)
            st.link_button("View Project", url=url)
        with col2:
            with st.container(border=True):
                image_filename = f"{project_name.lower().replace(' ', '_')}.jpg"
                image_filepath = f"images/{image_filename}"
                st.image(image_filepath)


def display_projects():
    for project_name, project_config in PROJECTS.items():
        display_project(
            project_name=project_name,
            project_config=project_config,
        )

def main():
    st.title("Noam Goldberg's Projects")
    display_projects()

if __name__ == "__main__":
    main()