
import collections
import json

instr = """vpryah (310) -> iedlpkf, epeain
aqfemi (38)
bwtsue (18) -> crdoq, lhxdfj
eeyaxfn (72) -> idsab, jnhyc, vswgxoh, hivnzrk, afcsq, vpryah, dqiby
vddsv (64)
xnoux (41)
apajk (61)
fdgjgwt (13174) -> piofa, uxrros, ngiys
tgjmrpl (43)
jjxhgkx (1478) -> jncwn, tydjgm
nbrqwvs (201) -> zzkzfln, htdimcs
qcnoadr (70)
wwcngr (77)
deweh (1549) -> qaqof, kvyiqr, zfmqlj
ygeoklq (12)
bpszadt (35)
bdlzzvy (98)
fbaiatg (13)
pidgnp (95856) -> ehlwoxs, hbldvzk, ezwzp, tylelk, jkxutle, kkflx, oucqw
vijgqvl (40)
ofjjqdj (46)
vgsqrp (46)
idqgxkl (81)
nafzy (65)
nxspzd (82)
cnrwew (222) -> vnyaqgw, zooxx
qhdqak (2571) -> vmgxg, knmmys, zkwplas, bsqpcne, xgqdjhe
rxbrsd (28)
hubvoh (152)
mpwlly (12)
rotzn (10)
drswab (57)
udkvb (250) -> fkvhdj, flhhbd
coedb (62)
fpwoels (35)
huzzk (131) -> fqozst, naacbhr
etxfihy (98) -> tgjmrpl, hdiprgd, hospabk, fvmws
mbtin (67)
yaawixo (67)
kxcid (77)
sibko (27)
khshj (177)
otnrfom (37)
hzqpddb (16)
ngiys (963) -> ybqzq, vcrgmn, ysmqsps, bwrenq, opomx
yybtd (16)
myhgys (11) -> daesbhs, qrmipn
amhmm (64) -> pxkhwuu, gnbmz
soiza (34)
dqiby (202) -> fdklcbu, qcnoadr
jleqdi (69)
fdyuo (91)
gxmdnq (42)
wdnlqh (43)
lmmffej (337) -> twjvtbu, suvwi
qrrdb (94) -> zqvhd, vcgcmuh
gkzpb (207)
rfkdn (163) -> zpjju, bxwtlj, igzrzi
iyegmn (58)
johqe (47)
nmfhgq (141) -> dzbnx, cveuc, sfrwf
jknrln (13)
hivnzrk (206) -> coxuqy, ewuohku
xulpd (54) -> itzmwqp, egtem
quqixmj (203) -> jykfxee, vsqcws
wjkfdvb (10)
fusiiz (47)
awvqy (71)
auztp (27)
ghuyt (65)
xzfrad (23)
nvkhow (96)
htdimcs (93)
kwolrk (90)
dhsyxu (35)
chjdhl (40)
gndjq (70)
izxeuz (97)
dgqquh (92)
yenbb (51)
wogrc (27)
cijhcl (16)
ebaevkk (97)
mxikfk (23)
elxfl (320) -> ohneffn, jyvhtle, sgymtmx, mitvkt, kaxvdwl
aivprd (58)
ujnas (94)
ubdfq (12)
ozuqsau (8)
hlszj (23)
tpdch (17)
atgamme (26)
nwlacty (167) -> vhuwgi, zaiopar
kyizmdu (53)
xgufltj (96)
rqbjjuo (49)
pkipyhb (98)
mojsngw (92)
bncmd (95)
hkssn (463) -> gjpglfg, bqlmhj, cvseh
mgoew (180) -> gqmbul, geqrb, oidjn
fdvfx (58)
mkohhbb (82)
btami (41)
ohbhyq (20)
jnyvdz (98)
sbzee (24)
dyeds (47)
xmendwz (76)
dwybhqe (326) -> ftyilib, lhmhrpi
dydlyj (88)
cgtddkw (164) -> jcikl, jaxjy
jircuj (729) -> qyqthsz, ctqaxh, scbjq
xernf (34)
ljpeina (81)
dvvlx (16)
itzmwqp (76)
opbrn (78)
ekpvnh (61)
btbuwwi (105) -> btami, ffrrwb, niuvu, atzuayu
ceqayn (77)
gtgdmny (11)
unqmapv (58) -> ofjjqdj, vgsqrp, ayogkum, ymerus
phrrm (5)
botmw (78)
fbhxulf (40) -> flbumzk, csxdpl
tdbwpcj (98)
qdfzlv (73) -> blkcnq, idqgxkl
cfiurqp (12)
pejkmud (33)
doqxpij (154) -> xaidhn, mcmijwy
mmjpziu (38)
ryjrq (69)
dzienj (115) -> gybbvb, mbtin
iisuf (42)
mtfqemm (8)
gwpzvb (48) -> qjlrpjn, prtah
pkjykh (81)
hgqesr (672) -> satuz, zozajw, hzauzw
ayogkum (46)
cdqkuuw (216) -> lhjpci, mlkddpw
dvips (13)
klvhv (34)
kvypj (91)
rcytc (700) -> doqxpij, dwybhqe, yeuaeqp, bpvit, ljhqql
wadeqe (98)
dqwocyn (1215) -> aepss, jtxphqg, gveca
unbjm (40)
qhwtf (97)
afxazvx (49)
pyraep (46)
lwpwtbj (71)
kasozsw (143) -> sayhdkv, ghhhiwl, kreehw
xfjpbus (96)
llalv (35)
xpzadg (15) -> ydjrtcd, ebaevkk
igzrzi (182) -> chjdhl, buyou
skzxsyk (31)
hontwg (58) -> pgnbhl, qoksme, dzlgor, gmfsl, sdvag, nbrqwvs
smmdlo (416) -> cxgdzl, facddx, doehwd
drtfi (19)
uglla (19)
mjbdmlf (67)
ykhycl (496) -> xmkkpat, iroikgp, khshj, kxqhlbm, vfrna
twvkgl (74)
iuagzo (69)
qxvpdh (28) -> qptzj, hkcghm
poviv (76)
knhati (51)
uashrrc (50)
ouiwlb (98)
tzxvnri (12)
bnqutso (11)
fqozst (39)
xypex (18)
gerpefi (69)
wbqjf (24)
xaidhn (91)
lwpmgk (61)
wuluf (72)
ffrrwb (41)
ooobx (45)
fdhvp (137) -> ybjld, uksim, wbqjf, sbzee
pxkhwuu (89)
rrxrsx (77)
crxbcqe (1033) -> rmocf, xjiql, mocrsqu
msywua (32)
zqatt (72) -> pzggi, abdjb, wvisr, ibushn, fdkvm, dobqmg, gbqig
jfclt (107) -> pjssvle, tmsnmf, iisuf, njhppm
upndyov (83) -> pkcpn, qvknu
gbbnux (279) -> yotrh, bnsqqv
scbjq (89) -> ogorkv, rvglq, upnls
ydgusm (66)
sayhdkv (87)
nqzlzs (10)
coazy (129) -> wkmey, skzxsyk
vhcza (20)
pgtmio (19)
tprgqt (81)
euoqdcd (62)
zddlo (62)
dlapc (26)
qorsgjk (62)
hsyoiy (23)
pyplv (26)
gqmbul (8)
jwgvg (62)
lyrxhp (90)
uekiz (23) -> wwcngr, xqyrozn, ikclk, uents
ibyvotn (65)
ewtqg (51)
qwlze (52) -> malwro, gwyrxmf, blstaec, ehoqrji, bqppw, btbuwwi
gjpglfg (29) -> vumpiw, yfzbdl, nlgoig, fqppio, uykfql, gvujhex
ftohrkw (16)
hmtnj (28) -> qorsgjk, vneld
qggjzz (106) -> yqxvhbl, wsyqwf
pgilb (19)
hueuhx (54)
thats (64)
arveor (80)
yuymxvd (80) -> llbxkj, zmpyqv
cisaxsf (161) -> rptfwu, mqjpes
pkuqykh (68) -> bpyce, fusiiz, mdrto
otqdauw (32)
ylnua (76)
uyjtxt (87) -> gahwap, fqxrjg, mnxmtp
zfzpgfw (25) -> rwouyb, gjvfc, zbtswr
vzrfuvn (83)
bdzkzv (318) -> baimp, wfgyg
ceywcm (68)
ypeap (60)
mqjqez (70)
iueqa (53)
hqhkw (70)
bpyce (47)
wseii (36)
vxxhu (32)
nqomdre (40)
pxnvwaj (11) -> rcytc, hontwg, vjhwn, deweh
qvknu (90)
qcsfpn (85)
eprljo (98) -> hdjlp, qqfgo, xbhww
cwdfqo (6) -> ctqym, nxxfgn, uoenrx, owdcg
fgzwvuy (67)
ajdtudl (263)
dngqchs (1012) -> mxpxbm, quqixmj, qneezf
zdiygz (207) -> tujrz, vpmuei
jkxutle (5247) -> scjrx, srcfgoo, rfkdn
jeywnj (13043) -> kkjro, jxysad, crxbcqe, pgdgh, qozxrgg
holcno (13)
qtjpthc (45) -> hfpspc, iniuzfq
malwro (93) -> saxar, dydlyj
bujphvu (154) -> dpcuy, rimobjs, mevce
hgogzfl (17)
xgqdjhe (327) -> gbbnux, zuanzd, nbykdlk
rtzodmx (76)
mdrto (47)
xuwmc (256) -> yekxli, xnfybs
ptmqsnr (83)
mplgqv (77)
uhoryyb (4957) -> slohro, kkjnouk, lmfchi
yrbwhz (19)
elcnwtn (110) -> mmqtzmj, rnfoji, xayhv
wtkxd (73)
ftyilib (5)
bztcy (224) -> mysjwy, wbqkf
unnvung (64)
gufqi (12)
zntrkc (71)
zxdhxrb (69)
tzvtu (78)
ohneffn (65) -> ffcefem, qjxyfa, bojjcl, bhqkvi
rtcicn (211) -> hqcwl, pgilb, dniub
hmwfqwz (225) -> zqczqd, xdrjmkv
obilnz (93)
satuz (271)
fdkvm (189) -> hueuhx, ujyxvl
mxtcei (11914) -> eeyaxfn, dhrbaor, mzgayzs, tfphsaq
cqupm (71) -> vsvne, wwrkqb, jtgcmc, yyria, hkntpfd, cbefqk
gymuodz (63) -> rimua, whfeq
zfmqlj (121) -> kdbfv, abccyo
muecxv (98)
cldldxp (14) -> uuztubk, hrqsnls, eeergq, vyqlzi
acpwe (135) -> yrbpdq, iwtqde
hcrxqbw (80)
xmkkpat (43) -> ivwybv, mjbdmlf
okqwb (85)
pwmazwj (59)
qwtheza (22)
euxrv (110) -> sfuegcs, kqfesp, azjunml
qvowcc (30)
zelwp (61) -> nxspzd, lrhkoc, ybfqzep, sqwovza
pqqfpa (355) -> dezgi, dtakrnu
uykfql (405) -> efijtd, phdetz
jyvhtle (25) -> jasol, esivz, wprhap, fqyog
czyok (75) -> pkipyhb, sbsfo, izkej
vpmuei (62)
ydjrtcd (97)
bgjwy (82)
xupkjdt (31) -> mzjhsq, cimubay
coxuqy (68)
wupsg (81)
prtah (59)
pewvv (39) -> rtcicn, vysjpf, lxxbgm, bztcy, fgbsxh
kemme (38)
rpanfr (42)
mmqtzmj (76)
auocefh (10)
mweox (60) -> ddrsd, nxwtdg, jlvakq, gmaxala, rtwur, qqkwjoy, lmmffej
kazlt (312) -> cgetpc, jknrln
rqqxoou (82) -> lbeqp, jfsnic
jrygk (124) -> zkkvh, xjvwjq
rvglq (18)
ajyzem (70)
qhgvoj (129) -> uwpuqd, pyplv
scgpm (19)
apbjfv (43)
waxvx (96)
dpqrxbr (55) -> nafzy, bgscxgk
jtzrvt (55)
qnzdaj (262) -> ablgyqv, xhang
jfvoui (45)
vfmiaz (38)
xnqznos (5)
qhfoy (63)
fsqws (95) -> yyrwb, vnuwoq, vlllp, reuaanp
aunrdo (61)
pbcpt (7)
xwunxz (1100) -> klhzgvj, walzh, snquxtz
lshkygc (19)
bkqndr (44)
dhrbaor (1511) -> fpkuumw, fytlv, knendm, xxsobt, wlqfnkr
opomx (191) -> pycim, khnemp
zlvgiq (76)
oioqg (63)
dkeosz (13)
irgymg (99)
iyqcty (19)
ozugcs (60)
ewoebye (55)
dxggcx (34) -> nuwpvd, ylnua, vljooo, ykzjkp
qyvxs (83) -> qtcsae, gjdrco, zffoytm
ogorkv (18)
zuanzd (73) -> tutmv, ubkhce, ebzton
qozxrgg (1351) -> yuymxvd, zjuupn, uyjtxt
lbeqp (62)
bqlmhj (2246) -> cvahi, jgbvdp, wehfli
ptyuh (70)
jlhsd (41) -> ygnlbv, wochkc, nzazpe
ayfafvc (33)
ldmgzql (17) -> qsods, ewoebye, yesozb, bfqotji
rdytzgp (127374) -> uhoryyb, vfwwc, hkssn
nxxfgn (59)
iniuzfq (81)
vysjpf (228) -> ohbhyq, bhzeep
scjrx (448) -> ejoee, uyvuqp, yaera
tzobgt (88)
ljhqql (44) -> tbzqsrb, wtkxd, amhug, axgpt
vvpacb (126) -> ijmaxm, cjoeyrm
zqvhd (88)
zagaz (88)
emhblpr (85)
lrosl (82)
orcrc (74)
vyfhcqp (109) -> jwgvg, pyfeav
njhppm (42)
eowjgp (188) -> ueqkrm, nhgchm
wlodh (39)
vsqcws (25)
jxcxv (60)
hybvw (92)
qdgsn (47)
jasol (41)
zgrcahy (64)
mhassg (80)
eeergq (53) -> oeehfxg, emhblpr
ojozup (29)
gmeqmy (66) -> mbslas, vimplcz
zzekx (81)
xjvwjq (14)
heezga (300) -> jtfdy, scgpm
pjhoue (56)
djejdy (98) -> fdvfx, ykoazai
fkzxmb (55)
ezwzp (7179) -> jlhsd, oedan, emuek
tlwqwlk (23)
fqyog (41)
elvzp (33)
ydusqh (80) -> qucxsqh, lrfttlb, vzrfuvn, ptmqsnr
dweli (58)
qbnldp (85) -> cguzndh, oldoxo
xbhww (55)
smjtypd (35)
vcgcmuh (88)
iedlpkf (16)
zttytvi (93) -> qkjed, jnxbxzk
bszaj (104) -> txhbij, kwolrk
qwagq (67)
gxzxapn (12)
fqppio (139) -> fllao, orcrc, uhmmouc, twvkgl
opnpx (94)
esivz (41)
iqbtc (94)
wznad (369)
nujmyt (309) -> vbzyp, qwagq
vuzkop (57)
dxzahps (8)
idsab (142) -> befsr, mhlgi, uashrrc, fkmyndg
vtjrflg (73)
wfgyg (69)
ghhhiwl (87)
phpjy (44)
ekffumh (295) -> wznad, metsfo, afycii, czyok
jhltpk (61)
kaxvdwl (125) -> hzqpddb, aqeqvr, esegn, hdyrxg
uxgux (53)
zhnug (77)
cjoeyrm (72)
sdvag (387)
efbvz (54)
rksqqfr (90)
xplsuaq (98)
joryloo (24)
mxpxa (128) -> vtjrflg, guccv
tjcujd (193) -> cmfit, tcvpst
wkmey (31)
hgkjgm (4609) -> xcjxzq, ekffumh, juscckl, dngqchs
vneld (62)
lmfchi (67) -> qnzdaj, efqrg, murzaw
umajdu (17)
ierjhuk (15)
bvviqc (60)
qcizo (70)
cwaymbr (98)
iemeek (37)
lhxdfj (92)
nlgoig (240) -> xyfsr, ghuyt, ibyvotn
xxviu (12)
doehwd (169) -> ahcba, pbqdzda, xijkpj
nzazpe (88)
wehfli (105) -> asuodq, fbaiatg
athdvrh (3021) -> ajika, gxmdnq
hwluwdo (5)
yvttt (201) -> fdgccyg, joryloo
dyxzd (216) -> gubya, pnxmfdc
ehoqrji (79) -> kqvsah, yanwn
iwdzu (98)
owdcg (59)
vgaxwnn (78)
wlqfnkr (47) -> wseii, axhfcb, iomjmn, rczoepp
jxysad (99) -> jtydj, udkvb, plpctjz, ydusqh
jaedvjj (76)
iemgv (23)
skjez (147) -> aivprd, cbdyc
bwrenq (295) -> lyaqynn, hlcnf
hoarkjh (12)
tyvhz (222) -> wjkfdvb, powfmo
yiyjz (71) -> ljpeina, zzekx
fiwnjv (45)
dzwnlq (54)
algav (26)
nhgchm (47)
ejoee (115) -> algav, atgamme
jncwn (94)
gypuu (21)
xeiur (185)
zqczqd (82)
zordz (166) -> zhubam, hoarkjh
xtocem (23) -> ajyzem, hqhkw, jcshcvr, zxbnkvs
hhndlt (17641) -> sfxvp, ypzqp, pewvv
rrtpjw (7238) -> ptfyi, hgqesr, jmdlczf
aduuei (65)
dzrywb (84)
fpnjjy (91) -> dgqquh, ftatt
wprhap (41)
cvahi (39) -> auorp, jypccpq
gxhjjv (62)
zbrhqwq (171) -> kckevg, pbcpt
rimua (86)
fxqaw (63) -> avfsez, tprgqt
lyorl (80)
csmjw (142) -> hwluwdo, phrrm
crqesym (75)
gkskqqb (13)
cnuygks (10)
owxbfr (80)
gubya (56)
nnjrm (69) -> nesoknh, mkohhbb
gjdrco (85)
gtditk (58)
vlfxdli (66)
qwtvro (870) -> cfiurqp, ubdfq, xxviu
isoayc (6)
coicjc (185)
yuktpa (74)
txnuvci (44)
jbomczw (82)
jykfxee (25)
yyria (21) -> qztfbzn, xfmneu
xgibks (66) -> qvuhbo, abspab, ehegh, bvelsl
liklroi (108) -> xowek, qdgsn
kdbfv (78)
flhhbd (81)
halwu (66)
enorooc (44)
jfnknli (2345) -> hubvoh, csmjw, kzpyvis, hmyuwix, fbhxulf
yeuaeqp (162) -> vojcrx, jnshvhq
plzrspg (188) -> pdprpyn, itacy
jcshcvr (70)
uckyywt (96)
zpyoxs (52)
gvujhex (419) -> jbmxm, ozuqsau
zxbnkvs (70)
ydcibyi (1431) -> sakmn, yuktpa, ielyzgp
ffcefem (31)
mxpxbm (77) -> mvldvib, phpjy, mtqdya, enorooc
yzssszb (80)
srltg (96)
txznlay (55)
jwmjagj (30)
ejzoa (468) -> pqqfpa, fsqws, kqhusg
iwtqde (57)
tdxsqf (391) -> ejrychc, wqpfc
hrqsnls (133) -> ooobx, jfvoui
ewgvg (14873) -> sohohlc, fxhlrok, ykhycl, xabull, gdvqsyp
flgjahm (5240) -> bwhovd, zqatt, hcqsg
odtetse (25)
floca (98)
jfsnic (62)
hdiprgd (43)
fwfbd (81) -> djxvowe, mssypcn
whfeq (86)
lrfttlb (83)
aygltsd (44)
ztoitoz (59)
zooxx (30)
cumlar (39)
gzarnps (75) -> mojsngw, hybvw, ssuho, phmoj
lpgtx (63)
psdhpk (110) -> ceqayn, kimsadh
jfvmu (44)
hfpspc (81)
nghcpr (88)
idfuz (87) -> lwpmgk, scfrwrg
qqnroz (666) -> uvexl, ldmgzql, vtphqb, tjcujd
tutmv (94)
gmaxala (403) -> yybtd, cijhcl
kimsadh (77)
tbzqsrb (73)
ijmaxm (72)
biokfm (155) -> nvflr, sabolzl
lnllv (255) -> tpdch, nyeur
ulpfyrr (93)
twjvtbu (49)
qkdiej (25)
deyxep (58)
jbolstg (1053) -> aizud, hxowycm, fzcerr
jvxecw (59)
rxwxqe (53)
geqrb (8)
fytlv (35) -> pshil, bppdgwm
lbgqy (20)
gmtsea (8)
nbvlp (47)
vkdpaip (50) -> xfjpbus, ilkhnhw
btsvvyg (21)
shjlwli (264)
uzxjt (8)
xichd (209)
vhuwgi (20)
plmaxee (62)
texooeb (55)
qneezf (143) -> bsnxzz, yntilqc
dzlgor (43) -> jnmgovh, lzqtep, umuur, nuajwg
ubkhce (94)
cvxkylq (99)
ctqaxh (61) -> tslfayy, xquzvw
yfzbdl (75) -> kmyvyx, lyrxhp, tuyon, rksqqfr
rdrrye (338)
jrgiha (7)
wpugb (69) -> xhubgcl, psdhpk, htgvzw, shjlwli, xtxppp, nusvn
odmmo (456)
hgblqo (31)
jcikl (59)
khkaq (16)
mcmijwy (91)
sgymtmx (85) -> uxbyymt, tnngtb
fqxrjg (15)
rhfznek (52) -> vckzclh, kurnhks, ftthnl, fseduzt, gxumijt
txhbij (90)
yaann (187) -> drtfi, golkvpd
dfolgy (80)
qoukeij (82) -> szdthny, bpszadt
rmocf (100) -> fkbivys, ryjrq
rpxni (39)
xmvthbd (40)
soddek (333) -> wragpj, qcldyng
gwyrxmf (93) -> ntugl, bkqndr, nhnwkzo, txnuvci
bzwiavk (122) -> vszfxh, unbjm, hkxefzm, vijgqvl
okrnkqa (70)
pasveb (20)
qxivh (85)
aakrpyc (14)
qfellsp (80)
yowbd (346) -> ooazmvu, jtzrvt
ielyzgp (74)
ihslyyb (51)
faubz (59)
itacy (93)
fwevqj (33)
zzsbd (78)
edygy (258) -> yzfnlfl, hwdkwn
sohswca (66)
jngifv (614) -> rdthc, ajdtudl, skjez, eprljo
ivfffiz (96) -> iqbtc, opnpx
hcbdbh (400) -> cibrtjo, gkxdmxg
rulkpe (27) -> faubz, ftbsur, luixm, jvxecw
fpkuumw (31) -> arveor, hsykei
xabull (769) -> egkqlyz, obdtlhg, mgoew
cvcvyeu (100) -> rawfw, ceywcm
wjqdusq (186) -> odtetse, swastze
khnemp (95)
rudbmkz (30)
llbxkj (26)
tbfkvty (97) -> aymgd, glmcscm, coedb
kufceqa (95)
exaqlbc (186) -> tejonrz, hlszj
hxxexy (82)
cveuc (57)
pnxmfdc (56)
jtwrh (43)
pfuyke (217) -> hsyoiy, ovfby
wdgfw (49)
obdtlhg (66) -> pbmni, gerpefi
abdjb (285) -> nzhfbo, begrb
onwhg (40)
wfixt (70)
ngtpz (98)
gxumijt (297) -> yrbwhz, yxzdn, otslex
murzaw (64) -> cwaymbr, iwdzu, ouiwlb
jtxphqg (108) -> aakrpyc, vjyhqx
wjkqpqr (235) -> auocefh, cnuygks, nkxdfu, rotzn
vsvne (183) -> qkllvda, uzxjt
jqhify (94)
ntadc (61)
niuvu (41)
bbsvfl (6)
powvrta (32)
nvflr (64)
kebfmsz (269) -> fhryrfj, vxxhu, wycfrkz, wrurg
ueqkrm (47)
elyuo (55)
kzpyvis (24) -> akumg, dfghz
fozgkmk (28)
skdbvqr (4471) -> smmdlo, cqupm, buyazh, elxfl
pycim (95)
spgyst (88)
vojcrx (87)
xorbfm (20) -> pwmazwj, ztoitoz, udiykt
wsyiyen (504) -> cisaxsf, rejss, zbrhqwq, xeiur, fyfjc, eaxqpmn
ivwybv (67)
zsjvdo (128) -> omnyr, hrhfd
uvfou (368) -> ygeoklq, tzxvnri, gufqi
objgx (80)
zpcqx (226) -> izxeuz, qhwtf
emuek (149) -> tzvtu, zzsbd
dytadg (35)
crdoq (92)
lljifba (68) -> jeywnj, fdgjgwt, ewgvg, mxtcei, wetrsmz, sgvaf, hhndlt
hcizj (91)
zzkzfln (93)
hmjzw (117) -> aujgtj, lshkygc
blkcnq (81)
udiykt (59)
nhnwkzo (44)
tiunb (46)
ccbgy (64)
khjexez (59)
tydjgm (94)
mssypcn (56)
swpjozm (66)
yryyz (249)
vdham (232)
scfrwrg (61)
xyfsr (65)
golkvpd (19)
qovcwth (59)
dzngp (183) -> onwhg, xmvthbd
vqbfan (51)
pkdeoh (16)
foozzq (114) -> klsxgx, kcorlw
ehegh (54)
kqhusg (155) -> dfolgy, yzssszb, qfellsp
jxzfb (88)
airlri (97) -> pidgnp, lljifba, gmewl, tbedct, ryvidhy, rdytzgp
kreehw (87)
zkkjh (93)
vqlyyx (43)
mkbjgur (34)
faqsp (40)
fiqnz (32)
esyzn (66)
swastze (25)
wbiys (58)
xiyhl (49) -> ktvry, ezoar
aonpvtr (82)
pgibhk (75)
axgpt (73)
kxqhlbm (31) -> sulyr, qeksx
apgqnys (82)
osipmuv (366) -> qkaaq, ffrgif, qxvpdh
lzqtep (86)
jrjkj (69)
omnyr (37)
jmdlczf (22) -> idfuz, xichd, pkuqykh, xpzadg, kioxu, huzzk, vgrbrzc
vvivo (60)
uents (77)
utprdt (33) -> ihslyyb, knhati
lcqed (45)
vnyaqgw (30)
szdthny (35)
rwqopie (35)
vgrbrzc (11) -> swpjozm, ibdon, sohswca
spjim (73)
bipyp (78)
mvxqfe (85)
vlszzu (333) -> nafvoj, foozzq, jgwajk, ppedet, hqpkdyb
jdrkeh (5)
ftbsur (59)
uldlh (30)
dzbnx (57)
vswgxoh (63) -> obilnz, zkkjh, ulpfyrr
xbowtoi (53) -> tdbwpcj, muecxv
mysjwy (22)
tetyj (135) -> xckaw, tadprtr
pbqdzda (38)
gahwap (15)
vjyhqx (14)
aywrlw (132) -> xxvfb, bmxoqy
zgzxr (235) -> ewvlay, slclu
jgwajk (104) -> fdyuo, keoqd
powfmo (10)
auorp (46)
jtydj (372) -> rpsmo, lbgqy
iomjmn (36)
slclu (34)
isvfa (95)
mhcyj (61) -> gxhjjv, ipppjn
rpsmo (20)
flbumzk (56)
xtxppp (72) -> miidkpe, srltg
vpsls (6)
hlansqa (53)
znbvji (44)
kieild (43)
klsxgx (86)
asuodq (13)
tuuzrr (98)
xckaw (50)
efqrg (202) -> vgaxwnn, opbrn
ibagnjs (59)
vyevfn (120) -> jtwrh, kieild, gmevoe
kvyiqr (95) -> kvypj, hcizj
qghotl (82)
pzywvr (92) -> txswi, jljgd, hxxexy, apgqnys
akmsaq (97)
mhseysh (49)
uarsqn (53)
ryvidhy (123921) -> pxnvwaj, skdbvqr, qhdqak
cqdggj (216) -> efkyht, gtgdmny, ohbzmqz
ykoazai (58)
sydiov (1417) -> xvhpqmh, exaex, utprdt
algetkl (73)
hbldvzk (2628) -> sydiov, ropjtoe, rhfznek
pzggi (189) -> efbvz, dzwnlq
rnfoji (76)
ytfnug (39)
jpxgvjl (82)
yotrh (38)
xpqnuh (31)
ewuohku (68)
vlllp (75)
erpdg (544) -> rdnozh, plzrspg, tirehn
ablgyqv (48)
yqxvhbl (42)
hgrjt (98)
joees (23)
eqsqenp (26)
mnxmtp (15)
wetrsmz (16444) -> wpfywy, litnjrv, rpmtne
bkicgcc (33)
dwvbnp (80)
qptzj (76)
ibvyfys (220) -> rpzit, bepnzsh, khjexez
bwhovd (457) -> yhgutqw, amhmm, cwdfqo, vlaowv, vkdpaip, tyvhz, unqmapv
fyfjc (21) -> qghotl, jbomczw
zaiopar (20)
rimobjs (88)
ipfmr (121) -> mkvblbi, btrdhk
mbslas (81)
zkwplas (63) -> tdxsqf, gzarnps, nujmyt
hoilkqz (84)
jljgd (82)
wfwma (85)
rfeqsq (77)
ptfyi (789) -> exaqlbc, vdham, vxjvov
jdtwus (115) -> cumlar, rpxni
ddrsd (319) -> aibabp, dweli
buyou (40)
plrma (94)
cmfit (22)
nbjrv (39)
aizud (118) -> eirze, xnoux
jgbvdp (91) -> pasveb, vhcza
vckzclh (240) -> vuzkop, gpgmx
xdzya (8219) -> malnjq, jircuj, zxdfpy
zfaxas (30)
keoqd (91)
xnqeu (30)
wycfrkz (32)
oidjn (8)
ihmqbiu (1005) -> hcbdbh, abicjs, rpiuf, zpcqx, pzywvr
rpiuf (332) -> znbvji, rjjeggt
ygykyu (85)
abicjs (375) -> ierjhuk, psmvz, nfkbhas
ehclf (40)
okmwjoa (92)
uxbyymt (52)
xqyrozn (77)
eaxqpmn (9) -> zagaz, tzobgt
undug (38)
uxrros (89) -> kebfmsz, sqnfn, mlztke, ibvyfys, facjth, soddek, kxsefnd
rlyxbi (303) -> qrrdb, vvpacb, klcuumi, etxfihy, tptxpuq
vmgxg (652) -> coicjc, dpqrxbr, mhcyj, pzmmc
xoabt (58)
qztfbzn (89)
jbmxm (8)
noqmsh (81)
pgujeq (325) -> fiqnz, msywua
gmewl (70663) -> sxpee, flgjahm, hrbukg, rrtpjw, hgkjgm, twxwam, xdzya
pnszexz (43) -> ycxyxg, ycnnc
aledrs (33)
rwouyb (94)
uuztubk (139) -> rxbrsd, hwekwoq, ffzjjj
uwojoup (80)
svlvlj (254) -> pqsfee, fguhavr
ykzjkp (76)
vfrna (72) -> dhsyxu, dytadg, gjihp
vimplcz (81)
cwppzzd (58)
bstqyq (35)
mtqdya (44)
enmoyyj (10)
lfqtv (510) -> lnllv, gelep, lwujegj, uowiif
aujgtj (19)
hdyrxg (16)
ezoar (72)
zkkvh (14)
ylmwjuo (155)
mdanw (181)
klhzgvj (77) -> qmsxr, wuluf
rpmtne (88) -> heezga, xuwmc, rdrrye, qyvxs, sppxgv
zozajw (139) -> esyzn, vlfxdli
drfzng (58) -> hmwfqwz, zelwp, pgujeq, gzqutgv
hzauzw (75) -> hgrjt, tuuzrr
aepss (136)
zkaqnra (1790) -> upndyov, mcnsxuh, rulkpe, pfuyke, dzngp
egtem (76)
reuaanp (75)
apexe (85) -> pkjykh, wupsg, kdrke
agmao (53)
ctdsj (58)
izkej (98)
wfpxk (30)
cmqni (56)
qoksme (241) -> algetkl, xhqrf
otslex (19)
vumpiw (269) -> uwoyjsd, xdwrl
zimidd (21) -> hcrxqbw, uwojoup
eegwdp (82)
pjssvle (42)
zbtswr (94)
dzugjhb (60) -> orxgo, irgymg, cvxkylq, svfgh
befsr (50)
lrhkoc (82)
cbaah (5)
cimubay (62)
vnuwoq (75)
vbzyp (67)
exaex (135)
nmvki (40)
xdwrl (83)
gmfsl (306) -> yktmvtf, auztp, vhlizib
wsyqwf (42)
phdetz (15)
krquje (51)
vyqlzi (111) -> wnqny, hwhhyhh
qmsxr (72)
ojzpzsa (10)
qvuhbo (54)
esegn (16)
bdqnomo (80)
tgexl (76)
nuvrtnk (69)
zarww (162) -> vrqdv, ojozup
qqmpq (2091) -> dxggcx, kazlt, elcnwtn
pgdgh (1072) -> uzoroj, yaann, pnszexz
walzh (127) -> nbvlp, suyawzr
kkjro (582) -> vyfhcqp, yiyjz, nnjrm, oojlo, fdhvp
sxpee (31) -> sppgjfx, qwlze, erpdg, xngnhi, jngifv, jjxhgkx, lfqtv
jnshvhq (87)
ppavww (82)
vljooo (76)
zdaorg (42)
hlcnf (43)
mzgayzs (814) -> hpsljy, rgpazuy, wjqdusq, cvcvyeu, qfzyvjr, euxrv, xfkpfqd
dfntl (44)
efijtd (15)
sqcet (53)
malnjq (550) -> xqrnd, jrygk, qoukeij, hmtnj
ktvry (72)
fkvhdj (81)
qtcsae (85)
uwpuqd (26)
oeehfxg (85)
nfchpk (47) -> amooqlb, rxwxqe, uarsqn
hykmnhl (82)
tadprtr (50)
kqfesp (42)
piofa (2046) -> mxpxa, jbkek, cqupq
fseduzt (174) -> cbacfi, ypeap, vvivo
moeujf (181) -> bkfbj, apajk
vlysce (28)
xowek (47)
cqfyjm (68)
nzhfbo (6)
ovfby (23)
nkxdfu (10)
ooazmvu (55)
qrmipn (77)
wragpj (32)
bgasdfq (408) -> zxphdt, jdrkeh
srcfgoo (9) -> tetyj, qdfzlv, gymuodz, qbnldp
hztzf (152) -> spgyst, jxzfb
ebzton (94)
imdqhns (35)
tejonrz (23)
yvpzbgp (64)
luviddq (61)
akumg (64)
ixwoprg (102) -> zpyoxs, wwkdvm
uowiif (106) -> luviddq, jhltpk, dtsdw
zznnz (18)
dnmsps (61) -> plrma, jqhify
wfkxhlf (82)
yyrwb (75)
kdwict (157) -> umajdu, hgogzfl
gpgmx (57)
mzjhsq (62)
cxgdzl (27) -> glumdc, unnvung, ccbgy, zgrcahy
knendm (39) -> jaedvjj, poviv
xymtys (154) -> ayfafvc, ywrze
xrmslfs (214)
ycnnc (91)
plpctjz (296) -> cwppzzd, taaoji
qazqwkj (30)
swqgxh (76)
phmoj (92)
knmmys (620) -> pyhohkx, xiyhl, jdtwus, fwfbd
vcrgmn (227) -> zhnug, rfeqsq
cibrtjo (10)
kkjnouk (9) -> tbfkvty, vaqhekv, zbxopzp, biokfm
bpmus (87)
yntilqc (55)
ejrychc (26)
nusvn (104) -> kqokslj, owxbfr
begrb (6)
axhfcb (36)
lgmjeng (35)
kqfob (25)
qqfgo (55)
fsose (121) -> tmpysyn, hsjbzgd
hospabk (43)
cvxcr (23)
nefpbc (64)
dpcuy (88)
zsratan (39)
gybbvb (67)
tbedct (142596) -> ydcibyi, ejzoa, lcbkylu, wpugb, rlyxbi, jbolstg
wpxhphx (146) -> otnrfom, iemeek
xjiql (84) -> mplgqv, rrxrsx
kurnhks (54) -> zlsrhdz, pgibhk, zsancei, crqesym
fknai (16)
abccyo (78)
jaxjy (59)
zxdfpy (59) -> ikeiwjo, qwfosq, mmotdue, hjkrxly, zttytvi, swjcx, kvheuf
cgetpc (13)
wwrkqb (185) -> ruhqq, jrgiha
sfrwf (57)
qjxyfa (31)
vhlizib (27)
hwekwoq (28)
mocrsqu (109) -> vqlyyx, wdnlqh, apbjfv
mevce (88)
yldsmt (57)
wwkdvm (52)
reqlm (51)
pdprpyn (93)
irgumpr (71) -> xgibks, eowjgp, bzwiavk, cgtddkw, tinitt, cnrwew
jjdfk (53)
lmtebyt (85)
ibdon (66)
jjvbyf (62)
ncffht (97)
hpsljy (156) -> cukfipr, nqomdre
wqpfc (26)
glmcscm (62)
mitvkt (137) -> dlapc, eqsqenp
kmemzft (51)
gqwfi (51)
lhmhrpi (5)
tirehn (80) -> bdlzzvy, jnyvdz, zkwzctg
tmsnmf (42)
lxxbgm (56) -> hlansqa, agmao, dihvt, uxgux
yhonqw (579) -> tcaex, nwlacty, gkzpb, qtjpthc, ipfmr
oedan (21) -> zntrkc, lwpwtbj, awvqy, mmomd
gelep (34) -> qxivh, lmtebyt, wfwma
fllao (74)
sabolzl (64)
tmpysyn (22)
wrurg (32)
sfuegcs (42)
bhqkvi (31)
qgkaso (58)
fhryrfj (32)
hjkrxly (47) -> texooeb, elyuo
ssuho (92)
rejss (89) -> powvrta, fojnd, otqdauw
ffzjjj (28)
qkaaq (180)
suvwi (49)
rczoepp (36)
bhzeep (20)
kkflx (7330) -> coazy, kdwict, ojcpgj, qjdqn
gkxdmxg (10)
upnls (18)
bepnzsh (59)
xxsobt (137) -> zznnz, ziyta, xypex
bgscxgk (65)
tptxpuq (194) -> kemme, vfmiaz
qummd (77)
efkyht (11)
mmomd (71)
sulyr (73)
txswi (82)
ksbjftc (185) -> gfghu, spjim
gjvfc (94)
egkqlyz (148) -> vlysce, fozgkmk
aqeqvr (16)
kvheuf (63) -> johqe, dyeds
ajika (42)
dihvt (53)
zmpyqv (26)
xxvfb (17)
fvmws (43)
hsjbzgd (22)
uyvuqp (79) -> dfntl, jfvmu
cvseh (2033) -> liklroi, zsjvdo, bwtsue
juscckl (99) -> svlvlj, bujphvu, bgasdfq, ctdcrl
ruhqq (7)
yekxli (41)
ywrze (33)
jrksg (58)
mkvblbi (43)
suyawzr (47)
yhgutqw (10) -> oybow, ctdsj, deyxep, iyegmn
qucxsqh (83)
iurmaj (40)
ejjgym (69)
jfajopz (76) -> aonpvtr, hykmnhl, ppavww, wfkxhlf
undaxyj (92)
avfsez (81)
gbqig (181) -> qgkaso, gtditk
qaqof (130) -> oxerrb, afxazvx, mhseysh
xdrjmkv (82)
tocdoo (82)
mlztke (233) -> bgjwy, lrosl
aymgd (62)
mcnsxuh (143) -> xnqeu, xrjrjp, qvowcc, qazqwkj
afycii (199) -> okqwb, mvxqfe
atzuayu (41)
svfgh (99)
tnngtb (52)
hwhhyhh (56)
qrlmd (98) -> xernf, klvhv
wnjtvt (11)
wzruwk (82)
luixm (59)
hkntpfd (107) -> pyraep, tiunb
mqjpes (12)
pshil (78)
wvisr (137) -> znkqj, dwvbnp
slohro (598) -> qhgvoj, mdanw, zimidd
rdnozh (304) -> lgmjeng, llalv
psmvz (15)
zlsrhdz (75)
taaoji (58)
wbqkf (22)
metsfo (253) -> xoabt, wbiys
kckevg (7)
hhrlaah (155) -> smjtypd, rwqopie
daesbhs (77)
tuyjnby (44)
danfue (32) -> okrnkqa, mqjqez, gndjq, qcizo
ropjtoe (942) -> wpxhphx, wrwusvc, zarww, xymtys
tinitt (240) -> gypuu, btsvvyg
kxsefnd (285) -> cmqni, pjhoue
yzfnlfl (27)
wpfywy (530) -> mifmz, edygy, nmfhgq, danfue
hwldx (66)
sakmn (74)
ehlwoxs (7524) -> qggjzz, zordz, phntkf
fekdmb (96)
ziyta (18)
cbdyc (58)
ibushn (41) -> thats, nefpbc, yvpzbgp, vddsv
lcbkylu (732) -> gawbtev, aejhrrh, zfzpgfw
mhlgi (50)
rptfwu (12)
fkmyndg (50)
tylelk (24) -> drfzng, yhonqw, wsyiyen, dqwocyn, qqnroz
azjunml (42)
hfjazyf (80)
nuajwg (86)
cukfipr (40)
pkcpn (90)
guccv (73)
pyfeav (62)
ikeiwjo (157)
hqcwl (19)
xayhv (76)
wemzz (76)
cqupq (88) -> jjvbyf, zddlo, plmaxee
btrdhk (43)
eirze (41)
litnjrv (1103) -> fxqaw, jbqehvt, hhrlaah
gveca (66) -> bstqyq, imdqhns
wpgziu (88)
vfwwc (61) -> anoza, zjhnhz, hgdghys
losjvw (61)
zbxopzp (147) -> qaqgap, cqfyjm
uksim (24)
uiiqr (1611) -> ysxuvi, yryyz, dnmsps, cqdggj, vyevfn, dzienj
mifmz (170) -> tgqxadm, efqzxka
hkxefzm (40)
ojcpgj (121) -> fpwoels, dzyfjvd
xqrnd (35) -> wlodh, gbmexj, zsratan
ahcba (38)
jnxbxzk (32)
ftthnl (222) -> halwu, mdktwy
qjlrpjn (59)
nuwpvd (76)
jnhyc (252) -> lcqed, fiwnjv
gmevoe (43)
glumdc (64)
rajiodp (268) -> uldlh, rudbmkz
qebkt (95)
vddfzu (67) -> wchtkp, aduuei
hcqsg (939) -> zgzxr, moeujf, xtocem, hivsxt
wrwusvc (60) -> bdqnomo, objgx
uzoroj (199) -> dvips, dkeosz
ujyxvl (54)
nltqkvf (66) -> fwevqj, aledrs, elvzp
lhjpci (34)
igqup (69)
vszfxh (40)
ztxjb (81)
aibabp (58)
vaqhekv (217) -> pejkmud, bkicgcc
wchtkp (65)
ycxyxg (91)
rgpazuy (44) -> waxvx, uckyywt
bppdgwm (78)
csxdpl (56)
vxjvov (68) -> tocdoo, jpxgvjl
vuckhv (87)
wnqny (56)
kcorlw (86)
jlvakq (239) -> ngtpz, xplsuaq
tcfmra (96)
twxwam (8975) -> qwtvro, osipmuv, cldldxp
xhang (48)
qneggdm (169) -> iurmaj, faqsp
umuur (86)
tuyon (90)
aqoik (53)
oldoxo (75)
rjjeggt (44)
fdklcbu (70)
tslfayy (41)
zpjju (68) -> ncffht, akmsaq
xijkpj (38)
xfmneu (89)
fdgccyg (24)
qkllvda (8)
zhubam (12)
emreip (94)
euypgtx (80)
tbwieh (108) -> uglla, iyqcty, pgtmio
mlkddpw (34)
zxphdt (5)
ohbzmqz (11)
dylrpo (69)
zjuupn (51) -> sibko, mlighq, wogrc
xykvys (160) -> iemgv, joees
nxwtdg (51) -> tcfmra, nvkhow, fekdmb, xgufltj
mlighq (27)
abspab (54)
fzcerr (10) -> zhnjnvg, bncmd
fxhlrok (69) -> dyxzd, rajiodp, hztzf, apexe
xvhpqmh (47) -> tuyjnby, aygltsd
nafvoj (127) -> aqoik, tapirho, kyizmdu
bkfbj (61)
hmyuwix (50) -> bpmrgr, soiza, mkbjgur
ilkhnhw (96)
fkbivys (69)
ikclk (77)
ysxuvi (249)
sppgjfx (530) -> bszaj, ozzxjr, ivfffiz, cdqkuuw
dfghz (64)
bxwtlj (214) -> khkaq, pkdeoh, dvvlx
uvexl (205) -> ftohrkw, fknai
xrjrjp (30)
oopiw (214)
yesozb (55)
wochkc (88)
dzyfjvd (35)
efqzxka (71)
hdjlp (55)
pbmni (69)
afcsq (190) -> zlvgiq, wemzz
hsykei (80)
swjcx (79) -> nbjrv, ytfnug
yanwn (95)
orxgo (99)
tcvpst (22)
xnfybs (41)
ctqym (59)
hwdkwn (27)
bvelsl (54)
gkegoh (51)
cbacfi (60)
gjihp (35)
hgdghys (1528) -> acpwe, yvttt, xbowtoi, hmrrarb, qneggdm
aejhrrh (281) -> gkskqqb, acgiwii
pzmmc (83) -> kmemzft, ewtqg
ffrgif (6) -> bpmus, vuckhv
naacbhr (39)
qeksx (73)
ncymzc (202) -> holcno, lmueep
gfghu (73)
qbncqqm (76)
qqkwjoy (297) -> iuagzo, nuvrtnk
sohohlc (697) -> gmeqmy, xstgov, ncymzc
zhnjnvg (95)
blstaec (115) -> kxcid, qummd
uhmmouc (74)
tfphsaq (1875) -> sndfkkd, vddfzu, xorbfm
phntkf (31) -> jjdfk, sqcet, iueqa
xfkpfqd (236)
tujrz (62)
sfxvp (167) -> uvfou, kasozsw, jfajopz
lyaqynn (43)
bfqotji (55)
jbkek (164) -> txznlay, fkzxmb
kqvsah (95)
zffoytm (85)
bpvit (184) -> tgexl, qbncqqm
ocuhfpd (95)
xhqrf (73)
jtgcmc (47) -> aqfemi, undug, bpznnqh, mmjpziu
rdthc (173) -> zfaxas, wfpxk, jwmjagj
hrbukg (6404) -> vlszzu, irgumpr, xwunxz
sndfkkd (83) -> yldsmt, drswab
znkqj (80)
xhubgcl (254) -> xnqznos, cbaah
epeain (16)
jbqehvt (225)
dobqmg (159) -> ejjgym, igqup
fguhavr (82)
dtakrnu (20)
ozzxjr (254) -> ojzpzsa, enmoyyj, nqzlzs
sqwovza (82)
hqpkdyb (106) -> bvviqc, jxcxv, ozugcs
ybfqzep (82)
bpmrgr (34)
qcldyng (32)
sbsfo (98)
saxar (88)
xucrab (63)
mdktwy (66)
nkegq (69)
gawbtev (100) -> jleqdi, dylrpo, zxdhxrb
htgvzw (180) -> rpanfr, zdaorg
fojnd (32)
yaera (143) -> mpwlly, gxzxapn
vlaowv (226) -> dxzahps, mtfqemm
lwujegj (101) -> emreip, ujnas
rtwur (311) -> shgcr, euoqdcd
dniub (19)
qaqgap (68)
oucqw (7596) -> qrlmd, gwpzvb, aywrlw
nesoknh (82)
rpzit (59)
uwoyjsd (83)
rawfw (68)
bnsqqv (38)
sgvaf (43) -> ihmqbiu, mweox, zkaqnra, uiiqr, athdvrh, qqmpq, jfnknli
ysmqsps (61) -> hfjazyf, lyorl, mhassg, euypgtx
facjth (57) -> wvaynsl, ygykyu, bhaebe, qcsfpn
gdvqsyp (388) -> zdiygz, ksbjftc, uekiz
bsnxzz (55)
qyqthsz (5) -> nkegq, jrjkj
xcjxzq (1306) -> hmjzw, ylmwjuo, xupkjdt
nbykdlk (339) -> gmtsea, qahfrp
acgiwii (13)
xquzvw (41)
kdrke (81)
bpznnqh (38)
zhckae (58)
ypzqp (1219) -> jewrs, juytoy
vrqdv (29)
klcuumi (42) -> swqgxh, rtzodmx, xmendwz
bsqpcne (362) -> xulpd, ixwoprg, rqqxoou, xykvys, nfchpk
oxerrb (49)
hivsxt (147) -> bipyp, botmw
kmyvyx (90)
nfkbhas (15)
hkcghm (76)
kqokslj (80)
djxvowe (56)
jypccpq (46)
yktmvtf (27)
dezgi (20)
bojjcl (31)
zsancei (75)
jnmgovh (86)
buyazh (1149) -> jrksg, zhckae
sppxgv (276) -> hgblqo, xpqnuh
cguzndh (75)
shgcr (62)
hmrrarb (53) -> wadeqe, floca
lmueep (13)
ntugl (44)
ftatt (92)
pgnbhl (210) -> qovcwth, bhxmn, ibagnjs
qsods (55)
xngnhi (841) -> jfclt, fpnjjy, wjkqpqr
relztcy (22)
vtphqb (237)
qahfrp (8)
bqppw (269)
hxowycm (16) -> okmwjoa, undaxyj
oojlo (111) -> losjvw, ekpvnh
fgbsxh (268)
mmotdue (113) -> relztcy, qwtheza
tienxkv (358) -> rqbjjuo, wdgfw
qwfosq (35) -> aunrdo, ntadc
anoza (37) -> bdzkzv, dzugjhb, hgltuwc, odmmo, tienxkv, yowbd
kioxu (159) -> qkdiej, kqfob
ybjld (24)
juytoy (80)
xstgov (206) -> wnjtvt, bnqutso
tapirho (53)
vjhwn (1738) -> xrmslfs, djejdy, oopiw
iroikgp (75) -> vqbfan, gkegoh
jtfdy (19)
ybqzq (363) -> vpsls, bbsvfl, isoayc
pqsfee (82)
bhxmn (59)
amhug (73)
yxzdn (19)
wvaynsl (85)
hrhfd (37)
yrbpdq (57)
ipppjn (62)
ygnlbv (88)
zjhnhz (2113) -> fsose, tbwieh, myhgys, nltqkvf
facddx (151) -> hwldx, ydgusm
gnbmz (89)
bmxoqy (17)
pyhohkx (17) -> nghcpr, wpgziu
sqnfn (235) -> ztxjb, noqmsh
gzqutgv (185) -> gqwfi, yenbb, reqlm, krquje
tgqxadm (71)
qjdqn (27) -> wzruwk, eegwdp
mvldvib (44)
gbmexj (39)
ppedet (34) -> qhfoy, lpgtx, xucrab, oioqg
ctdcrl (38) -> kufceqa, qebkt, ocuhfpd, isvfa
bhaebe (85)
amooqlb (53)
tcaex (115) -> cvxcr, mxikfk, xzfrad, tlwqwlk
uoenrx (59)
ewvlay (34)
zkwzctg (98)
qkjed (32)
jewrs (80)
snquxtz (53) -> dzrywb, hoilkqz
miidkpe (96)
hgltuwc (316) -> ptyuh, wfixt
oybow (58)
dtsdw (61)
qfzyvjr (156) -> ehclf, nmvki
ymerus (46)
cbefqk (65) -> fgzwvuy, yaawixo
nyeur (17)
baimp (69)"""


