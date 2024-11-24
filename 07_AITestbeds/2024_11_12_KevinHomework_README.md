# Intro to AI Series: AI Accelerators


Scientific applications are increasingly adopting Artificial Intelligence (AI) techniques to advance science. There are specialized hardware accelerators designed and built to run AI applications efficiently. With a wide diversity in the hardware architectures and software stacks of these systems, it is challenging to understand the differences between these accelerators, their capabilities, programming approaches, and how they perform, particularly for scientific applications. 

We will cover an overview of the AI accelerators landscape with a focus on SambaNova, Cerebras, Graphcore, and Groq systems along with architectural features and details of their software stacks. We will have hands-on exercises that will help attendees understand how to program these systems by learning how to refactor codes written in standard AI framework implementations and compile and run the models on these systems. 



## Slides

* [Intro to AI Series: AI Accelerators](./AI_Accelerators.pdf) 

## Hands-On Sessions


* [Cerebras](./Cerebras/README.md)
* [Graphcore](./Graphcore/README.md)  
* [SambaNova](./Sambanova/README.md)                                    
* [Groq](./Groq/README.md)        


### Director’s Discretionary Allocation Program

To gain access to AI Testbeds at ALCF after current allocation expires apply for [Director’s Discretionary Allocation Program](https://www.alcf.anl.gov/science/directors-discretionary-allocation-program)

The ALCF Director’s Discretionary program provides “start up” awards to researchers working to achieve computational readiness for for a major allocation award.

## Homework 

You need to submit either Theory Homework or Hands-on Homework. 

#####  Theory Homework
* What are the key architectural features that make these systems suitable for AI workloads?
* Identify the primary differences between these AI accelerator systems in terms of their architecture and programming models.
* Based on hands-on sessions, describe a typical workflow for refactoring an AI model to run on one of ALCF's AI testbeds (e.g., SambaNova or Cerebras). What tools or software stacks are typically used in this process?
* Give an example of a project that would benefit from AI accelerators and why?

##### Hands-on Homework

* [Cerebras Homework](./Cerebras/README.md#homework)
* [Sambanova Homework](./Sambanova/README.md#homework)
* [Graphcore Homework](./Graphcore/README.md#homework)
* [Groq Homework](./Groq/README.md#homework)

## Solution

##### Solution 1: 

* [Groq Homework](./Groq/README.md#homework) - Run MiniLM example with custom input instead of dummy input. Submit proof (contents printed out to your terminal, path to a logfile or screenshot) that you were able to successfully follow the instructions and execute.

<details>
    <summary>Groq Terminal Print Out here</summary>
  
```bash
Last login: Sat Nov 23 16:25:49 on ttys000
kevinfang@Kevins-MacBook-Air-8 ~ % ssh kevinfang@groq.ai.alcf.anl.gov
(kevinfang@groq.ai.alcf.anl.gov) ---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Password: 
---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-102-generic x86_64)
Last login: Sun Nov 24 00:26:31 2024 from 192.145.118.6
(base) kevinfang@groq-login-02:~$ ls
BertLarge			   slurm-43631.out  slurm-43637.out
Miniconda3-latest-Linux-x86_64.sh  slurm-43632.out  slurm-43639.out
ai-science-training-series	   slurm-43634.out  slurm-43641.out
miniconda3			   slurm-43635.out
(base) kevinfang@groq-login-02:~$ rm -rf Miniconda3-latest-Linux-x86_64.sh 
(base) kevinfang@groq-login-02:~$ rm -rf miniconda3/
(base) kevinfang@groq-login-02:~$ ls
BertLarge		    slurm-43632.out  slurm-43637.out
ai-science-training-series  slurm-43634.out  slurm-43639.out
slurm-43631.out		    slurm-43635.out  slurm-43641.out
(base) kevinfang@groq-login-02:~$ ssh groq-r01-gn-04.ai.alcf.anl.gov
---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-107-generic x86_64)
 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.
To restore this content, you can run the 'unminimize' command.
-----------------------------------------------------------------------------
                           Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
                           Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
-----------------------------------------------------------------------------
kevinfang@groq-r01-gn-04:~$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
--2024-11-24 00:43:37--  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
Resolving repo.anaconda.com (repo.anaconda.com)... 104.16.32.241, 104.16.191.158, 2606:4700::6810:20f1, ...
Connecting to repo.anaconda.com (repo.anaconda.com)|104.16.32.241|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 148337011 (141M) [application/octet-stream]
Saving to: ‘Miniconda3-latest-Linux-x86_64.sh’
Miniconda3-latest-L 100%[===================>] 141.46M   279MB/s    in 0.5s    
2024-11-24 00:43:38 (279 MB/s) - ‘Miniconda3-latest-Linux-x86_64.sh’ saved [148337011/148337011]
kevinfang@groq-r01-gn-04:~$ bash Miniconda3-latest-Linux-x86_64.sh
Welcome to Miniconda3 py312_24.9.2-0
In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 
ANACONDA TERMS OF SERVICE
Please read these Terms of Service carefully before purchasing, using, accessing
, or downloading any Anaconda Offerings (the "Offerings"). These Anaconda Terms 
of Service ("TOS") are between Anaconda, Inc. ("Anaconda") and you ("You"), the 
individual or entity acquiring and/or providing access to the Offerings. These T
OS govern Your access, download, installation, or use of the Anaconda Offerings,
 which are provided to You in combination with the terms set forth in the applic
able Offering Description, and are hereby incorporated into these TOS. Except wh
ere indicated otherwise, references to "You" shall include Your Users. You hereb
y acknowledge that these TOS are binding, and You affirm and signify your consen
t to these TOS by registering to, using, installing, downloading, or accessing t
he Anaconda Offerings effective as of the date of first registration, use, insta
ll, download or access, as applicable (the "Effective Date"). Capitalized defini
tions not otherwise defined herein are set forth in Section 15 (Definitions). If
 You do not agree to these Terms of Service, You must not register, use, install
, download, or access the Anaconda Offerings.
1. ACCESS & USE
1.1 General License Grant. Subject to compliance with these TOS and any applicab
le Offering Description, Anaconda grants You a personal, non-exclusive, non-tran
sferable, non-sublicensable, revocable, limited right to use the applicable Anac
onda Offering strictly as detailed herein and as set forth in a relevant Offerin
g Description. If You purchase a subscription to an Offering as set forth in a r
elevant Order, then the license grant(s) applicable to your access, download, in
stallation, or use of a specific Anaconda Offering will be set forth in the rele
vant Offering Description and any definitive agreement which may be executed by you in writing or electronic in connection with your Order ("Custom Agreement"). License grants for specific Anaconda Offerings are set forth in the relevant Offe
ring Description, if applicable.
1.2 License Restrictions. Unless expressly agreed by Anaconda, You may not:  (a) Make, sell, resell, license, sublicense, distribute, rent, or lease any Offerings available to anyone other than You or Your Users, unless expressly stated other
wise in an Order, Custom Agreement or the Documentation or as otherwise expressly permitted in writing by Anaconda; (b) Use the Offerings to store or transmit infringing, libelous, or otherwise unlawful or tortious material, or to store or tr
ansmit material in violation of third-party privacy rights; (c) Use the Offerings or Third Party Services to store or transmit Malicious Code, or attempt to gain unauthorized access to any Offerings or Third Party Services or their related sy
stems or networks; (d)Interfere with or disrupt the integrity or performance of any Offerings or Third Party Services, or third-party data contained therein; (e) Permit direct or indirect access to or use of any Offerings or Third Party Servi
ces in a way that circumvents a contractual usage limit, or use any Offerings to access, copy or use any Anaconda intellectual property except as permitted under these TOS, a Custom Agreement, an Order or the Documentation; (f) Modify, copy o
r create derivative works of the Offerings or any part, feature, function or user interface thereof except, and then solely to the extent that, such activity is required to be permitted under applicable law; (g) Copy Content except as permitt
ed herein or in an Order, a Custom Agreement or the Documentation or republish any material portion of any Offering in a manner competitive with the offering by Anaconda, including republication on another website or redistribute or embed any
 or all Offerings in a commercial product for redistribution or resale; (h) Frame or Mirror any part of any Content or Offerings, except if and to the extent permitted in an applicable Custom Agreement or Order for your own Internal Use and a
s permitted in a Custom Agreement or Documentation; (i) Except and then solely to the extent required to be permitted by applicable law, copy, disassemble, reverse engineer, or decompile an Offering, or access an Offering to build a competiti
ve  service by copying or using similar ideas, features, functions or graphics of the Offering. You may not use any "deep-link", "page-scrape", "robot", "spider" or other automatic device, program, algorithm or methodology, or any similar or 
equivalent manual process, to access, acquire, copy or monitor any portion of our Offerings or Content. Anaconda reserves the right to end any such activity. If You would like to redistribute or embed any Offering in any product You are devel
oping, please contact the Anaconda team for a third party redistribution commercial license.
2. USERS & LICENSING
2.1 Organizational Use.  Your registration, download, use, installation, access, or enjoyment of all Anaconda Offerings on behalf of an organization that has two hundred (200) or more employees or contractors ("Organizational Use") requires a
 paid license of Anaconda Business or Anaconda Enterprise. For sake of clarity, use by government entities and nonprofit entities with over 200 employees or contractors is considered Organizational Use.  Purchasing Starter tier license(s) doe
s not satisfy the Organizational Use paid license requirement set forth in this Section 2.1.
 Educational Entities will be exempt from the paid license requirement, provided that the use of the Anaconda Offering(s) is solely limited to being used for a curriculum-based course. Anaconda reserves the right to monitor the registration, 
download, use, installation, access, or enjoyment of the Anaconda Offerings to ensure it is part of a curriculum.
2.2 Use by Authorized Users. Your "Authorized Users" are your employees, agents, and independent contractors (including outsourcing service providers) who you authorize to use the Anaconda Offering(s) on Your behalf for Your Internal Use, pro
vided that You are responsible for: (a) ensuring that such Authorized Users comply with these TOS or an applicable Custom Agreement; and  (b) any breach of these TOS by such Authorized Users.
2.3 Use by Your Affiliates. Your Affiliates may use the Anaconda Offering(s) on Your behalf for Your Internal Use only with prior written approval from Anaconda. Such Affiliate usage is limited to those Affiliates who were defined as such upo
n the Effective Date of these TOS. Usage by organizations who become Your Affiliates after the Effective Date may require a separate license, at Anaconda's discretion.
2.4 Licenses for Systems. For each End User Computing Device ("EUCD") (i.e. laptops, desktop devices) one license covers one installation and a reasonable number of virtual installations on the EUCD (e.g. Docker, VirtualBox, Parallels, etc.).
 Any other installations, usage, deployments, or access must have an individual license per each additional usage.
2.5 Mirroring. You may only Mirror the Anaconda Offerings with the purchase of a Site License unless explicitly included in an Order Form or Custom Agreement.
2.6 Beta Offerings. Anaconda provides Beta Offerings "AS-IS" without support or any express or implied warranty or indemnity for any problems or issue s, and Anaconda has no liability relating to Your use of the Beta Offerings. Unless agreed 
in writing by Anaconda, You will not put Beta Offerings into production use. You may only use the Beta Offerings for the period specified by Anaconda in writing; (b) Anaconda, in its discretion, may stop providing the Beta Offerings at any ti
me, at which point You must immediately cease using the Beta Offering(s); and (c) Beta Offerings may contain bugs, errors, or other issues..
2.7 Content. In consideration of Your payment of Subscription Fees, Anaconda hereby grants to You and Your Users a personal, non-exclusive, non-transferable, non-sublicensable, revocable, limited right and license during the Usage Term to acc
ess, input, use, transmit, copy, process, and measure the Content solely (1) within the Offerings and to the extent required to enable the ordinary and unmodified functionality of the Offerings as described in the Offering descriptions, and (
2) for your Internal Use. Customer hereby acknowledge that the grant hereunder is solely being provided for your Internal Use and not to modify or to create any derivatives based on the Content.
3. ANACONDA OFFERINGS
3.1 Upgrades or Additional Copies of Offerings. You may only use additional copies of the Offerings beyond Your Order if You have acquired such rights under an agreement with Anaconda and you may only use Upgrades under Your Order to the exte
nt you have discontinued use of prior versions of the Offerings.
3.2 Changes to Offerings; Maintenance. Anaconda may: (a) enhance or refine an Offering, although in doing so, Anaconda will not materially reduce the core functionality of that Offering, except as contemplated in Section 3.4 (End of Life); an
d (b) perform scheduled maintenance of the infrastructure and software used to provide an Offering, during which You may experience some disruption to that Offering.  Whenever reasonably practicable, Anaconda will provide You with advance not
ice of such maintenance. You acknowledge that occasionally, Anaconda may need to perform emergency maintenance without providing You advance notice, during which Anaconda may temporarily suspend Your access to, and use of, the Offering.
3.3 Use with Third Party Products. If You use the Anaconda Offering(s) with third party products, such use is at Your risk. Anaconda does not provide support or guarantee ongoing integration support for products that are not a native part of 
the Anaconda Offering(s).
3.4 End of Life. Anaconda reserves the right to discontinue the availability of an Anaconda Offering, including its component functionality, hereinafter referred to as "End of Life" or "EOL", by providing written notice through its official w
ebsite, accessible at www.anaconda.com at least sixty (60) days prior to the EOL. In such instances, Anaconda is under no obligation to provide support in the transition away from the EOL Offering or feature, You shall transition to the lates
t version of the Anaconda Offering, as soon as the newest Version is released in order to maintain uninterrupted service. In the event that You or Your designated Anaconda Partner have previously remitted a prepaid fee for the utilization of 
Anaconda Offering, and if the said Offering becomes subject to End of Life (EOL) before the end of an existing Usage Term, Anaconda shall undertake commercially reasonable efforts to provide the necessary information to facilitate a smooth tr
ansition to an alternative Anaconda Offering that bears substantial similarity in terms of functionality and capabilities. Anaconda will not be held liable for any direct or indirect consequences arising from the EOL of an Offering or feature
, including but not limited to data loss, service interruption, or any impact on business operations.
4. OPEN SOURCE, CONTENT & APPLICATIONS
4.1 Open-Source Software & Packages. Our Offerings include open-source libraries, components, utilities, and third-party software that is distributed or otherwise made available as "free software," "open-source software," or under a similar l
icensing or distribution model ("Open-Source Software"), which may be subject to third party open-source license terms (the "Open-Source Terms"). Certain Offerings are intended for use with open-source Python and R software packages and tools
 for statistical computing and graphical analysis ("Packages"), which are made available in source code form by third parties and Community Users. As such, certain Offerings interoperate with certain Open-Source Software components, including
 without limitation Open Source Packages, as part of its basic functionality; and to use certain Offerings, You will need to separately license Open-Source Software and Packages from the licensor. Anaconda is not responsible for Open-Source S
oftware or Packages and does not assume any obligations or liability with respect to You or Your Users' use of Open-Source Software or Packages. Notwithstanding anything to the contrary, Anaconda makes no warranty or indemnity hereunder with 
respect to any Open-Source Software or Packages. Some of such Open-Source Terms or other license agreements applicable to Packages determine that to the extent applicable to the respective Open-Source Software or Packages licensed thereunder.
  Any such terms prevail over any conflicting license terms, including these TOS. Anaconda will use best efforts to use only Open-Source Software and Packages that do not impose any obligation or affect the Customer Data (as defined hereinaft
er) or Intellectual Property Rights of Customer (beyond what is stated in the Open-Source Terms and herein), on an ordinary use of our Offerings that do not involve any modification, distribution, or independent use of such Open-Source Softwa
re.
4.2 Open Source Project Affiliation. Anaconda's software packages are not affiliated with upstream open source projects. While Anaconda may distribute and adapt open source software packages for user convenience, such distribution does not im
ply any endorsement, approval, or validation of the original software's quality, security, or suitability for specific purposes.
4.3 Third-Party Services and Content. You may access or use, at Your sole discretion, certain third-party products, services, and Content that interoperate with the Offerings including, but not limited to: (a) third party Packages, components
, applications, services, data, content, or resources found in the Offerings, and (b) third-party service integrations made available through the Offerings or APIs (collectively, "Third-Party Services"). Each Third-Party Service is governed b
y the applicable terms and policies of the third-party provider. The terms under which You access, use, or download Third-Party Services are solely between You and the applicable Third-Party Service provider. Anaconda does not make any repres
entations, warranties, or guarantees regarding the Third-Party Services or the providers thereof, including, but not limited to, the Third-Party Services' continued availability, security, and integrity. Third-Party Services are made availabl
e by Anaconda on an "AS IS" and "AS AVAILABLE" basis, and Anaconda may cease providing them in the Offerings at any time in its sole discretion and You shall not be entitled to any refund, credit, or other compensation.
5. CUSTOMER CONTENT, APPLICATIONS & RESPONSIBILITIES
5.1 Customer Content and Applications. Your content remains your own. We assume no liability for the content you publish through our services. However, you must adhere to our Acceptable Use Policy while utilizing our platform. You can share y
our submitted Customer Content or Customer Applications with others using our Offerings. By sharing Your Content, you grant legal rights to those You give access to. Anaconda has no responsibility to enforce, police, or otherwise aid You in e
nforcing or policing the terms of the license(s) or permission(s) You have chosen to offer. Anaconda is not liable for third-party misuse of your submitted Customer Content or Customer Applications on our Offerings. Customer Applications does
 not include any derivative works that might be created out of open source where the license prohibits derivative works.
5.2 Removal of Customer Content and Applications. If You received a removal notification regarding any Customer Content or a Customer Application due to legal reasons or policy violations, you promptly must do so. If You don't comply or the v
iolation persists, Anaconda may disable the Content or your access to the Content. If required, You must confirm in writing that you've deleted or stopped using the Customer Content or Customer Applications. Anaconda might also remove Custome
r Content or Customer Applications if requested by a Third-party rights holder whose rights have been violated. Anaconda isn't obliged to store or provide copies of Customer Content or Customer Applications that have been removed, is Your res
ponsibility to maintain a back-up of Your Content.
5.3 Protecting Account Access. You will keep all account information up to date, use reasonable means to protect Your account information, passwords, and other login credentials, and promptly notify Anaconda of any known or suspected unauthor
ized use of or access to Your account.
6. YOUR DATA, PRIVACY & SECURITY
6.1 Your Data. Your Data, hereinafter "Customer Data", is any data, files, attachments, text, images, reports, personal information, or any other data that is, uploaded or submitted, transmitted, or otherwise made available, to or through the
 Offerings, by You or any of your Authorized Users and is processed by Anaconda on your behalf. For the avoidance of doubt, Anonymized Data is not regarded as Customer Data. You retain all right, title, interest, and control, in and to the Cu
stomer Data, in the form submitted to the Offerings. Subject to these TOS, You grant Anaconda a worldwide, royalty-free, non-exclusive license to store, access, use, process, copy, transmit, distribute, perform, export, and display the Custom
er Data, and solely to the extent that reformatting Customer Data for display in the Offerings constitutes a modification or derivative work, the foregoing license also includes the right to make modifications and derivative works. The aforem
entioned license is hereby granted solely: (i) to maintain, improve and provide You the Offerings; (ii) to prevent or address technical or security issues and resolve support requests; (iii) to investigate when we have a good faith belief, or
 have received a complaint alleging, that such Customer Data is in violation of these TOS; (iv) to comply with a valid legal subpoena, request, or other lawful process; (v) detect and avoid overage of use of our Offering and confirm complianc
e by Customer with these TOS and other applicable agreements and policies;  (vi) to create Anonymized Data whether directly or through telemetry, and (vi) as expressly permitted in writing by You. Anaconda may use and retain your Account Info
rmation for business purposes related to these TOS and to the extent necessary to meet Anaconda's legal compliance obligations (including, for audit and anti-fraud purposes). We reserve the right to utilize aggregated data to enhance our Offe
rings functionality, ensure  compliance, avoid Offering overuse, and derive insights from customer behavior, in strict adherence to our Privacy Policy.
6.2 Processing Customer Data. The ordinary operation of certain Offerings requires Customer Data to pass through Anaconda's network. To the extent that Anaconda processes Customer Data on your behalf that includes Personal Data, Anaconda will
 handle such Personal Data in compliance with our Data Processing Addendum.
6.3 Privacy Policy.  If You obtained the Offering under these TOS, the conditions pertaining to the handling of your Personal Data, as described in our Privacy Policy, shall govern. However, in instances where your offering acquisition is exe
cuted through a Custom Agreement, the terms articulated within our Data Processing Agreement ("DPA") shall take precedence over our Privacy Policy concerning data processing matters.
6.4 Aggregated  Data. Anaconda retains all right, title, and interest in the models, observations, reports, analyses, statistics, databases, and other information created, compiled, analyzed, generated or derived by Anaconda from platform, ne
twork, or traffic data in the course of providing the Offerings ("Aggregated Data"). To the extent the Aggregated Data includes any Personal Data, Anaconda will handle such Personal Data in compliance with applicable data protection laws and 
the Privacy Policy or DPA, as applicable.
6.5 Offering Security. Anaconda will implement industry standard security safeguards for the protection of Customer Confidential Information, including any Customer Content originating or transmitted from or processed by the Offerings and/or 
cached on or within Anaconda's network and stored within the Offerings in accordance with its policies and procedures. These safeguards include commercially reasonable administrative, technical, and organizational measures to protect Customer
 Content against destruction, loss, alteration, unauthorized disclosure, or unauthorized access, including such things as information security policies and procedures, security awareness training, threat and vulnerability management, incident
 response and breach notification, and vendor risk management procedures.
7. SUPPORT
7.1 Support Services. Anaconda offers Support Services that may be included with an Offering. Anaconda will provide the purchased level of Support Services in accordance with the terms of the Support Policy as detailed in the applicable Order
. Unless ordered, Anaconda shall have no responsibility to deliver Support Services to You. The Support Service Levels and Tiers are described in the relevant Support Policy, found here.
7.2 Information Backups. You are aware of the risk that Your Content may be lost or irreparably damaged due to faults, suspension, or termination. While we might back up data, we cannot guarantee these backups will occur to meet your frequenc
y needs or ensure successful recovery of Your Content. It is your obligation to back up any Content you wish to preserve. We bear no legal liability for the loss or damage of Your Content.
8. OWNERSHIP & INTELLECTUAL PROPERTY
8.1 General. Unless agreed in writing, nothing in these TOS transfers ownership in, or grants any license to, any Intellectual Property Rights.
8.2 Feedback. Anaconda may use any feedback You provide in connection with Your use of the Anaconda Offering(s) as part of its business operations. You hereby agree that any feedback provided to Anaconda will be the intellectual property of A
naconda without compensation to the provider, author, creator, or inventor of providing the feedback.
8.3 DMCA Compliance. You agree to adhere to our Digital Millennium Copyright Act (DMCA) policies established in our Acceptable Use Policy.
9. CONFIDENTIAL INFORMATION
9.1 Confidential Information. In connection with these TOS and the Offerings (including the evaluation thereof), each Party ("Discloser") may disclose to the other Party ("Recipient"), non-public business, product, technology and marketing in
formation, including without limitation, customers lists and information, know-how, software and any other non-public information that is either identified as such or should reasonably be understood to be confidential given the nature of the 
information and the circumstances of disclosure, whether disclosed prior or after the Effective Date ("Confidential Information"). For the avoidance of doubt, (i) Customer Data is regarded as your Confidential Information, and (ii) our Offeri
ngs, including Beta Offerings, and inclusive of their underlying technology, and their respective performance information, as well as any data, reports, and materials we provided to You in connection with your evaluation or use of the Offerin
gs, are regarded as our Confidential Information. Confidential Information does not include information that (a) is or becomes generally available to the public without breach of any obligation owed to the Discloser; (b) was known to the Reci
pient prior to its disclosure by the Discloser without breach of any obligation owed to the Discloser; (c) is received from a third party without breach of any obligation owed to the Discloser; or (d) was independently developed by the Recipi
ent without any use or reference to the Confidential Information.
9.2 Confidentiality Obligations. The Recipient will (i) take at least reasonable measures to prevent the unauthorized disclosure or use of Confidential Information, and limit access to those employees, affiliates, service providers and agents
, on a need to know basis and who are bound by confidentiality obligations at least as restrictive as those contained herein; and (ii) not use or disclose any Confidential Information to any third party, except as part of its performance unde
r these TOS and to consultants and advisors to such party, provided that any such disclosure shall be governed by confidentiality obligations at least as restrictive as those contained herein.
9.3 Compelled Disclosure. Notwithstanding the above, Confidential Information may be disclosed pursuant to the order or requirement of a court, administrative agency, or other governmental body; provided, however, that to the extent legally p
ermissible, the Recipient shall make best efforts to provide prompt written notice of such court order or requirement to the Discloser to enable the Discloser to seek a protective order or otherwise prevent or restrict such disclosure.
10. INDEMNIFICATION
10.1 By Customer. Customer hereby agree to indemnify, defend and hold harmless Anaconda and our Affiliates and their respective officers, directors, employees and agents from and against any and all claims, damages, obligations, liabilities, 
losses, reasonable expenses or costs incurred as a result of any third party claim arising from (i) You and/or any of your Authorized Users', violation of these TOS or applicable law; and/or (ii) Customer Data and/or Customer Content, includi
ng the use of Customer Data and/or Customer Content by Anaconda and/or any of our subcontractors, which infringes or violates, any third party's rights, including, without limitation, Intellectual Property Rights.
10.2 By Anaconda. Anaconda will defend any third party claim against You that Your valid use of Anaconda Offering(s) under Your Order infringes a third party's U.S. patent, copyright or U.S. registered trademark (the "IP Claim"). Anaconda wil
l indemnify You against the final judgment entered by a court of competent jurisdiction or any settlements arising out of an IP Claim, provided that You:  (a) promptly notify Anaconda in writing of the IP Claim;  (b) fully cooperate with Anac
onda in the defense of the IP Claim; and (c) grant Anaconda the right to exclusively control the defense and settlement of the IP Claim, and any subsequent appeal. Anaconda will have no obligation to reimburse You for Your attorney fees and c
osts in connection with any IP Claim for which Anaconda is providing defense and indemnification hereunder. You, at Your own expense, may retain Your own legal representation.
10.3 Additional Remedies. If an IP Claim is made and prevents Your exercise of the Usage Rights, Anaconda will either procure for You the right to continue using the Anaconda Offering(s), or replace or modify the Anaconda Offering(s) with fun
ctionality that is non-infringing. Only if Anaconda determines that these alternatives are not reasonably available, Anaconda may terminate Your Usage Rights granted under these TOS upon written notice to You and will refund You a prorated po
rtion of the fee You paid for the Anaconda Offering(s) for the remainder of the unexpired Usage Term.
10.4 Exclusions.  Anaconda has no obligation regarding any IP Claim based on: (a) compliance with any designs, specifications, or requirements You provide or a third party provides; (b) Your modification of any Anaconda Offering(s) or modific
ation by a third party; (c) the amount or duration of use made of the Anaconda Offering(s), revenue You earned, or services You offered; (d) combination, operation, or use of the Anaconda Offering(s) with non-Anaconda products, software or bu
siness processes; (e) Your failure to modify or replace the Anaconda Offering(s) as required by Anaconda; or (f) any Anaconda Offering(s) provided on a no charge, beta or evaluation basis; or (g) your use of the Open Source Software and/or Th
ird Party Services made available to You within the Anaconda Offerings.
10.5 Exclusive Remedy. This Section 9 (Indemnification) states Anaconda's entire obligation and Your exclusive remedy regarding any IP Claim against You.
11. LIMITATION OF LIABILITY
11.1 Limitation of Liability. Neither Party will be liable for indirect, incidental, exemplary, punitive, special or consequential damages; loss or corruption of data or interruption or loss of business; or loss of revenues, profits, goodwill
 or anticipated sales or savings except as a result of violation of Anaconda's Intellectual Property Rights. Except as a result of violation of Anaconda's Intellectual Property Rights, the maximum aggregate liability of each party under these
 TOS is limited to: (a) for claims solely arising from software licensed on a perpetual basis, the fees received by Anaconda for that Offering; or (b) for all other claims, the fees received by Anaconda for the applicable Anaconda Offering an
d attributable to the 12 month period immediately preceding the first claim giving rise to such liability; provided if no fees have been received by Anaconda, the maximum aggregate liability shall be one hundred US dollars ($100). This limita
tion of liability applies whether the claims are in warranty, contract, tort (including negligence), infringement, or otherwise, even if either party has been advised of the possibility of such damages. Nothing in these TOS limits or excludes
 any liability that cannot be limited or excluded under applicable law. This limitation of liability is cumulative and not per incident.
12. FEES & PAYMENT
12.1 Fees. Orders for the Anaconda Offering(s) are non-cancellable. Fees for Your use of an Anaconda Offering are set out in Your Order or similar purchase terms with Your Approved Source. If payment is not received within the specified payme
nt terms, any overdue and unpaid balances will be charged interest at a rate of five percent (5%) per month, charged daily until the balance is paid.
12.2 Billing. You agree to provide us with updated, accurate, and complete billing information, and You hereby authorize Anaconda, either directly or through our payment processing service or our Affiliates, to charge the applicable Fees set 
forth in Your Order via your selected payment method, upon the due date. Unless expressly set forth herein, the Fees are non-cancelable and non-refundable. We reserve the right to change the Fees at any time, upon notice to You if such change
 may affect your existing Subscriptions or other renewable services upon renewal. In the event of failure to collect the Fees You owe, we may, at our sole discretion (but shall not be obligated to), retry to collect at a later time, and/or su
spend or cancel the Account, without notice. If You pay fees by credit card, Anaconda will charge the credit card in accordance with Your Subscription plan. You remain liable for any fees which are rejected by the card issuer or charged back 
to Anaconda.
12.3 Taxes. The Fees are exclusive of any and all taxes (including without limitation, value added tax, sales tax, use tax, excise, goods and services tax, etc.), levies, or duties, which may be imposed in respect of these TOS and the purchas
e or sale, of the Offerings or other services set forth in the Order (the "Taxes"), except for Taxes imposed on our income.
12.4 Payment Through Anaconda Partner. If You purchased an Offering from an Anaconda Partner or other Approved Source, then to the extent there is any conflict between these TOS and any terms of service entered between You and the respective 
Partner, including any purchase order, then, as between You and Anaconda, these TOS shall prevail. Any rights granted to You and/or any of the other Users in a separate agreement with a Partner which are not contained in these TOS, apply only
 in connection vis a vis the Partner.
13. TERM, TERMINATION & SUSPENSION
13.1 Subscription Term. The Offerings are provided on a subscription basis for the term specified in your Order (the "Subscription Term"). The termination or suspension of an individual Order will not terminate or suspend any other Order. If 
these TOS are terminated in whole, all outstanding Order(s) will terminate.
13.2 Subscription Auto-Renewal. To prevent interruption or loss of service when using the Offerings or any Subscription and Support Services will renew automatically, unless You cancel your license to the Offering, Subscription or Support Ser
vices agreement prior to their expiration.
13.3 Termination. If a party materially breaches these TOS and does not cure that breach within 30 days after receipt of written notice of the breach, the non-breaching party may terminate these TOS for cause.  Anaconda may immediately termin
ate your Usage Rights if You breach Section 1 (Access & Use), Section 4 (Open Source, Content & Applications), Section 8 (Ownership & Intellectual Property) or Section 16.10 (Export) or any of the Offering Descriptions.
13.4 Survival. Section 8 (Ownership & Intellectual Property), Section 6.4 (Aggregated Data), Section 9 (Confidential Information), Section 9.3 (Warranty Disclaimer), Section 12 (Limitation of Liability), Section 14 (Term, Termination & Suspen
sion),  obligations to make payment under Section 13 which accrued prior to termination (Fees & Payment), Section 14.4 (Survival), Section 14.5 (Effect of Termination), Section 15 (Records, User Count) and Section 16 (General Provisions) surv
ive termination or expiration of these TOS.
13.5 Effect of Termination. Upon termination of the TOS, You must stop using the Anaconda Offering(s) and destroy any copies of Anaconda Proprietary Technology and Confidential Information within Your control. Upon Anaconda's termination of t
hese TOS for Your material breach, You will pay Anaconda or the Approved Source any unpaid fees through to the end of the then-current Usage Term. If You continue to use or access any Anaconda Offering(s) after termination, Anaconda or the Ap
proved Source may invoice You, and You agree to pay, for such continued use. Anaconda may require evidence of compliance with this Section 13. Upon request, you agree to provide evidence of compliance to Anaconda demonstrating that all propri
etary Anaconda Offering(s) or components thereof have been removed from your systems. Such evidence may be in the form of a system scan report or other similarly detailed method.
13.6 Excessive Usage. We shall have the right to throttle or restrict Your access to the Offerings where we, at our sole discretion, believe that You and/or any of your Authorized Users, have misused the Offerings or otherwise use the Offerin
gs in an excessive manner compared to the anticipated standard use (at our sole discretion) of the Offerings, including, without limitation, excessive network traffic and bandwidth, size and/or length of Content, quality and/or format of Cont
ent, sources of Content, volume of download time, etc.
14. RECORDS, USER COUNT
14.1 Verification Records. During the Usage Term and for a period of thirty six (36) months after its expiry or termination, You will take reasonable steps to maintain complete and accurate records of Your use of the Anaconda Offering(s) suff
icient to verify compliance with these TOS ("Verification Records"). Upon reasonable advance notice, and no more than once per 12 month period unless the prior review showed a breach by You, You will, within thirty (30) days from Anaconda's n
otice, allow Anaconda and/or its auditors access to the Verification Records and any applicable books, systems (including Anaconda product(s) or other equipment), and accounts during Your normal business hours.
14.2 Quarterly User Count. In accordance with the pricing structure stipulated within the relevant Order Form and this Agreement, in instances where the pricing assessment is contingent upon the number of users, Anaconda will conduct a period
ic true-up on  a quarterly basis to ascertain the alignment between the actual number of users utilizing the services and the initially reported user count, and to assess for any unauthorized or noncompliant usage.
14.3 Penalties for Overage or Noncompliant Use.  Should the actual user count exceed the figure initially provided, or unauthorized usage is uncovered, the contracting party shall remunerate the difference to Anaconda, encompassing the additi
onal users or noncompliant use in compliance with Anaconda's then-current pricing terms. The payment for such difference shall be due in accordance with the invoicing and payment provisions specified in these TOS and/or within the relevant Or
der and the Agreement. In the event there is no custom commercial agreement beyond these TOS between You and Anaconda at the time of a true-up pursuant to Section 13.2, and said true-up uncovers unauthorized or noncompliant usage, You will re
munerate Anaconda via a back bill for any fees owed as a result of all unauthorized usage after April of 2020.  Fees may be waived by Anaconda at its discretion.
15. GENERAL PROVISIONS
15.1 Order of Precedence. If there is any conflict between these TOS and any Offering Description expressly referenced in these TOS, the order of precedence is: (a) such Offering Description;  (b) these TOS (excluding the Offering Description
 and any Anaconda policies); then (c) any applicable Anaconda policy expressly referenced in these TOS and any agreement expressly incorporated by reference.  If there is a Custom Agreement, the Custom Agreement shall control over these TOS.
15.2 Entire Agreement. These TOS are the complete agreement between the parties regarding the subject matter of these TOS and supersedes all prior or contemporaneous communications, understandings or agreements (whether written or oral) unles
s a Custom Agreement has been executed where, in such case, the Custom Agreement shall continue in full force and effect and shall control.
15.3 Modifications to the TOS. Anaconda may change these TOS or any of its components by updating these TOS on legal.anaconda.com/terms-of-service. Changes to the TOS apply to any Orders acquired or renewed after the date of modification.
15.4 Third Party Beneficiaries. These TOS do not grant any right or cause of action to any third party.
15.5 Assignment. Anaconda may assign this Agreement to (a) an Affiliate; or (b) a successor or acquirer pursuant to a merger or sale of all or substantially all of such party's assets at any time and without written notice. Subject to the for
egoing, this Agreement will be binding upon and will inure to the benefit of Anaconda and their respective successors and permitted assigns.
15.6 US Government End Users. The Offerings and Documentation are deemed to be "commercial computer software" and "commercial computer software documentation" pursuant to FAR 12.212 and DFARS 227.7202. All US Government end users acquire the 
Offering(s) and Documentation with only those rights set forth in these TOS. Any provisions that are inconsistent with federal procurement regulations are not enforceable against the US Government. In no event shall source code be provided or
 considered to be a deliverable or a software deliverable under these TOS.
15.7 Anaconda Partner Transactions. If You purchase access to an Anaconda Offering from an Anaconda Partner, the terms of these TOS apply to Your use of that Anaconda Offering and prevail over any inconsistent provisions in Your agreement wit
h the Anaconda Partner.
15.8 Children and Minors. If You are under 18 years old, then by entering into these TOS You explicitly stipulate that (i) You have legal capacity to consent to these TOS or Your parent or legal guardian has done so on Your behalf;  (ii) You 
understand the Anaconda Privacy Policy; and (iii) You understand that certain underage users are strictly prohibited from using certain features and functionalities provided by the Anaconda Offering(s). You may not enter into these TOS if You
 are under 13 years old.  Anaconda does not intentionally seek to collect or solicit personal information from individuals under the age of 13. In the event we become aware that we have inadvertently obtained personal information from a child
 under the age of 13 without appropriate parental consent, we shall expeditiously delete such information. If applicable law allows the utilization of an Offering with parental consent, such consent shall be demonstrated in accordance with th
e prescribed process outlined by Anaconda's Privacy Policy for obtaining parental approval.
15.9 Compliance with Laws.  Each party will comply with all laws and regulations applicable to their respective obligations under these TOS.
15.10 Export. The Anaconda Offerings are subject to U.S. and local export control and sanctions laws. You acknowledge and agree to the applicability of and Your compliance with those laws, and You will not receive, use, transfer, export or re
-export any Anaconda Offerings in a way that would cause Anaconda to violate those laws. You also agree to obtain any required licenses or authorizations.  Without limiting the foregoing, You may not acquire Offerings if: (1) you are in, unde
r the control of, or a national or resident of Cuba, Iran, North Korea, Sudan or Syria or if you are on the U.S. Treasury Department's Specially Designated Nationals List or the U.S. Commerce Department's Denied Persons List, Unverified List 
or Entity List or (2) you intend to supply the acquired goods, services or software to Cuba, Iran, North Korea, Sudan or Syria (or a national or resident of one of these countries) or to a person on the Specially Designated Nationals List, De
nied Persons List, Unverified List or Entity List.
15.11 Governing Law and Venue. THESE TOS, AND ANY DISPUTES ARISING FROM THEM, WILL BE GOVERNED EXCLUSIVELY BY THE GOVERNING LAW OF DELAWARE AND WITHOUT REGARD TO CONFLICTS OF LAWS RULES OR THE UNITED NATIONS CONVENTION ON THE INTERNATIONAL SA
LE OF GOODS. EACH PARTY CONSENTS AND SUBMITS TO THE EXCLUSIVE JURISDICTION OF COURTS LOCATED WITHIN THE STATE OF DELAWARE.  EACH PARTY DOES HEREBY WAIVE HIS/HER/ITS RIGHT TO A TRIAL BY JURY, TO PARTICIPATE AS THE MEMBER OF A CLASS IN ANY PURP
ORTED CLASS ACTION OR OTHER PROCEEDING OR TO NAME UNNAMED MEMBERS IN ANY PURPORTED CLASS ACTION OR OTHER PROCEEDINGS. You acknowledge that any violation of the requirements under Section 4 (Ownership & Intellectual Property) or Section 7 (Con
fidential Information) may cause irreparable damage to Anaconda and that Anaconda will be entitled to seek injunctive and other equitable or legal relief to prevent or compensate for such unauthorized use.
15.12 California Residents. If you are a California resident, in accordance with Cal. Civ. Code subsection 1789.3, you may report complaints to the Complaint Assistance Unit of the Division of Consumer Services of the California Department of
 Consumer Affairs by contacting them in writing at 1625 North Market Blvd., Suite N 112, Sacramento, CA 95834, or by telephone at (800) 952-5210.
15.13 Notices. Any notice delivered by Anaconda to You under these TOS will be delivered via email, regular mail or postings on www.anaconda.com. Notices to Anaconda should be sent to Anaconda, Inc., Attn: Legal at 1108 Lavaca Street, Suite 1
10-645 Austin, TX 78701 and legal@anaconda.com.
15.14 Publicity. Anaconda reserves the right to reference You as a customer and display your logo and name on our website and other promotional materials for marketing purposes. Any display of your logo and name shall be in compliance with Yo
ur branding guidelines, if provided  by notice pursuant to Section 14.12 by You. Except as provided in this Section 14.13 or by separate mutual written agreement, neither party will use the logo, name or trademarks of the other party or refer
 to the other party in any form of publicity or press release without such party's prior written approval.
15.15 Force Majeure. Except for payment obligations, neither Party will be responsible for failure to perform its obligations due to an event or circumstances beyond its reasonable control.
15.16 No Waiver; Severability. Failure by either party to enforce any right under these TOS will not waive that right. If any portion of these TOS are not enforceable, it will not affect any other terms.
15.17 Electronic Signatures.  IF YOUR ACCEPTANCE OF THESE TERMS FURTHER EVIDENCED BY YOUR AFFIRMATIVE ASSENT TO THE SAME (E.G., BY A "CHECK THE BOX" ACKNOWLEDGMENT PROCEDURE), THEN THAT AFFIRMATIVE ASSENT IS THE EQUIVALENT OF YOUR ELECTRONIC 
SIGNATURE TO THESE TERMS.  HOWEVER, FOR THE AVOIDANCE OF DOUBT, YOUR ELECTRONIC SIGNATURE IS NOT REQUIRED TO EVIDENCE OR FACILITATE YOUR ACCEPTANCE AND AGREEMENT TO THESE TERMS, AS YOU AGREE THAT THE CONDUCT DESCRIBED IN THESE TOS AS RELATING
 TO YOUR ACCEPTANCE AND AGREEMENT TO THESE TERMS ALONE SUFFICES.
16. DEFINITIONS
"Affiliate" means any corporation or legal entity that directly or indirectly controls, or is controlled by, or is under common control with the relevant party, where "control" means to: (a) own more than 50% of the relevant party; or (b) be 
able to direct the affairs of the relevant party through any lawful means (e.g., a contract that allows control).
"Anaconda" "we" "our" or "us" means Anaconda, Inc. or its applicable Affiliate(s).
"Anaconda Content" means any:  Anaconda Content includes geographic and domain information, rules, signatures, threat intelligence and data feeds and Anaconda's compilation of suspicious URLs.
"Anaconda Partner" or "Partner" means an Anaconda authorized reseller, distributor or systems integrator authorized by Anaconda to sell Anaconda Offerings.
"Anaconda Offering" or "Offering" means the Anaconda Services, Anaconda software, Documentation, software development kits ("SDKs"), application programming interfaces ("APIs"), and any other items or services provided by Anaconda any Upgrade
s thereto under the terms of these TOS, the relevant Offering Descriptions, as identified in the relevant Order, and/or any updates thereto.
"Anaconda Proprietary Technology" means any software, code, tools, libraries, scripts, APIs, SDKs, templates, algorithms, data science recipes (including any source code for data science recipes and any modifications to such source code), dat
a science workflows, user interfaces, links, proprietary methods and systems, know-how, trade secrets, techniques, designs, inventions, and other tangible or intangible technical material, information and works of authorship underlying or oth
erwise used to make available the Anaconda Offerings including, without limitation, all Intellectual Property Rights therein and thereto.
"Anaconda Service" means Support Services and any other consultation or professional services provided by or on behalf of Anaconda under the terms of the Agreement, as identified in the applicable Order and/or SOW.
"Approved Source" means Anaconda or an Anaconda Partner.
"Anonymized Data" means any Personal Data (including Customer Personal Data) and data regarding usage trends and behavior with respect to Offerings, that has been anonymized such that the Data Subject to whom it relates cannot be identified, 
directly or indirectly, by Anaconda or any other party reasonably likely to receive or access that anonymized Personal Data or usage trends and behavior.
"Authorized Users" means Your Users, Your Affiliates who have been identified to Anaconda and approved, Your third-party service providers, and each of their respective Users who are permitted to access and use the Anaconda Offering(s) on You
r behalf as part of Your Order.
"Beta Offerings" Beta Offerings means any portion of the Offerings offered on a "beta" basis, as designated by Anaconda, including but not limited to, products, plans, services, and platforms.
"Content" means Packages, components, applications, services, data, content, or resources, which are available for download access or use through the Offerings, and owned by third-party providers, defined herein as Third Party Content, or Ana
conda, defined herein as Anaconda Content.
"Documentation" means the technical specifications and usage materials officially published by Anaconda specifying the functionalities and capabilities of the applicable Anaconda Offerings.
"Educational Entities" means educational organizations, classroom learning environments, or academic instructional organizations.
"Fees" mean the costs and fees for the Anaconda Offerings(s) set forth within the Order and/or SOW, or any fees due immediately when purchasing via the web-portal.
"Government Entities" means any body, board, department, commission, court, tribunal, authority, agency or other instrumentality of any such government or otherwise exercising any executive, legislative, judicial, administrative or regulatory
 functions of any Federal, State, or local government (including multijurisdictional agencies, instrumentalities, and entities of such government)
"Internal Use" means Customer's use of an Offering for Customer's own internal operations, to perform Python/R data science and machine learning on a single platform from Customer's systems, networks, and devices. Such use does not include us
e on a service bureau basis or otherwise to provide services to, or process data for, any third party, or otherwise use to monitor or service the systems, networks, and devices of third parties.
"Intellectual Property Rights" means any and all now known or hereafter existing worldwide: (a) rights associated with works of authorship, including copyrights, mask work rights, and moral rights; (b) trademark or service mark rights; (c) Co
nfidential Information, including trade secret rights; (d) patents, patent rights, and industrial property rights; (e) layout design rights, design rights, and other proprietary rights of every kind and nature other than trade dress, and simi
lar rights; and (f) all registrations, applications, renewals, extensions, or reissues of the foregoing.
"Malicious Code" means code designed or intended to disable or impede the normal operation of, or provide unauthorized access to, networks, systems, Software or Cloud Services other than as intended by the Anaconda Offerings (for example, as 
part of some of Anaconda's Security Offering(s).
"Mirror" or "Mirroring" means the unauthorized or authorized act of duplicating, copying, or replicating an Anaconda Offering,  (e.g. repository, including its contents, files, and data),, from Anaconda's servers to another location. If Mirro
ring is not performed under a site license, or by written authorization by Anaconda, the Mirroring constitutes a violation of Anaconda's Terms of Service and licensing agreements.
"Offering Description"' means a legally structured and detailed description outlining the features, specifications, terms, and conditions associated with a particular product, service, or offering made available to customers or users. The Off
ering Description serves as a legally binding document that defines the scope of the offering, including pricing, licensing terms, usage restrictions, and any additional terms and conditions.
"Order" or "Order Form"  means a legally binding document, website page, or electronic mail that outlines the specific details of Your purchase of Anaconda Offerings or Anaconda Services, including but not limited to product specifications, p
ricing, quantities, and payment terms either issued by Anaconda or from an Approved Source.
"Personal Data" Refers to information falling within the definition of 'personal data' and/or 'personal information' as outlined by Relevant Data Protection Regulations, such as a personal identifier (e.g., name, last name, and email), financ
ial information (e.g., bank account numbers) and online identifiers (e.g., IP addresses, geolocation.
"Relevant Data Protection Regulations" mean, as applicable, (a) Personal Information Protection and Electronic Documents Act (S.C. 2000, c. 5) along with any supplementary or replacement bills enacted into law by the Government of Canada (col
lectively "PIPEDA"); (b) the General Data Protection Regulation (Regulation (EU) 2016/679) and applicable laws by EU member states which either supplement or are necessary to implement the GDPR (collectively "GDPR"); (c) the California Consum
er Privacy Act of 2018 (Cal. Civ. Code subsection 1798.198(a)), along with its various amendments (collectively "CCPA"); (d) the GDPR as applicable under section 3 of the European Union (Withdrawal) Act 2018 and as amended by the Data Protect
ion, Privacy and Electronic Communications (Amendments etc.) (EU Exit) Regulations 2019 (as amended) (collectively "UK GDPR"); (e) the Swiss Federal Act on Data Protection  of June 19, 1992 and as it may be revised from time to time (the "FAD
P"); and (f) any other applicable law related to the protection of Personal Data.
"Site License'' means a License that confers Customer the right to use Anaconda Offerings throughout an organization, encompassing authorized Users without requiring individual licensing arrangements. Site Licenses have limits based on compan
y size as set forth in a relevant Order, and do not cover future assignment of Users through mergers and acquisitions unless otherwise specified in writing by Anaconda.
"Software" means the Anaconda Offerings, including Upgrades, firmware, and applicable Documentation.
"Subscription" means the payment of recurring Fees for accessing and using Anaconda's Software and/or an Anaconda Service over a specified period. Your subscription grants you the right to utilize our products, receive updates, and access sup
port, all in accordance with our terms and conditions for such Offering.
"Subscription Fees" means the costs and Fees associated with a Subscription.
"Support Services" means the support and maintenance services provided by Anaconda to You in accordance with the relevant support and maintenance policy ("Support Policy") located at legal.anaconda.com/support-policy.
"Third Party Services" means external products, applications, or services provided by entities other than Anaconda. These services may be integrated with or used in conjunction with Anaconda's offerings but are not directly provided or contro
lled by Anaconda.
"Upgrades" means all updates, upgrades, bug fixes, error corrections, enhancements and other modifications to the Software.
"Usage Term" means the period commencing on the date of delivery and continuing until expiration or termination of the Order, during which period You have the right to use the applicable Anaconda Offering.
"User"  means the individual, system (e.g. virtual machine, automated system, server-side container, etc.) or organization that (a) has visited, downloaded or used the Offerings(s), (b) is using the Offering or any part of the Offerings(s), o
r (c) directs the use of the Offerings(s) in the performance of its functions.
"Version" means the Offering configuration identified by a numeric representation, whether left or right of the decimal place.
OFFERING DESCRIPTION: MINICONDA
This Offering Description describes the Anaconda Premium Repository (hereinafter the "Premium Repository"). Your use of the Premium Repository is governed by this Offering Description, and the Anaconda Terms of Service (the "TOS", available a
t www.anaconda.com/legal), collectively the "Agreement" between you ("You") and Anaconda, Inc. ("We" or "Anaconda"). In the event of a conflict, the order of precedence is as follows: 1) this Offering Description; 2) if applicable, a Custom A
greement; and 3) the TOS if no Custom Agreement is in place. Capitalized terms used in this Offering Description and/or the Order not otherwise defined herein, including in Section 6 (Definitions), have the meaning given to them in the TOS or
 Custom Agreement, as applicable. Anaconda may, at any time, terminate this Agreement and the license granted hereunder if you fail to comply with any term of this Agreement. Anaconda reserves all rights not expressly granted to you in this A
greement.
1. Miniconda. In order to access some features and functionalities of Business, You may need to first download and install Miniconda.
2. Copyright Notice. Miniconda(R) (C) 2015-2024, Anaconda, Inc. All rights reserved under the 3-clause BSD License.
3. License Grant. Subject to the terms of this Agreement, Anaconda hereby grants You a non-exclusive, non-transferable license to: (1) Install and use Miniconda(R); (2) Modify and create derivative works of sample source code delivered in Min
iconda(R) subject to the Anaconda Terms of Service (available at https://legal.anaconda.com/policies/en/?name=terms-of-service); and (3) Redistribute code files in source (if provided to You by Anaconda as source) and binary forms, with or wi
thout modification subject to the requirements set forth below.
4. Updates. Anaconda may, at its option, make available patches, workarounds or other updates to Miniconda(R). Unless the updates are provided with their separate governing terms, they are deemed part of Miniconda(R) licensed to You as provid
ed in this Agreement.
5. Support. This Agreement does not entitle You to any support for Miniconda(R).
6. Redistribution. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: (1) Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer; (2) Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the 
distribution.
7. Intellectual Property Notice. You acknowledge that, as between You and Anaconda, Anaconda owns all right, title, and interest, including all intellectual property rights, in and to Miniconda(R) and, with respect to third-party products dis
tributed with or through Miniconda(R), the applicable third-party licensors own all right, title and interest, including all intellectual property rights, in and to such products.
Do you accept the license terms? [yes|no]
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> 
Please answer 'yes' or 'no':'
>>> yes
Miniconda3 will now be installed into this location:
/home/kevinfang/miniconda3
  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below
[/home/kevinfang/miniconda3] >>> 
PREFIX=/home/kevinfang/miniconda3
Unpacking payload ...
                                                                                                                                                                                                                                                  
Installing base environment...
Downloading and Extracting Packages:
## Package Plan ##
  environment location: /home/kevinfang/miniconda3
  added / updated specs:
    - defaults/linux-64::_libgcc_mutex==0.1=main[md5=c3473ff8bdb3d124ed5ff11ec380d6f9]
    - defaults/linux-64::_openmp_mutex==5.1=1_gnu[md5=71d281e9c2192cb3fa425655a8defb85]
    - defaults/linux-64::anaconda-anon-usage==0.4.4=py312hfc0e8ea_100[md5=97f7e102a7075404bbcb7e801b260e3a]
    - defaults/linux-64::boltons==23.0.0=py312h06a4308_0[md5=36d464442713fc92897b7da029a08fb6]
    - defaults/linux-64::brotli-python==1.0.9=py312h6a678d5_8[md5=e6bdf1f9e8e1ad3543aaec7e9ecea7e7]
    - defaults/linux-64::bzip2==1.0.8=h5eee18b_6[md5=f21a3ff51c1b271977f53ce956a69297]
    - defaults/linux-64::c-ares==1.19.1=h5eee18b_0[md5=6cfbce52273a1cb888821f18ceaa83c4]
    - defaults/linux-64::ca-certificates==2024.9.24=h06a4308_0[md5=e4369d7b4b0707ee0765794d14710e2e]
    - defaults/linux-64::certifi==2024.8.30=py312h06a4308_0[md5=42ef53b6872f15913c0d7d702ec7475e]
    - defaults/linux-64::cffi==1.17.1=py312h1fdaa30_0[md5=8472aea146fecf25898d67adea2ddbf8]
    - defaults/linux-64::conda-content-trust==0.2.0=py312h06a4308_1[md5=fdcf7a04d9cc833ea3f397a414010206]
    - defaults/linux-64::conda-package-handling==2.3.0=py312h06a4308_0[md5=230372bd2a09fbe75dc99c655f671e04]
    - defaults/linux-64::conda-package-streaming==0.10.0=py312h06a4308_0[md5=4801fce7f441672d195966cf23a12186]
    - defaults/linux-64::conda==24.9.2=py312h06a4308_0[md5=4c35348e64d09d83ce731fbbe9018b26]
    - defaults/linux-64::cryptography==43.0.0=py312hdda0065_0[md5=76ab63809027e6311b6aa8b4f922ddcf]
    - defaults/linux-64::distro==1.9.0=py312h06a4308_0[md5=71b90a563af005b336c976cc9466221c]
    - defaults/linux-64::expat==2.6.3=h6a678d5_0[md5=5e184279ccb8b85331093305cb548f5c]
    - defaults/linux-64::fmt==9.1.0=hdb19cb5_1[md5=4f12930203ff2d84df5d287af9b29858]
    - defaults/linux-64::frozendict==2.4.2=py312h06a4308_0[md5=76ae0259102a2156cc0e1ff9ada0f2c6]
    - defaults/linux-64::icu==73.1=h6a678d5_0[md5=6d09df641fc23f7d277a04dc7ea32dd4]
    - defaults/linux-64::idna==3.7=py312h06a4308_0[md5=03cc59cdabff44c47be0fadffcef003c]
    - defaults/linux-64::jsonpatch==1.33=py312h06a4308_1[md5=c3de52aaf670064f85106ddb32d720d9]
    - defaults/linux-64::krb5==1.20.1=h143b758_1[md5=cf1accc86321fa25d6b978cc748039ae]
    - defaults/linux-64::ld_impl_linux-64==2.40=h12ee557_0[md5=ee672b5f635340734f58d618b7bca024]
    - defaults/linux-64::libarchive==3.7.4=hfab0078_0[md5=fcc6a63f95a80a5d2ff9d3e208e9a638]
    - defaults/linux-64::libcurl==8.9.1=h251f7ec_0[md5=8133d8f19e8136a10f9f81180026c859]
    - defaults/linux-64::libedit==3.1.20230828=h5eee18b_0[md5=850eb5a9d2d7d3c66cce12e84406ca08]
    - defaults/linux-64::libev==4.33=h7f8727e_1[md5=5065620db4393fb549f30114a33897d1]
    - defaults/linux-64::libffi==3.4.4=h6a678d5_1[md5=70646cc713f0c43926cfdcfe9b695fe0]
    - defaults/linux-64::libgcc-ng==11.2.0=h1234567_1[md5=a87728dabf3151fb9cfa990bd2eb0464]
    - defaults/linux-64::libgomp==11.2.0=h1234567_1[md5=b372c0eea9b60732fdae4b817a63c8cd]
    - defaults/linux-64::libmamba==1.5.8=hfe524e5_3[md5=cf9c3aa352a0d48f9dc0b5a0222f3065]
    - defaults/linux-64::libmambapy==1.5.8=py312h2dafd23_3[md5=e1345dac45e08fef865200a7f57c2429]
    - defaults/linux-64::libnghttp2==1.57.0=h2d74bed_0[md5=674871621300f54e7ffcf93e6e341638]
    - defaults/linux-64::libsolv==0.7.24=he621ea3_1[md5=c22067963515e7a8d27a5a222a48d870]
    - defaults/linux-64::libssh2==1.11.0=h251f7ec_0[md5=ce46cf257d73fe85c18c78597196f0d8]
    - defaults/linux-64::libstdcxx-ng==11.2.0=h1234567_1[md5=57623d10a70e09e1d048c2b2b6f4e2dd]
    - defaults/linux-64::libuuid==1.41.5=h5eee18b_0[md5=4a6a2354414c9080327274aa514e5299]
    - defaults/linux-64::libxml2==2.13.1=hfdd30dd_2[md5=193c6940cccb654f7c543b0f680dc0b9]
    - defaults/linux-64::lz4-c==1.9.4=h6a678d5_1[md5=2ee58861f2b92b868ce761abb831819d]
    - defaults/linux-64::menuinst==2.1.2=py312h06a4308_0[md5=dea01dc88eee0a74dc9d982144b93371]
    - defaults/linux-64::ncurses==6.4=h6a678d5_0[md5=5558eec6e2191741a92f832ea826251c]
    - defaults/linux-64::openssl==3.0.15=h5eee18b_0[md5=019e501b69841c6d4aeaef3b8619a678]
    - defaults/linux-64::packaging==24.1=py312h06a4308_0[md5=756ec42d4f934b642b8476689af2781f]
    - defaults/linux-64::pcre2==10.42=hebb0a14_1[md5=727e15c3cfa02b032da4eb0c1123e977]
    - defaults/linux-64::pip==24.2=py312h06a4308_0[md5=798cbea8112672434d0cd7551f8fc4b9]
    - defaults/linux-64::platformdirs==3.10.0=py312h06a4308_0[md5=39dc9eb538e73250dadcdec7a8ed6595]
    - defaults/linux-64::pluggy==1.0.0=py312h06a4308_1[md5=65e3925b7c284b6a111d8971cac0d0c7]
    - defaults/linux-64::pycosat==0.6.6=py312h5eee18b_1[md5=4ccf6371e1ccb1ccbecac26ab4fd1607]
    - defaults/linux-64::pysocks==1.7.1=py312h06a4308_0[md5=8efb8494277b7f0faedf9d437b23cbe1]
    - defaults/linux-64::python==3.12.7=h5148396_0[md5=268d2cb6563a9bcb77afd31721d330c2]
    - defaults/linux-64::readline==8.2=h5eee18b_0[md5=be42180685cce6e6b0329201d9f48efb]
    - defaults/linux-64::reproc-cpp==14.2.4=h6a678d5_2[md5=b03aa4903158279f003e7032ab9f5601]
    - defaults/linux-64::reproc==14.2.4=h6a678d5_2[md5=3c6dbc6c60b3897222d79359343e90fa]
    - defaults/linux-64::requests==2.32.3=py312h06a4308_0[md5=a321cefcf9b6681a45418d5adf647d80]
    - defaults/linux-64::ruamel.yaml.clib==0.2.8=py312h5eee18b_0[md5=4e151915d3acb78754b5cd1be029fcd2]
    - defaults/linux-64::ruamel.yaml==0.18.6=py312h5eee18b_0[md5=b4817fd05fdab4ce718bf1e7aab55f75]
    - defaults/linux-64::setuptools==75.1.0=py312h06a4308_0[md5=c96d08a405d335f2b0200c0f281b1fdc]
    - defaults/linux-64::sqlite==3.45.3=h5eee18b_0[md5=acf93d6aceb74d6110e20b44cc45939e]
    - defaults/linux-64::tk==8.6.14=h39e8969_0[md5=78dbc5e3c69143ebc037fc5d5b22e597]
    - defaults/linux-64::tqdm==4.66.5=py312he106c6f_0[md5=099959333950bef1a3d7d12133cbfafc]
    - defaults/linux-64::truststore==0.8.0=py312h06a4308_0[md5=ad93bd626fc17c1606394fe258b4ed18]
    - defaults/linux-64::urllib3==2.2.3=py312h06a4308_0[md5=08b5f80f188ed801e9f463124a481289]
    - defaults/linux-64::wheel==0.44.0=py312h06a4308_0[md5=6d495438dd44e8f16b1a05d0a8648644]
    - defaults/linux-64::xz==5.4.6=h5eee18b_1[md5=1562802f843297ee776a50b9329597ed]
    - defaults/linux-64::yaml-cpp==0.8.0=h6a678d5_1[md5=015d2d74ad3c8e53eec3358637433718]
    - defaults/linux-64::zlib==1.2.13=h5eee18b_1[md5=92e42d8310108b0a440fb2e60b2b2a25]
    - defaults/linux-64::zstandard==0.23.0=py312h2c38b39_0[md5=6128bfbcbc551afe6cad2af1c8493a1c]
    - defaults/linux-64::zstd==1.5.6=hc292b87_0[md5=78ae7abd3020b41f827b35085845e1b8]
    - defaults/noarch::archspec==0.2.3=pyhd3eb1b0_0[md5=13d01ee2d343d8539bb47055a6c0b5b2]
    - defaults/noarch::charset-normalizer==3.3.2=pyhd3eb1b0_0[md5=c6fea3691e85cf7f568b0618ec29fc4f]
    - defaults/noarch::conda-libmamba-solver==24.9.0=pyhd3eb1b0_0[md5=251a69a5bf578ef59fdf8255c7c25c5d]
    - defaults/noarch::jsonpointer==2.1=pyhd3eb1b0_0[md5=298ff809e733cb04366e4e629c65aa8d]
    - defaults/noarch::pybind11-abi==5=hd3eb1b0_0[md5=7f0df6639fdf60ccd3045ee6faedd32f]
    - defaults/noarch::pycparser==2.21=pyhd3eb1b0_0[md5=135a72ff2a31150a3a3ff0b1edd41ca9]
    - defaults/noarch::tzdata==2024b=h04d1e81_0[md5=9be694715c6a65f9631bb1b242125e9d]
The following NEW packages will be INSTALLED:
  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  anaconda-anon-usa~ pkgs/main/linux-64::anaconda-anon-usage-0.4.4-py312hfc0e8ea_100 
  archspec           pkgs/main/noarch::archspec-0.2.3-pyhd3eb1b0_0 
  boltons            pkgs/main/linux-64::boltons-23.0.0-py312h06a4308_0 
  brotli-python      pkgs/main/linux-64::brotli-python-1.0.9-py312h6a678d5_8 
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_6 
  c-ares             pkgs/main/linux-64::c-ares-1.19.1-h5eee18b_0 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.9.24-h06a4308_0 
  certifi            pkgs/main/linux-64::certifi-2024.8.30-py312h06a4308_0 
  cffi               pkgs/main/linux-64::cffi-1.17.1-py312h1fdaa30_0 
  charset-normalizer pkgs/main/noarch::charset-normalizer-3.3.2-pyhd3eb1b0_0 
  conda              pkgs/main/linux-64::conda-24.9.2-py312h06a4308_0 
  conda-content-tru~ pkgs/main/linux-64::conda-content-trust-0.2.0-py312h06a4308_1 
  conda-libmamba-so~ pkgs/main/noarch::conda-libmamba-solver-24.9.0-pyhd3eb1b0_0 
  conda-package-han~ pkgs/main/linux-64::conda-package-handling-2.3.0-py312h06a4308_0 
  conda-package-str~ pkgs/main/linux-64::conda-package-streaming-0.10.0-py312h06a4308_0 
  cryptography       pkgs/main/linux-64::cryptography-43.0.0-py312hdda0065_0 
  distro             pkgs/main/linux-64::distro-1.9.0-py312h06a4308_0 
  expat              pkgs/main/linux-64::expat-2.6.3-h6a678d5_0 
  fmt                pkgs/main/linux-64::fmt-9.1.0-hdb19cb5_1 
  frozendict         pkgs/main/linux-64::frozendict-2.4.2-py312h06a4308_0 
  icu                pkgs/main/linux-64::icu-73.1-h6a678d5_0 
  idna               pkgs/main/linux-64::idna-3.7-py312h06a4308_0 
  jsonpatch          pkgs/main/linux-64::jsonpatch-1.33-py312h06a4308_1 
  jsonpointer        pkgs/main/noarch::jsonpointer-2.1-pyhd3eb1b0_0 
  krb5               pkgs/main/linux-64::krb5-1.20.1-h143b758_1 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.40-h12ee557_0 
  libarchive         pkgs/main/linux-64::libarchive-3.7.4-hfab0078_0 
  libcurl            pkgs/main/linux-64::libcurl-8.9.1-h251f7ec_0 
  libedit            pkgs/main/linux-64::libedit-3.1.20230828-h5eee18b_0 
  libev              pkgs/main/linux-64::libev-4.33-h7f8727e_1 
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1 
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1 
  libmamba           pkgs/main/linux-64::libmamba-1.5.8-hfe524e5_3 
  libmambapy         pkgs/main/linux-64::libmambapy-1.5.8-py312h2dafd23_3 
  libnghttp2         pkgs/main/linux-64::libnghttp2-1.57.0-h2d74bed_0 
  libsolv            pkgs/main/linux-64::libsolv-0.7.24-he621ea3_1 
  libssh2            pkgs/main/linux-64::libssh2-1.11.0-h251f7ec_0 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1 
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  libxml2            pkgs/main/linux-64::libxml2-2.13.1-hfdd30dd_2 
  lz4-c              pkgs/main/linux-64::lz4-c-1.9.4-h6a678d5_1 
  menuinst           pkgs/main/linux-64::menuinst-2.1.2-py312h06a4308_0 
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0 
  openssl            pkgs/main/linux-64::openssl-3.0.15-h5eee18b_0 
  packaging          pkgs/main/linux-64::packaging-24.1-py312h06a4308_0 
  pcre2              pkgs/main/linux-64::pcre2-10.42-hebb0a14_1 
  pip                pkgs/main/linux-64::pip-24.2-py312h06a4308_0 
  platformdirs       pkgs/main/linux-64::platformdirs-3.10.0-py312h06a4308_0 
  pluggy             pkgs/main/linux-64::pluggy-1.0.0-py312h06a4308_1 
  pybind11-abi       pkgs/main/noarch::pybind11-abi-5-hd3eb1b0_0 
  pycosat            pkgs/main/linux-64::pycosat-0.6.6-py312h5eee18b_1 
  pycparser          pkgs/main/noarch::pycparser-2.21-pyhd3eb1b0_0 
  pysocks            pkgs/main/linux-64::pysocks-1.7.1-py312h06a4308_0 
  python             pkgs/main/linux-64::python-3.12.7-h5148396_0 
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0 
  reproc             pkgs/main/linux-64::reproc-14.2.4-h6a678d5_2 
  reproc-cpp         pkgs/main/linux-64::reproc-cpp-14.2.4-h6a678d5_2 
  requests           pkgs/main/linux-64::requests-2.32.3-py312h06a4308_0 
  ruamel.yaml        pkgs/main/linux-64::ruamel.yaml-0.18.6-py312h5eee18b_0 
  ruamel.yaml.clib   pkgs/main/linux-64::ruamel.yaml.clib-0.2.8-py312h5eee18b_0 
  setuptools         pkgs/main/linux-64::setuptools-75.1.0-py312h06a4308_0 
  sqlite             pkgs/main/linux-64::sqlite-3.45.3-h5eee18b_0 
  tk                 pkgs/main/linux-64::tk-8.6.14-h39e8969_0 
  tqdm               pkgs/main/linux-64::tqdm-4.66.5-py312he106c6f_0 
  truststore         pkgs/main/linux-64::truststore-0.8.0-py312h06a4308_0 
  tzdata             pkgs/main/noarch::tzdata-2024b-h04d1e81_0 
  urllib3            pkgs/main/linux-64::urllib3-2.2.3-py312h06a4308_0 
  wheel              pkgs/main/linux-64::wheel-0.44.0-py312h06a4308_0 
  xz                 pkgs/main/linux-64::xz-5.4.6-h5eee18b_1 
  yaml-cpp           pkgs/main/linux-64::yaml-cpp-0.8.0-h6a678d5_1 
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_1 
  zstandard          pkgs/main/linux-64::zstandard-0.23.0-py312h2c38b39_0 
  zstd               pkgs/main/linux-64::zstd-1.5.6-hc292b87_0 
Downloading and Extracting Packages:
Preparing transaction: done
Executing transaction: done
installation finished.
WARNING:
    You currently have a PYTHONPATH environment variable set. This may cause
    unexpected behavior when running the Python interpreter in Miniconda3.
    For best results, please verify that your PYTHONPATH only points to
    directories of packages that are compatible with the Python interpreter
    in Miniconda3: /home/kevinfang/miniconda3
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:
conda config --set auto_activate_base false
You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>> yes
no change     /home/kevinfang/miniconda3/condabin/conda
no change     /home/kevinfang/miniconda3/bin/conda
no change     /home/kevinfang/miniconda3/bin/conda-env
no change     /home/kevinfang/miniconda3/bin/activate
no change     /home/kevinfang/miniconda3/bin/deactivate
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.sh
no change     /home/kevinfang/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/kevinfang/miniconda3/shell/condabin/Conda.psm1
no change     /home/kevinfang/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/kevinfang/miniconda3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.csh
no change     /home/kevinfang/.bashrc
No action taken.
Thank you for installing Miniconda3!
kevinfang@groq-r01-gn-04:~$ export PYTHON_VERSION=3.10.12
kevinfang@groq-r01-gn-04:~$ conda create -n groqflow python=$PYTHON_VERSION -y
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done
## Package Plan ##
  environment location: /home/kevinfang/miniconda3/envs/groqflow
  added / updated specs:
    - python=3.10.12
The following packages will be downloaded:
    package                    |            build
    ---------------------------|-----------------
    pip-24.2                   |  py310h06a4308_0         2.3 MB
    python-3.10.12             |       h955ad1f_0        26.8 MB
    setuptools-75.1.0          |  py310h06a4308_0         1.7 MB
    wheel-0.44.0               |  py310h06a4308_0         109 KB
    ------------------------------------------------------------
                                           Total:        30.9 MB
The following NEW packages will be INSTALLED:
  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_6 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.9.24-h06a4308_0 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.40-h12ee557_0 
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1 
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1 
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0 
  openssl            pkgs/main/linux-64::openssl-3.0.15-h5eee18b_0 
  pip                pkgs/main/linux-64::pip-24.2-py310h06a4308_0 
  python             pkgs/main/linux-64::python-3.10.12-h955ad1f_0 
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0 
  setuptools         pkgs/main/linux-64::setuptools-75.1.0-py310h06a4308_0 
  sqlite             pkgs/main/linux-64::sqlite-3.45.3-h5eee18b_0 
  tk                 pkgs/main/linux-64::tk-8.6.14-h39e8969_0 
  tzdata             pkgs/main/noarch::tzdata-2024b-h04d1e81_0 
  wheel              pkgs/main/linux-64::wheel-0.44.0-py310h06a4308_0 
  xz                 pkgs/main/linux-64::xz-5.4.6-h5eee18b_1 
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_1 
Downloading and Extracting Packages:
                                                                                                                                                                                                                                                  
Preparing transaction: done                                                                                                                                                                                                                       
Verifying transaction: done                                                                                                                                                                                                                       
Executing transaction: done                                                                                                                                                                                                                       
#
# To activate this environment, use
#
#     $ conda activate groqflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate
kevinfang@groq-r01-gn-04:~$ conda activate groqflow
CondaError: Run 'conda init' before 'conda activate'
kevinfang@groq-r01-gn-04:~$ conda init
no change     /home/kevinfang/miniconda3/condabin/conda
no change     /home/kevinfang/miniconda3/bin/conda
no change     /home/kevinfang/miniconda3/bin/conda-env
no change     /home/kevinfang/miniconda3/bin/activate
no change     /home/kevinfang/miniconda3/bin/deactivate
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.sh
no change     /home/kevinfang/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/kevinfang/miniconda3/shell/condabin/Conda.psm1
no change     /home/kevinfang/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/kevinfang/miniconda3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.csh
no change     /home/kevinfang/.bashrc
No action taken.
kevinfang@groq-r01-gn-04:~$ vim /home/kevinfang/.bashrc
kevinfang@groq-r01-gn-04:~$ conda init
no change     /home/kevinfang/miniconda3/condabin/conda
no change     /home/kevinfang/miniconda3/bin/conda
no change     /home/kevinfang/miniconda3/bin/conda-env
no change     /home/kevinfang/miniconda3/bin/activate
no change     /home/kevinfang/miniconda3/bin/deactivate
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.sh
no change     /home/kevinfang/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/kevinfang/miniconda3/shell/condabin/Conda.psm1
no change     /home/kevinfang/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/kevinfang/miniconda3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/kevinfang/miniconda3/etc/profile.d/conda.csh
modified      /home/kevinfang/.bashrc
==> For changes to take effect, close and re-open your current shell. <==
kevinfang@groq-r01-gn-04:~$ exit
logout
Connection to groq-r01-gn-04.ai.alcf.anl.gov closed.
(base) kevinfang@groq-login-02:~$ ssh groq-r01-gn-04.ai.alcf.anl.gov
---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-107-generic x86_64)
 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.
To restore this content, you can run the 'unminimize' command.
New release '24.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.
-----------------------------------------------------------------------------
                           Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
-----------------------------------------------------------------------------
Last login: Sun Nov 24 00:43:29 2024 from groq-login-02.ai.alcf.anl.gov
-----------------------------------------------------------------------------
                           Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
-----------------------------------------------------------------------------
(base) kevinfang@groq-r01-gn-04:~$ conda activate groqflow
(groqflow) kevinfang@groq-r01-gn-04:~$ git clone https://github.com/groq/groqflow.git
Cloning into 'groqflow'...
remote: Enumerating objects: 850, done.
remote: Counting objects: 100% (253/253), done.
remote: Compressing objects: 100% (157/157), done.
remote: Total 850 (delta 106), reused 171 (delta 87), pack-reused 597 (from 1)
Receiving objects: 100% (850/850), 14.61 MiB | 59.13 MiB/s, done.
Resolving deltas: 100% (450/450), done.
Updating files: 100% (104/104), done.
(groqflow) kevinfang@groq-r01-gn-04:~$ cd ~/groqflow
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ if [ -d "groqflow.egg-info" ]; then rm -r groqflow.egg-info; fi
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pip install --upgrade pip
Requirement already satisfied: pip in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (24.2)
Collecting pip
  Using cached pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
Using cached pip-24.3.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.2
    Uninstalling pip-24.2:
      Successfully uninstalled pip-24.2
Successfully installed pip-24.3.1
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pip list --format=freeze > frozen.txt
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pip install -r frozen.txt -e .
Obtaining file:///home/kevinfang/groqflow
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: ansicolors==1.1.8 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 1)) (1.1.8)
Requirement already satisfied: bitstring==3.1.9 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 2)) (3.1.9)
Requirement already satisfied: click==8.0.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 3)) (8.0.3)
Requirement already satisfied: contourpy==1.2.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 4)) (1.2.0)
Requirement already satisfied: crcmod==1.7 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 5)) (1.7)
Requirement already satisfied: cycler==0.12.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 6)) (0.12.1)
Requirement already satisfied: Deprecated==1.2.13 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 7)) (1.2.13)
Requirement already satisfied: fonttools==4.49.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 8)) (4.49.0)
Requirement already satisfied: groq-runtime==0.30 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 9)) (0.30)
Requirement already satisfied: groq-systems==1.13.8 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 10)) (1.13.8)
Requirement already satisfied: grpcio==1.53.2 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 11)) (1.53.2)
Requirement already satisfied: grpcio-tools==1.42.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 12)) (1.42.0)
Requirement already satisfied: host-daemon==0.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 13)) (0.1)
Requirement already satisfied: imageio==2.21.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 14)) (2.21.0)
Requirement already satisfied: kiwisolver==1.4.5 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 15)) (1.4.5)
Requirement already satisfied: matplotlib==3.8.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 16)) (3.8.3)
Requirement already satisfied: mpi4py==3.1.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 17)) (3.1.3)
Requirement already satisfied: networkx==3.2.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 18)) (3.2.1)
Requirement already satisfied: numa==1.4.6 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 19)) (1.4.6)
Requirement already satisfied: numpy==1.21.6 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 20)) (1.21.6)
Requirement already satisfied: ordered-set==4.0.2 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 21)) (4.0.2)
Requirement already satisfied: packaging==23.2 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 22)) (23.2)
Requirement already satisfied: parse==1.19.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 23)) (1.19.0)
Requirement already satisfied: parsimonious==0.8.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 24)) (0.8.1)
Requirement already satisfied: pillow==10.2.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 25)) (10.2.0)
Requirement already satisfied: pip==24.3.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from -r frozen.txt (line 26)) (24.3.1)
Requirement already satisfied: protobuf==3.20.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 27)) (3.20.3)
Requirement already satisfied: pycryptodome==3.11.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 28)) (3.11.0)
Requirement already satisfied: pyftdi==0.53.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 29)) (0.53.3)
Requirement already satisfied: pyparsing==3.1.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 30)) (3.1.1)
Requirement already satisfied: pyserial==3.5 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 31)) (3.5)
Requirement already satisfied: python-dateutil==2.8.2 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 32)) (2.8.2)
Requirement already satisfied: pyusb==1.2.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 33)) (1.2.1)
Requirement already satisfied: PyWavelets==1.4.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 34)) (1.4.1)
Requirement already satisfied: PyYAML==5.4.1 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 35)) (5.4.1)
Requirement already satisfied: scikit-image==0.18.3 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 36)) (0.18.3)
Requirement already satisfied: scipy==1.8.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 37)) (1.8.0)
Requirement already satisfied: setuptools==57.2.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 38)) (57.2.0)
Requirement already satisfied: six==1.16.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 39)) (1.16.0)
Requirement already satisfied: tifffile==2024.2.12 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 40)) (2024.2.12)
Requirement already satisfied: typing_extensions==4.9.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 41)) (4.9.0)
Requirement already satisfied: wheel==0.36.2 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 42)) (0.36.2)
Requirement already satisfied: wrapt==1.16.0 in /opt/groq/runtime/site-packages (from -r frozen.txt (line 43)) (1.16.0)
Collecting mlagility==3.3.1 (from groqflow==4.3.1)
  Using cached mlagility-3.3.1-py3-none-any.whl.metadata (6.1 kB)
Collecting onnx==1.14.0 (from groqflow==4.3.1)
  Using cached onnx-1.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (15 kB)
Collecting onnxruntime==1.15.1 (from groqflow==4.3.1)
  Using cached onnxruntime-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Collecting scikit-learn==1.1.1 (from groqflow==4.3.1)
  Using cached scikit_learn-1.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
Collecting torch==2.1.0 (from groqflow==4.3.1)
  Using cached torch-2.1.0-cp310-cp310-manylinux1_x86_64.whl.metadata (25 kB)
Collecting typeguard==4.0.0 (from groqflow==4.3.1)
  Using cached typeguard-4.0.0-py3-none-any.whl.metadata (3.6 kB)
Collecting invoke>=2.0.0 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached invoke-2.2.0-py3-none-any.whl.metadata (3.3 kB)
Collecting onnxmltools==1.11.2 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached onnxmltools-1.11.2-py2.py3-none-any.whl.metadata (9.2 kB)
Collecting hummingbird-ml==0.4.4 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached hummingbird_ml-0.4.4-py2.py3-none-any.whl.metadata (10 kB)
Collecting xgboost==1.6.1 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached xgboost-1.6.1-py3-none-manylinux2014_x86_64.whl.metadata (1.8 kB)
Collecting lightgbm==3.3.5 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached lightgbm-3.3.5-py3-none-manylinux1_x86_64.whl.metadata (15 kB)
Collecting paramiko==2.11.0 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached paramiko-2.11.0-py2.py3-none-any.whl.metadata (4.6 kB)
Collecting torchvision==0.16.0 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached torchvision-0.16.0-cp310-cp310-manylinux1_x86_64.whl.metadata (6.6 kB)
Collecting pandas>=1.5.3 (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached pandas-2.2.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (89 kB)
Collecting fasteners (from mlagility==3.3.1->groqflow==4.3.1)
  Using cached fasteners-0.19-py3-none-any.whl.metadata (4.9 kB)
Collecting coloredlogs (from onnxruntime==1.15.1->groqflow==4.3.1)
  Using cached coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)
Collecting flatbuffers (from onnxruntime==1.15.1->groqflow==4.3.1)
  Using cached flatbuffers-24.3.25-py2.py3-none-any.whl.metadata (850 bytes)
Collecting sympy (from onnxruntime==1.15.1->groqflow==4.3.1)
  Using cached sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
Collecting joblib>=1.0.0 (from scikit-learn==1.1.1->groqflow==4.3.1)
  Using cached joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting threadpoolctl>=2.0.0 (from scikit-learn==1.1.1->groqflow==4.3.1)
  Using cached threadpoolctl-3.5.0-py3-none-any.whl.metadata (13 kB)
Collecting filelock (from torch==2.1.0->groqflow==4.3.1)
  Using cached filelock-3.16.1-py3-none-any.whl.metadata (2.9 kB)
Collecting jinja2 (from torch==2.1.0->groqflow==4.3.1)
  Using cached jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting fsspec (from torch==2.1.0->groqflow==4.3.1)
  Using cached fsspec-2024.10.0-py3-none-any.whl.metadata (11 kB)
Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cuda-runtime-cu12==12.1.105 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cuda-cupti-cu12==12.1.105 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cudnn-cu12==8.9.2.26 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cublas-cu12==12.1.3.1 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cufft-cu12==11.0.2.54 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-curand-cu12==10.3.2.106 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cusolver-cu12==11.4.5.107 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cusparse-cu12==12.1.0.106 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-nccl-cu12==2.18.1 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl.metadata (1.8 kB)
Collecting nvidia-nvtx-cu12==12.1.105 (from torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.7 kB)
Collecting triton==2.1.0 (from torch==2.1.0->groqflow==4.3.1)
  Using cached triton-2.1.0-0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.3 kB)
Collecting onnxconverter-common>=1.6.0 (from hummingbird-ml==0.4.4->mlagility==3.3.1->groqflow==4.3.1)
  Using cached onnxconverter_common-1.14.0-py2.py3-none-any.whl.metadata (4.2 kB)
Collecting psutil (from hummingbird-ml==0.4.4->mlagility==3.3.1->groqflow==4.3.1)
  Using cached psutil-6.1.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (22 kB)
Collecting dill (from hummingbird-ml==0.4.4->mlagility==3.3.1->groqflow==4.3.1)
  Using cached dill-0.3.9-py3-none-any.whl.metadata (10 kB)
Collecting nvidia-nvjitlink-cu12 (from nvidia-cusolver-cu12==11.4.5.107->torch==2.1.0->groqflow==4.3.1)
  Using cached nvidia_nvjitlink_cu12-12.6.85-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.5 kB)
Collecting skl2onnx (from onnxmltools==1.11.2->mlagility==3.3.1->groqflow==4.3.1)
  Using cached skl2onnx-1.17.0-py2.py3-none-any.whl.metadata (3.2 kB)
Collecting bcrypt>=3.1.3 (from paramiko==2.11.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached bcrypt-4.2.1-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (9.8 kB)
Collecting cryptography>=2.5 (from paramiko==2.11.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached cryptography-43.0.3-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (5.4 kB)
Collecting pynacl>=1.0.1 (from paramiko==2.11.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl.metadata (8.6 kB)
Collecting requests (from torchvision==0.16.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
INFO: pip is looking at multiple versions of pandas to determine which version is compatible with other requirements. This could take a while.
Collecting pandas>=1.5.3 (from mlagility==3.3.1->groqflow==4.3.1)
  Downloading pandas-2.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
  Downloading pandas-2.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
  Downloading pandas-2.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
  Downloading pandas-2.1.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
  Downloading pandas-2.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
  Downloading pandas-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
  Downloading pandas-2.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
INFO: pip is still looking at multiple versions of pandas to determine which version is compatible with other requirements. This could take a while.
  Downloading pandas-2.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
  Downloading pandas-2.0.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
Collecting pytz>=2020.1 (from pandas>=1.5.3->mlagility==3.3.1->groqflow==4.3.1)
  Using cached pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.1 (from pandas>=1.5.3->mlagility==3.3.1->groqflow==4.3.1)
  Using cached tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime==1.15.1->groqflow==4.3.1)
  Using cached humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch==2.1.0->groqflow==4.3.1)
  Using cached MarkupSafe-3.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy->onnxruntime==1.15.1->groqflow==4.3.1)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting cffi>=1.12 (from cryptography>=2.5->paramiko==2.11.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached cffi-1.17.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
INFO: pip is looking at multiple versions of onnxconverter-common to determine which version is compatible with other requirements. This could take a while.
Collecting onnxconverter-common>=1.6.0 (from hummingbird-ml==0.4.4->mlagility==3.3.1->groqflow==4.3.1)
  Using cached onnxconverter_common-1.13.0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting charset-normalizer<4,>=2 (from requests->torchvision==0.16.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (34 kB)
Collecting idna<4,>=2.5 (from requests->torchvision==0.16.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests->torchvision==0.16.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached urllib3-2.2.3-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests->torchvision==0.16.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=2.5->paramiko==2.11.0->mlagility==3.3.1->groqflow==4.3.1)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Using cached mlagility-3.3.1-py3-none-any.whl (1.2 MB)
Using cached onnx-1.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (14.6 MB)
Using cached onnxruntime-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.9 MB)
Using cached scikit_learn-1.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30.4 MB)
Using cached torch-2.1.0-cp310-cp310-manylinux1_x86_64.whl (670.2 MB)
Using cached typeguard-4.0.0-py3-none-any.whl (33 kB)
Using cached hummingbird_ml-0.4.4-py2.py3-none-any.whl (181 kB)
Using cached lightgbm-3.3.5-py3-none-manylinux1_x86_64.whl (2.0 MB)
Using cached nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)
Using cached nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (14.1 MB)
Using cached nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (23.7 MB)
Using cached nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (823 kB)
Using cached nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)
Using cached nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl (121.6 MB)
Using cached nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl (56.5 MB)
Using cached nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl (124.2 MB)
Using cached nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl (196.0 MB)
Using cached nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl (209.8 MB)
Using cached nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (99 kB)
Using cached onnxmltools-1.11.2-py2.py3-none-any.whl (322 kB)
Using cached paramiko-2.11.0-py2.py3-none-any.whl (212 kB)
Using cached torchvision-0.16.0-cp310-cp310-manylinux1_x86_64.whl (6.9 MB)
Using cached triton-2.1.0-0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89.2 MB)
Using cached xgboost-1.6.1-py3-none-manylinux2014_x86_64.whl (192.9 MB)
Using cached invoke-2.2.0-py3-none-any.whl (160 kB)
Using cached joblib-1.4.2-py3-none-any.whl (301 kB)
Downloading pandas-2.0.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 135.7 MB/s eta 0:00:00
Using cached threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Using cached coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Using cached fasteners-0.19-py3-none-any.whl (18 kB)
Using cached filelock-3.16.1-py3-none-any.whl (16 kB)
Using cached flatbuffers-24.3.25-py2.py3-none-any.whl (26 kB)
Using cached fsspec-2024.10.0-py3-none-any.whl (179 kB)
Using cached jinja2-3.1.4-py3-none-any.whl (133 kB)
Using cached sympy-1.13.3-py3-none-any.whl (6.2 MB)
Using cached bcrypt-4.2.1-cp39-abi3-manylinux_2_28_x86_64.whl (278 kB)
Using cached cryptography-43.0.3-cp39-abi3-manylinux_2_28_x86_64.whl (4.0 MB)
Using cached humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Using cached MarkupSafe-3.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (20 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Using cached onnxconverter_common-1.13.0-py2.py3-none-any.whl (83 kB)
Using cached PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (856 kB)
Using cached pytz-2024.2-py2.py3-none-any.whl (508 kB)
Using cached tzdata-2024.2-py2.py3-none-any.whl (346 kB)
Using cached dill-0.3.9-py3-none-any.whl (119 kB)
Using cached nvidia_nvjitlink_cu12-12.6.85-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (19.7 MB)
Using cached psutil-6.1.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (287 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached skl2onnx-1.17.0-py2.py3-none-any.whl (298 kB)
Using cached certifi-2024.8.30-py3-none-any.whl (167 kB)
Using cached cffi-1.17.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (446 kB)
Using cached charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached urllib3-2.2.3-py3-none-any.whl (126 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Building wheels for collected packages: groqflow
  Building editable for groqflow (pyproject.toml) ... done
  Created wheel for groqflow: filename=groqflow-4.3.1-0.editable-py3-none-any.whl size=3825 sha256=0eb4af88f6d318c7499dd7476f7c0bead377a6790ad716872bc2b73259f312da
  Stored in directory: /tmp/pip-ephem-wheel-cache-22rmuwb6/wheels/3c/db/58/435b02729609d3415429f67dd1778af3d9386748f94f896baf
Successfully built groqflow
Installing collected packages: pytz, mpmath, flatbuffers, urllib3, tzdata, typeguard, threadpoolctl, sympy, pycparser, psutil, onnx, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, MarkupSafe, joblib, invoke, idna, humanfriendly, fsspec, filelock, fasteners, dill, charset-normalizer, certifi, bcrypt, xgboost, triton, scikit-learn, requests, pandas, onnxconverter-common, nvidia-cusparse-cu12, nvidia-cudnn-cu12, jinja2, coloredlogs, cffi, skl2onnx, pynacl, onnxruntime, nvidia-cusolver-cu12, lightgbm, cryptography, torch, paramiko, onnxmltools, torchvision, hummingbird-ml, mlagility, groqflow
Successfully installed MarkupSafe-3.0.2 bcrypt-4.2.1 certifi-2024.8.30 cffi-1.17.1 charset-normalizer-3.4.0 coloredlogs-15.0.1 cryptography-43.0.3 dill-0.3.9 fasteners-0.19 filelock-3.16.1 flatbuffers-24.3.25 fsspec-2024.10.0 groqflow-4.3.1 humanfriendly-10.0 hummingbird-ml-0.4.4 idna-3.10 invoke-2.2.0 jinja2-3.1.4 joblib-1.4.2 lightgbm-3.3.5 mlagility-3.3.1 mpmath-1.3.0 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.18.1 nvidia-nvjitlink-cu12-12.6.85 nvidia-nvtx-cu12-12.1.105 onnx-1.14.0 onnxconverter-common-1.13.0 onnxmltools-1.11.2 onnxruntime-1.15.1 pandas-2.0.3 paramiko-2.11.0 psutil-6.1.0 pycparser-2.22 pynacl-1.5.0 pytz-2024.2 requests-2.32.3 scikit-learn-1.1.1 skl2onnx-1.17.0 sympy-1.13.3 threadpoolctl-3.5.0 torch-2.1.0 torchvision-0.16.0 triton-2.1.0 typeguard-4.0.0 tzdata-2024.2 urllib3-2.2.3 xgboost-1.6.1
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ 
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pushd .
~/groqflow ~/groqflow
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ cd demo_helpers
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow/demo_helpers$ if [ -d "groqflow_demo_helpers.egg-info" ]; then rm -r groqflow_demo_helpers.egg-info; fi
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow/demo_helpers$ pip install -e .
Obtaining file:///home/kevinfang/groqflow/demo_helpers
  Preparing metadata (setup.py) ... done
Collecting charset-normalizer==3.3.2 (from groqflow-demo-helpers==0.2.0)
  Downloading charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (33 kB)
Collecting transformers>=4.20.0 (from groqflow-demo-helpers==0.2.0)
  Using cached transformers-4.46.3-py3-none-any.whl.metadata (44 kB)
Collecting datasets>=2.3.2 (from groqflow-demo-helpers==0.2.0)
  Downloading datasets-3.1.0-py3-none-any.whl.metadata (20 kB)
Collecting prettytable>=3.3.0 (from groqflow-demo-helpers==0.2.0)
  Downloading prettytable-3.12.0-py3-none-any.whl.metadata (30 kB)
Collecting wget>=3.2 (from groqflow-demo-helpers==0.2.0)
  Downloading wget-3.2.zip (10 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: setuptools==57.2.0 in /opt/groq/runtime/site-packages (from groqflow-demo-helpers==0.2.0) (57.2.0)
Requirement already satisfied: torchvision==0.16.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from groqflow-demo-helpers==0.2.0) (0.16.0)
Collecting torchaudio==2.1.0 (from groqflow-demo-helpers==0.2.0)
  Downloading torchaudio-2.1.0-cp310-cp310-manylinux1_x86_64.whl.metadata (5.7 kB)
Collecting path>=16.4.0 (from groqflow-demo-helpers==0.2.0)
  Downloading path-17.0.0-py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: torch==2.1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (2.1.0)
Requirement already satisfied: numpy in /opt/groq/runtime/site-packages (from torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (1.21.6)
Requirement already satisfied: requests in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (2.32.3)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /opt/groq/runtime/site-packages (from torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (10.2.0)
Requirement already satisfied: filelock in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (3.16.1)
Requirement already satisfied: typing-extensions in /opt/groq/runtime/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (4.9.0)
Requirement already satisfied: sympy in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (1.13.3)
Requirement already satisfied: networkx in /opt/groq/runtime/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (3.2.1)
Requirement already satisfied: jinja2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (3.1.4)
Requirement already satisfied: fsspec in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (2024.10.0)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.105)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.105)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.105)
Requirement already satisfied: nvidia-cudnn-cu12==8.9.2.26 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (8.9.2.26)
Requirement already satisfied: nvidia-cublas-cu12==12.1.3.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.3.1)
Requirement already satisfied: nvidia-cufft-cu12==11.0.2.54 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (11.0.2.54)
Requirement already satisfied: nvidia-curand-cu12==10.3.2.106 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (10.3.2.106)
Requirement already satisfied: nvidia-cusolver-cu12==11.4.5.107 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (11.4.5.107)
Requirement already satisfied: nvidia-cusparse-cu12==12.1.0.106 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.0.106)
Requirement already satisfied: nvidia-nccl-cu12==2.18.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (2.18.1)
Requirement already satisfied: nvidia-nvtx-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.1.105)
Requirement already satisfied: triton==2.1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (2.1.0)
Requirement already satisfied: nvidia-nvjitlink-cu12 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from nvidia-cusolver-cu12==11.4.5.107->torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (12.6.85)
Collecting pyarrow>=15.0.0 (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached pyarrow-18.0.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (3.3 kB)
Collecting dill<0.3.9,>=0.3.0 (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached dill-0.3.8-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: pandas in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (2.0.3)
Collecting tqdm>=4.66.3 (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached tqdm-4.67.0-py3-none-any.whl.metadata (57 kB)
Collecting xxhash (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting multiprocess<0.70.17 (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached multiprocess-0.70.16-py310-none-any.whl.metadata (7.2 kB)
Collecting fsspec (from torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0)
  Downloading fsspec-2024.9.0-py3-none-any.whl.metadata (11 kB)
Collecting aiohttp (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached aiohttp-3.11.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
Collecting huggingface-hub>=0.23.0 (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached huggingface_hub-0.26.2-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: packaging in /opt/groq/runtime/site-packages (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (23.2)
Requirement already satisfied: pyyaml>=5.1 in /opt/groq/runtime/site-packages (from datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (5.4.1)
Collecting wcwidth (from prettytable>=3.3.0->groqflow-demo-helpers==0.2.0)
  Using cached wcwidth-0.2.13-py2.py3-none-any.whl.metadata (14 kB)
Collecting regex!=2019.12.17 (from transformers>=4.20.0->groqflow-demo-helpers==0.2.0)
  Using cached regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (40 kB)
Collecting tokenizers<0.21,>=0.20 (from transformers>=4.20.0->groqflow-demo-helpers==0.2.0)
  Using cached tokenizers-0.20.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
Collecting safetensors>=0.4.1 (from transformers>=4.20.0->groqflow-demo-helpers==0.2.0)
  Using cached safetensors-0.4.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.8 kB)
Collecting aiohappyeyeballs>=2.3.0 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached aiohappyeyeballs-2.4.3-py3-none-any.whl.metadata (6.1 kB)
Collecting aiosignal>=1.1.2 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached aiosignal-1.3.1-py3-none-any.whl.metadata (4.0 kB)
Collecting async-timeout<6.0,>=4.0 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached async_timeout-5.0.1-py3-none-any.whl.metadata (5.1 kB)
Collecting attrs>=17.3.0 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting frozenlist>=1.1.1 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached frozenlist-1.5.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (13 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached multidict-6.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.0 kB)
Collecting propcache>=0.2.0 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached propcache-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp->datasets>=2.3.2->groqflow-demo-helpers==0.2.0)
  Using cached yarl-1.18.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (67 kB)
Requirement already satisfied: idna<4,>=2.5 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->torchvision==0.16.0->groqflow-demo-helpers==0.2.0) (2024.8.30)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/groq/runtime/site-packages (from pandas->datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from pandas->datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (2024.2)
Requirement already satisfied: tzdata>=2022.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from pandas->datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (2024.2)
Requirement already satisfied: six>=1.5 in /opt/groq/runtime/site-packages (from python-dateutil>=2.8.2->pandas->datasets>=2.3.2->groqflow-demo-helpers==0.2.0) (1.16.0)
Requirement already satisfied: MarkupSafe>=2.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from jinja2->torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (3.0.2)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from sympy->torch==2.1.0->torchaudio==2.1.0->groqflow-demo-helpers==0.2.0) (1.3.0)
Downloading charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (142 kB)
Downloading torchaudio-2.1.0-cp310-cp310-manylinux1_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 32.7 MB/s eta 0:00:00
Downloading datasets-3.1.0-py3-none-any.whl (480 kB)
Downloading path-17.0.0-py3-none-any.whl (24 kB)
Downloading prettytable-3.12.0-py3-none-any.whl (31 kB)
Using cached transformers-4.46.3-py3-none-any.whl (10.0 MB)
Using cached dill-0.3.8-py3-none-any.whl (116 kB)
Downloading fsspec-2024.9.0-py3-none-any.whl (179 kB)
Using cached aiohttp-3.11.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
Using cached huggingface_hub-0.26.2-py3-none-any.whl (447 kB)
Using cached multiprocess-0.70.16-py310-none-any.whl (134 kB)
Using cached pyarrow-18.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (40.0 MB)
Using cached regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (781 kB)
Using cached safetensors-0.4.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (435 kB)
Using cached tokenizers-0.20.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached tqdm-4.67.0-py3-none-any.whl (78 kB)
Using cached wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Using cached xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
Using cached aiohappyeyeballs-2.4.3-py3-none-any.whl (14 kB)
Using cached aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Using cached async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Using cached attrs-24.2.0-py3-none-any.whl (63 kB)
Using cached frozenlist-1.5.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (241 kB)
Using cached multidict-6.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (124 kB)
Using cached propcache-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (208 kB)
Using cached yarl-1.18.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (319 kB)
Building wheels for collected packages: wget
  Building wheel for wget (setup.py) ... done
  Created wheel for wget: filename=wget-3.2-py3-none-any.whl size=9673 sha256=a932ee3f384b6c43ce8bbdcb8e3b871d7b0eea0cd55ecd2487e283f0832c9109
  Stored in directory: /home/kevinfang/.cache/pip/wheels/8b/f1/7f/5c94f0a7a505ca1c81cd1d9208ae2064675d97582078e6c769
Successfully built wget
Installing collected packages: wget, wcwidth, xxhash, tqdm, safetensors, regex, pyarrow, propcache, prettytable, path, multidict, fsspec, frozenlist, dill, charset-normalizer, attrs, async-timeout, aiohappyeyeballs, yarl, multiprocess, aiosignal, huggingface-hub, aiohttp, torchaudio, tokenizers, transformers, datasets, groqflow-demo-helpers
  Attempting uninstall: fsspec
    Found existing installation: fsspec 2024.10.0
    Uninstalling fsspec-2024.10.0:
      Successfully uninstalled fsspec-2024.10.0
  Attempting uninstall: dill
    Found existing installation: dill 0.3.9
    Uninstalling dill-0.3.9:
      Successfully uninstalled dill-0.3.9
  Attempting uninstall: charset-normalizer
    Found existing installation: charset-normalizer 3.4.0
    Uninstalling charset-normalizer-3.4.0:
      Successfully uninstalled charset-normalizer-3.4.0
  DEPRECATION: Legacy editable install of groqflow-demo-helpers==0.2.0 from file:///home/kevinfang/groqflow/demo_helpers (setup.py develop) is deprecated. pip 25.0 will enforce this behaviour change. A possible replacement is to add a pyproject.toml or enable --use-pep517, and use setuptools >= 64. If the resulting installation is not behaving as expected, try using --config-settings editable_mode=compat. Please consult the setuptools documentation for more information. Discussion can be found at https://github.com/pypa/pip/issues/11457
  Running setup.py develop for groqflow-demo-helpers
Successfully installed aiohappyeyeballs-2.4.3 aiohttp-3.11.7 aiosignal-1.3.1 async-timeout-5.0.1 attrs-24.2.0 charset-normalizer-3.3.2 datasets-3.1.0 dill-0.3.8 frozenlist-1.5.0 fsspec-2024.9.0 groqflow-demo-helpers huggingface-hub-0.26.2 multidict-6.1.0 multiprocess-0.70.16 path-17.0.0 prettytable-3.12.0 propcache-0.2.0 pyarrow-18.0.0 regex-2024.11.6 safetensors-0.4.5 tokenizers-0.20.3 torchaudio-2.1.0 tqdm-4.67.0 transformers-4.46.3 wcwidth-0.2.13 wget-3.2 xxhash-3.5.0 yarl-1.18.0
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow/demo_helpers$ popd
~/groqflow
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pip install soundfile
Collecting soundfile
  Using cached soundfile-0.12.1-py2.py3-none-manylinux_2_31_x86_64.whl.metadata (14 kB)
Requirement already satisfied: cffi>=1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from soundfile) (1.17.1)
Requirement already satisfied: pycparser in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from cffi>=1.0->soundfile) (2.22)
Using cached soundfile-0.12.1-py2.py3-none-manylinux_2_31_x86_64.whl (1.2 MB)
Installing collected packages: soundfile
Successfully installed soundfile-0.12.1
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ pip install datasets==2.21.0
Collecting datasets==2.21.0
  Using cached datasets-2.21.0-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: filelock in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (3.16.1)
Requirement already satisfied: numpy>=1.17 in /opt/groq/runtime/site-packages (from datasets==2.21.0) (1.21.6)
Requirement already satisfied: pyarrow>=15.0.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (18.0.0)
Requirement already satisfied: dill<0.3.9,>=0.3.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (0.3.8)
Requirement already satisfied: pandas in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (2.0.3)
Requirement already satisfied: requests>=2.32.2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (2.32.3)
Requirement already satisfied: tqdm>=4.66.3 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (4.67.0)
Requirement already satisfied: xxhash in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (3.5.0)
Requirement already satisfied: multiprocess in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (0.70.16)
Collecting fsspec<=2024.6.1,>=2023.1.0 (from fsspec[http]<=2024.6.1,>=2023.1.0->datasets==2.21.0)
  Using cached fsspec-2024.6.1-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: aiohttp in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (3.11.7)
Requirement already satisfied: huggingface-hub>=0.21.2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from datasets==2.21.0) (0.26.2)
Requirement already satisfied: packaging in /opt/groq/runtime/site-packages (from datasets==2.21.0) (23.2)
Requirement already satisfied: pyyaml>=5.1 in /opt/groq/runtime/site-packages (from datasets==2.21.0) (5.4.1)
Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (2.4.3)
Requirement already satisfied: aiosignal>=1.1.2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (1.3.1)
Requirement already satisfied: async-timeout<6.0,>=4.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (5.0.1)
Requirement already satisfied: attrs>=17.3.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (24.2.0)
Requirement already satisfied: frozenlist>=1.1.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (1.5.0)
Requirement already satisfied: multidict<7.0,>=4.5 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (6.1.0)
Requirement already satisfied: propcache>=0.2.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (0.2.0)
Requirement already satisfied: yarl<2.0,>=1.17.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from aiohttp->datasets==2.21.0) (1.18.0)
Requirement already satisfied: typing-extensions>=3.7.4.3 in /opt/groq/runtime/site-packages (from huggingface-hub>=0.21.2->datasets==2.21.0) (4.9.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests>=2.32.2->datasets==2.21.0) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests>=2.32.2->datasets==2.21.0) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests>=2.32.2->datasets==2.21.0) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests>=2.32.2->datasets==2.21.0) (2024.8.30)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/groq/runtime/site-packages (from pandas->datasets==2.21.0) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from pandas->datasets==2.21.0) (2024.2)
Requirement already satisfied: tzdata>=2022.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from pandas->datasets==2.21.0) (2024.2)
Requirement already satisfied: six>=1.5 in /opt/groq/runtime/site-packages (from python-dateutil>=2.8.2->pandas->datasets==2.21.0) (1.16.0)
Using cached datasets-2.21.0-py3-none-any.whl (527 kB)
Using cached fsspec-2024.6.1-py3-none-any.whl (177 kB)
Installing collected packages: fsspec, datasets
  Attempting uninstall: fsspec
    Found existing installation: fsspec 2024.9.0
    Uninstalling fsspec-2024.9.0:
      Successfully uninstalled fsspec-2024.9.0
  Attempting uninstall: datasets
    Found existing installation: datasets 3.1.0
    Uninstalling datasets-3.1.0:
      Successfully uninstalled datasets-3.1.0
Successfully installed datasets-2.21.0 fsspec-2024.6.1
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ conda activate groqflow
(groqflow) kevinfang@groq-r01-gn-04:~/groqflow$ qsub -I -l walltime=1:00:00
qsub: waiting for job 6324.groq-r01-controller.ai.alcf.anl.gov to start
qsub: job 6324.groq-r01-controller.ai.alcf.anl.gov ready
(base) kevinfang@groq-r01-gn-08:~$ cd ~/proof_points/natural_language_processing/minilm
-bash: cd: /home/kevinfang/proof_points/natural_language_processing/minilm: No such file or directory
(base) kevinfang@groq-r01-gn-08:~$ ls
BertLarge  Miniconda3-latest-Linux-x86_64.sh  ai-science-training-series  groqflow  miniconda3	slurm-43631.out  slurm-43632.out  slurm-43634.out  slurm-43635.out  slurm-43637.out  slurm-43639.out  slurm-43641.out
(base) kevinfang@groq-r01-gn-08:~$ cd groqflow
(base) kevinfang@groq-r01-gn-08:~/groqflow$ ls
README.md  cla.md  demo_helpers  docs  examples  frozen.txt  groqflow  groqflow.egg-info  license.md  proof_points  pyproject.toml  setup.py
(base) kevinfang@groq-r01-gn-08:~/groqflow$ cd proof_points/
(base) kevinfang@groq-r01-gn-08:~/groqflow/proof_points$ ls
README.md  computer_vision  natural_language_processing  speech
(base) kevinfang@groq-r01-gn-08:~/groqflow/proof_points$ cd natural_language_processing/minilm/
(base) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ ls
README.md  minilmv2.py	requirements.txt
(base) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ conda activate groqflow
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ pip install -r requirements.txt
Requirement already satisfied: torch>=1.12.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from -r requirements.txt (line 1)) (2.1.0)
Requirement already satisfied: transformers>=4.20.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (4.46.3)
Requirement already satisfied: filelock in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (3.16.1)
Requirement already satisfied: typing-extensions in /opt/groq/runtime/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (4.9.0)
Requirement already satisfied: sympy in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (1.13.3)
Requirement already satisfied: networkx in /opt/groq/runtime/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (3.2.1)
Requirement already satisfied: jinja2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (3.1.4)
Requirement already satisfied: fsspec in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (2024.6.1)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.105)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.105)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.105)
Requirement already satisfied: nvidia-cudnn-cu12==8.9.2.26 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (8.9.2.26)
Requirement already satisfied: nvidia-cublas-cu12==12.1.3.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.3.1)
Requirement already satisfied: nvidia-cufft-cu12==11.0.2.54 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (11.0.2.54)
Requirement already satisfied: nvidia-curand-cu12==10.3.2.106 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (10.3.2.106)
Requirement already satisfied: nvidia-cusolver-cu12==11.4.5.107 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (11.4.5.107)
Requirement already satisfied: nvidia-cusparse-cu12==12.1.0.106 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.0.106)
Requirement already satisfied: nvidia-nccl-cu12==2.18.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (2.18.1)
Requirement already satisfied: nvidia-nvtx-cu12==12.1.105 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (12.1.105)
Requirement already satisfied: triton==2.1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from torch>=1.12.0->-r requirements.txt (line 1)) (2.1.0)
Requirement already satisfied: nvidia-nvjitlink-cu12 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from nvidia-cusolver-cu12==11.4.5.107->torch>=1.12.0->-r requirements.txt (line 1)) (12.6.85)
Requirement already satisfied: huggingface-hub<1.0,>=0.23.2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (0.26.2)
Requirement already satisfied: numpy>=1.17 in /opt/groq/runtime/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (1.21.6)
Requirement already satisfied: packaging>=20.0 in /opt/groq/runtime/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (23.2)
Requirement already satisfied: pyyaml>=5.1 in /opt/groq/runtime/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (5.4.1)
Requirement already satisfied: regex!=2019.12.17 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (2024.11.6)
Requirement already satisfied: requests in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (2.32.3)
Requirement already satisfied: tokenizers<0.21,>=0.20 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (0.20.3)
Requirement already satisfied: safetensors>=0.4.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (0.4.5)
Requirement already satisfied: tqdm>=4.27 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from transformers>=4.20.0->-r requirements.txt (line 2)) (4.67.0)
Requirement already satisfied: MarkupSafe>=2.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from jinja2->torch>=1.12.0->-r requirements.txt (line 1)) (3.0.2)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->transformers>=4.20.0->-r requirements.txt (line 2)) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->transformers>=4.20.0->-r requirements.txt (line 2)) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->transformers>=4.20.0->-r requirements.txt (line 2)) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from requests->transformers>=4.20.0->-r requirements.txt (line 2)) (2024.8.30)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/kevinfang/miniconda3/envs/groqflow/lib/python3.10/site-packages (from sympy->torch>=1.12.0->-r requirements.txt (line 1)) (1.3.0)
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ ls  
README.md  minilmv2.py	requirements.txt
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ vim minilmv2.py

tokenizer_config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 350/350 [00:00<00:00, 2.05MB/s]
vocab.txt: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 12.8MB/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 5.09MB/s]
special_tokens_map.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 112/112 [00:00<00:00, 1.51MB/s]
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 612/612 [00:00<00:00, 6.86MB/s]
model.safetensors: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 90.9M/90.9M [00:00<00:00, 208MB/s]



Building "minilmv2"
    ✓ Exporting PyTorch to ONNX
    ✓ Optimizing ONNX file
    ✓ Checking for Op support
    ✓ Converting to FP16
    ✓ Compiling model
    ✓ Assembling model

Woohoo! Saved to ~/.cache/groqflow/minilmv2
Preprocessing data.
Downloading readme: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 11.4k/11.4k [00:00<00:00, 148kB/s]
Downloading data: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 470k/470k [00:00<00:00, 1.81MB/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 108k/108k [00:00<00:00, 814kB/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 142k/142k [00:00<00:00, 823kB/s]
Generating train split: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5749/5749 [00:00<00:00, 95574.08 examples/s]
Generating test split: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1379/1379 [00:00<00:00, 294423.27 examples/s]
Generating dev split: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1500/1500 [00:00<00:00, 269880.58 examples/s]
Map: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1379/1379 [00:00<00:00, 30104.17 examples/s]

Info: No inputs received for benchmark. Using the inputs provided during model compilation.
Running inference on GroqChip.
Running inference using PyTorch model (CPU).
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1379/1379 [01:30<00:00, 15.30it/s]
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
| Source | Spearman Rank Correlation Coefficient | end-to-end latency (ms) | end-to-end IPS | on-chip latency (ms) | on-chip IPS |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
|  cpu   |                 0.8203                |          65.35          |     15.30      |          --          |      --     |
|  groq  |                 0.8203                |           0.48          |    2065.11     |         0.41         |   2460.74   |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
Proof point /home/kevinfang/groqflow/proof_points/natural_language_processing/minilm/minilmv2.py finished!
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ ls
README.md  minilmv2.py  requirements.txt
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ vim minilmv2.py
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ vim minilmv2.py
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ (groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ python minilmv2.py

Woohoo! Build "minilmv2" (build_name auto-selected) found in cache. Loading it!
Preprocessing data.

Info: No inputs received for benchmark. Using the inputs provided during model compilation.
Running inference on GroqChip.
Running inference using PyTorch model (CPU).
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1379/1379 [01:29<00:00, 15.46it/s]
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
| Source | Spearman Rank Correlation Coefficient | end-to-end latency (ms) | end-to-end IPS | on-chip latency (ms) | on-chip IPS |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
|  cpu   |                 0.8203                |          64.70          |     15.46      |          --          |      --     |
|  groq  |                 0.8203                |           0.48          |    2072.15     |         0.41         |   2460.74   |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
Proof point /home/kevinfang/groqflow/proof_points/natural_language_processing/minilm/minilmv2.py finished!
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ ls
README.md  minilmv2.py  requirements.txt
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ mv minilmv2.py minilmv2_custom.py
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ ls
README.md  minilmv2_custom.py  requirements.txt
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$ python minilmv2_custom.py



Building "minilmv2_custom"
    ✓ Exporting PyTorch to ONNX
    ✓ Optimizing ONNX file
    ✓ Checking for Op support
    ✓ Converting to FP16
    ✓ Compiling model
    ✓ Assembling model

Woohoo! Saved to ~/.cache/groqflow/minilmv2_custom
Preprocessing data.

Info: No inputs received for benchmark. Using the inputs provided during model compilation.
Running inference on GroqChip.
Running inference using PyTorch model (CPU).
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1379/1379 [01:31<00:00, 15.03it/s]
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
| Source | Spearman Rank Correlation Coefficient | end-to-end latency (ms) | end-to-end IPS | on-chip latency (ms) | on-chip IPS |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
|  cpu   |                 0.8203                |          66.55          |     15.03      |          --          |      --     |
|  groq  |                 0.8203                |           0.48          |    2064.04     |         0.41         |   2460.74   |
+--------+---------------------------------------+-------------------------+----------------+----------------------+-------------+
Proof point /home/kevinfang/groqflow/proof_points/natural_language_processing/minilm/minilmv2_custom.py finished!
(groqflow) kevinfang@groq-r01-gn-08:~/groqflow/proof_points/natural_language_processing/minilm$
```
</details>

- This [minilmv2_custom.py](minilmv2_custom.py) contains the code to run MiniLM training with custom input instead of dummy input.

##### Solution 2:
* [Sambanova Homework](./Sambanova/README.md#homework) - For BERT example, understand flags used in the script. Change values for flag --ntasks and measure its effect on performance. Submit proof (contents printed out to your terminal, path to a logfile or screenshot) that you were able to successfully follow the instructions and execute.

<details>
    <summary>Sambanova Terminal Print Out here</summary>
  
```bash
Last login: Tue Nov 19 23:19:12 on ttys000
kevinfang@Kevins-MacBook-Air-8 ~ % ssh kevinfang@sambanova.alcf.anl.gov
(kevinfang@sambanova.alcf.anl.gov) ---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Password: 
---------------------------------------------------------------------------
                            Notice to Users
This is a Federal computer system and is the property of the United States
Government. It is for authorized use only. Users (authorized or unauthorized)
have no explicit or implicit expectation of privacy.
Any or all uses of this system and all files on this system may be intercepted,
monitored, recorded, copied, audited, inspected, and disclosed to authorized
site, Department of Energy, and law enforcement personnel, as well as
authorized officials of other agencies, both domestic and foreign. By using
this system, the user consents to such interception, monitoring, recording,
copying, auditing, inspection, and disclosure at the discretion of authorized
site or Department of Energy personnel.
Unauthorized or improper use of this system may result in administrative
disciplinary action and civil and criminal penalties. By continuing to use
this system you indicate your awareness of and consent to these terms and
conditions of use. LOG OFF IMMEDIATELY if you do not agree to the conditions
stated in this warning.
----------------------------------------------------------------------------
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-174-generic x86_64)
 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
 System information as of Thu 19 Sep 2024 11:32:31 AM UTC
  System load:  0.05               Processes:               270
  Usage of /:   32.6% of 23.45GB   Users logged in:         3
  Memory usage: 38%                IPv4 address for ens224: 140.221.69.48
  Swap usage:   3%
 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.
   https://ubuntu.com/engage/secure-kubernetes-at-the-edge
Expanded Security Maintenance for Applications is not enabled.
2 updates can be applied immediately.
To see these additional updates run: apt list --upgradable
13 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm
New release '22.04.5 LTS' available.
Run 'do-release-upgrade' to upgrade to it.
*** System restart required ***
Last login: Wed Nov 20 07:19:47 2024 from 181.214.196.74
kevinfang@sn-login-01:~$ ssh sn30-r4-h1
The authenticity of host 'sn30-r4-h1 (140.221.82.11)' can't be established.
ECDSA key fingerprint is SHA256:NoWZ0yp8fe/Fj/B+pImIF6dpC6cMf3paWGuu0Cm40M4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'sn30-r4-h1' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-147-generic x86_64)
 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
  System information as of Wed 20 Nov 2024 07:53:29 AM UTC
  System load:     1.09                IPv4 address for snhni0: 140.221.82.11
  Usage of /:      29.2% of 847.12GB   IPv4 address for snni0:  172.16.0.45
  Memory usage:    55%                 IPv4 address for snni2:  172.16.0.46
  Swap usage:      0%                  IPv4 address for snni4:  172.16.0.47
  Processes:       1964                IPv4 address for snni6:  172.16.0.48
  Users logged in: 1                   IPv4 address for virbr0: 192.168.122.1
32 updates can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable
The list of available updates is more than a week old.
To check for new updates run: sudo apt update
#################################### Please note update on 12-20-2023 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Now Running Sambaflow 1.17.7-27
Acceptance Test scripts are in /data/ANL/scripts.
Acceptance Test results are in /data/ANL/results.
Older scripts are in /data/ANL/scripts/1.17.4-28
see /data/ANL/scripts/model_all_run.sh  for examples on how to run each test.
see also /data/ANL/scripts/Readme. 
snfadm will report 8 RDUS.
In 1.16 for the purpose of slurm there were 16 four tile RDUS.  
IN 1.17 slurm now thinks that there are 8 RDUs.
sinfo -O AllocNodes,GresUsed,Gres,NodeList
ALLOCNODES          GRES_USED           GRES                NODELIST            
oll                 rdu:0,rdu_mem:0,rdu_rdu:8,rdu_mem:104854sn30-r1-h[1-2],sn30-
Now
If you compile, then by default you will get a pef that
requires 8 tiles and you should use --gres=rdu:1 with sbatch.
--nchips=2 will get you a pef that uses 8 tiles.
But if you use ---num-tiles=4 you will only use 1/2 an RDU.
I do not know how to ask for 1/2.
So you will have to use --gres=rdu:1.
With multi-node slurm please not the gres value is the
number of RDUs per NODE!
rick weisner
While using bert I discovered that it wanted an environment
variable named SOFTWARE_HOME defined. This a bug.
As a best practice please use
export SOFTWARE_HOME=/opt
Since 1.14 there is no longer a common venv. Each model has its own venv.
In /opt/sambaflow
./apps/private/anl/venv
./apps/micros/venv
./apps/starters/mlp/venv
./apps/starters/lenet/venv
./apps/starters/ffn_mnist/venv
./apps/starters/logreg/venv
./apps/starters/upscalenet/venv
./apps/starters/power_pca/venv
./apps/image/segmentation_3d/venv
./apps/image/deepvit/venv
./apps/image/segmentation/venv
./apps/image/object_detection/venv
./apps/image/classification/venv
./apps/recommender/dlrm/venv
./apps/recommender/ncf/venv
./apps/recommender/deepinterest/venv
./apps/nlp/transformers_on_rdu/venv
./apps/nlp/transformers_on_rdu/gpt13b/venv
./apps/nlp/data_processing/venv
If in doubt start with:
/opt/sambaflow/apps/private/anl/venv
These machines should not be rebooted, they should be reset.
power off host
  ipmitool -I lanplus -H XX.XX.XX.XX -U xxxxx -P YYYYYYYYYY chassis power soft
login to XRDU0
  ssh -l UN XX.XX.XX.XX
Poweroff xrdus
  xrduutil -U UN -P XXXXXXXXXXXXXXXXXX poweroff
wait 30 sec
  sleep 30
poweron the XRDUs
  xrduutil -U UN -P XXXXXXXXXXXXX poweron
  sleep 30
poweron host
  ipmitool -I lanplus -H XX.XX.XX.XX -U UN -P YYYYYYYYYY chassis power on  
!!!!!!!!!!!!!!!!!!
scancel should ran against running jobs.
scancel.exe should be ran against pending jobs.
Additionally, the `---full` option  helps ensure that the signal is sent to every process in the SLURM job. In general, we recommend using these two options with scancel.
scancel --signal=TERM --full
scancel now does TERM by default. If you need the old behavior use scancel.exe.
#################################### Please note update on 12-20-2023 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Now Running Sambaflow 1.17.7-27
Acceptance Test scripts are in /data/ANL/scripts.
Acceptance Test results are in /data/ANL/results.
Older scripts are in /data/ANL/scripts/1.17.4-28
see /data/ANL/scripts/model_all_run.sh  for examples on how to run each test.
see also /data/ANL/scripts/Readme. 
snfadm will report 8 RDUS.
In 1.16 for the purpose of slurm there were 16 four tile RDUS.  
IN 1.17 slurm now thinks that there are 8 RDUs.
sinfo -O AllocNodes,GresUsed,Gres,NodeList
ALLOCNODES          GRES_USED           GRES                NODELIST            
oll                 rdu:0,rdu_mem:0,rdu_rdu:8,rdu_mem:104854sn30-r1-h[1-2],sn30-
Now
If you compile, then by default you will get a pef that
requires 8 tiles and you should use --gres=rdu:1 with sbatch.
--nchips=2 will get you a pef that uses 8 tiles.
But if you use ---num-tiles=4 you will only use 1/2 an RDU.
I do not know how to ask for 1/2.
So you will have to use --gres=rdu:1.
With multi-node slurm please not the gres value is the
number of RDUs per NODE!
rick weisner
While using bert I discovered that it wanted an environment
variable named SOFTWARE_HOME defined. This a bug.
As a best practice please use
export SOFTWARE_HOME=/opt
Since 1.14 there is no longer a common venv. Each model has its own venv.
In /opt/sambaflow
./apps/private/anl/venv
./apps/micros/venv
./apps/starters/mlp/venv
./apps/starters/lenet/venv
./apps/starters/ffn_mnist/venv
./apps/starters/logreg/venv
./apps/starters/upscalenet/venv
./apps/starters/power_pca/venv
./apps/image/segmentation_3d/venv
./apps/image/deepvit/venv
./apps/image/segmentation/venv
./apps/image/object_detection/venv
./apps/image/classification/venv
./apps/recommender/dlrm/venv
./apps/recommender/ncf/venv
./apps/recommender/deepinterest/venv
./apps/nlp/transformers_on_rdu/venv
./apps/nlp/transformers_on_rdu/gpt13b/venv
./apps/nlp/data_processing/venv
If in doubt start with:
/opt/sambaflow/apps/private/anl/venv
These machines should not be rebooted, they should be reset.
power off host
  ipmitool -I lanplus -H XX.XX.XX.XX -U xxxxx -P YYYYYYYYYY chassis power soft
login to XRDU0
  ssh -l UN XX.XX.XX.XX
Poweroff xrdus
  xrduutil -U UN -P XXXXXXXXXXXXXXXXXX poweroff
wait 30 sec
  sleep 30
poweron the XRDUs
  xrduutil -U UN -P XXXXXXXXXXXXX poweron
  sleep 30
poweron host
  ipmitool -I lanplus -H XX.XX.XX.XX -U UN -P YYYYYYYYYY chassis power on  
!!!!!!!!!!!!!!!!!!
scancel should ran against running jobs.
scancel.exe should be ran against pending jobs.
Additionally, the `---full` option  helps ensure that the signal is sent to every process in the SLURM job. In general, we recommend using these two options with scancel.
scancel --signal=TERM --full
scancel now does TERM by default. If you need the old behavior use scancel.exe.
kevinfang@sn30-r4-h1:~$ git clone https://github.com/argonne-lcf/ai-science-training-series.git/
kevinfang@sn30-r4-h1:~$ cd ai-science-training-series/07_AITestbeds/Sambanova/bert/
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ chmod +x BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.07/BertLarge.out for output
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  BertLarge_run.sh	BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  BertLarge_run.sh	BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
/home/kevinfang/BertLarge/bertlrg/bertlrg.pef exists
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ chmod +x BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
/home/kevinfang/BertLarge/bertlrg/bertlrg.pef exists
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  112024.08  BertLarge_run.sh  BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ rm -rf 112024.08
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  BertLarge_run.sh	BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh 
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  112024.08  BertLarge_run.sh  BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ rm 112024.08
rm: cannot remove '112024.08': Is a directory
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  112024.08  BertLarge_run.sh  BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ rmdir 112024.08
rmdir: failed to remove '112024.08': Directory not empty
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ cd ai-science-training-series/07_AITestbeds/Sambanova/bert/
-bash: cd: ai-science-training-series/07_AITestbeds/Sambanova/bert/: No such file or directory
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ cd 112024.08
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ ls
BertLarge.out
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ cd ..
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ vim BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ chmod +x BertLarge.sh
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
/home/kevinfang/BertLarge/bertlrg/bertlrg.pef exists
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  112024.08  BertLarge_run.sh  BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ cd ..
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova$ cd ..
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds$ cd ..
kevinfang@sn30-r4-h1:~/ai-science-training-series$ cd ..
kevinfang@sn30-r4-h1:~$ ls
ai-science-training-series  BertLarge  slurm-43631.out	slurm-43632.out  slurm-43634.out  slurm-43635.out  slurm-43637.out  slurm-43639.out
kevinfang@sn30-r4-h1:~$ cd BertLarge/
kevinfang@sn30-r4-h1:~/BertLarge$ ls
112024.08  bertlrg  cache  hf_output
kevinfang@sn30-r4-h1:~/BertLarge$ cd bertlrg/
kevinfang@sn30-r4-h1:~/BertLarge/bertlrg$ rm bertlrg.pef
kevinfang@sn30-r4-h1:~/BertLarge/bertlrg$ cd ..
kevinfang@sn30-r4-h1:~/BertLarge$ cd ..
kevinfang@sn30-r4-h1:~$ cd ai-science-training-series/07_AITestbeds/Sambanova/
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova$ cd bert/
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ls
111924.07  112024.07  112024.08  BertLarge_run.sh  BertLarge.sh  bert.md
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ cd 112024.08
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ ls
BertLarge.out
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ mv BertLarge.out BertLarge-08.out
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ ls
BertLarge-08.out
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08$ cd ..
kevinfang@sn30-r4-h1:~/ai-science-training-series/07_AITestbeds/Sambanova/bert$ ./BertLarge.sh
Using /home/kevinfang/ai-science-training-series/07_AITestbeds/Sambanova/bert/112024.08/BertLarge.out for output
```
</details>


- Compiled logs
  - [BertLarge.out](BertLarge.out) - 16 tasks (default) should provide efficient parallelism and training throughput by allowing more tasks to work simultaneously.
  - [BertLarge-32.out](BertLarge-32.out) - 32 tasks should provide a higher degree of parallelism but may encounter diminishing returns if there’s excessive communication overhead.


## Useful Links 

* [Overview of AI Testbeds at ALCF](https://www.alcf.anl.gov/alcf-ai-testbed)
* [ALCF AI Testbed Documentation](https://www.alcf.anl.gov/support/ai-testbed-userdocs/)
* [Director’s Discretionary Allocation Program](https://www.alcf.anl.gov/science/directors-discretionary-allocation-program)
* [ALCF Events Page](https://www.alcf.anl.gov/events/intro-ai-series-ai-accelerators-0)  

##### Acknowledgements

Contributors: [Siddhisanket (Sid) Raskar](https://sraskar.github.io/), [Murali Emani](https://memani1.github.io/), [Varuni Sastry](https://www.alcf.anl.gov/about/people/varuni-katti-sastry), [Bill Arnold](https://www.alcf.anl.gov/about/people/bill-arnold), and  [Venkat Vishwanath](https://www.alcf.anl.gov/about/people/venkatram-vishwanath).

> This research used resources of the Argonne Leadership Computing Facility, which is a DOE Office of Science User Facility supported under Contract DE-AC02-06CH11357.
