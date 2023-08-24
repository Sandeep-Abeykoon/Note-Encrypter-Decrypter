# --------------------------------------Encryption Program------------------------------------------
#20210057-Sandeep
# Initializing the variables
char_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
          'x','y','0','1','2','3','4','5','6','7','8','9','z','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','`','~','!','@','#','$','%',
          '^','&','*','(',')','-','_','+','=','|',']','}','[','{',';',':','/','.',' ','>','<','\\','\n',
          '?','\'',',','\"','\t','é','â','€','“','Ã','©','¢','\b','Â','®','£','°','µ','·','¸','¼','½',
          '¾','Å','’','³','º','±','‘','¡','¿','¬','«','»','¦','Ÿ','²','‚','ž','\xa0','Ë','†','\x7f','‡',
          '¤','¥','§','ª','¨','¯','´','¶','¹','Æ','\xad','”','•','–','—','™','œ','„','š','›','ƒ','…',
          'ˆ','‰','Š','‹','Œ','Ž','Ä','“','”','Γ','Ç','ô','Ö','ÿ','ö','á','┬','ñ','╢','├','ç','╝','⌐',
          'ó','Ñ','å','┤','▓','╗','╣','┐','ú','╞','í','│','║','▒','æ','╜','╡','░','╖','₧','╦','┼','ä',
          '╕','╛','ü','à','ê','ë','è','ï','î','ì','É','ò','û','ù','Ü','╬','╧','∩','α','ß','π','╩','╔',
          'Ω','▌','╥','═','█','≡','∞','╪','╠','╤','╙','─','╟','╚','┘','┌','σ','Σ','τ','Θ','Φ','╨','≤']
           

enc_list=['c}2jj','UeMjG','i=x@B',';VCPa','txWL;',':;Kk,',']Y@HF','E2qGT','*93iH','Sm=T9','Ah4UZ','w,rV]',
          'ewNBg','zia8{','%eA#g','6n%E#','GSEe/','$N:&=',')Nr4/','e_[RJ','V&zHJ','De4zU','2hKr4',')Nyb]',
          '2_D8y',')cW+X','5zACP','R4+u5','W#T6-','6v6{t','Zw}Np','qDAk$','ZG:aH','dZ9wq','GEwnf','c6-xy',
          'i]Qf4','MZRd.','K8+J.','Djf[B','e.=##','dit8w','8[VBd','Yxr!d',']fNUh','&3rgA','L4TDb','F-mga',
          '6MqSt','M)agu','wY?H/','P$y;R','i@WJR',';jnf-','KvFn)','uGDCg','Dp#/t','2A/]f','z;zg-','tuZp&',
          '}Wf3c',']UNZ!','xrX3{','W5Ndv','Sp2M!','rCY4(','kpGd+','.jMD8','5Qj7H','{!X;y','#WHGu','C?wdy',
          '}}tEf','9Hn$j','p&Y7K','EF:jv','pUbL4','fFwqS','CAYGM','&2_{E','M{yA(',')Vavn','9=]HB','iijdJ',
          '*-n_W','}#bA=',']_[Mp','N{bj!','@+FnH','US:6S','2EqC[','8U{*c','hyv::','7TTg!','SP!=,','zA.Y2',
          '[Deh=','J(ix{','&tz$)','He/xt','MW6xF',';Qn8m','6Gt?M','yqBX+','}62n2','y_p@d','y$.}m',')iJxL',
          '_uan?','W=.{2','bp)nn','T5ALA','muUyY','cR=]r','Sh[cQ','R;%5e','mx5w!',':Yh]e','&,DH@','wLN8H',
          '&=fe}','/4pGG','bA(4R','M3&+-','?A-{4','*5wM&','r-7W6','u+bBd','=qzS;','P]{Tv','Q+]Vk','{)p9.',
          '@E_if','dkVJp','EEDdB','ax44(','5_Xzm','46ADv','BR(dw','#r)=!','&Y;54','JY%2-','tj[9J','.MVeS',
          '{(5{.','[9N:+','hK}x9','&-#nH','[3h{d','REvfm','J;C}}','H.$!m','YT58z','7NfC8','=Vki7','CALJ*',
          '3%hj:','6eXH&','.grA?','[S#JN','Z%?U7','XTVpf','./V@=','cWX_M','}Z]QF','U#,/t','gG-4q','yccrV',
          'b[7x$','7.9;?','(mgU6','&.D66',':*vhk','.Xr?/','VvpHS','d2K_K','!{&=@',']dLD&','?Q:{9','uMimS',
          'H/KnH','eL@X%','Cd3te','*Y]Xe','6)J?}','j7j]}','%d]bT','VX#H@','DbHk4','RQM:T','Sw4MD','!kqpa',
          '@RAJD','r?$dk','m_GaH','#n&-[','p}eE5','7FgWz','ZGcXw','z@ab+','&cMb:','k.8+/','E;K$e','W8Z{-',
          'HyJgZ','KvHvL','NYHc6','CJgMm','./SL$','&d*)S',')h[+z','-!Q&r','T5@zj','A:}!b','BCC6i','egrt?',
          'W$fBv','jWMiv','b-5k2','mJdqS',';#z&V','@S*gN','{9m?w','-6VYg','f,xi7','N,3cm','QT;L(','9H?!i',
          '@MUDC','CZ-?i','kpqcz','-vS*Z','[YcHX','5F4Lp','Wp/yf','X?qRT','8{a:@','{Q(:?','ex[@Z','Ty/]q',
          'fu8Ab','Wc{9B','gr*+@','m:,Tx','F3[*{','bkd69','dJap]','qD9+e','=j5vj','t;(e&','vfrvS','hGYDm']
         
         
       
# Checking the length of the two lists
print(len(char_list),len(enc_list))

append_list=[]
read_list=[]
encrypt_list=[]
i=0
count=0
read_file_ob=''
wri_file_ob=''
length=0


# Opening the file objects
read_file_ob=open("read.txt",encoding='cp437')
wri_file_ob=open("encrypted.txt","w")
length=len(read_file_ob.read())
read_file_ob.seek(0,0)

#Process
for i in range(length):
    read_list.append(read_file_ob.read(1))
read_file_ob.close()

for x in read_list:
    append_list.append(char_list.index(x))
print(append_list)

for count in range(len(append_list)):
   wri_file_ob.write(enc_list[append_list[count]])
wri_file_ob.close()










   

    


