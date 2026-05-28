"""
ResumeCraft AI Studio - UI Components
High-contrast Streamlit UI helpers: score cards, gauges, charts, chips, and alerts.
"""

import streamlit as st
import plotly.graph_objects as go
from typing import Dict, List
import base64


# ─────────────────────────────────────────────────────────────────────────────
# ACCESSIBLE COLOR SCHEME
# ─────────────────────────────────────────────────────────────────────────────

COLORS = {
    'primary': '#2563EB',
    'secondary': '#0F766E',
    'success': '#16A34A',
    'warning': '#D97706',
    'danger': '#DC2626',
    'dark': '#0F172A',
    'medium': '#334155',
    'light': '#F8FAFC',
    'text': '#111827',
    'muted': '#475569',
    'card_bg': '#FFFFFF',
    'card_border': '#D6DEE8',
}


def score_color(score: int) -> str:
    """Return accessible color based on score value."""
    if score >= 80:
        return COLORS['success']
    elif score >= 60:
        return '#15803D'
    elif score >= 45:
        return COLORS['warning']
    elif score >= 30:
        return '#EA580C'
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
    """Render a readable gauge chart for a score."""
    color = score_color(score)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': title, 'font': {'size': 17, 'color': COLORS['text']}},
        number={'font': {'size': 36, 'color': color}, 'suffix': f'/{max_score}'},
        gauge={
            'axis': {
                'range': [0, max_score],
                'tickcolor': COLORS['muted'],
                'tickfont': {'color': COLORS['muted']}
            },
            'bar': {'color': color, 'thickness': 0.35},
            'bgcolor': '#E5E7EB',
            'borderwidth': 0,
            'steps': [
                {'range': [0, max_score * 0.4], 'color': '#FEE2E2'},
                {'range': [max_score * 0.4, max_score * 0.7], 'color': '#FEF3C7'},
                {'range': [max_score * 0.7, max_score], 'color': '#DCFCE7'},
            ],
            'threshold': {
                'line': {'color': COLORS['dark'], 'width': 2},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': COLORS['text']},
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
        marker=dict(colors=[color, '#E5E7EB']),
        showlegend=False,
        textinfo='none',
        hoverinfo='skip',
    )])
    fig.add_annotation(
        text=f"<b>{score}</b>",
        x=0.5,
        y=0.5,
        font=dict(size=28, color=color, family='Inter'),
        showarrow=False
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=size,
        margin=dict(t=5, b=5, l=5, r=5),
        title=dict(text=title, x=0.5, font=dict(size=12, color=COLORS['text'])),
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

    if not scores:
        st.info("No section scores available yet.")
        return

    pcts = [s / m * 100 for s, m in zip(scores, maxes)]
    colors = [score_color(int(p)) for p in pcts]

    fig = go.Figure(go.Bar(
        x=scores,
        y=labels,
        orientation='h',
        marker=dict(color=colors),
        text=[f"{s}/{m}" for s, m in zip(scores, maxes)],
        textposition='outside',
        textfont=dict(color=COLORS['text'], size=12),
        hovertemplate='<b>%{y}</b><br>Score: %{x}<extra></extra>',
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text'], size=12),
        xaxis=dict(showgrid=True, gridcolor='#E5E7EB', zeroline=False, range=[0, max(maxes) + 3]),
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
    """Render a high-contrast score card."""
    color = score_color(score)
    pct = int(score / max_score * 100) if max_score else 0
    label = score_label(pct)
    st.markdown(f"""
    <div style="background: #FFFFFF;
                border-radius: 16px; padding: 18px; text-align: center;
                border: 1px solid #D6DEE8; box-shadow: 0 8px 24px rgba(15,23,42,0.08);">
        <div style="font-size: 28px; margin-bottom: 8px;">{icon}</div>
        <div style="color: #334155; font-size: 12px; text-transform: uppercase;
                    letter-spacing: 1px; font-weight: 800;">{title}</div>
        <div style="color: {color}; font-size: 34px; font-weight: 900;
                    margin: 8px 0;">{score}<span style="font-size:14px;color:#475569">/{max_score}</span></div>
        <div style="background: #E5E7EB; border-radius: 999px; height: 7px; margin: 10px 0;">
            <div style="background: {color}; width: {pct}%; height: 100%;
                        border-radius: 999px; transition: width 0.5s;"></div>
        </div>
        <div style="color: {color}; font-size: 13px; font-weight: 800;">{label}</div>
        {f'<div style="color: #475569; font-size: 11px; margin-top: 5px; font-weight: 600;">{subtitle}</div>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FLAG DISPLAY
# ─────────────────────────────────────────────────────────────────────────────

def render_red_flag(flag: str, severity: str):
    """Render a single red flag alert."""
    colors_map = {
        'critical': ('#DC2626', '🚨', '#FEE2E2'),
        'high': ('#D97706', '⚠️', '#FEF3C7'),
        'medium': ('#2563EB', 'ℹ️', '#DBEAFE'),
        'low': ('#16A34A', '💡', '#DCFCE7'),
    }
    color, icon, bg = colors_map.get(severity, ('#475569', '•', '#F1F5F9'))
    st.markdown(f"""
    <div style="background: {bg}; border-left: 4px solid {color};
                border-radius: 10px; padding: 11px 14px; margin: 6px 0;
                display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 17px;">{icon}</span>
        <span style="color: #111827; font-size: 14px; font-weight: 600;">{flag}</span>
        <span style="margin-left: auto; color: {color}; font-size: 11px;
                     text-transform: uppercase; font-weight: 900;">{severity}</span>
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

def render_keyword_chips(keywords: List[str], color: str = '#2563EB',
                         label: str = "Keywords"):
    """Render keywords as styled chips."""
    if not keywords:
        return
    chips_html = ''.join([
        f'<span style="background: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE; '
        f'border-radius: 999px; padding: 4px 11px; font-size: 12px; margin: 4px 3px; '
        f'display: inline-block; font-weight: 700;">{kw}</span>'
        for kw in keywords
    ])
    if label:
        st.markdown(f"**{label}:**", unsafe_allow_html=False)
    st.markdown(chips_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# QUICK ACTION CARD
# ─────────────────────────────────────────────────────────────────────────────

def render_quick_action_card(icon: str, title: str, description: str,
                             color: str = '#2563EB'):
    """Render a readable quick-action dashboard card."""
    st.markdown(f"""
    <div style="background: #FFFFFF;
                border-radius: 18px; padding: 26px 20px; text-align: center;
                border: 1px solid #D6DEE8;
                box-shadow: 0 10px 26px rgba(15, 23, 42, 0.08);
                min-height: 130px;">
        <div style="font-size: 42px; margin-bottom: 12px;">{icon}</div>
        <div style="color: #0F172A; font-size: 17px; font-weight: 900;
                    margin-bottom: 8px;">{title}</div>
        <div style="color: #475569; font-size: 13px; line-height: 1.55; font-weight: 600;">{description}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# IMPROVEMENT SUGGESTION BOX
# ─────────────────────────────────────────────────────────────────────────────

def render_suggestion(text: str, severity: str = "info"):
    """Render an improvement suggestion box."""
    config = {
        'success': ('#16A34A', '✅', '#DCFCE7'),
        'warning': ('#D97706', '💡', '#FEF3C7'),
        'error': ('#DC2626', '🔴', '#FEE2E2'),
        'info': ('#2563EB', 'ℹ️', '#DBEAFE'),
    }
    color, icon, bg = config.get(severity, config['info'])
    st.markdown(f"""
    <div style="background: {bg}; border-left: 4px solid {color};
                border-radius: 10px; padding: 12px 16px; margin: 7px 0;
                color: #111827; font-weight: 600;">
        <span style="font-size: 14px; color: #111827;">{icon} {text}</span>
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
    btn = (f'{href}<button style="background: linear-gradient(135deg, #2563EB, #0F766E); '
           f'color: white; border: none; border-radius: 10px; padding: 10px 20px; '
           f'font-size: 14px; cursor: pointer; font-weight: 800;">{label}</button></a>')
    st.markdown(btn, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRESS BAR
# ─────────────────────────────────────────────────────────────────────────────

def render_progress_bar(value: float, label: str = "", color: str = '#2563EB'):
    """Render a custom progress bar."""
    pct = min(100, max(0, value))
    st.markdown(f"""
    <div style="margin: 5px 0 13px 0;">
        {f'<div style="color: #334155; font-size: 12px; margin-bottom: 5px; font-weight: 700;">{label}</div>' if label else ''}
        <div style="background: #E5E7EB; border-radius: 999px; height: 9px; overflow: hidden;">
            <div style="background: {color}; width: {pct}%; height: 100%;
                        border-radius: 999px; transition: width 0.6s ease;"></div>
        </div>
        <div style="color: #475569; font-size: 11px; margin-top: 3px; text-align: right; font-weight: 700;">{pct:.0f}%</div>
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
        textfont=dict(color='#111827', size=12),
        hoverinfo='label+value',
    )])
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text']),
        title=dict(text=title, x=0.5, font=dict(size=15, color=COLORS['text'])),
        height=250,
        margin=dict(t=40, b=10, l=10, r=10),
        legend=dict(font=dict(color=COLORS['text']))
    )
    st.plotly_chart(fig, use_container_width=True)
