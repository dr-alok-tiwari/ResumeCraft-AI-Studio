"""
ResumeCraft AI Studio - Bullet Point Improver
Rule-based bullet improvement. No AI APIs. Never invents facts.
"""

import re
from typing import Dict, List, Tuple

# ─────────────────────────────────────────────
# ACTION VERBS BY DOMAIN
# ─────────────────────────────────────────────

ACTION_VERBS_BY_DOMAIN = {
    'general': [
        'Analyzed', 'Designed', 'Developed', 'Implemented', 'Optimized', 'Automated',
        'Led', 'Coordinated', 'Evaluated', 'Improved', 'Built', 'Delivered',
        'Researched', 'Presented', 'Managed', 'Created', 'Established', 'Launched',
        'Streamlined', 'Enhanced', 'Reduced', 'Increased', 'Generated', 'Achieved',
        'Collaborated', 'Facilitated', 'Initiated', 'Executed', 'Deployed',
    ],
    'data_analytics': [
        'Analyzed', 'Visualized', 'Modeled', 'Forecasted', 'Extracted', 'Processed',
        'Queried', 'Cleaned', 'Transformed', 'Aggregated', 'Integrated', 'Interpreted',
        'Profiled', 'Validated', 'Benchmarked', 'Synthesized', 'Identified',
    ],
    'software': [
        'Developed', 'Engineered', 'Architected', 'Debugged', 'Deployed', 'Configured',
        'Integrated', 'Migrated', 'Refactored', 'Automated', 'Tested', 'Optimized',
        'Built', 'Implemented', 'Programmed', 'Designed', 'Maintained',
    ],
    'management': [
        'Led', 'Managed', 'Supervised', 'Mentored', 'Directed', 'Coordinated',
        'Spearheaded', 'Orchestrated', 'Strategized', 'Planned', 'Delegated',
        'Facilitated', 'Negotiated', 'Influenced', 'Guided', 'Oversaw',
    ],
    'research': [
        'Researched', 'Investigated', 'Analyzed', 'Published', 'Authored', 'Conducted',
        'Designed', 'Evaluated', 'Synthesized', 'Reviewed', 'Documented', 'Explored',
        'Tested', 'Validated', 'Hypothesized', 'Presented', 'Discovered',
    ],
    'finance': [
        'Analyzed', 'Forecasted', 'Budgeted', 'Audited', 'Modeled', 'Calculated',
        'Evaluated', 'Monitored', 'Optimized', 'Reconciled', 'Reported', 'Assessed',
        'Projected', 'Advised', 'Structured', 'Managed',
    ],
    'marketing': [
        'Launched', 'Developed', 'Executed', 'Drove', 'Grew', 'Managed', 'Created',
        'Designed', 'Campaigned', 'Generated', 'Increased', 'Targeted', 'Segmented',
        'Optimized', 'Presented', 'Tracked', 'Reported',
    ],
}

# Passive/weak patterns
WEAK_PATTERNS = [
    (r'^\s*helped\s+', 'weak_verb'),
    (r'^\s*assisted\s+', 'weak_verb'),
    (r'^\s*worked\s+on\s+', 'weak_verb'),
    (r'^\s*was\s+responsible\s+for\s+', 'passive'),
    (r'^\s*responsible\s+for\s+', 'passive'),
    (r'^\s*tried\s+to\s+', 'tentative'),
    (r'^\s*participated\s+in\s+', 'weak_verb'),
    (r'^\s*involved\s+in\s+', 'weak_verb'),
    (r'^\s*did\s+', 'weak_verb'),
    (r'^\s*made\s+', 'weak_verb'),
    (r'^\s*contributed\s+to\s+', 'weak_verb'),
    (r'^\s*was\s+part\s+of\s+', 'passive'),
    (r'^\s*took\s+part\s+in\s+', 'weak_verb'),
]

