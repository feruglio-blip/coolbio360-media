from mk import build
build('petsit01','Sitter',
 feeds={'murphysmuttsdogwalking':(7.5,6.5),'baulcombeandbark':(7,9),'mackspackadventures':(8,7.5),'oly_paws':(7,7),'daphnespetadventures':(6.5,6)},
 deltas={'murphysmuttsdogwalking':[0,0.5,-1,0.5],'baulcombeandbark':[-0.5,0.5,1,-0.5],'mackspackadventures':[-0.5,0.5,0,0.5],'oly_paws':[-0.5,0.5,0,1],'daphnespetadventures':[1,0,-0.5,-0.5]},
 steal={'h':'Your pet sitter bio,<br>in four lines.','lines':[
   ('🐾 [what you do] in [your town]','THE OFFER'),
   ('[the pets you love] · [walks, visits, stays]','THE SERVICES'),
   ('🔒 [insured / first aid / years with pets]','THE TRUST'),
   ('👇 [DM to book / book online]','THE ACTION')],
  'ex_h':'your_pet_sitter_here','ex':['Dog walker &amp; pet sitter in Bristol 🐾','Dogs, cats and the odd tortoise · walks, visits, stays','🔒 Insured · canine first aid · 6 years with pets','👇 DM to book a meet and greet']},
 nxt='Baker Bios, vol. 27')
