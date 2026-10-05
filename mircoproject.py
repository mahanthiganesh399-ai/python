"""
AI in Autonomous Vehicles: Global Route Planner & Traffic Optimisation
======================================================================
Single-file Python script that builds and outputs a fully interactive 
HTML/JS webpage where users can select starting points and destinations
in ANY country, county, or city worldwide.

Python Concepts Used:
- Functions (def, return)
- Arithmetic operations (division, multiplication, rounding)
- Iteration & Loops (for loops, list comprehension)
- Built-in min() with key selector (lambda)
- Formatted string literals (f-strings)
"""

import os
import urllib.parse
import webbrowser

# =============================================================================
# 0. TITLE & TOPIC CONFIGURATION
# =============================================================================
title = "AI in Autonomous Vehicles: Global Route Optimisation & Traffic Prediction"

# =============================================================================
# 1. DATA: Default 5 Routes across different corridor types (Distance km & Speed km/h)
# =============================================================================
default_origin = "Koramangala, Bengaluru, Karnataka, India"
default_destination = "Kempegowda International Airport (BLR), Bengaluru, India"

routes_data = [
    {
        "id": 1,
        "name": "Route A (Direct Highway / NH Expressway)",
        "factor": 1.05,
        "speed": 70.0,
        "desc": "High-capacity multi-lane expressway with dynamic tolling and high speed limits."
    },
    {
        "id": 2,
        "name": "Route B (City Central Arterial Road)",
        "factor": 0.78,
        "speed": 35.0,
        "desc": "Shorter physical distance passing through urban corridors with traffic signals."
    },
    {
        "id": 3,
        "name": "Route C (Outer Ring Road / Bypass Expressway)",
        "factor": 1.35,
        "speed": 90.0,
        "desc": "Perimeter expressway designed to bypass urban congestion at high cruising velocity."
    },
    {
        "id": 4,
        "name": "Route D (Green Belt / Eco Byway)",
        "factor": 0.95,
        "speed": 48.0,
        "desc": "Scenic steady-speed corridor optimized for electric vehicle (EV) battery conservation."
    },
    {
        "id": 5,
        "name": "Route E (Metro Bypass Tunnel)",
        "factor": 0.65,
        "speed": 52.0,
        "desc": "Dedicated underground transit tunnel with zero pedestrian interference and steady latency."
    }
]

# =============================================================================
# 2. FUNCTIONS (Python Logic)
# =============================================================================
# Task 1: travel_time(distance, speed) returning minutes
def travel_time(distance: float, speed: float) -> float:
    """
    Computes travel time in minutes.
    Formula: Time (minutes) = (Distance / Speed) * 60
    """
    if speed <= 0:
        return 0.0
    return (distance / speed) * 60.0


def make_google_maps_url(origin: str, destination: str) -> str:
    """Generates a direct Google Maps Driving Directions URL for any location worldwide."""
    o = urllib.parse.quote(origin)
    d = urllib.parse.quote(destination)
    return f"https://www.google.com/maps/dir/?api=1&origin={o}&destination={d}&travelmode=driving"


# =============================================================================
# 3. PYTHON EXECUTION & LOGIC DEMO (Terminal Verification)
# =============================================================================
base_distance = 40.0  # Base distance in km for initial demonstration

# Task 2: Loop over routes and compute each travel time
for r in routes_data:
    r["distance"] = round(base_distance * r["factor"], 1)
    r["time_min"] = travel_time(r["distance"], r["speed"])

# Task 3: Mark the fastest route using min() with a key
fastest_route = min(routes_data, key=lambda x: x["time_min"])

print("=" * 80)
print(f"🚦 {title.upper()}")
print("=" * 80)
print(f"📍 Sample Origin:      {default_origin}")
print(f"🏁 Sample Destination: {default_destination}")
print("-" * 80)
print(f"{'Route Identifier':<38} | {'Distance':<10} | {'Avg Speed':<11} | {'Time (min)':<11} | Status")
print("-" * 80)
for r in routes_data:
    status = "⭐ FASTEST" if r == fastest_route else "Alternative"
    print(f"{r['name']:<38} | {r['distance']:>6.1f} km | {r['speed']:>7.1f} km/h | {r['time_min']:>8.1f} min | {status}")
print("-" * 80)
print(f"🎯 OPTIMAL ROUTE: {fastest_route['name']} ({fastest_route['time_min']:.1f} minutes)")
print("=" * 80)

# Technical note on autonomous vehicles
av_technical_note = """
Autonomous vehicles (AVs) do not merely evaluate static road distances. 
Modern self-driving fleets operate on a decentralized Predictive Traffic Optimization Pipeline 
combining V2X (Vehicle-to-Everything) communication, deep learning graph search (dynamic A* & Dijkstra), 
and regenerative braking efficiency. By calculating minimal latency trajectories continuously, 
AVs optimize individual commute times while helping balance municipal traffic flow.
"""

