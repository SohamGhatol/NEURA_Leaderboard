import asyncio
import aiohttp
import time
import sys
import random
from typing import Dict, List

# ==============================================================================
# CONFIGURATION
# ==============================================================================
BASE_URL = "https://prompt-engineering-behind.onrender.com/api/v1" 

CREDENTIALS = [
    {"email": "shaikhjoya702@gmail.com", "password": "shai9395"},
    {"email": "krutikakokate2025.ainds@mmcoe.edu.in", "password": "krut0636"},
    {"email": "sakshamyadav2024.it@mmcoe.edu.in", "password": "saks1977"},
    {"email": "kartiktikhe2025.it@mmcoe.edu.in", "password": "kart7816"},
    {"email": "rushikeshchadekar2025.it@mmcoe.edu.in", "password": "rush6977"},
    {"email": "piyushsonawane2025.ainds@mmcoe.edu.in", "password": "piyu0358"},
    {"email": "sahebmule7@gmail.com", "password": "sahe6924"},
    {"email": "sohamdegaonkar2025.it@mmcoe.edu.in", "password": "soha8590"},
    {"email": "atharvamangalgi2025.ainds@mmcoe.edu.in", "password": "Atha4890"},
    {"email": "sakshikamble2025.comp@mmcoe.edu.in", "password": "saks9007"},
    {"email": "vedantchandgude2026.it@mmcoe.edu.in", "password": "veda0445"},
    {"email": "virajtarade2024.ainds@mmcoe.edu.in", "password": "vira3899"},
    {"email": "mrunmayidhuldhar2025.it@mmcoe.edu.in", "password": "mrun7616"},
    {"email": "parthdahiphale2025.it@mmcoe.edu.in", "password": "part9577"},
    {"email": "aryanwaghre2025.it@mmcoe.edu.in", "password": "arya1542"},
    {"email": "srujanperkunde2024.ainds@mmcoe.edu.in", "password": "sruj0595"},
    {"email": "machalesamruddhi@gmail.com", "password": "mach0144"},
    {"email": "swarajkavthekar2025.etc@mmcoe.edu.in", "password": "swar7974"},
    {"email": "divyatakhatdeo2025.ainds@mmcoe.edu.in", "password": "divy7640"},
    {"email": "sanikadhore2025.ainds@mmcoe.edu.in", "password": "sani9752"},
    {"email": "rukminiraut444@gmail.com", "password": "rukm4323"},
    {"email": "tanayvidhate2025.ainds@mmcoe.edu.in", "password": "tana7448"},
    {"email": "sohambhopale2025.it@mmcoe.edu.in", "password": "soha9385"},
    {"email": "abhishekmadke2025.ainds@mmcoe.edu.in", "password": "abhi6988"},
    {"email": "likhitrakhade2025.comp@mmcoe.edu.in", "password": "likh5977"},
    {"email": "shivrajtakkalaki2025.etc@mmcoe.edu.in", "password": "shiv0376"},
    {"email": "abdulmerchant2025.ainds@mmcoe.edu.in", "password": "abdu5151"},
    {"email": "atharvaraut2025.elect@mmcoe.edu.in", "password": "atha1577"},
    {"email": "sarthakdeshmukh2024.ainds@mmcoe.edu.in", "password": "sart8216"},
    {"email": "chinmaygade2024.ainds@mmcoe.edu.in", "password": "chin9184"},
    {"email": "yashkharabe2025.comp@mmcoe.edu.in", "password": "yash2732"},
    {"email": "vedantsuryawanshi2025.elect@mmcoe.edu.in", "password": "veda3868"},
    {"email": "abhishekgodbole2025.comp@mmcoe.edu.in", "password": "abhi6905"},
    {"email": "ojaskute2025.comp@mmcoe.edu.in", "password": "ojas9041"},
    {"email": "aparnabhamare2025.comp@mmcoe.edu.in", "password": "apar6801"},
    {"email": "pratikshachavan2024.comp@mmcoe.edu.in", "password": "prat6918"},
    {"email": "prachimorkhade07@gmail.com", "password": "prac8578"},
    {"email": "sammrudhikulkarni2024.comp@mmcoe.edu.in", "password": "samm8191"},
    {"email": "suyashkolhe2025.etc@mmcoe.edu.in", "password": "suya6528"},
    {"email": "vidhikabra2024.ainds@mmcoe.edu.in", "password": "vidh8988"},
    {"email": "yugantvarekar2024.comp@mmcoe.edu.in", "password": "yuga9646"},
    {"email": "shrutijadhav2025.comp@mmcoe.edu.in", "password": "shru8057"},
    {"email": "radhikasuryatal2024.it@mmcoe.edu.in", "password": "radh9205"},
    {"email": "ishakamthe2025.it@mmcoe.edu.in", "password": "isha9527"},
    {"email": "mrunaldoifode2025.ainds@mmcoe.edu.in", "password": "mrun9134"},
    {"email": "swarakulkarni2025.etc@mmcoe.edu.in", "password": "swar1875"},
    {"email": "atharvapardeshi992@gmail.com", "password": "atha0668"},
    {"email": "utkarshgedam2024.ainds@mmcoe.edu.in", "password": "utka6916"},
    {"email": "krishnamarne2025.ainds@mmcoe.edu.in", "password": "kris9073"},
    {"email": "tusharbarve2025.etc@mmcoe.edu.in", "password": "tush1488"},
    {"email": "sohambhoir2024.etc@mmcoe.edu.in", "password": "soha8103"},
    {"email": "adinathshinde2025.it@mmcoe.edu.in", "password": "adin2058"},
    {"email": "pritideshmukh2026.it@mmcoe.edu.in", "password": "prit9121"},
    {"email": "tejaswinikor2025.ainds@mmcoe.edu.in", "password": "teja9574"},
    {"email": "adityajathar2024.elect@mmcoe.edu.in", "password": "adit3358"},
    {"email": "shreyarathod2024.comp@mmcoe.edu.in", "password": "shre9195"},
    {"email": "shrutishelar2025.it@mmcoe.edu.in", "password": "shru9698"},
    {"email": "shrutimanval104@gmail.com", "password": "shru5383"}
]

