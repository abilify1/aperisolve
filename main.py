 #-*-coding:utf-8-*-
qu = '\033[0;36m'
hi = '\033[0;32m'
tm = '\033[0;30m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
try:
 import requests, os, sys, inquirer, json
except ImportError:os.system('pip2 install requests inquirer')
import requests, os, sys, inquirer, json,time
def line(txt):
      print "\n%s•••••••••••••••••••••%s«%s[%s%s%s]%s»%s•••••••••••••••••••••%s"%(pu,qu,pu,ku,txt,pu,qu,pu,pu)
def line1(txt):
         print "         >>%s%s%s<<"%(ku,txt,pu)
def setting():
     cnfig = json.loads(open('.config.json','rb').read())
     dfg = cnfig["list"]
     hhb = ["View","Zsteg","Steghide","Outguess","ExifTool","Binwalk","Foremost","Strings","Use Password","Zsteg extract","Zsteg all"]
   #  if cnfig["use_password"] == True:
    #  dfg.append('Use Password')
 #    if cnfig["zsteg_ext"] == True:
  #    dfg.append('Zsteg extract')
#     if cnfig["zsteg_all"] == True:
#      dfg.append('Zsteg all')
     print "%s[%s!%s] %sPress SPACE to enable/disable settings | Press ENTER to save settings"%(pu,ku,pu,pu)
     op2 = inquirer.prompt([inquirer.Checkbox('op2',message="Settings",choices=hhb,default=dfg)])["op2"]
     bbum = op2
     if "Use Password" in op2:cnfig["use_password"] = True;bbum.remove('Use Password');wyu=raw_input('%s[%s?%s] Password : '%(pu,ku,pu));cnfig["password"]=wyu
     elif "Zsteg extract" in op2:cnfig["zsteg_ext"] = True;bbum.remove('Zsteg extract')
     elif "Zsteg all" in op2:cnfig["zsteg_all"]=True;bbum.remove('Zsteg all')
     else:
      cnfig["use_password"] = False
      cnfig["zsteg_ext"] = False
      cnfig["zsteg_all"]=False
     cnfig["list"] = bbum
     open('.config.json','wb').write(json.dumps(cnfig))
def simpan(url,name):
    namafile = 'result/'+name
    down = requests.get(url,stream=True)
    with open(namafile,'wb') as g:
     for chnk in down.iter_content(chunk_size=128):
      g.write(chnk)
     sys.stdout.write("%s[%s!%s] %sFile 7z/zip saved to %s%s                                "%(pu,ku,pu,pu,ku,namafile))
     g.close()
    if "Not Found" in open(namafile,'rb').read():
     os.remove(namafile)
     sys.stdout.write("\r%s[%s!%s] %sFile 7z/zip not found                         "%(pu,ku,pu,me))
     print ""
def tik(text):
  hm = "%"
  for eek in range(31):
   sys.stdout.write('\r%s[%s!%s] %s%s %s(%s%s%s)'%(pu,ku,pu,pu,text,pu,me,str(eek),pu))
   time.sleep(1)
   sys.stdout.flush()
  print ""
