from mk2 import build
d=dict(slug='pilates01',vol='36',tag='PILATES',accent='#F7A072',emoji='🧘‍♀️',word='Pilates',sub='Pilates teachers and studios under 1,500 followers',next='Next list tomorrow',
 steal={'h':'Your Pilates bio,<br>in four lines.','lines':[
  ('[your vibe in one line] 🌶️','THE HOOK'),
  ('[mat / reformer / tower] · [who you teach]','THE OFFER'),
  ('📍 [studio, city or online] · [certified]','THE TRUST'),
  ('👇 [book a class / free first session]','THE ACTION')],
  'ex_h':'your_pilates_here','ex':['Strong core, zero ego 🌶️','Reformer &amp; mat · beginners and mums-to-be','📍 Leeds studio + online · fully certified','👇 Book your first class free']})
build(d,[
 ('pilateswithbridge','9.3','Reformer and hot mat instructor','“ur fav reformer + hot mat instructor.” Six words, one chilli, all personality.',8.5,9),
 ('dariahorb.pilates','9.0','Pilates teacher, Munich','Certified, a neuro-training fan, home workouts for real life. Three lines, zero fluff.',8.5,9),
 ('sonapilates','8.7','Pilates studio, Bristol','“Expert-led Pilates for every body.” Then: come as you are. Warm and clear.',7.5,7.5),
 ('thereformerspace','8.3','Reformer and tower studio, UK','Boutique, small groups, 1:1. And a feed that looks like a design magazine.',8.5,9),
 ('alignwell_studio','8.0','Reformer studio, Bristol','Studio, method, address, “find out more.” The essentials, neatly stacked.',8,8.5)])
d['people'][0]['congrats']='CONGRATULATIONS, BRIDGE'
import json; json.dump(d,open('new/pilates01.json','w'),ensure_ascii=False,indent=1)