# =============================================================================
# 4. HTML TEMPLATE: Interactive Global Web Application
# =============================================================================
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Worldwide autonomous vehicle route planner and traffic prediction system.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-main: #0a0d14;
            --bg-card: rgba(18, 24, 38, 0.75);
            --border-color: rgba(56, 189, 248, 0.2);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.35);
            --emerald: #10b981;
            --amber: #f59e0b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --font-sans: 'Outfit', -apple-system, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg-main);
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(16, 185, 129, 0.06) 0%, transparent 40%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
            color: var(--text-main);
            font-family: var(--font-sans);
            min-height: 100vh;
            padding: 30px 20px;
            line-height: 1.5;
        }}
        .app-container {{
            max-width: 1360px;
            margin: 0 auto;
        }}
        /* Header */
        header.hud-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 28px;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .brand {{ display: flex; align-items: center; gap: 14px; }}
        .logo-icon {{
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #0284c7, #06b6d4);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        }}
        h1.title {{ font-size: 1.65rem; font-weight: 800; letter-spacing: -0.5px; }}
        h1.title span {{ color: var(--primary); }}
        .subtitle {{ font-size: 0.84rem; color: var(--text-muted); }}
        .telemetry-bar {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .telemetry-pill {{
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid var(--border-color);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-family: var(--font-mono);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .dot {{ width: 8px; height: 8px; border-radius: 50%; background: var(--emerald); box-shadow: 0 0 8px var(--emerald); }}
        
        /* Grid Layout */
        .dashboard-grid {{
            display: grid;
            grid-template-columns: 1.35fr 1fr;
            gap: 28px;
        }}
        @media (max-width: 1024px) {{
            .dashboard-grid {{ grid-template-columns: 1fr; }}
        }}

        /* Glass Cards */
        .glass-card {{
            background: var(--bg-card);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
            margin-bottom: 24px;
        }}
        
        /* Global Route Discovery Box */
        .od-card {{
            background: linear-gradient(135deg, rgba(30, 58, 138, 0.3), rgba(15, 23, 42, 0.9));
            border: 1px solid rgba(56, 189, 248, 0.35);
        }}
        .card-title-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .panel-tag {{
            font-size: 0.72rem;
            font-family: var(--font-mono);
            color: var(--primary);
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }}
        .section-title {{ font-size: 1.25rem; font-weight: 700; color: #fff; }}
        
        /* Country & Region Switcher */
        .country-tabs {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .country-tab-btn {{
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 5px 12px;
            border-radius: 16px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            font-family: var(--font-sans);
        }}
        .country-tab-btn:hover {{ color: #fff; border-color: var(--primary); }}
        .country-tab-btn.active {{
            background: linear-gradient(135deg, #0284c7, #06b6d4);
            color: #fff;
            border-color: transparent;
            box-shadow: 0 0 10px rgba(6, 182, 212, 0.4);
        }}

        /* Inputs Row */
        .od-inputs {{
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 12px;
            align-items: flex-end;
            margin-bottom: 16px;
        }}
        @media (max-width: 768px) {{
            .od-inputs {{ grid-template-columns: 1fr; }}
        }}
        .input-group label {{
            display: block;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 6px;
        }}
        .input-group input {{
            width: 100%;
            background: rgba(10, 15, 29, 0.85);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px 14px;
            color: #ffffff;
            font-family: var(--font-sans);
            font-size: 0.9rem;
            outline: none;
            transition: all 0.2s;
        }}
        .input-group input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 10px var(--primary-glow);
        }}
        .swap-btn {{
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            width: 42px;
            height: 42px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 1.1rem;
        }}
        .swap-btn:hover {{ color: var(--primary); border-color: var(--primary); background: rgba(56, 189, 248, 0.15); }}

        /* Buttons & Chips */
        .controls-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .preset-chips {{ display: flex; gap: 6px; flex-wrap: wrap; }}
        .preset-chip {{
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 4px 10px;
            border-radius: 14px;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .preset-chip:hover {{ background: rgba(56, 189, 248, 0.15); color: #fff; border-color: var(--primary); }}
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 9px 18px;
            font-size: 0.88rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            transition: all 0.2s;
            font-family: var(--font-sans);
            text-decoration: none;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, #0284c7, #06b6d4);
            color: #ffffff;
            box-shadow: 0 4px 16px rgba(6, 182, 212, 0.35);
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5); }}
        .btn-gmaps {{
            background: linear-gradient(135deg, #1a73e8, #4285f4);
            color: #ffffff;
        }}
        .btn-gmaps:hover {{ opacity: 0.9; transform: translateY(-2px); }}

        /* Optimal Route Inspector Banner */
        .optimal-banner {{
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.08));
            border: 2px solid var(--emerald);
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 0 28px rgba(16, 185, 129, 0.2);
            margin-bottom: 24px;
            transition: all 0.3s ease;
        }}
        .optimal-banner.alt-selected {{
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(30, 41, 59, 0.6));
            border-color: var(--primary);
            box-shadow: 0 0 24px rgba(56, 189, 248, 0.25);
        }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-family: var(--font-mono);
            font-weight: 700;
        }}
        .badge.fastest {{ background: rgba(16, 185, 129, 0.25); color: #34d399; border: 1px solid var(--emerald); }}
        .badge.alt {{ background: rgba(56, 189, 248, 0.15); color: var(--primary); border: 1px solid var(--primary); }}
        
        .hero-body {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 14px 0 18px;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .hero-name {{ font-size: 1.45rem; font-weight: 700; color: #fff; }}
        .hero-trajectory {{ font-size: 0.88rem; color: var(--text-muted); }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
            margin-top: 10px;
        }}
        .metric-cell {{
            background: rgba(15, 23, 42, 0.7);
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .m-title {{ font-size: 0.68rem; color: var(--text-muted); font-family: var(--font-mono); text-transform: uppercase; }}
        .m-val {{ font-size: 0.95rem; font-weight: 700; color: #fff; font-family: var(--font-mono); }}
        
        .hero-time-box {{
            text-align: right;
            background: rgba(15, 23, 42, 0.7);
            padding: 12px 20px;
            border-radius: 10px;
            border: 1px solid rgba(16, 185, 129, 0.3);
            min-width: 140px;
        }}
        .time-num {{ font-size: 2.2rem; font-weight: 800; font-family: var(--font-mono); color: #fff; }}
        .time-hours {{ font-size: 0.75rem; color: var(--text-muted); font-family: var(--font-mono); }}

        /* Routes Table */
        .table-container {{
            padding: 0;
            overflow-x: auto;
            border-radius: 14px;
        }}
        table.routes-table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.88rem;
        }}
        table.routes-table th {{
            padding: 14px 18px;
            background: rgba(15, 23, 42, 0.8);
            color: var(--text-muted);
            font-weight: 600;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 1px solid var(--border-color);
        }}
        table.routes-table td {{
            padding: 14px 18px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        table.routes-table tbody tr {{ cursor: pointer; transition: all 0.2s; }}
        table.routes-table tbody tr:hover {{ background: rgba(28, 38, 58, 0.8); }}
        table.routes-table tr.selected-row {{ background: rgba(56, 189, 248, 0.15) !important; border-left: 4px solid var(--primary); }}
        table.routes-table tr.fastest-row {{ background: rgba(16, 185, 129, 0.08); }}
        table.routes-table tr.fastest-row.selected-row {{ background: rgba(16, 185, 129, 0.18) !important; border-left: 4px solid var(--emerald); }}
        
        .gmap-table-link {{
            color: #60a5fa;
            text-decoration: none;
            font-size: 0.78rem;
            background: rgba(59, 130, 246, 0.12);
            padding: 4px 8px;
            border-radius: 4px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            display: inline-block;
        }}
        .gmap-table-link:hover {{ background: rgba(59, 130, 246, 0.25); color: #93c5fd; }}

        /* Bar Chart */
        .chart-bars {{ display: flex; flex-direction: column; gap: 12px; }}
        .bar-row {{
            display: grid;
            grid-template-columns: 200px 1fr 70px;
            align-items: center;
            gap: 14px;
            cursor: pointer;
        }}
        .bar-label {{ font-size: 0.8rem; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .bar-track {{ height: 14px; background: rgba(255, 255, 255, 0.05); border-radius: 7px; overflow: hidden; }}
        .bar-fill {{
            height: 100%;
            border-radius: 7px;
            background: linear-gradient(90deg, #0284c7, #38bdf8);
            transition: width 0.6s ease;
        }}
        .bar-fill.fastest {{ background: linear-gradient(90deg, #059669, #10b981); box-shadow: 0 0 10px rgba(16, 185, 129, 0.5); }}
        .bar-val {{ font-size: 0.82rem; font-family: var(--font-mono); text-align: right; }}

        /* Canvas & Live Map Views */
        .view-switcher {{
            display: flex;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 3px;
            gap: 4px;
        }}
        .view-tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 4px 12px;
            border-radius: 16px;
            cursor: pointer;
            font-family: var(--font-sans);
        }}
        .view-tab-btn.active {{ background: var(--primary); color: #060911; }}
        .canvas-wrapper {{
            position: relative;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid rgba(56, 189, 248, 0.2);
            background: #060911;
        }}
        #navCanvas {{ width: 100%; height: 260px; display: block; }}
        .gmap-frame {{
            width: 100%;
            height: 260px;
            border: none;
            display: block;
            filter: invert(90%) hue-rotate(180deg) contrast(95%);
        }}
        .hidden {{ display: none !important; }}

        /* Technical Note */
        .note-box {{
            background: rgba(56, 189, 248, 0.06);
            border-left: 4px solid var(--primary);
            padding: 16px 20px;
            border-radius: 0 10px 10px 0;
            font-size: 0.9rem;
            color: var(--text-muted);
        }}
        .note-box strong {{ color: #fff; }}
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Header -->
        <header class="hud-header">
            <div class="brand">
                <div class="logo-icon">🚗</div>
                <div>
                    <h1 class="title">NaviAuto <span>AI</span></h1>
                    <span class="subtitle">{title}</span>
                </div>
            </div>
            <div class="telemetry-bar">
                <div class="telemetry-pill"><span class="dot"></span> LiDAR Sensor: ONLINE</div>
                <div class="telemetry-pill">🌍 Global Navigation Engine</div>
                <div class="telemetry-pill" style="color: var(--primary);">⚡ AI Optimizer: ACTIVE</div>
            </div>
        </header>

        <!-- Main Dashboard -->
        <main class="dashboard-grid">
            <!-- Left Column: Controls, Matrix & Selector -->
            <section class="left-col">
                <!-- Global / Any Country Origin & Destination Discovery -->
                <div class="glass-card od-card">
                    <div class="card-title-row">
                        <div>
                            <span class="panel-tag">ANY COUNTRY / COUNTY / CITY</span>
                            <h2 class="section-title">Select Starting Point & Destination</h2>
                        </div>
                    </div>

                    <!-- Region Filter Tabs -->
                    <div class="country-tabs">
                        <button type="button" class="country-tab-btn active" onclick="switchRegion('india')">🇮🇳 India</button>
                        <button type="button" class="country-tab-btn" onclick="switchRegion('usa')">🇺🇸 USA</button>
                        <button type="button" class="country-tab-btn" onclick="switchRegion('uk')">🇬🇧 UK & Europe</button>
                        <button type="button" class="country-tab-btn" onclick="switchRegion('global')">🌐 Global Cities</button>
                    </div>

                    <form id="routeForm" onsubmit="handleFormSubmit(event)">
                        <div class="od-inputs">
                            <!-- Starting Point -->
                            <div class="input-group">
                                <label for="originInput">🟢 Starting Point (Origin / County / City)</label>
                                <input type="text" id="originInput" placeholder="Enter starting point anywhere in the world..." value="{default_origin}" required>
                            </div>
                            <!-- Swap Button -->
                            <button type="button" class="swap-btn" onclick="swapPoints()" title="Swap Endpoints">⇄</button>
                            <!-- Destination -->
                            <div class="input-group">
                                <label for="destInput">🔴 Destination (Target City / Airport / Hub)</label>
                                <input type="text" id="destInput" placeholder="Enter destination anywhere in the world..." value="{default_destination}" required>
                            </div>
                        </div>

                        <div class="controls-row">
                            <div class="preset-chips" id="presetChipsContainer">
                                <!-- Populated dynamically by JS -->
                            </div>
                            <button type="submit" class="btn btn-primary">
                                ⚡ Calculate & Plan Routes
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Active / Selected Route Hero Banner -->
                <div id="heroCard" class="optimal-banner">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span id="heroBadge" class="badge fastest">★ FASTEST & SHORTEST ROUTE (AI OPTIMAL)</span>
                        <span id="routeIndexPill" style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted);">Route 1 of 5</span>
                    </div>

                    <div class="hero-body">
                        <div>
                            <div id="heroName" class="hero-name">Loading...</div>
                            <div id="heroTrajectory" class="hero-trajectory">Origin ➔ Destination</div>
                            
                            <div class="metrics-grid">
                                <div class="metric-cell">
                                    <div class="m-title">Distance</div>
                                    <div id="heroDist" class="m-val">-- km</div>
                                </div>
                                <div class="metric-cell">
                                    <div class="m-title">Travel Time</div>
                                    <div id="heroTime" class="m-val">-- min</div>
                                </div>
                                <div class="metric-cell">
                                    <div class="m-title">Avg Speed</div>
                                    <div id="heroSpeed" class="m-val">-- km/h</div>
                                </div>
                                <div class="metric-cell">
                                    <div class="m-title">Shortest Status</div>
                                    <div id="heroDelta" class="m-val" style="color: var(--emerald);">Optimal</div>
                                </div>
                            </div>
                        </div>

                        <div class="hero-time-box">
                            <div class="m-title">ESTIMATED ETA</div>
                            <div id="heroTimeBig" class="time-num">--</div>
                            <div id="heroTimeHours" class="time-hours">~0.00 hrs</div>
                        </div>
                    </div>

                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <a id="heroGmapBtn" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-gmaps">
                            🗺️ Open in Google Maps ↗
                        </a>
                        <button id="switchShortestBtn" class="btn" style="background: rgba(30,41,59,0.8); border: 1px solid var(--border-color); color: #fff; display: none;" onclick="selectRoute(fastestRouteId)">
                            ⚡ Switch to Shortest Route
                        </button>
                    </div>
                </div>

                <!-- Evaluated Trajectories Table -->
                <div class="glass-card table-container">
                    <table class="routes-table">
                        <thead>
                            <tr>
                                <th>Route Identifier</th>
                                <th>Distance</th>
                                <th>Avg Speed</th>
                                <th>Travel Time</th>
                                <th>Status</th>
                                <th>Google Maps</th>
                            </tr>
                        </thead>
                        <tbody id="routesTableBody">
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>

                <!-- Comparison Bar Chart -->
                <div class="glass-card">
                    <div style="margin-bottom: 16px;">
                        <h3 style="font-size: 1.1rem; color: #fff;">Travel Time Comparison (Minutes)</h3>
                        <span style="font-size: 0.78rem; color: var(--text-muted);">Calculated using <code>travel_time(distance, speed) = (distance / speed) * 60</code></span>
                    </div>
                    <div id="chartContainer" class="chart-bars">
                        <!-- Populated dynamically by JS -->
                    </div>
                </div>
            </section>

            <!-- Right Column: Live HUD / Google Maps Embed & Technical Note -->
            <section class="right-col">
                <div class="glass-card">
                    <div class="card-title-row">
                        <div>
                            <span class="panel-tag">LIVE TELEMETRY VIEW</span>
                            <h2 class="section-title">Trajectory Visualizer</h2>
                        </div>
                        <div class="view-switcher">
                            <button id="btnViewHud" class="view-tab-btn active" onclick="switchView('hud')">⚡ LiDAR HUD</button>
                            <button id="btnViewGmap" class="view-tab-btn" onclick="switchView('gmap')">🗺️ Google Maps</button>
                        </div>
                    </div>

                    <!-- View 1: Canvas HUD -->
                    <div id="hudWrapper" class="canvas-wrapper">
                        <canvas id="navCanvas" width="520" height="260"></canvas>
                        <div style="position: absolute; bottom: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; background: rgba(10,13,20,0.8); padding: 6px 14px; border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem;">
                            <span>SPEED: <strong id="hudSpeed" style="color: var(--primary);">70 km/h</strong></span>
                            <span>CRUISE: <strong style="color: var(--emerald);">L4 AUTONOMOUS</strong></span>
                        </div>
                    </div>

                    <!-- View 2: Google Maps Embed -->
                    <div id="gmapWrapper" class="canvas-wrapper hidden">
                        <iframe id="gmapIframe" class="gmap-frame" src="about:blank" loading="lazy"></iframe>
                        <div style="padding: 10px; background: rgba(10,13,20,0.9); font-size: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
                            <span id="gmapLabel" style="color: var(--text-muted); overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Maps Live View</span>
                            <a id="gmapDirectLink" href="#" target="_blank" class="btn btn-gmaps" style="padding: 4px 10px; font-size: 0.75rem;">Launch Fullscreen ↗</a>
                        </div>
                    </div>
                </div>

                <!-- Autonomous Vehicle AI Note -->
                <div class="glass-card">
                    <div style="color: var(--primary); font-family: var(--font-mono); font-size: 0.78rem; font-weight: 700; margin-bottom: 8px;">
                        🤖 AI IN SELF-DRIVING VEHICLES
                    </div>
                    <h3 style="font-size: 1.15rem; margin-bottom: 10px; color: #fff;">Predictive Traffic & Trajectory Optimization</h3>
                    <div class="note-box">
                        <p>{av_technical_note}</p>
                    </div>
                </div>
            </section>
        </main>
    </div>

    <!-- Client-Side JavaScript for Real-Time Recalculation & Worldwide Interactivity -->
    <script>
        const PRESETS = {{
            india: [
                {{ label: "BLR: Koramangala ➔ Airport", origin: "Koramangala, Bengaluru, Karnataka, India", dest: "Kempegowda International Airport (BLR), Bengaluru, India" }},
                {{ label: "MUM: BKC ➔ Pune Expressway", origin: "Bandra Kurla Complex (BKC), Mumbai, India", dest: "Pune IT Park (via Mumbai-Pune Expressway), India" }},
                {{ label: "DEL: Connaught ➔ Gurugram", origin: "Connaught Place, New Delhi, India", dest: "Cyber City, Gurugram, Haryana, India" }},
                {{ label: "HYD: HITEC ➔ Airport", origin: "HITEC City, Hyderabad, Telangana, India", dest: "Rajiv Gandhi International Airport (HYD), Hyderabad, India" }},
                {{ label: "VIZAG: Beach Rd ➔ Airport", origin: "Beach Road, Visakhapatnam, Andhra Pradesh, India", dest: "Visakhapatnam International Airport (VTZ), India" }}
            ],
            usa: [
                {{ label: "SF ➔ Stanford Hub", origin: "San Francisco Ferry Building, CA, USA", dest: "Stanford University, Palo Alto, CA, USA" }},
                {{ label: "SOMA ➔ SFO Airport", origin: "Central SOMA Tech Depot, San Francisco, CA, USA", dest: "San Francisco International Airport (SFO), CA, USA" }},
                {{ label: "NYC: Manhattan ➔ JFK", origin: "Manhattan, New York, NY, USA", dest: "JFK International Airport, New York, NY, USA" }}
            ],
            uk: [
                {{ label: "London: Central ➔ Heathrow", origin: "Central London, United Kingdom", dest: "Heathrow Airport (LHR), London, UK" }},
                {{ label: "Manchester ➔ Airport", origin: "Manchester City Centre, UK", dest: "Manchester Airport (MAN), UK" }}
            ],
            global: [
                {{ label: "Dubai: Marina ➔ DXB", origin: "Dubai Marina, United Arab Emirates", dest: "Dubai International Airport (DXB), UAE" }},
                {{ label: "Tokyo: Station ➔ Haneda", origin: "Tokyo Station, Tokyo, Japan", dest: "Haneda Airport (HND), Tokyo, Japan" }},
                {{ label: "Sydney ➔ Airport", origin: "Sydney Opera House, NSW, Australia", dest: "Sydney Airport (SYD), Australia" }}
            ]
        }};

        let currentRoutes = [];
        let selectedRouteId = 1;
        let fastestRouteId = 1;

        // Python's travel_time(distance, speed) logic implemented in JS
        function travelTime(dist, speed) {{
            if (speed <= 0) return 0;
            return (dist / speed) * 60;
        }}

        function getBaseDistance(origin, dest) {{
            const o = (origin || "").toLowerCase();
            const d = (dest || "").toLowerCase();
            if (o.includes("koramangala") && d.includes("blr")) return 41.5;
            if (o.includes("mumbai") && d.includes("pune")) return 148.0;
            if (o.includes("connaught") && d.includes("gurugram")) return 28.5;
            if (o.includes("hitec") && d.includes("airport")) return 34.0;
            if (o.includes("beach road") && d.includes("vtz")) return 16.5;
            if (o.includes("soma") && d.includes("sfo")) return 24.0;
            if (o.includes("sf") && d.includes("stanford")) return 42.0;
            if (o.includes("london") && d.includes("heathrow")) return 27.5;
            
            // Deterministic hash for any worldwide custom city/county
            let hash = 0;
            const str = o + "->" + d;
            for (let i = 0; i < str.length; i++) {{
                hash = (hash << 5) - hash + str.charCodeAt(i);
                hash |= 0;
            }}
            return Math.abs(hash % 45) + 15.0;
        }}

        function buildTrajectories(origin, dest) {{
            const base = getBaseDistance(origin, dest);
            const isIndia = (origin + dest).toLowerCase().includes("india");

            return [
                {{
                    id: 1,
                    name: isIndia ? "Route A (NH Expressway Corridor)" : "Route A (Direct Highway Corridor)",
                    origin: origin,
                    dest: dest,
                    distance: Number((base * 1.05).toFixed(1)),
                    speed: isIndia ? 68.0 : 70.0
                }},
                {{
                    id: 2,
                    name: isIndia ? "Route B (City Central Arterial Road)" : "Route B (City Center Expressway)",
                    origin: origin,
                    dest: dest,
                    distance: Number((Math.max(base * 0.78, 5.0)).toFixed(1)),
                    speed: isIndia ? 32.0 : 35.0
                }},
                {{
                    id: 3,
                    name: isIndia ? "Route C (Outer Ring Road Bypass)" : "Route C (Outer Perimeter Expressway)",
                    origin: origin,
                    dest: dest,
                    distance: Number((base * 1.35).toFixed(1)),
                    speed: isIndia ? 85.0 : 90.0
                }},
                {{
                    id: 4,
                    name: isIndia ? "Route D (Green Belt / Eco Byway)" : "Route D (Scenic Coastal / Eco Byway)",
                    origin: origin,
                    dest: dest,
                    distance: Number((base * 0.95).toFixed(1)),
                    speed: isIndia ? 45.0 : 48.0
                }},
                {{
                    id: 5,
                    name: isIndia ? "Route E (Metro Bypass Tunnel)" : "Route E (Metro Bypass Tunnel)",
                    origin: origin,
                    dest: dest,
                    distance: Number((Math.max(base * 0.65, 4.0)).toFixed(1)),
                    speed: isIndia ? 50.0 : 52.0
                }}
            ];
        }}

        function recalculate(origin, dest) {{
            currentRoutes = buildTrajectories(origin, dest);
            currentRoutes.forEach(r => {{
                r.time_min = travelTime(r.distance, r.speed);
                r.gmapUrl = `https://www.google.com/maps/dir/?api=1&origin=${{encodeURIComponent(r.origin)}}&destination=${{encodeURIComponent(r.dest)}}&travelmode=driving`;
            }});

            // Find fastest route using min equivalent
            const fastest = currentRoutes.reduce((min, r) => (r.time_min < min.time_min ? r : min), currentRoutes[0]);
            fastestRouteId = fastest.id;
            selectedRouteId = fastest.id;

            renderAll();
        }}

        function selectRoute(id) {{
            selectedRouteId = id;
            renderAll();
        }}

        function renderAll() {{
            const selected = currentRoutes.find(r => r.id === selectedRouteId) || currentRoutes[0];
            const fastest = currentRoutes.find(r => r.id === fastestRouteId) || currentRoutes[0];
            const isFastest = selected.id === fastest.id;

            // Update Hero Card
            const heroCard = document.getElementById("heroCard");
            const heroBadge = document.getElementById("heroBadge");
            const switchBtn = document.getElementById("switchShortestBtn");

            if (isFastest) {{
                heroCard.classList.remove("alt-selected");
                heroBadge.className = "badge fastest";
                heroBadge.textContent = "★ FASTEST & SHORTEST ROUTE (AI OPTIMAL)";
                switchBtn.style.display = "none";
            }} else {{
                heroCard.classList.add("alt-selected");
                heroBadge.className = "badge alt";
                heroBadge.textContent = "ℹ SELECTED ALTERNATIVE TRAJECTORY";
                switchBtn.style.display = "inline-flex";
            }}

            document.getElementById("heroName").textContent = selected.name;
            document.getElementById("heroTrajectory").textContent = `${{selected.origin}} ➔ ${{selected.dest}}`;
            document.getElementById("heroDist").textContent = `${{selected.distance.toFixed(1)}} km`;
            document.getElementById("heroTime").textContent = `${{selected.time_min.toFixed(1)}} min`;
            document.getElementById("heroSpeed").textContent = `${{selected.speed.toFixed(1)}} km/h`;
            document.getElementById("heroTimeBig").textContent = selected.time_min.toFixed(1);
            document.getElementById("heroTimeHours").textContent = `~${{(selected.time_min / 60).toFixed(2)}} hrs`;
            document.getElementById("heroGmapBtn").href = selected.gmapUrl;
            document.getElementById("hudSpeed").textContent = `${{selected.speed.toFixed(1)}} km/h`;

            const deltaEl = document.getElementById("heroDelta");
            if (isFastest) {{
                deltaEl.textContent = "🏆 AI Optimal";
                deltaEl.style.color = "var(--emerald)";
            }} else {{
                const diff = selected.time_min - fastest.time_min;
                deltaEl.textContent = `+${{diff.toFixed(1)}} min slower`;
                deltaEl.style.color = "var(--amber)";
            }}

            // Render Table
            const tbody = document.getElementById("routesTableBody");
            tbody.innerHTML = "";
            currentRoutes.forEach(r => {{
                const tr = document.createElement("tr");
                const isF = r.id === fastest.id;
                const isS = r.id === selected.id;

                if (isF) tr.classList.add("fastest-row");
                if (isS) tr.classList.add("selected-row");

                tr.onclick = () => selectRoute(r.id);
                tr.innerHTML = `
                    <td><strong>${{r.name}} ${{isS ? '🔹 [ACTIVE]' : ''}}</strong><br><small style="color:var(--text-muted);">${{r.origin}} ➔ ${{r.dest}}</small></td>
                    <td><code>${{r.distance.toFixed(1)}} km</code></td>
                    <td><code>${{r.speed.toFixed(1)}} km/h</code></td>
                    <td><strong>${{r.time_min.toFixed(1)}} min</strong></td>
                    <td><span class="badge ${{isF ? 'fastest' : 'alt'}}">${{isF ? '★ SHORTEST' : 'Alternative'}}</span></td>
                    <td><a href="${{r.gmapUrl}}" target="_blank" class="gmap-table-link" onclick="event.stopPropagation();">Google Maps ↗</a></td>
                `;
                tbody.appendChild(tr);
            }});

            // Render Chart
            const chart = document.getElementById("chartContainer");
            chart.innerHTML = "";
            const maxTime = Math.max(...currentRoutes.map(r => r.time_min), 50);

            currentRoutes.forEach(r => {{
                const isF = r.id === fastest.id;
                const isS = r.id === selected.id;
                const pct = Math.min((r.time_min / maxTime) * 100, 100);

                const row = document.createElement("div");
                row.className = "bar-row";
                row.onclick = () => selectRoute(r.id);
                row.innerHTML = `
                    <div class="bar-label" style="${{isS ? 'color: var(--primary); font-weight:700;' : ''}}">${{isS ? '▶ ' : ''}}${{r.name}}</div>
                    <div class="bar-track">
                        <div class="bar-fill ${{isF ? 'fastest' : ''}}" style="width: ${{pct.toFixed(1)}}%; ${{isS && !isF ? 'box-shadow: 0 0 10px var(--primary);' : ''}}"></div>
                    </div>
                    <div class="bar-val">${{r.time_min.toFixed(1)}} m</div>
                `;
                chart.appendChild(row);
            }});

            // Update Maps Embed
            document.getElementById("gmapIframe").src = `https://maps.google.com/maps?q=${{encodeURIComponent(selected.origin + " to " + selected.dest)}}&t=&z=11&ie=UTF8&iwloc=&output=embed`;
            document.getElementById("gmapLabel").textContent = `Google Maps: ${{selected.origin}} ➔ ${{selected.dest}}`;
            document.getElementById("gmapDirectLink").href = selected.gmapUrl;

            drawCanvas();
        }}

        function switchRegion(reg) {{
            document.querySelectorAll(".country-tab-btn").forEach(b => b.classList.remove("active"));
            event.target.classList.add("active");
            renderPresetChips(reg);
            const first = PRESETS[reg][0];
            if (first) {{
                document.getElementById("originInput").value = first.origin;
                document.getElementById("destInput").value = first.dest;
                recalculate(first.origin, first.dest);
            }}
        }}

        function renderPresetChips(reg) {{
            const c = document.getElementById("presetChipsContainer");
            c.innerHTML = "";
            (PRESETS[reg] || PRESETS.india).forEach(p => {{
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = "preset-chip";
                btn.textContent = p.label;
                btn.onclick = () => {{
                    document.getElementById("originInput").value = p.origin;
                    document.getElementById("destInput").value = p.dest;
                    recalculate(p.origin, p.dest);
                }};
                c.appendChild(btn);
            }});
        }}

        function swapPoints() {{
            const o = document.getElementById("originInput");
            const d = document.getElementById("destInput");
            const temp = o.value;
            o.value = d.value;
            d.value = temp;
            recalculate(o.value, d.value);
        }}

        function handleFormSubmit(e) {{
            e.preventDefault();
            const o = document.getElementById("originInput").value.trim();
            const d = document.getElementById("destInput").value.trim();
            if (o && d) recalculate(o, d);
        }}

        function switchView(mode) {{
            const hud = document.getElementById("hudWrapper");
            const gmap = document.getElementById("gmapWrapper");
            const bHud = document.getElementById("btnViewHud");
            const bGmap = document.getElementById("btnViewGmap");

            if (mode === "hud") {{
                hud.classList.remove("hidden");
                gmap.classList.add("hidden");
                bHud.classList.add("active");
                bGmap.classList.remove("active");
            }} else {{
                hud.classList.add("hidden");
                gmap.classList.remove("hidden");
                bGmap.classList.add("active");
                bHud.classList.remove("active");
            }}
        }}

        // Canvas Simulation Drawing
        function drawCanvas() {{
            const cvs = document.getElementById("navCanvas");
            if (!cvs) return;
            const ctx = cvs.getContext("2d");
            const w = cvs.width;
            const h = cvs.height;
            ctx.clearRect(0, 0, w, h);

            // Grid
            ctx.strokeStyle = "rgba(56, 189, 248, 0.06)";
            for (let x = 0; x < w; x += 30) {{ ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke(); }}
            for (let y = 0; y < h; y += 30) {{ ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }}

            // Bezier Route Line
            ctx.beginPath();
            ctx.moveTo(50, h - 50);
            ctx.bezierCurveTo(w * 0.35, h * 0.85, w * 0.6, h * 0.15, w - 50, 50);
            ctx.strokeStyle = "#10b981";
            ctx.lineWidth = 4;
            ctx.shadowColor = "rgba(16, 185, 129, 0.8)";
            ctx.shadowBlur = 10;
            ctx.stroke();
            ctx.shadowBlur = 0;

            // Markers
            ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(50, h - 50, 6, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(w - 50, 50, 6, 0, Math.PI*2); ctx.fill();
        }}

        // Initial setup
        renderPresetChips("india");
        recalculate("{default_origin}", "{default_destination}");
    </script>
</body>
</html>
"""

# =============================================================================
# 5. SAVE & AUTOMATICALLY LAUNCH IN BROWSER
# =============================================================================
output_file = "index.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"\n✅ Created interactive webpage: {os.path.abspath(output_file)}")
try:
    webbrowser.open(f"file://{os.path.abspath(output_file)}")
    print("🌐 Opened in your default browser.")
except Exception as err:
    print(f"Notice: {err}")