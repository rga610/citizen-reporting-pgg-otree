# Citizen Reporting Public Goods Game (oTree)

A multi-round public goods game with citizen reporting framing, supporting 4 treatment groups with configurable group sizes.

## Setup

1. **Activate the virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Run the development server:**
   
   **Recommended - Using the startup script:**
   ```powershell
   .\start_server.ps1
   ```
   
   **Alternative - Using uvicorn directly (recommended if otree devserver doesn't work):**
   ```powershell
   uvicorn otree.asgi:app --host 127.0.0.1 --port 8000 --reload
   ```
   
   **Or using otree command:**
   ```powershell
   otree devserver
   ```

3. **Access the application:**
   Open http://localhost:8000 in your browser

## Troubleshooting

If the server doesn't start:
- Make sure port 8000 is not already in use
- Check that the virtual environment is activated
- Try deleting `db.sqlite3` and running `otree resetdb --noinput` again
- Make sure you're in the project root directory (`public_goods_project`)

## Experiment Design

- **Treatment Groups:** 4 different groups (Treatment 1, 2, 3, 4)
- **Players per group:** Configurable (default: 4, set in `settings.py`)
- **Rounds:** 10 rounds (standard PGG structure)
- **Endowment:** 100 points per player per round
- **Multiplier:** 2x (public good multiplier)
- **Context:** Citizen reporting of faulty public infrastructure

## Treatment Groups

The experiment includes 4 separate session configurations:
- **Treatment 1:** `public_goods_treatment_1`
- **Treatment 2:** `public_goods_treatment_2`
- **Treatment 3:** `public_goods_treatment_3`
- **Treatment 4:** `public_goods_treatment_4`

Each treatment can be run independently. The treatment number is stored in the database for analysis.

## Admin Access

- Username: `admin`
- Password: `changeme`

**Note:** Change the admin password in `settings.py` before deploying to production.

## Experiment Flow

1. **Citizen Reporting Introduction** - Frames the experiment as citizen reporting
2. **Instructions** - Standard PGG instructions with citizen reporting context
3. **Contribute** - Players decide how much to contribute (repeated for each round)
4. **Results Wait Page** - Wait for all players
5. **Results** - Show round results
6. **Final Results** - Show total earnings after all rounds (shown only after final round)

## Configuration

To change the number of participants per group, edit `settings.py`:

```python
PARTICIPANTS_PER_GROUP = 4  # Change this value
```

To change the number of rounds, edit `public_goods/models.py`:

```python
num_rounds = 10  # Change this value
```

## Project Structure

```
public_goods_project/
├── settings.py          # oTree project settings (4 treatment configs)
├── requirements.txt     # Python dependencies
├── start_server.ps1     # Startup script
├── _static/            # Static files directory
└── public_goods/       # The game app
    ├── models.py       # Game models, treatment tracking, PGG logic
    ├── pages.py        # Page definitions (intro, contribute, results)
    ├── tests.py        # Automated tests
    └── templates/      # HTML templates
        ├── CitizenReportingIntro.html  # Citizen reporting framing
        ├── Introduction.html           # Instructions page
        ├── Instructions.html           # PGG instructions
        ├── Contribute.html             # Contribution decision
        ├── Results.html                # Round results
        └── FinalResults.html           # Final summary
```

