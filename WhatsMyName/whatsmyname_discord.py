# Header + WhatsMyName Data .json (WMN sites list)
WMN_URL = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
WMN_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

#Timeout to make the search more accurate
TIMEOUT = 3  

#Check sites and existence codes and existence strings 
async def check_site(session, site, username):
    try:
        async with session.get(site["uri_check"].format(account=username), headers=WMN_HEADERS) as response:
            text = await response.text()
            if response.status == site["e_code"] and site["e_string"] in text:
                print(f"Username '{username}' found on site {site['name']}")  # Logging
                return site["name"], site["uri_check"].format(account=username)
    except Exception as e:
        print(f"Error checking {site['name']}: {e}")
    return None


# check username existence
async def check_username_existence(username, data):
    found_sites = []
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, site, username) for site in data["sites"]]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        found_sites.extend([res for res in results if res is not None])
    print(f"Found username '{username}' on {len(found_sites)} sites.")  
    return found_sites


# GitOSINT discord Bot Command = !whatsmyname {username}
@discord_bot.command(name="whatsmyname")
async def checkuser(ctx, *, username: str):
    await ctx.send(f"Checking for username `{username}`... The scan can take anything in between 2-5 minutes as I set the timeout longer to make searches more accurate.")
    
    data = None
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.get(WMN_URL, headers=WMN_HEADERS)
            
            if response.content_type != 'application/json':
                print(f"Unexpected content type: {response.content_type}")
                data_content = await response.text()
                data = json.loads(data_content)
            else:
                data = await response.json()
                
        except Exception as e:
            print(f"Error fetching WMN data: {e}")
            await ctx.send("Failed to fetch data from WMN.")
            return

    if data:
        found_sites = await check_username_existence(username, data)
        if found_sites:
            embed = discord.Embed(title=f"Websites where '{username}' was found:", color=0x3498db)
            for site, url in found_sites:
                embed.add_field(name=site, value=url, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"No websites found for username '{username}'.")
    else:
        await ctx.send("Nothing was found or an error occurred.")

