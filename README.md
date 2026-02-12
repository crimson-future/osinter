To run this code: 
1) Install UV: [https://docs.astral.sh/uv/getting-started/installation/]
2) Install/Confirm installation of Python3 3.13+:
    - python3 --version
        - If this returns Not Found, you need to do a fresh install. On Linux, this is usually | sudo apt update, then | sudo apt install python3. 
        - If the version is older than 3.13, you may need to do | sudo apt upgrade or a fresh install of python to a new version via Tarball.
2) Open the command line, and use cd <path_to_code_directory>
3) Run the code: uv run main.py


=====SUMMARY=====
This code is designed to accept an artifact via command line, then return a general OSINT report of that artifact in a readable format.
Output is both shown directly in the command line and output to priors.json as a unique JSON entry with the artifact as the header.
You can also review prior artifacts you've searched for by navigating the Artifacts menu and selecting the one you wish to see the results for. 

IMPORTANT NOTE: Osinter only stores the last 20 entries. To save a report, you can use the Export function to dump that specific artfiact's 
results from the JSON record into a standalone file as a plaintext report. 


=====GENERAL ABSTRACT=====
> This is a work in progress and should not be considered a completed project for use. 
1) Select from menu: 
    - SEARCH_NEW
    - REVIEW EXISTING

2: IF SEARCH NEW: 
    - SELECT ARTIFACT TYPE - HASH | DOMAIN | IP | EMAIL | FILE_NAME 
        - Perform queries via API against relevant OSINT sites
        - Format results in JSON structure
        - Present as Plaintext in CLI, Append results to existing Priors file, remove oldest as needed
        - FEATURE ADD: Direct export switch, allowing for a dump to a report file without needing to go to menu to do it
        - FEATURE ADD: Bulk Search (max 5 unique). Spaces out queries to avoid rate limiting. Automatically creates Dump.  

3: IF REVIEW EXISTING:
    - READ PRIORS
    - Display list of artifacts with number selection. Use arrow keys to navigate or keyboard interrupt to input specific artifact. 
        - Alpha will likely use number menu from shard_tracker project instead
    - SELECT OPTION: 
        1: DISPLAY RESULTS: Show the report for that artifact in plaintext
        2: EXPORT RESULTS: Dumps report for the selected artifact into a plaintext TXT file. 
            - FEATURE ADD: Bulk selection for output.
            - FEATURE ADD: Send results to email and/or save as write-protected PDF. 


Additional hurdles: 
    APIs for use require accounts in most cases. May need sign-in or general <broad> account usage. Investigate how Sputnik requests work, see if that's something I can replicate.
        
Additional dream ideas: 
    TKinter/similar interface for easier packaging/usage, or general standalone packaging for simpler execution, including a localized Python version to be shipped/embedded. 
        - General hope: maximally simplified usage with minimal setup beyond Install from the Github. 