def start():
   ffli = inquirer.prompt([inquirer.Text('ffli',message="File Name",default=open('.cache1.json','rb').read())])["ffli"]
   open('.cache1.json','wb').write(ffli)
   ready1 = requests.post('https://aperisolve.fr/upload',files={'file':open(ffli,'rb')},data=json.loads(open('.config.json','rb').read())).text
   mhj = json.loads(open('.config.json','rb').read())["list"]
   idimg = json.loads(ready1)["File"]
   if idimg in open('.cache.json').read():
      pass
   else:
    hh = open('.cache.json','r').readlines()
    with open('.cache.json','w') as yy:
     hh.append(idimg+'\n')
     yy.writelines(hh)
    tik('Waiting for uploading')

   while True:
    try:
     os.mkdir('result/%s'%idimg)
    except:break
   urlori = "https://aperisolve.fr/static/uploads/%s/"%idimg
   if "Zsteg" in mhj:
    zsteg = requests.get(urlori+'zsteg.txt').text
    print "%s•••••••••••••••••••••%s«%s[%sZSTEG%s]%s»%s•••••••••••••••••••••\n%s%s"%(pu,qu,pu,ku,pu,qu,pu,pu,zsteg.encode('utf-8'))
    simpan(urlori+'zsteg.7z',idimg+'/zsteg.7z')
    open('result/%s/zsteg.txt'%idimg,'wb').write(zsteg.encode('utf-8'))
   if "Steghide" in mhj:
    line('STEGHIDE')
    steghide = requests.get(urlori+'steghide.txt').text
    print steghide
    simpan(urlori+'steghide.7z',idimg+'/steghide.7z')
    open('result/%s/steghide.txt'%idimg,'wb').write(steghide.encode('utf-8'))
   if "Outguess" in mhj:
    line('OUTGUESS')
    outguess = requests.get(urlori+'outguess.txt').text
    print outguess
    simpan(urlori+'outguess.7z',idimg+'/outguess.7z')
    open('result/%s/outguess.txt'%idimg,'wb').write(outguess.encode('utf-8'))
   if "ExifTool" in mhj:
    line('EXIFTOOL')
    exiftool = json.loads(requests.get(urlori+'exiftool.json').text)
    with open('result/%s/exiftool.txt'%idimg,'wb') as mek:
     line1('ExifTool')
     print "ExifToolVersion : %s"%exiftool[0]["ExifTool"]["ExifToolVersion"]
     line1('System')
     for k, v in exiftool[0]["System"].iteritems():
      print str(k)+' : '+str(v)
      mek.write(str(k)+' : '+str(v))
     line1('File')
     for x, y in exiftool[0]["File"].iteritems():
      print str(x)+' : '+str(y)
      mek.write(str(x)+' : '+str(y))
     line1('PNG')
     while True:
      try:
       for tt, tu in exiftool[0]["PNG"].iteritems():
        print str(tt)+' : '+str(tu)
        mek.write(str(tt)+' : '+str(tu))
      except:print "nothing:(";break
      else:pass
    line1('Composite')
    for uh, ih in exiftool[0]["Composite"].iteritems():
      print str(uh)+' : '+str(ih)
      mek.write(str(uh)+' : '+str(ih))
    print "%s[%s!%s] %sTxt File succes saved to %sresult/%s/exiftool.txt"%(pu,ku,pu,pu,ku,idimg)
    mek.close()
   if "Binwalk" in mhj:
    line('BINWALK')
    binwalk = requests.get(urlori+'binwalk.txt').text
    print binwalk
    simpan(urlori+'binwalk.7z',idimg+'/binwalk.7z')
   if "Foremost" in mhj:
    line('FOREMOST')
    simpan(urlori+'foremost.7z',idimg+'/foremost.7z')
   if "Strings" in mhj:
    line('STRINGS')
    strings = requests.get(urlori+'strings.txt').text
    print strings
   if "View" in mhj:
    line('VIEW')
    line1('Supperimposed')
    print "%s[%s!%s] %sDownloading... do not close console"%(pu,ku,pu,pu)
    rgb = ['image_rgb_1.png','image_rgb_2.png','image_rgb_3.png','image_rgb_4.png','image_rgb_5.png','image_rgb_6.png','image_rgb_7.png','image_rgb_8.png']
    for wow in rgb:
     with open('result/%s/%s'%(idimg,wow),'wb') as gg:
         gh = requests.get(urlori+'view/'+wow).content
         gg.write(gh)
         sys.stdout.write('\r%s[%s!%s] %sSuccess download %s%s'%(pu,ku,pu,pu,ku,wow))
         time.sleep(0.7)
    print ""
    print "%s[%s!%s] %sDownload complete..."%(pu,ku,pu,pu)
    line1('Red')
    print "%s[%s!%s] %sDownloading... do not close console"%(pu,ku,pu,pu)
    red = ['image_r_1.png','image_r_2.png','image_r_3.png','image_r_4.png','image_r_5.png','image_r_6.png','image_r_7.png','image_r_8.png']
    for wow1 in red:
     with open('result/%s/%s'%(idimg,wow), 'wb') as mm:
      mh = requests.get(urlori+'view/'+wow1).content
      mm.write(mh)
      sys.stdout.write('\r%s[%s!%s] %sSuccess download %s%s'%(pu,ku,pu,pu,ku,wow1))
      time.sleep(0.7)
    print ""
    print "%s[%s!%s] %sDownload complete..."%(pu,ku,pu,pu)
    line1('Green')
    print "%s[%s!%s] %sDownloading... do not close console"%(pu,ku,pu,pu)
    green = ['image_g_1.png','image_g_2.png','image_g_3.png','image_g_4.png','image_g_5.png','image_g_6.png','image_g_7.png','image_g_8.png']
    for wow2 in green:
     with open('result/%s/%s'%(idimg,wow2),'wb') as yu:
         yh = requests.get(urlori+'view/'+wow2).content
         yu.write(yh)
         sys.stdout.write('\r%s[%s!%s] %sSuccess download %s%s'%(pu,ku,pu,pu,ku,wow2))
         time.sleep(0.7)
    print ""
    print "%s[%s!%s] %sDownload complete..."%(pu,ku,pu,pu)
    line1('Blue')
    print "%s[%s!%s] %sDownloading... do not close console"%(pu,ku,pu,pu)
    blue = ['image_b_1.png','image_b_2.png','image_b_3.png','image_b_4.png','image_b_5.png','image_b_6.png','image_b_7.png','image_b_8.png']
    for wow3 in blue:
     with open('result/%s/%s'%(idimg,wow3),'wb') as zz:
         zh = requests.get(urlori+'view/'+wow).content
         zz.write(zh)
         sys.stdout.write('\r%s[%s!%s] %sSuccess download %s%s'%(pu,ku,pu,pu,ku,wow3))
         time.sleep(0.7)
    print ""
    print "%s[%s!%s] %sDownload complete..."%(pu,ku,pu,pu)



def banner():
    print """%s
╔═╗┌─┐┌─┐┬─┐┬╔═╗┌─┐┬ ┬  ┬┌─┐ %s| %sAuthor %sabilseno11%s 
╠═╣├─┘├┤ ├┬┘│╚═╗│ ││ └┐┌┘├┤  %s| %sGithub %sgithub.com/AbilSeno%s
╩ ╩┴  └─┘┴└─┴╚═╝└─┘┴─┘└┘ └─  %s| %sTools %saperisolve.fr%s"""%(ku,hi,qu,ku,ku,hi,qu,ku,ku,hi,qu,ku,ku)
if __name__ == "__main__":
   os.system('clear')
   banner()
   global input1
   input1 = inquirer.prompt([inquirer.List('input1',message='Choose a option',choices=['Start','Setting','Gallery'],)])["input1"] 
   if input1 == "Start":
     start()
   elif input1 == "Setting":
     setting()
