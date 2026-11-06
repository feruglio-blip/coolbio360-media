# Liste test fasce follower (6/11/2026): attività dal 16/10, Cool Score = 80% bio + 20% feed
import json
def P(r,h,cat,v,bio,feed): 
    s=0.8*sum(bio)/4+0.2*sum(feed)/3; return dict(rank=r,h=h,score=f'{s:.1f}',cat=cat,v=v,bio=bio,feed=feed,congrats='')
L=[
dict(slug='florist02',vol='37',tag='FLORISTS',accent='#F2789F',emoji='💐',word='Florist',band='under 1,000',
 sub='Florists under 1,000 followers',
 steal={'h':'Your florist bio,<br>in four lines.','lines':[['[what you make, in your words] 🌷','THE HOOK'],['[weddings / gifts / everyday] · [your style]','THE OFFER'],['📍 [town] · [delivery area]','THE TRUST'],['💌 [DM to order / bookings open for 2027]','THE ACTION']],
  'ex_h':'your_florist_here','ex':['Wild, seasonal, never stiff 🌷','Weddings &amp; everyday bouquets','📍 Bath studio · local delivery','💌 Bookings open for 2027']},
 people=[P(1,'bettyandbloom','Floral design studio, Manchester','“Bookings open for 2026, 2027 &amp; 2028.” Three years of diary in one line. That is confidence.'.replace('&amp;','&'),[8.5,9.5,8.5,9.0],[10,9.5,10]),
  P(2,'floralsbyhoor','Florist, Dudley','Bloom Bar, baskets, one week notice, nationwide. Everything you need before you DM.',[7.5,9.5,9.5,9.0],[9,9,9.5]),
  P(3,'bloome.x','Gifts and florals, UK','“Thoughtfully made. Beautifully gifted.” Six words that sound like the bouquets look.',[9.5,9.0,9.0,8.0],[8,8,8]),
  P(4,'aprilflowers239','Wedding and event florist, Fort Myers','Premier, booking until 2028, inside a nursery. You already know where to find her.',[8.0,9.0,8.5,8.5],[8.5,8,10]),
  P(5,'house_of_flores_','Florist, New South Wales','“Romantic garden style floristry with a modern edge.” A whole style guide in one line.',[9.0,8.5,7.0,8.5],[8,7.5,9.5])]),
dict(slug='candle01',vol='38',tag='CANDLES',accent='#F4A259',emoji='🕯️',word='Candle',band='1,000 to 2,000',
 sub='Candle makers with 1,000 to 2,000 followers',
 steal={'h':'Your candle bio,<br>in four lines.','lines':[['[the feeling your candles give] 🕯️','THE HOOK'],['[soy / coconut] · [hand-poured where]','THE OFFER'],['🌱 [vegan · small batch · what makes you different]','THE TRUST'],['👇 [shop the new scent / find us at markets]','THE ACTION']],
  'ex_h':'your_candles_here','ex':['Light one, switch off the world 🕯️','Soy wax · hand-poured in Leeds','🌱 Vegan · small batch · refillable jars','👇 Shop the winter scents']},
 people=[P(1,'wildnaturecandles','Soy wax candles, Cotswolds','Nature-inspired, Cotswolds, vegan, a tree planted per order. Clear, warm and on brand.',[8.5,9.5,7.5,9.0],[9,9,10]),
  P(2,'lostfond','Soy candles, UK','“Hand-poured in my garden shed.” The most honest line on this list, and the cosiest.',[9.5,9.0,7.5,8.5],[8.5,8.5,10]),
  P(3,'esccandles','Artisan candles, UK','“Hit Escape & log out of reality.” Pun in the name, promise in the first line.',[9.5,8.5,7.5,8.5],[9.5,9.5,8]),
  P(4,'spe_candle','Scottish candles, Speyside','“Wild Luxury ~ Scent Rituals.” Speyside does the rest. Elegant, if a little long.',[8.5,8.0,7.0,8.5],[9,9.5,10]),
  P(5,'misneachremedies','Essential oil candles, Cotswolds','Mood boosting, non toxic, award winning workshops. A list that sells, one line at a time.',[8.0,8.5,7.5,8.5],[7.5,8,10])]),
dict(slug='nails02',vol='39',tag='NAIL TECHS',accent='#B98CF2',emoji='💅',word='Nail Tech',band='2,000 to 5,000',
 sub='Nail techs with 2,000 to 5,000 followers',
 steal={'h':'Your nail tech bio,<br>in four lines.','lines':[['[your specialty, in plain words] 💅','THE HOOK'],['[BIAB / gel / Russian mani] · [extras]','THE OFFER'],['📍 [town or studio] · [products you use]','THE TRUST'],['👇 [booking link / books open on the 1st]','THE ACTION']],
  'ex_h':'your_nails_here','ex':['Short nails, big personality 💅','BIAB · Russian manicure · nail art','📍 Leeds studio · HEMA free products','👇 Books open on the 1st']},
 people=[P(1,'geesbeautycheltenham','Beauty salon, Cheltenham','Nails, lashes, brows, HEMA free, educator. Everything a nervous first client wants to read.',[8.0,9.5,8.0,9.5],[9,9.5,10]),
  P(2,'bymillicent_','Manicurist, Shrewsbury','Russian manicure, toenail reconstruction, a discount code. Niche, specific and useful.',[8.0,9.0,8.5,9.5],[9,9.5,9]),
  P(3,'shonaelunedbeauty','Nails and beauty, Abertillery','Booked up and says so kindly, with the link right below. Honest and on brand.',[8.0,9.0,8.5,8.5],[9.5,9,10]),
  P(4,'homey.nailbeauty','Nail tech and press-ons, UK','Handmade press-ons, two languages, two flags. A bio that knows exactly who it talks to.',[7.5,8.5,8.0,8.0],[9,8.5,9]),
  P(5,'by_oliviamcdonald','Nail and lash educator','Co-owner, academy, “DM for appointments.” Strong offer, a bit of a list.',[7.0,8.5,8.5,8.0],[8,8,9.5])])]
for d in L:
    d['people'].sort(key=lambda p:-float(p['score']))
    for r,p in enumerate(d['people'],1): p['rank']=r
    json.dump(d,open(f"new/{d['slug']}.json",'w'),ensure_ascii=False,indent=1)
    print(d['slug'],[(p['rank'],p['h'],p['score']) for p in d['people']])
