file1 = open('predictions.txt', 'r')
file2 = open('expected.txt', 'r')
Lines1 = file1.readlines()
Lines2 = file2.readlines()

cpt = 0
tp_total = 0

cpt_HTTP_get = 0
cpt_icmp = 0
cpt_TCP = 0
cpt_UDP = 0
cpt_Scan = 0
cpt_BF = 0
cpt_nrml = 0

tp_HTTP_get =0
tp_icmp = 0
tp_TCP = 0
tp_UDP = 0
tp_Scan = 0
tp_BF = 0
tp_nrml = 0

fn_HTTP_get =0
fn_icmp = 0
fn_TCP = 0
fn_UDP = 0
fn_Scan = 0
fn_BF = 0
fn_nrml = 0

fp_HTTP_get =0
fp_icmp = 0
fp_TCP = 0
fp_UDP = 0
fp_Scan = 0
fp_BF = 0
fp_nrml = 0

for line1, line2 in zip(Lines1, Lines2):
    str1 = line1.strip()
    str2 = line2.strip()
    cpt += 1

    if str2 == "[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]":
        cpt_HTTP_get += 1
        if str1 == str2:    
            tp_HTTP_get += 1
        else:
            fn_HTTP_get += 1

    elif str2 == "[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]":
        cpt_icmp += 1
        if str1 == str2:
            tp_icmp += 1
        else:
            fn_icmp += 1 

    elif str2 == "[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]":
        cpt_TCP += 1
        if str1 == str2:
            tp_TCP += 1
        else:
            fn_TCP += 1 

    elif str2 == "[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]":
        cpt_UDP += 1
        if str1 == str2:
            tp_UDP += 1
        else:
            fn_UDP += 1 

    elif str2 == "[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]":
        cpt_Scan += 1
        if str1 == str2:
            tp_Scan += 1
        else:
            fn_Scan += 1 

    elif str2 == "[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]":
        cpt_BF += 1
        if str1 == str2:
            tp_BF += 1
        else:
            fn_BF += 1 

    elif str2 == "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]":
        cpt_nrml += 1
        if str1 == str2:
            tp_nrml += 1
        else:
            fn_nrml += 1 

    if str1 == "[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]" and (str1 != str2):
        fp_HTTP_get += 1
    elif str1 == "[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]" and (str1 != str2):
        fp_icmp += 1 
    elif str1 == "[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]" and (str1 != str2):
        fp_TCP += 1
    elif str1 == "[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]" and (str1 != str2):
        fp_UDP += 1
    elif str1 == "[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]" and (str1 != str2):
        fp_Scan += 1
    elif str1 == "[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]" and (str1 != str2):
        fp_BF += 1
    elif str1 == "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]" and (str1 != str2):
        fp_nrml += 1

tp_total = tp_HTTP_get+tp_icmp+tp_TCP+tp_UDP+tp_Scan+tp_BF+tp_nrml
fp_total = fp_HTTP_get+fp_icmp+fp_TCP+fp_UDP+fp_Scan+fp_BF+fp_nrml

Recall_HTTP_get = tp_HTTP_get/cpt_HTTP_get
Recall_icmp     = tp_icmp    /cpt_icmp
Recall_TCP      = tp_TCP     /cpt_TCP
Recall_UDP      = tp_UDP     /cpt_UDP
Recall_Scan     = tp_Scan    /cpt_Scan
Recall_BF       = tp_BF      /cpt_BF
Recall_nrml     = tp_nrml    /cpt_nrml

Precision_HTTP_get = tp_HTTP_get/(tp_HTTP_get + fp_HTTP_get)
Precision_icmp     = tp_icmp    /(tp_icmp     + fp_icmp    )
Precision_TCP      = tp_TCP     /(tp_TCP      + fp_TCP     )
Precision_UDP      = tp_UDP     /(tp_UDP      + fp_UDP     )
Precision_Scan     = tp_Scan    /(tp_Scan     + fp_Scan    )
Precision_BF       = tp_BF      /(tp_BF       + fp_BF      )
Precision_nrml     = tp_nrml    /(tp_nrml     + fp_nrml    )

