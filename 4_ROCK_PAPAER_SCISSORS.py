print("welcome USER")
user1=input("enter your choice user1:(rock,paper,scissors)")
user2=input("enter your choice user2:(rock,paper,scissors)")
if user1=="rock" and user2=="rock":
    print("user1")
    print("""
              _______
            ---'   ____)
                 (_____)
                 (_____)
                  (____)
            ---.__(___) """)
    print("user2")
    print("""
              _______
            ---'   ____)
                 (_____)
                 (_____)
                  (____)
            ---.__(___) """)
    print("oops, its a draw")
elif user1=="paper" and user2=="paper":
    print("user1")
    print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
    print("user1")
    print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
    print("oops, its a draw")
elif user1=="scissors" and user2=="scissors":
    print("user1")
    print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
    print("user1")
    print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
  
    print("oops, its a draw")
elif user1=="rock" and user2=="paper":
     print("user1")
     print("""
                 _______
             ---'   ____)
                  (_____)
                  (_____)
                   (____)
             ---.__(___) """)
     print("user2")
     print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
     print("user 2 wins")
elif user1=="rock" and user2=="scissors":
     print("user1")
     print("""
                 _______
             ---'   ____)
                  (_____)
                  (_____)
                   (____)
             ---.__(___) """)
     print("user2")
     print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
  
    
     print("user 1 wins")

elif user1=="paper" and user2=="scissors":
     print("user1")
     print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
     print("user2")
     print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
  
    
     print("user 2 wins")


elif user1=="paper" and user2=="rock":
     print("user1")
     print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
     print("user2")
     print("""
              _______
            ---'   ____)
                 (_____)
                 (_____)
                  (____)
            ---.__(___) """)
    
     print("user 1 wins")


elif user1=="scissors" and user2=="rock":
     print("user1")
     print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
  

     print("user2")
     print("""
              _______
            ---'   ____)
                 (_____)
                 (_____)
                  (____)
            ---.__(___) """)
    
     print("user 2 wins")

elif user1=="scissors" and user2=="paper":
     print("user1")
     print("""
        ---'   ____)____
                   ______)
                __________)
             (____)
        ---.__(___)
   """)
  

     print("user2")
     print("""
        ---'   ____)____
                  ______)
                 _______)
                 _______)
        ---.__________)
""")
    
     print("user 1 wins")
else:
     print("enter valid command")
