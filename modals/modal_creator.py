file = open("modals.html", 'a')

#this is in order 1 applies to number one on the map etc.
Names = [
"", # 0 based indexing
            "", # 1
            "Condor parking area",
            "",
            "",
            "The R. Johnson Building",
            "Vonnegut Humanities Department.",
            "Zizek Social Sciences building",
            "Trump Business College",
            "Twintail Urgent Care",
            "To be demolished",
            "P Garfield Chemistry Building", #10
            "Macow International Administration building",
            "Lyrebirds Dormitory",
            "Student Union Building: SUB",
            "Club Administration Area",
            "Magpie building",
            "Palmer Dorms",
            "Bookstore",
            "Swansons School of Music",
            "Crows Nest Library",
            "P Saml Engineering college.", #20
            "Parking mgmt",
            "Wren Activity Center",
            "RoadRunner college of Sports Science",
            "Whydah Dormitories",
            "The River Access Center",
            "Accentor Dormitories",
            "Parrotbill Agricultural Center",
            "Warbler Math Department",
            "",
            "Cowbird Bridge", #30
            "",
            "Varinka nuclear reactor",
            "Grosbeak Laboratory Sciences",
            "Water Treatment",
            "",
            "",
            "",
            "",
            "",
            "", #40
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "", #50
]

details = [
            "", # 0 based indexing
            "The statue of Brewer Mayor Tom Dickinson", # 1
            "An on-campus parking lot restricted to students and faculty possessing a B level parking pass, purchasable at the front desk.",
            "",
            "",
            "The twin R. Johnson buildings are the newest building at NEST. Here youll find all the latest and greatest technological advancements in the Computer Science department.",
            "Dedicated to Kurt Vonnegut, writer and humorist best known for his novel Slaughterhouse Five. Here students participate in languages, histories and many discussion-based classes designed to help them unfurl their wings as future writers, speakers and community members. ",
            "",
            "Dedicated 24/7 Urgent care. Students can be ensured that they will be in qualified medical hands while studying at NEST.",
            "",
            "",
            "", #10
            "",
            "Get adjusted to campus and American life in our special optional dormitories for foreign exchange students. Here you will find translators and other services meant to help you adjust to our university.",
            "At the Student Union you will find great food and great friends.",
            "",
            "If your laptop is acting funny, head over to the Magpie building to let one of our techs take a look!",
            "",
            "",
            "Swanson School of Music allows students to immerse themselves in a large variety of musical styles from a number of different eras.",
            "The Crows Nest library offers students a variety of quality learning resources. With the latest in both print and digital books, students can access updated materials to meet their educational needs.",
            "The P Samul Engineering college is dedicated to making sure each of its students is prepared for a rigorous engineering job immediately after graduation.", #20
            "The New England School of Technology features state of the art, cutting edge technology for premium parking on campus. We offer affordable pricing for students, staff, and visitors.",
            "",
            "RoadRunner has classes in Sports Medicine, Sport Science, and other sports theory classes.",
            "Beautiful rustic looking Dormitories with plenty of amenities.",
            "Enjoy Rowing, Swimming and other water sports in our natural blocked off swimming area.",
            "Beautiful rustic looking Dormitories with plenty of amenities.",
            "",
            "The best mathematical minds come together to ensure you understand both the theoretical and applicable parts of mathematical sciences.",
            "",
            "The famous Cowbird Bridge is a great place for a view of the riven, and allows access to the nuclear reactor and Grosbeak labs.", #30
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "", #40
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "", #50
        ]


for x in range(0, 45):
    html = '<form id="NAME" class="modal">\n  <div style="min-width:900px">\n    <img src="images/NUMBER.jpg" width="400px"/><br>\n    <span class="nameText"><b>PLACE</b></span>\n    <span class="detail_text">Details:</span>\n    <div class="details">DETAILS</div>\n    <a class="closer" href="images/NUMBER.jpg">Full Size</a>\n  </div>\n</form>\n'
    html = html.replace("NAME", "a"+str(x))
    html = html.replace("NUMBER", "temp") #str(x))
    html = html.replace("DETAILS", details[x])
    html = html.replace("PLACE", Names[x])

    file.write(html)

file.close() 