F1_score_HTTP_get = 2*(Precision_HTTP_get * Recall_HTTP_get / (Precision_HTTP_get + Recall_HTTP_get))
F1_score_icmp     = 2*(Precision_icmp     * Recall_icmp     / (Precision_icmp     + Recall_icmp    ))
F1_score_TCP      = 2*(Precision_TCP      * Recall_TCP      / (Precision_TCP      + Recall_TCP     ))
F1_score_UDP      = 2*(Precision_UDP      * Recall_UDP      / (Precision_UDP      + Recall_UDP     ))
F1_score_Scan     = 2*(Precision_Scan     * Recall_Scan     / (Precision_Scan     + Recall_Scan    ))
F1_score_BF       = 2*(Precision_BF       * Recall_BF       / (Precision_BF       + Recall_BF      ))
F1_score_nrml     = 2*(Precision_nrml     * Recall_nrml     / (Precision_nrml     + Recall_nrml    ))

print("Total number of predictions : ", cpt)
print("Number of correct predictions: ", tp_total)

if cpt_HTTP_get  != 0 : print("Precision for HTTP get    Attack : ", round(100*Precision_HTTP_get,5))
if cpt_HTTP_get  != 0 : print("Recall for HTTP get    Attack : ", round(100*Recall_HTTP_get,5), " --- ", tp_HTTP_get, "/", cpt_HTTP_get)
if cpt_HTTP_get  != 0 : print("F1-score for HTTP get    Attack : ", round(100*F1_score_HTTP_get,5))
print("\n")
if cpt_icmp      != 0 : print("Precision for ICMP        Attack : ", round(100*Precision_icmp,5))
if cpt_icmp      != 0 : print("Recall for ICMP        Attack : ", round(100*Recall_icmp,5), " --- ", tp_icmp, "/", cpt_icmp)
if cpt_icmp      != 0 : print("F1-score for ICMP        Attack : ", round(100*F1_score_icmp,5))
print("\n")
if cpt_TCP       != 0 : print("Precision for TCP         Attack : ", round(100*Precision_TCP,5))
if cpt_TCP       != 0 : print("Recall for TCP         Attack : ", round(100*Recall_TCP,5), " --- ", tp_TCP, "/", cpt_TCP)
if cpt_TCP       != 0 : print("F1-score for TCP         Attack : ", round(100*F1_score_TCP,5))
print("\n")
if cpt_UDP       != 0 : print("Precision for UDP         Attack : ", round(100*Precision_UDP,5))
if cpt_UDP       != 0 : print("Recall for UDP         Attack : ", round(100*Recall_UDP,5), " --- ", tp_UDP, "/", cpt_UDP)
if cpt_UDP       != 0 : print("F1-score for UDP         Attack : ", round(100*F1_score_UDP,5))
print("\n")
if cpt_Scan      != 0 : print("Precision for Port Scan   Attack : ", round(100*Precision_Scan,5))
if cpt_Scan      != 0 : print("Recall for Port Scan   Attack : ", round(100*Recall_Scan,5), " --- ", tp_Scan, "/", cpt_Scan)
if cpt_Scan      != 0 : print("F1-score for Port Scan   Attack : ", round(100*F1_score_Scan,5))
print("\n")
if cpt_BF        != 0 : print("Precision for Brute Force Attack : ", round(100*Precision_BF,5))
if cpt_BF        != 0 : print("Recall for Brute Force Attack : ", round(100*Recall_BF,5), " --- ", tp_BF, "/", cpt_BF)
if cpt_BF        != 0 : print("F1-score for Brute Force Attack : ", round(100*F1_score_BF,5))
print("\n")
if cpt_nrml      != 0 : print("Precision for Normal Traffic     : ", round(100*Precision_nrml,5))
if cpt_nrml      != 0 : print("Recall for Normal Traffic     : ", round(100*Recall_nrml,5), " --- ", tp_nrml, "/", cpt_nrml)
if cpt_nrml      != 0 : print("F1-score for Normal Traffic     : ", round(100*F1_score_nrml,5))
