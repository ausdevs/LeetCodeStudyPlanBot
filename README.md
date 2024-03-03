# LeetCodeStudyPlanBot

A discord bot to post a challenge from the NeetCode150 daily.

Contact @JackWFinlay if you want to add this to your server. This is currently in beta. Note that things are fragile for now :)

## Configuring
You will have to configure the following secrets in GitHub to allow this to run:

```env
DISCORD_TOKEN=<Discord bot token>
DISCORD_CHANNEL_ID=<ChannelId>
DISCORD_DEFAULT_PING=<Default Ping RoleId>
DISCORD_EASY_PING=<RoleId for Easy difficulty pings>
DISCORD_MEDIUM_PING=<RoleId for Medium difficulty pings>
DISCORD_HARD_PING=<RoleId for Hard difficulty pings>
STUDY_PLAN_START_DATE=<Start date e.g. 2024-01-01T00:00:00>
```