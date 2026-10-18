import json
TIN=dict(name='Tinder',bg='#FE3C72',fg='#FFFFFF',radar='#FE3C72')
LIN=dict(name='LinkedIn',bg='#0A66C2',fg='#FFFFFF',radar='#2E8BFF')
IG=dict(name='Instagram',bg='#C13584',fg='#FFFFFF',radar='#E1306C')
WA=dict(name='WhatsApp',bg='#25D366',fg='#0B2E13',radar='#25D366')
STR=dict(name='Strava',bg='#FC4C02',fg='#FFFFFF',radar='#FC4C02')
HIN=dict(name='Hinge',bg='#2B2B2B',fg='#FFFFFF',radar='#D6D6D6')
X=dict(name='X',bg='#000000',fg='#FFFFFF',radar='#E7E9EA')
DIS=dict(name='Discord',bg='#5865F2',fg='#FFFFFF',radar='#8C94FF')
TW=dict(name='Twitch',bg='#9146FF',fg='#FFFFFF',radar='#A970FF')
TT=dict(name='TikTok',bg='#000000',fg='#FFFFFF',radar='#25F4EE')
def P(base,**k): d=dict(base); d.update(k); return d
def C(*a): return [[a[i],a[i+1]] for i in range(0,10,2)]
E=[]
E.append(dict(ep=3,name='Jake',title='The 25-year-old<br>gym bro',kicker='THE 25-YEAR-OLD GYM BRO',plat=[
 P(TIN,img='jake_tinder',who='Jake <span style="font-weight: 400">25</span>',bio='6\'1 if you count the lifting shoes. Looking for a gym partner and a protein partner. Swipe left if you skip leg day.',crit=C('Honesty',6,'Charm',7,'Effort',7.5,'Desperation',7,'Fun',8),joke='He brought the shaker to the beach. On purpose.'),
 P(STR,img='jake_strava',who='Jake',meta='5:42 AM · 10.2 km',bio='Pain is temporary. Kudos are forever. 🏃 Training for my 3rd half marathon (registered for zero).',crit=C('Discipline',10,'Honesty',9,'Humility',3,'Effort',10,'Fun',8),joke='Wakes up at 5am so the app can tell everyone.'),
 P(LIN,img='jake_linkedin',who='Jake, 25',bio='Results-Driven Growth Enthusiast | I apply gym discipline to Excel | Reps, sets and KPIs 💪',foot='312 connections · Junior Sales Associate',crit=C('Buzzwords',9,'Optimism',9.5,'Experience',3,'Honesty',4,'Fun',4),joke='The suit is a medium. He is not.'),
 P(IG,img='jake_instagram',who='Jake',meta='41 posts · 2,980 followers',bio='Chest day is every day 🏋️<br>Coaching? DM me (I am not a coach)<br>Link below for my creatine code',crit=C('Aesthetic',7,'Mirror use',10,'Effort',8,'Honesty',5,'Fun',7),joke='Same mirror, same pose, 41 posts.')],
 headline='Jake is most himself on Strava.',sub='At 5:42 AM. Uninvited.',tag='Tag the Jake who sends you his run stats. 👇',next='The 24-year-old graduate',follow='Follow for episode 4',
 cap='''One person. Four apps. Four completely different guys. 😅

Meet Jake, 25, gym bro.
On Tinder he wants a protein partner.
On Strava he's up at 5:42 AM.
On LinkedIn he applies gym discipline to Excel.
On Instagram it's chest day. Every day.

We scored every version. Swipe to see which app gets the real Jake 👉

💬 Your turn: comment the weirdest bio you've ever seen from a gym bro.
Tinder, Strava, LinkedIn, Instagram… we want them all.
The best ones end up in a future episode 👀

Tag the Jake who sends you his run stats 👇

#instagrambio #bioideas #gymbro #tinderbio #gymhumor #relatable #socialmediahumor #coolbio360'''))
E.append(dict(ep=4,name='Sofia',title='The 24-year-old<br>graduate',kicker='THE 24-YEAR-OLD GRADUATE',rot=-2,plat=[
 P(WA,img='sofia_whatsapp',who='Sofia',meta='last seen today at 03:12',label='About',bio='Available for full-time, part-time, any-time 🎓',fs=34,crit=C('Effort',7,'Desperation',9.5,'Honesty',10,'Mystery',1,'Fun',6),joke='The graduation photo is doing a lot of work here.'),
 P(LIN,img='sofia_linkedin',who='Sofia, 24',bio='#OpenToWork | Recent Graduate | MSc in Things Employers Find Interesting | Fast learner, faster at reading rejection emails',foot='500+ connections · 214 applications sent',crit=C('Buzzwords',8,'Optimism',7,'Experience',2,'Honesty',8.5,'Fun',7),joke='Smiling like the recruiter is watching. The recruiter is not.'),
 P(HIN,img='sofia_hinge',who='Sofia, 24',label='My most irrational fear',bio='Getting asked “where do you see yourself in 5 years?” on a date AND in an interview in the same week.',crit=C('Honesty',9.5,'Charm',9,'Effort',8,'Desperation',4,'Fun',9.5),joke='Funniest she\'s been all year. No cover letter needed.'),
 P(IG,img='sofia_instagram',who='Sofia',meta='112 posts · 846 followers',bio='📍 Somewhere with good wifi<br>Reading, writing, refreshing my inbox ☕<br>Currently: between chapters',crit=C('Aesthetic',9,'Mystery',8,'Effort',8.5,'Honesty',3,'Fun',6),joke='“Between chapters” means unemployed. Beautifully lit.')],
 headline='Sofia is most herself on Hinge.',sub='Where nobody asks for a CV.',tag='Tag the Sofia still refreshing her inbox. 👇',next='The 28-year-old founder',follow='Follow for episode 5',
 cap='''One person. Four apps. Four completely different women. 😅

Meet Sofia, 24, fresh graduate looking for a job.
On WhatsApp she's available any-time.
On LinkedIn she's #OpenToWork (214 applications and counting).
On Hinge she's finally funny.
On Instagram she's "between chapters".

We scored every version. Swipe to see which app gets the real Sofia 👉

💬 Your turn: comment the weirdest bio you've ever seen from a job hunter.
LinkedIn, Hinge, WhatsApp, Instagram… we want them all.
The best ones end up in a future episode 👀

Tag the Sofia still refreshing her inbox 👇

#instagrambio #bioideas #linkedinbio #opentowork #gradlife #jobhunt #relatable #coolbio360'''))
E.append(dict(ep=5,name='Ethan',title='The 28-year-old<br>startup founder',tfs=64,kicker='THE 28-YEAR-OLD STARTUP FOUNDER',plat=[
 P(X,img='ethan_x',who='Ethan',meta='@ethanbuilds · 418 followers',bio='Founder &amp; CEO @[stealth] 🚀 | Building the future of [redacted] | Ex-nothing | Opinions are my own (and my cofounder\'s)',crit=C('Hype',10,'Mystery',9,'Clarity',1,'Honesty',3,'Fun',7),joke='Six people in the room. He called it a keynote.'),
 P(TIN,img='ethan_tinder',who='Ethan <span style="font-weight: 400">28</span>',bio='Founder. Looking for a co-founder of my heart 💼❤️ The dog is borrowed. Pitch me your best first date in 3 slides.',crit=C('Honesty',7,'Charm',7.5,'Effort',8,'Desperation',6,'Fun',9),joke='The dog has more equity than his investors.'),
 P(IG,img='ethan_instagram',who='Ethan',meta='64 posts · 1,950 followers',bio='Building in public 🌴<br>Day 214 of working from anywhere<br>My morning routine below 👇',crit=C('Aesthetic',9,'Humblebrag',10,'Effort',8,'Honesty',4,'Fun',6),joke='Working on the beach. Laptop at 3% battery.'),
 P(LIN,img='ethan_linkedin',who='Ethan, 28',bio='Founder &amp; CEO at Stealth | Serial Entrepreneur (2 exits, both from the company) | Hiring a rockstar ninja, equity only',foot='3,201 followers · Agree?',crit=C('Buzzwords',10,'Optimism',10,'Experience',5,'Honesty',6,'Fun',9.5),joke='Turtleneck on, arms crossed, revenue pending.',pos=20)],
 headline='Ethan is most himself on LinkedIn.',sub='Sadly, he means every word.',tag='Tag the Ethan pitching at every party. 👇',next='The 27-year-old gamer',follow='Follow for episode 6',
 cap='''One person. Four apps. Four completely different founders. 😅

Meet Ethan, 28, startup founder.
On X he's building the future of [redacted].
On Tinder he wants a co-founder of his heart.
On Instagram he works from a beach.
On LinkedIn he's hiring a rockstar ninja. Equity only.

We scored every version. Swipe to see which app gets the real Ethan 👉

💬 Your turn: comment the weirdest bio you've ever seen from a founder.
LinkedIn, X, Tinder, Instagram… we want them all.
The best ones end up in a future episode 👀

Tag the Ethan pitching at every party 👇

#instagrambio #bioideas #linkedinbio #startuplife #founder #relatable #socialmediahumor #coolbio360'''))
E.append(dict(ep=6,name='Kai',title='The 27-year-old<br>gamer',kicker='THE 27-YEAR-OLD GAMER',rot=-2,plat=[
 P(DIS,img='kai_discord',who='Kai',meta='🟢 Online for 14 hours',label='About me',bio='gg no re · 27 · my sleep schedule is a speedrun · don\'t @ me during ranked',crit=C('Honesty',10,'Relatability',10,'Effort',3,'Chaos',8.5,'Fun',9),joke='4am, RGB on, three servers muted. Peak Kai.'),
 P(LIN,img='kai_linkedin',who='Kai, 27',bio='Strategic Problem Solver | Team Leader (Guild Master, 200 members) | Expert in Real-Time Decision Making Under Pressure',foot='88 connections · Skills: patience, respawning',crit=C('Buzzwords',8.5,'Optimism',7,'Experience',6,'Honesty',7,'Fun',9),joke='Every single word is technically true.'),
 P(TW,img='kai_twitch',who='kai_plays',meta='LIVE · 7 viewers',bio='Streaming every night until my mom says stop 🎮 Drop a follow, I read every chat (all three of them)',crit=C('Energy',10,'Honesty',8,'Effort',9,'Reach',2,'Fun',8.5),joke='Screaming at a boss fight for an audience of seven.'),
 P(TIN,img='kai_tinder',who='Kai <span style="font-weight: 400">27</span>',bio='Yes I go outside (photo proof attached). Looking for player 2. Will let you win at Mario Kart. Once.',crit=C('Honesty',6,'Charm',7.5,'Effort',8,'Desperation',6.5,'Fun',8),joke='The one outdoor photo. He\'s still recovering.')],
 headline='Kai is most himself on Discord.',sub='At 4am. Online for 14 hours.',tag='Tag the Kai who only replies on Discord. 👇',next='The 23-year-old influencer',follow='Follow for episode 7',
 cap='''One person. Four apps. Four completely different players. 😅

Meet Kai, 27, gamer.
On Discord he's been online for 14 hours.
On LinkedIn he's a "Guild Master".
On Twitch he streams for 7 loyal viewers.
On Tinder he went outside (photo proof attached).

We scored every version. Swipe to see which app gets the real Kai 👉

💬 Your turn: comment the weirdest bio you've ever seen from a gamer.
Discord, Twitch, Tinder, LinkedIn… we want them all.
The best ones end up in a future episode 👀

Tag the Kai who only replies on Discord 👇

#instagrambio #bioideas #gamer #gaminghumor #tinderbio #relatable #socialmediahumor #coolbio360'''))
E.append(dict(ep=7,name='Chloe',title='The 23-year-old<br>aspiring influencer',tfs=60,kicker='THE 23-YEAR-OLD ASPIRING INFLUENCER',plat=[
 P(LIN,img='chloe_linkedin',who='Chloe, 23',bio='Content Creator | Digital Storyteller | Personal Brand Strategist | Open to collabs, gifted PR and actual salaries',foot='1,047 followers · Featured: my own TikTok',crit=C('Buzzwords',9,'Optimism',9.5,'Experience',3,'Honesty',5,'Fun',7),joke='The ring light is in her eyes. That\'s commitment.'),
 P(TT,img='chloe_tiktok',who='@chloe.daily',meta='2.1K followers · 46K likes',bio='day 98 of posting until I go viral 🎀<br>new video every day, no matter what',crit=C('Honesty',9,'Relatability',9,'Effort',10,'Chaos',7.5,'Fun',7.5),joke='Laundry pile in frame. Day 98. Still going.',pos=30),
 P(TIN,img='chloe_tinder',who='Chloe <span style="font-weight: 400">23</span>',bio='Will film our first date for content (with consent 🎀). Looking for someone who knows good lighting. Rooftops only.',crit=C('Honesty',8,'Charm',8,'Effort',7,'Desperation',5,'Fun',8.5),joke='Peace sign, cocktail, flash on. Textbook.'),
 P(IG,img='chloe_instagram',who='chloe.daily',meta='318 posts · 2,412 followers',bio='✨ lifestyle | matcha | soft life<br>📍 wherever the light is good<br>💌 PR &amp; collabs in DMs',crit=C('Aesthetic',10,'Mystery',6,'Effort',9.5,'Honesty',2.5,'Fun',5),joke='Looking away from the camera. Take 47.')],
 headline='Chloe is most herself on TikTok.',sub='Day 98. Laundry in frame.',tag='Tag the Chloe who films every brunch. 👇',next='You choose. Comment below.',follow='Follow for the next season',
 cap='''One person. Four apps. Four completely different creators. 😅

Meet Chloe, 23, aspiring influencer.
On LinkedIn she's a "Personal Brand Strategist".
On TikTok it's day 98 of posting until she goes viral.
On Tinder she'll film your first date.
On Instagram it's matcha and soft life. Take 47.

We scored every version. Swipe to see which app gets the real Chloe 👉

💬 Your turn: comment the weirdest bio you've ever seen from an influencer.
TikTok, Instagram, LinkedIn, Tinder… we want them all.
The best ones end up in a future episode 👀

Tag the Chloe who films every brunch 👇

#instagrambio #bioideas #influencer #tiktokbio #contentcreator #relatable #socialmediahumor #coolbio360'''))
json.dump(E,open('episodes.json','w'),ensure_ascii=False,indent=1)