# We use an optimized prompt string to score high marks and stress test the regex engine
DUMMY_PROMPT = """
You are an expert strategist and analyst. Your role is to carefully analyze the input context and generate a highly structured output based on the following guidelines.
- You must always format your response as a JSON array of objects.
- Ensure that the output strictly follows the required format.
- Do not include any conversational preamble or extra text. Output only the JSON.
- If any input is ambiguous or unclear, return a null value for that specific field.
- For example, you could write exactly 3 bullet points inside the JSON array.
- The word count must be at least 30 words so that we can accurately assess the response quality and clarity.
"""

# Global statistics
stats = {
    "login_times": [],
    "fetch_challenge_times": [],
    "submit_challenge_times": [],
    "completed": 0,
    "failed": 0
}

class TeamClient:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None

    async def login(self, session: aiohttp.ClientSession, delay: float):
        await asyncio.sleep(delay)
        start = time.time()
        try:
            resp = await session.post(f"{BASE_URL}/auth/login", json={"email": self.email, "password": self.password}, timeout=30)
            if resp.status == 200:
                data = await resp.json()
                self.token = data.get("access_token")
                stats["login_times"].append(time.time() - start)
                return True
            else:
                print(f"[!] Login failed for {self.email}: {resp.status}")
                return False
        except Exception as e:
            print(f"[!] Login error for {self.email}: {e}")
            return False

    async def complete_arena(self, session: aiohttp.ClientSession):
        headers = {"Authorization": f"Bearer {self.token}"}
        
        for i in range(1, 6): # 5 Challenges
            # 1. Fetch Challenge
            start = time.time()
            try:
                fetch_resp = await session.get(f"{BASE_URL}/arena/my-challenge", headers=headers, timeout=20)
                if fetch_resp.status != 200:
                    print(f"[-] {self.email} failed to fetch challenge {i}: {fetch_resp.status}")
                    stats["failed"] += 1
                    return
                stats["fetch_challenge_times"].append(time.time() - start)
            except Exception as e:
                print(f"[-] {self.email} fetch timeout on challenge {i}: {e}")
                stats["failed"] += 1
                return

            # Simulate typing / thinking time (Random between 1 to 5 seconds to stagger CPU load slightly)
            await asyncio.sleep(random.uniform(1.0, 5.0))

            # 2. Submit Challenge
            start = time.time()
            try:
                payload = {
                    "challenge_index": i,
                    "prompt_text": DUMMY_PROMPT,
                    "diagnosis_notes": "Identified lack of context and formatting."
                }
                sub_resp = await session.post(f"{BASE_URL}/arena/submit-challenge", json=payload, headers=headers, timeout=30)
                if sub_resp.status == 200:
                    stats["submit_challenge_times"].append(time.time() - start)
                else:
                    data = await sub_resp.text()
                    print(f"[-] {self.email} failed to submit challenge {i}: {sub_resp.status} {data}")
                    stats["failed"] += 1
                    return
            except Exception as e:
                print(f"[-] {self.email} submit timeout on challenge {i}: {e}")
                stats["failed"] += 1
                return
            
            print(f"[+] {self.email} completed challenge {i}/5")

        stats["completed"] += 1


