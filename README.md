# GitOSINT Bot 🤖

<br>

> ⚠️ **Update 20th of August 2023**:<br>
> Originally, my intention was to design a Bot solely for my personal use, enhancing my investigative capacities particularly when I'm on the move. Situations where I might be without laptop access or when Termux proves insufficient made the idea of accessing my Discord BOT via smartphone the perfect remedy.

>Believing in the power of community and the spirit of sharing, I opened access to the Bot for everyone, free of charge. The enthusiasm with which GitOSINT was received was [remarkable](https://twitter.com/cyb_detective/status/1692944310856024535).
>In fact, it was integrated into over 100 servers. This led to a verification process by Discord, requiring personal identification on my part. I complied, and am pleased to note that the Bot was verified and acknowledged by Discord's team.

> **However, I've made the decision to discontinue the GITOSINT Bot**. My attention was drawn to certain concerns: <br>
Notably, the Bot being invited to servers which don't align with community standards. **A particular instance being its presence in a server promoting racism.**

<br>


<img width="633" alt="GITOSINT" src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/a0277f17-f13b-4116-be75-76899e0cf6b6">

# Description 🧠
GitOSINT is a Discord bot that helps you to find information/intelligence.

The bot can:
- Provide information on github users and find their email address and more...
- Provide information on phone numbers with Firefly
- Provide intelligence on a username and scan across +2500 sites with the Maigret OSINT Tool
- Provide information on the username history of a Twitter user
- Extract intelligence from Instagram accounts
- Provide intelligence on Mastodon users
- Find out if a Gmail address is deliverable, meaning if it exists and is valid or not.
- Scan a username across all sites that are part of the Sherlock-project
- Provide intelligence on a public Google Document with xeuledoc OSINT Tool.
- Provide intelligence on sites the target email is registered on with holehe. (holehe is one of the best tools out there)
- Scan 2 usernames at once using socialscan
- Scan usernames across +600 sites using the WhatsMyName project
- Get Historical weather from any city ona given date



**Simply invite the BOT to your server.**

Bot : ```𝐏𝐮𝐫𝐫𝐥𝐨𝐜𝐤𝐇𝐨𝐥𝐦𝐞𝐬 🐾#0607```
<br>
Handler: ```𝙲.𝟶.𝟺#1860```

# Why use a Discord Bot 🦾

Using command line OSINT Tools on a computer requires the opening of numerous scripts.
Same on a phone if you are doing OSINT "On-the-Go" by using Termux which can be demanding.

**GitOSINT Bot (Purrlock Holmes) consolidates many tools into one**, eliminating the need to individually open scripts. This means that individuals can conveniently conduct OSINT investigations right from their Discord on their phones. Many CTF teams already dedicate countless hours on Discord discussing findings and communicating. The Bot can be a big help. 

By adding this BOT to your server, you'll save valuable time. No more manual searches or launching python scripts. Simply initiate a search within your server and receive immediate results.

Many CTF teams spend hours on discord sharing their findings and communicating, so inviting the BOT to your server is a time saver, no need to search manually or to open python scripts, just run the search from your own server and get results.

# About GitOSINT Bot 😺
- GitOSint Bot wasn't always a Bot. He used to be a real cat and was a very prolific spy-cat called **Purrlock Holmes**. 
- Read more about the life of **Purrlock Holmes** [Here](https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/blob/master/Project_Resurrection.png)


<img width="333" alt="Purrlock" src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/d7c10db1-1b80-4198-bd49-f508430fe757">



# Commands 🎮

**ℹ️ Bot General Information**
- `!hello` | Greetings
- `!bot_help`| This will show you all the commands available  
- `!whoami` | Find out about GitOsint and his past
- `!gitosint_bot` | Get information on the bot's handler/creator
<br>

**:octocat: GitHub OSINT Tool**
- `!user {username}` | Input Github username to find information on a GitHub user
- `!email {email_address}` | Input an email address, this reverse search can find a github user
- `!repo_emails {username} {repo_name}` | Input username + repo name to get all emails associated with a repo
- `!gitrepos {username}` | Powerful tool, this is based on GitStalk tool, from a username, all user repos are scanned and all emails associated are provided
- `!search_keys {username}` | Based on OSGINT made by [Hippiiee](https://github.com/hippiiee/osgint) | Input username to search for GPG and SSH Keys. (*GPG Keys found are decoded and will show the user email address)
<br>

**📱 Cellphone Investigations**
- `!phone_search {phone number}` | Firefly Tool made by [Lexxrt](https://github.com/Lexxrt) | You will get intelligence on the phone number such as country, phone company, and sometimes location for the USA | Phone international format to input= +336XXXXXXXX
<br>


**📧 Email Investigations**
- `!holehe {email}` | holehe is a powerful tool known by most OSINT professionals | It is made by [@megadose also known as Palenath](https://github.com/megadose) | Get information on the sites the target email is registered on.
- `!gmail {email}` | Gmail existence verification | coded by me [@C3n7ral051nt4g3ncy](https://github.com/C3n7ral051nt4g3ncy) | Find out if a gmail address is deliverable (Valid)
<br>


**👤 Username Investigations**
- `!whatsmyname {username}` | WhatsMyName OSINT Tool for username enumeration by [Webbreacher](https://github.com/webbreacher) | Input username and get a full scan on +600 sites.
- `!maigret {username}` | Maigret OSINT Tool for username enumeration by [soxoj](https://github.com/soxoj) | Input username and get a full scan on over 2500 sites. (The sites are in the data.json file)
- `!twitter_history {username}` | Twitter Historical OSINT Tool | It can currently be used to look up **542 million** historical screen names for 443 million Twitter accounts | Made by [@travisbrown](https://github.com/travisbrown)
- `!masto {username}` | Masto OSINT Tool | It will scan for the username across Mastodon instances/servers by using the Mastodon API and also the Masto OSINT Tool own database which often beats the Mastodon API | Made by me [@C3n7ral051nt4g3ncy](https://github.com/C3n7ral051nt4g3ncy)
- `!toutatis {username} {sessionID}` | Toutatis made by [@megadose aka Palenath](https://github.com/megadose) | Extract some interesting Instagram account information
- `!sherlock {username}` | Sherlock username OSINT Tool | by [@sherlock-project](github.com/sherlock-project)
- `!socialscan {username}` or `!socialscan {username_1},{username_2} `| socialscan is a well-known tool made by [@iojw](https://github.com/iojw) | Scan for one or two usernames simultaneously across various social websites.
<br>

**📂 Document Investigations**
- `!xeuledoc {Google_doc_link}` | xeuledoc created by [@Malfrats](https://github.com/Malfrats)
<br>

**📌 Location Intelligence**
- `!historical_weather {city} {date}` | Format e.g for 30th of March 2023: `{2023-03-30}` |  Made by me [@C3n7ral051nt4g3ncy](https://github.com/C3n7ral051nt4g3ncy)
<br>


# Invite GitOSINT Bot 📨
- GitOSINT Bot has been verified and approved by discord teams
- GitOSINT Bot has been approved by Top.GG 🎉! You can invite the Bot from Top.gg by clicking [here](https://top.gg/bot/1114671244676177950) and you can also leave stars and feedback on [top.gg](https://top.gg/bot/1114671244676177950)
<img width="133" src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/e30842a7-abf7-41fe-9177-dcdc2e92e59b">

# Future updates 🔮
Will be updating the Bot with more search possibilities in the future...
If there is any problem, just open an issue on this repository.

# Contributions ❤️
**The Bot is not free for me**, it is online 24/7, and hosting Mr. Purrlock Holmes costs money.
If you like this bot and find it useful for your research, you can contribute financially in 2 ways:
- Send Nitros to my Discord --> `𝙲.𝟶.𝟺#1860` <br>
or
- Buy me a coffee --> [Tactical OSINT Analyst Ko-Fi](https://ko-fi.com/tacticalintelanalyst)

# Thanks 🙏
A big Thanks to Megadose (Palenath), Webbreacher, Soxoj, Sherlock-prokect, Hippiiee, Lexxrt, TravisBrown, un1k0n, Malfrats Industries, iojw: ⬇

<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/0c6461ea-68e5-4bf5-8e6e-50229f2ba9b3" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/5fc7eda5-51a8-4d50-8f03-0e4ee267480d" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/586213da-5870-4af3-b3c9-4431da31b820" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/77971867-3b51-4262-bae8-07ec15a039ec" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/2efae689-307a-489f-9012-54b41d847927" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/e64ede6e-3873-4110-9fd0-d2aa1ea3bf8b" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/1967c6a4-f625-428a-b4aa-afd61564b26c" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/d1c93f48-44b9-48c2-999c-e7fd3f0944a9" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/6e765ab5-35a8-4117-aa7f-9b8889f5be4b" height="77"></a>
<img src="https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot/assets/104733166/7f9fd7e7-f4da-43cd-a26d-f35a81c79a4b" height="77"></a>




# Use of third-party tools and code 🛠️
The tools I use within this project are mentionned, as well as their authors.
The tools are under the **GNU General Public License**

**(GNU GPL or simply GPL) is a series of widely-used free software licenses that guarantee end-users the freedom to run, study, share, and modify the software licensed under it.** Specifically, the GPL grants users the following four freedoms:

- Freedom 0: The freedom to run the program for any purpose.
- Freedom 1: The freedom to study how the program works and adapt it to your needs (access to the source code is a precondition for this).
- Freedom 2: The freedom to redistribute copies so you can help others.
- Freedom 3: The freedom to improve the program and release your improvements to the public, so the whole community benefits from this.