# Strong action verb patterns
STRONG_VERB_PATTERN = re.compile(
    r'^\s*(Analyzed|Designed|Developed|Implemented|Optimized|Automated|Led|'
    r'Coordinated|Evaluated|Improved|Built|Delivered|Researched|Presented|'
    r'Managed|Created|Established|Launched|Streamlined|Enhanced|Reduced|'
    r'Increased|Generated|Achieved|Collaborated|Facilitated|Initiated|'
    r'Executed|Deployed|Integrated|Monitored|Resolved|Supervised|Trained|'
    r'Mentored|Spearheaded|Formulated|Negotiated|Identified|Transformed|'
    r'Engineered|Architected|Forecasted|Budgeted|Audited|Modeled|Published)',
    re.IGNORECASE
)

# Improvement templates
IMPROVEMENT_TEMPLATES = [
    {
        'pattern': r'(?:worked on|helped with|assisted with)?\s*(.+?)\s*(?:data|dataset|database)',
        'template': 'Analyzed {subject} data using [tool/method] to identify [pattern/insight], supporting [business decision/outcome].',
        'category': 'data_work'
    },
    {
        'pattern': r'(?:worked on|built|created|developed)\s*(.+?)\s*(?:report|dashboard|visualization)',
        'template': 'Developed [interactive/automated] {subject} dashboard/report using [tool], enabling [stakeholder group] to [decision made].',
        'category': 'reporting'
    },
    {
        'pattern': r'(?:helped|assisted|supported)\s*(.+?)\s*(?:team|project|initiative)',
        'template': 'Collaborated with {subject} team to [specific contribution], resulting in [outcome/impact].',
        'category': 'collaboration'
    },
    {
        'pattern': r'(?:managed|handled|led)\s*(.+?)\s*(?:team|people|employees|members)',
        'template': 'Led {subject} team of [N] members to [achieve specific goal], delivering [outcome] within [timeframe].',
        'category': 'leadership'
    },
    {
        'pattern': r'(?:wrote|created|developed)\s*(.+?)\s*(?:code|program|script|application)',
        'template': 'Developed {subject} [application/script/tool] using [technology], reducing [process/time] by [insert real percentage].',
        'category': 'development'
    },
    {
        'pattern': r'(?:analyzed|studied|reviewed)\s*(.+)',
        'template': 'Analyzed {subject} to identify [key findings/trends], providing actionable insights for [decision/team].',
        'category': 'analysis'
    },
]

METRIC_PLACEHOLDERS = [
    '[insert real percentage improvement]',
    '[insert number of records/items processed]',
    '[insert time saved per week/month]',
    '[insert revenue/cost impact if known]',
    '[insert team size]',
    '[insert number of stakeholders/users]',
]


# ─────────────────────────────────────────────
# ANALYSIS
# ─────────────────────────────────────────────

