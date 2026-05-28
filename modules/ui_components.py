"""
ResumeCraft AI Studio - UI Components
Shared Streamlit UI helpers: score cards, gauges, charts, etc.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Optional
import base64


# ─────────────────────────────────────────────────────────────────────────────
# COLOR SCHEME
# ─────────────────────────────────────────────────────────────────────────────

COLORS = {
    'primary': '#6C63FF',
    'secondary': '#4ECDC4',
    'success': '#2ECC71',
    'warning': '#F39C12',
    'danger': '#E74C3C',
    'dark': '#1a1a2e',
    'medium': '#16213e',
    'light': '#0f3460',
    'text': '#e0e0e0',
    'card_bg': '#1e2a3a',
}


def score_color(score: int) -> str:
    """Return color based on score value."""
    if score >= 80:
        return COLORS['success']
    elif score >= 60:
        return '#27AE60'
    elif score >= 45:
        return COLORS['warning']
    elif score >= 30:
        return '#E67E22'
    else:
        return COLORS['danger']


def score_label(score: int) -> str:
    """Return text label for score."""
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 55:
        return "Average"
    elif score >= 40:
        return "Needs Work"
    else:
        return "Poor"


# ─────────────────────────────────────────────────────────────────────────────
# SCORE GAUGE CHART
# ─────────────────────────────────────────────────────────────────────────────

def render_score_gauge(score: int, title: str = "ATS Score", max_score: int = 100):
    """Render a donut/gauge chart for a score."""
    color = score_color(score)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': title, 'font': {'size': 16, 'color': '#e0e0e0'}},
        number={'font': {'size': 36, 'color': color}, 'suffix': f'/{max_score}'},
        gauge={
            'axis': {'range': [0, max_score], 'tickcolor': '#888', 'tickfont': {'color': '#888'}},
            'bar': {'color': color, 'thickness': 0.35},
            'bgcolor': '#1e2a3a',
            'borderwidth': 0,
            'steps': [
                {'range': [0, max_score * 0.4], 'color': '#2d1b1b'},
                {'range': [max_score * 0.4, max_score * 0.7], 'color': '#2d2a1b'},
                {'range': [max_score * 0.7, max_score], 'color': '#1b2d1e'},
            ],
            'threshold': {
                'line': {'color': '#ffffff', 'width': 2},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#e0e0e0'},
        height=220,
        margin=dict(t=60, b=10, l=30, r=30),
    )
    st.plotly_chart(fig, use_container_width=True)


def render_score_donut(score: int, title: str = "Score", size: int = 180):
    """Render a compact donut chart."""
    color = score_color(score)
    fig = go.Figure(data=[go.Pie(
        values=[score, 100 - score],
        hole=0.72,
        marker=dict(colors=[color, '#2d3748']),
        showlegend=False,
        textinfo='none',
        hoverinfo='skip',
    )])
    fig.add_annotation(
        text=f"<b>{score}</b>",
        x=0.5, y=0.5,
        font=dict(size=28, color=color, family='Arial'),
        showarrow=False
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=size,
        margin=dict(t=5, b=5, l=5, r=5),
        title=dict(text=title, x=0.5, font=dict(size=12, color='#aaa')),
    )
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION SCORE BAR CHART
# ─────────────────────────────────────────────────────────────────────────────

def render_section_scores_chart(sections: Dict):
    """Render horizontal bar chart of section scores."""
    labels = []
    scores = []
    maxes = []

    label_map = {
        'contact_info': 'Contact Info',
        'professional_summary': 'Summary',
        'education': 'Education',
        'skills': 'Skills',
        'experience_projects': 'Experience/Projects',
        'action_verbs': 'Action Verbs',
        'quantified_achievements': 'Quantified Results',
        'ats_formatting': 'ATS Formatting',
        'length_readability': 'Length & Readability',
    }

    for key, data in sections.items():
        labels.append(label_map.get(key, key))
        scores.append(data['score'])
        maxes.append(data['max'])

    pcts = [s / m * 100 for s, m in zip(scores, maxes)]
    colors = [score_color(int(p)) for p in pcts]

    fig = go.Figure(go.Bar(
        x=scores,
        y=labels,
        orientation='h',
        marker=dict(color=colors),
        text=[f"{s}/{m}" for s, m in zip(scores, maxes)],
        textposition='outside',
        textfont=dict(color='#ccc', size=11),
        hovertemplate='<b>%{y}</b><br>Score: %{x}<extra></extra>',
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0', size=11),
        xaxis=dict(showgrid=False, showticklabels=False, range=[0, max(maxes) + 3]),
        yaxis=dict(showgrid=False),
        height=350,
        margin=dict(t=10, b=10, l=10, r=60),
        bargap=0.3,
    )
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# SCORE CARD
# ─────────────────────────────────────────────────────────────────────────────

def render_score_card(title: str, score: int, max_score: int = 100,
                       subtitle: str = "", icon: str = "📊"):
    """Render a styled score card."""
    color = score_color(score)
    pct = int(score / max_score * 100)
    label = score_label(pct)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1e2a3a 0%, #162032 100%);
                border-radius: 12px; padding: 16px; text-align: center;
                border: 1px solid {color}33; box-shadow: 0 4px 15px {color}22;">
        <div style="font-size: 24px; margin-bottom: 4px;">{icon}</div>
        <div style="color: #aaa; font-size: 11px; text-transform: uppercase;
                    letter-spacing: 1px;">{title}</div>
        <div style="color: {color}; font-size: 32px; font-weight: 800;
                    margin: 6px 0;">{score}<span style="font-size:14px;color:#888">/{max_score}</span></div>
        <div style="background: #0d1117; border-radius: 6px; height: 6px; margin: 8px 0;">
            <div style="background: {color}; width: {pct}%; height: 100%;
                        border-radius: 6px; transition: width 0.5s;"></div>
        </div>
        <div style="color: {color}; font-size: 12px; font-weight: 600;">{label}</div>
        {f'<div style="color: #666; font-size: 10px; margin-top: 4px;">{subtitle}</div>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FLAG DISPLAY
# ─────────────────────────────────────────────────────────────────────────────

def render_red_flag(flag: str, severity: str):
    """Render a single red flag alert."""
    colors_map = {
        'critical': ('#E74C3C', '🚨', '#2d1b1b'),
        'high': ('#F39C12', '⚠️', '#2d2a1b'),
        'medium': ('#3498DB', 'ℹ️', '#1b2036'),
        'low': ('#2ECC71', '💡', '#1b2d1b'),
    }
    color, icon, bg = colors_map.get(severity, ('#888', '•', '#1e2a3a'))
    st.markdown(f"""
    <div style="background: {bg}; border-left: 3px solid {color};
                border-radius: 6px; padding: 10px 14px; margin: 4px 0;
                display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 16px;">{icon}</span>
        <span style="color: #e0e0e0; font-size: 13px;">{flag}</span>
        <span style="margin-left: auto; color: {color}; font-size: 10px;
                     text-transform: uppercase; font-weight: 700;">{severity}</span>
    </div>
    """, unsafe_allow_html=True)


def render_red_flags_list(flags: List[Dict]):
    """Render all red flags grouped by severity."""
    if not flags:
        st.success("✅ No critical red flags detected!")
        return

    for severity in ['critical', 'high', 'medium', 'low']:
        severity_flags = [f for f in flags if f.get('severity') == severity]
        if severity_flags:
            for flag in severity_flags:
                render_red_flag(flag['flag'], flag['severity'])


# ─────────────────────────────────────────────────────────────────────────────
# KEYWORD CHIPS
# ─────────────────────────────────────────────────────────────────────────────

def render_keyword_chips(keywords: List[str], color: str = '#6C63FF',
                          label: str = "Keywords"):
    """Render keywords as styled chips."""
    if not keywords:
        return
    chips_html = ''.join([
        f'<span style="background: {color}22; color: {color}; border: 1px solid {color}44; '
        f'border-radius: 16px; padding: 3px 10px; font-size: 12px; margin: 3px 2px; '
        f'display: inline-block;">{kw}</span>'
        for kw in keywords
    ])
    st.markdown(f"**{label}:**", unsafe_allow_html=False)
    st.markdown(f'<div style="line-height: 2.2;">{chips_html}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# QUICK ACTION CARD
# ─────────────────────────────────────────────────────────────────────────────

def render_quick_action_card(icon: str, title: str, description: str,
                              color: str = '#6C63FF'):
    """Render a quick-action dashboard card."""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1e2a3a 0%, #162032 100%);
                border-radius: 14px; padding: 24px; text-align: center;
                border: 1px solid {color}33; cursor: pointer;
                box-shadow: 0 4px 20px {color}11;
                transition: transform 0.2s, box-shadow 0.2s;">
        <div style="font-size: 40px; margin-bottom: 12px;">{icon}</div>
        <div style="color: #ffffff; font-size: 16px; font-weight: 700;
                    margin-bottom: 8px;">{title}</div>
        <div style="color: #aaaaaa; font-size: 13px; line-height: 1.5;">{description}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# IMPROVEMENT SUGGESTION BOX
# ─────────────────────────────────────────────────────────────────────────────

def render_suggestion(text: str, severity: str = "info"):
    """Render an improvement suggestion box."""
    config = {
        'success': ('#2ECC71', '✅', '#1b2d1b'),
        'warning': ('#F39C12', '💡', '#2d2a1b'),
        'error': ('#E74C3C', '🔴', '#2d1b1b'),
        'info': ('#3498DB', 'ℹ️', '#1b2036'),
    }
    color, icon, bg = config.get(severity, config['info'])
    st.markdown(f"""
    <div style="background: {bg}; border-left: 3px solid {color};
                border-radius: 6px; padding: 12px 16px; margin: 6px 0;">
        <span style="font-size: 14px;">{icon} {text}</span>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# DOWNLOAD BUTTON HELPER