v = [x for x in instr.split('\n')]


all_children = set()

all_nodes = {}

node_weights = {}

node_calc_weights = collections.defaultdict(int)

for l in v:
    name = l.split(" ")[0]
    weight = int(l.split("(")[1].split(")")[0])
    if len(l.split("->")) > 1:
        children = [a.strip() for a in l.split("->")[-1].split(",")]
    else:
        children = []
    all_nodes[name] = children

    node_weights[name] = weight

    for c in children:
        all_children.add(c)

root = "airlri"

def weight_for_node(name):
    n_children = all_nodes[name]

    weights = []

    for c in n_children:
        weights.append(weight_for_node(c))

    ws = collections.Counter(weights)
    #if len(ws) != 1 and len(ws) > 0:
    #    print name
    #    print(n_children)
    #    print(ws)
    #    for c in n_children:
    #    exit()

    if len(n_children) == 0:
        return node_weights[name]

    if name in ['drfzng', 'yhonqw', 'wsyiyen', 'dqwocyn', 'qqnroz']:
        print node_weights[name]
        print sum(weights) + node_weights[name]


    return sum(weights) + node_weights[name]



weight_for_node(root)

#for node in all_nodes:
#    c = all_nodes[node]
#
#    balanced = True
#    if c is None or len(c) == 0:
#        continue
#
#    #print node
#    #print [node_calc_weights[x] for x in c]
#    allweights = [node_calc_weights[x] for x in c]
#    ws = collections.Counter(allweights)
#
#    if len(ws) > 1:
#        print(node)
#        print([a for a in  c if len(all_nodes[a]) == 0])
#        print(ws)