def analyze_bullet(bullet: str) -> Dict:
    """Analyze a bullet point for quality issues."""
    result = {
        'original': bullet,
        'issues': [],
        'suggestions': [],
        'has_weak_verb': False,
        'has_passive': False,
        'has_metrics': False,
        'is_vague': False,
        'is_too_long': False,
        'starts_with_action_verb': False,
        'score': 0
    }

    # Length check
    word_count = len(bullet.split())
    if word_count > 35:
        result['is_too_long'] = True
        result['issues'].append(f'Too long ({word_count} words) — aim for 15–25 words')
    elif word_count < 5:
        result['issues'].append('Too short — add more detail')

    # Weak verb check
    for pattern, ptype in WEAK_PATTERNS:
        if re.search(pattern, bullet, re.IGNORECASE):
            result['has_weak_verb'] = True if ptype == 'weak_verb' else result['has_weak_verb']
            result['has_passive'] = True if ptype == 'passive' else result['has_passive']
            if ptype == 'weak_verb':
                result['issues'].append('Starts with a weak verb — use a strong action verb')
            elif ptype == 'passive':
                result['issues'].append('Passive/vague phrasing — rewrite in active voice')
            elif ptype == 'tentative':
                result['issues'].append('Tentative language — be assertive about what you did')
            break

    # Strong verb check
    if STRONG_VERB_PATTERN.match(bullet):
        result['starts_with_action_verb'] = True
        result['score'] += 30
    else:
        result['suggestions'].append('Start with a strong action verb (e.g., Analyzed, Developed, Led)')

    # Metrics check
    metric_patterns = [
        r'\d+\s*%', r'\$\s*\d+', r'\d+x', r'\d+\s*(users|customers|records|projects)',
        r'(increased|decreased|reduced|improved|grew).*\d+',
        r'\d+\s*(hours|days|weeks|months)',
    ]
    for mp in metric_patterns:
        if re.search(mp, bullet, re.IGNORECASE):
            result['has_metrics'] = True
            result['score'] += 30
            break

    if not result['has_metrics']:
        result['issues'].append('No measurable impact — add numbers/percentages if truthfully available')
        result['suggestions'].append('Add a metric: ' + METRIC_PLACEHOLDERS[0])

    # Vagueness check
    vague_words = ['various', 'several', 'many', 'some', 'things', 'stuff',
                   'good', 'great', 'excellent', 'various tasks', 'etc.']
    vague_found = [w for w in vague_words if w in bullet.lower()]
    if vague_found:
        result['is_vague'] = True
        result['issues'].append(f'Vague language detected: "{vague_found[0]}" — be specific')

    # Score
    if result['starts_with_action_verb']:
        result['score'] += 20
    if not result['has_weak_verb'] and not result['has_passive']:
        result['score'] += 20
    if not result['is_vague']:
        result['score'] += 10
    if not result['is_too_long']:
        result['score'] += 10
    if result['has_metrics']:
        result['score'] += 10

    result['score'] = min(100, result['score'])
    return result


def improve_bullet(bullet: str) -> Dict:
    """Generate an improved version of a bullet point using rule-based templates."""
    analysis = analyze_bullet(bullet)
    improved = bullet.strip()
    reasoning = []

    # Try template matching
    for tmpl in IMPROVEMENT_TEMPLATES:
        match = re.search(tmpl['pattern'], bullet, re.IGNORECASE)
        if match:
            try:
                subject = match.group(1).strip() if match.lastindex else 'relevant'
                improved = tmpl['template'].replace('{subject}', subject)
                reasoning.append(f'Applied {tmpl["category"]} improvement template')
            except Exception:
                pass
            break

    # Verb replacement if weak start
    if analysis['has_weak_verb'] or analysis['has_passive']:
        for pattern, _ in WEAK_PATTERNS:
            cleaned = re.sub(pattern, '', improved, flags=re.IGNORECASE).strip()
            if cleaned and len(cleaned) > 5:
                improved = 'Developed ' + cleaned[0].lower() + cleaned[1:]
                reasoning.append('Replaced weak opening verb with strong action verb')
                break

    # Capitalize first word
    if improved and not improved[0].isupper():
        improved = improved[0].upper() + improved[1:]

    # Add metric placeholder if no metrics
    if not analysis['has_metrics'] and '[insert' not in improved:
        improved = improved.rstrip('.') + ', achieving [insert real percentage or outcome].'
        reasoning.append('Added metric placeholder — replace with your actual result')

    # Ensure starts with action verb
    if not STRONG_VERB_PATTERN.match(improved):
        reasoning.append('Suggestion: Start with a strong action verb from the list below')

    return {
        'original': bullet,
        'improved': improved,
        'analysis': analysis,
        'reasoning': reasoning if reasoning else ['Applied general structure improvements'],
        'action_verbs': ACTION_VERBS_BY_DOMAIN['general'][:10],
        'is_placeholder_present': '[insert' in improved,
        'note': 'All [insert X] placeholders must be replaced with your real, verifiable facts.'
    }


def improve_multiple_bullets(bullets: List[str]) -> List[Dict]:
    """Improve a list of bullet points."""
    return [improve_bullet(b) for b in bullets if b.strip()]