def print_stats():
    def get_avg(arr): return sum(arr)/len(arr) if arr else 0
    def get_max(arr): return max(arr) if arr else 0
    def get_min(arr): return min(arr) if arr else 0

    print("\n" + "="*50)
    print("ARENA STRESS TEST RESULTS")
    print("="*50)
    print(f"Teams Successfully Completed: {stats['completed']}")
    print(f"Teams Failed/Dropped: {stats['failed']}")
    print("\n[Inference & API Timings]")
    print(f"Average Login Time:       {get_avg(stats['login_times']):.2f}s (Min: {get_min(stats['login_times']):.2f}s, Max: {get_max(stats['login_times']):.2f}s)")
    print(f"Average Fetch Challenge:  {get_avg(stats['fetch_challenge_times']):.2f}s (Min: {get_min(stats['fetch_challenge_times']):.2f}s, Max: {get_max(stats['fetch_challenge_times']):.2f}s)")
    print(f"Average Submit & Score:   {get_avg(stats['submit_challenge_times']):.2f}s (Min: {get_min(stats['submit_challenge_times']):.2f}s, Max: {get_max(stats['submit_challenge_times']):.2f}s)")
    print("="*50 + "\n")


async def main():
    print("========================================")
    print("NEURA ARENA END-TO-END SIMULATOR")
    print("========================================\n")
    
    async with aiohttp.ClientSession() as session:
        # STEP 1: Log in all teams (Staggered to simulate natural entry)
        print("1. Logging in all 58 teams...")
        teams = [TeamClient(cred["email"], cred["password"]) for cred in CREDENTIALS]
        
        login_tasks = [t.login(session, random.uniform(0, 10)) for t in teams]
        await asyncio.gather(*login_tasks)
        
        active_teams = [t for t in teams if t.token]
        print(f"\n=> {len(active_teams)} teams successfully logged in and standing by.")
        
        # STEP 2: Wait for Judge to start the Arena
        print("\n" + "*"*60)
        print("PLEASE GO TO YOUR JUDGE DASHBOARD AND START THE ARENA NOW!")
        print("This script is actively polling the server and will launch the")
        print("participants as soon as the status changes to LIVE.")
        print("*"*60 + "\n")
        
        arena_live = False
        while not arena_live:
            try:
                resp = await session.get(f"{BASE_URL}/arena/status", timeout=5)
                data = await resp.json()
                if data.get("status") == "live":
                    arena_live = True
                    print("\n[LIVE] ARENA IS LIVE! TEAMS ARE NOW SUBMITTING PROMPTS...")
                else:
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    await asyncio.sleep(2)
            except Exception as e:
                print(f"\nPolling error: {e}")
                await asyncio.sleep(2)

        # STEP 3: Blast all 5 challenges concurrently across all active teams
        # We add a slight 5-second random stagger because Supabase Free Tier only allows 15 concurrent DB connections.
        start_arena = time.time()
        
        async def staggered_complete(t):
            await asyncio.sleep(random.uniform(0, 5))
            await t.complete_arena(session)
            
        challenge_tasks = [staggered_complete(t) for t in active_teams]
        await asyncio.gather(*challenge_tasks)
        
        print(f"\nAll teams finished in {time.time() - start_arena:.2f} seconds!")

        # STEP 4: Print Statistics
        print_stats()
        
        print("You can now End the Arena and Release Results from the dashboard.")


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