# ─────────────────────────────────────────────────────────────────────────────

def get_download_button(data: bytes, filename: str, label: str,
                         mime: str = 'application/octet-stream'):
    """Return a styled download button."""
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:{mime};base64,{b64}" download="{filename}" style="text-decoration: none;">'
    btn = (f'{href}<button style="background: linear-gradient(135deg, #6C63FF, #4ECDC4); '
           f'color: white; border: none; border-radius: 8px; padding: 10px 20px; '
           f'font-size: 14px; cursor: pointer; font-weight: 600;">{label}</button></a>')
    st.markdown(btn, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRESS BAR
# ─────────────────────────────────────────────────────────────────────────────

def render_progress_bar(value: float, label: str = "", color: str = '#6C63FF'):
    """Render a custom progress bar."""
    pct = min(100, max(0, value))
    st.markdown(f"""
    <div style="margin: 4px 0 12px 0;">
        {f'<div style="color: #aaa; font-size: 12px; margin-bottom: 4px;">{label}</div>' if label else ''}
        <div style="background: #1e2a3a; border-radius: 6px; height: 8px; overflow: hidden;">
            <div style="background: {color}; width: {pct}%; height: 100%;
                        border-radius: 6px; transition: width 0.6s ease;"></div>
        </div>
        <div style="color: #888; font-size: 11px; margin-top: 2px; text-align: right;">{pct:.0f}%</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# JD MATCH VISUALIZATION
# ─────────────────────────────────────────────────────────────────────────────

def render_jd_match_chart(matched: int, missing: int, title: str = "Keyword Match"):
    """Render pie chart for keyword matching."""
    fig = go.Figure(data=[go.Pie(
        labels=['Matched', 'Missing'],
        values=[matched, missing],
        hole=0.5,
        marker=dict(colors=[COLORS['success'], COLORS['danger']]),
        textinfo='label+percent',
        textfont=dict(color='white', size=12),
        hoverinfo='label+value',
    )])
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        title=dict(text=title, x=0.5, font=dict(size=14, color='#e0e0e0')),
        height=250,
        margin=dict(t=40, b=10, l=10, r=10),
        legend=dict(font=dict(color='#ccc'))
    )
    st.plotly_chart(fig, use_container_width=True)
