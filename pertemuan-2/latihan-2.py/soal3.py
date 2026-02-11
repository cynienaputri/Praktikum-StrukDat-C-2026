tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL","NodeJS"}

# No 3.1
irisan_FE_BE = tim_frontend.intersection(tim_backend)
print(f'Irisan dari tim frontend dan tim backend adalah : {irisan_FE_BE}')

# No 3.2
    # Cara 1
BE_only_cara1 =  tim_backend - tim_frontend
print(f'Mencari FE Komplemen (cara 1) : {BE_only_cara1}')

    # Cara 2
BE_only_cara2 = tim_backend.difference(tim_frontend)
print(F'Mencari FE Komplemen (cara 2) : {BE_only_cara2}')