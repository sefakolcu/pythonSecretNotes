import tkinter as tk
from PIL import ImageTk, Image
import EncryptionPackage.stringCryption
import EncryptionPackage.stringUncryption
import SecretNotes

control_string_for_password = str()
control_list_for_password = list()


def on_client_crypt_click():
    collected_text_for_cryption = screen_text_entrance.get("1.0", tk.END)
    collected_password_for_cryption = screen_password_entrance.get()
    if collected_password_for_cryption == " ":
        if not collected_text_for_cryption == " ":
            cryp_note = EncryptionPackage.stringCryption.string_cryption_main(collected_text_for_cryption)

            SecretNotes.strings_to_add_in_file(cryp_note)

            information_text_update()
            text_entrance_update(cryp_note)
        else:
            print("Herhangi bir değer girilmedi")
    else:
        if not collected_text_for_cryption == " ":
            cryp_pw = EncryptionPackage.stringCryption.string_cryption_password_main(collected_text_for_cryption,
                                                                                     collected_password_for_cryption)
            SecretNotes.strings_to_add_in_file(cryp_pw)

            information_text_update()
            text_entrance_update(cryp_pw)
        else:
            print("Herhangi bir değer girilmedi")


def on_client_uncrypt_click():
    global control_string_for_password
    global control_list_for_password
    collected_text_for_uncryption = screen_text_entrance.get("1.0", tk.END)
    collected_password_for_uncryption = screen_password_entrance.get()

    for control_password in collected_text_for_uncryption:
        control_string_for_password = control_string_for_password + control_password
        if len(control_string_for_password) == 4:
            control_list_for_password.append(control_string_for_password)
            control_string_for_password = ""

    if "A9B8" in control_list_for_password:
        if not collected_text_for_uncryption == " ":
            unc_pw = (EncryptionPackage.stringUncryption.string_uncryption_password_main
                        (collected_text_for_uncryption, collected_password_for_uncryption))

            SecretNotes.strings_to_add_in_file(unc_pw)

            information_text_update()
            text_entrance_update(unc_pw)
        else:
            print("Herhangi bir değer girilmemiş")
    else:
        if not collected_text_for_uncryption == " ":
            unc_note = EncryptionPackage.stringUncryption.string_uncryption_main(collected_text_for_uncryption)

            SecretNotes.strings_to_add_in_file(unc_note)

            information_text_update()
            text_entrance_update(unc_note)

        else:
            print("Herhangi bir değer girilmemiş")


screen_window = tk.Tk()
screen_window.geometry("350x450")
screen_image = ImageTk.PhotoImage(Image.open("topsecret.png").resize((75, 75)))
screen_image_label = tk.Label(image=screen_image)
screen_text_entrance = tk.Text(width=30, height=7)
screen_text_entrance.insert(1.0, "")
screen_password_entrance = tk.Entry(width=40)
screen_password_entrance.insert(0, "")
screen_crypt_button = tk.Button(text="Crypt", width=10, command=on_client_crypt_click)
screen_uncrypt_button = tk.Button(text="Uncrypt", width=10, command=on_client_uncrypt_click)
screen_text_label = tk.Label(text="Lütfen Metnini Girin!")
screen_text_label_password = tk.Label(text="Lütfen Şifreyi Girin! (Opsiyonel)")
screen_text_label_status = tk.Label(text="")

screen_window.update()

screen_width = screen_window.winfo_width()
screen_height = screen_window.winfo_height()


def make_widgets_visible():
    screen_image_label.place(x=screen_width / 2 - 25, y=screen_height / 2 - 210)
    screen_text_entrance.place(x=screen_width / 2 - 115, y=screen_height / 2 - 90)
    screen_password_entrance.place(x=screen_width / 2 - 115, y=screen_height / 2 + 60)
    screen_crypt_button.place(x=screen_width / 2 - 30, y=screen_height / 2 + 100)
    screen_uncrypt_button.place(x=screen_width / 2 - 30, y=screen_height / 2 + 140)
    screen_text_label.place(x=screen_width / 2 - 115, y=screen_height / 2 - 115)
    screen_text_label_password.place(x=screen_width / 2 - 115, y=screen_height / 2 + 35)
    screen_text_label_status.place(x=screen_width / 2 - 70, y=screen_height / 2 + 190)


def information_text_update():
    screen_text_label_status.config(text="Sistem Durumu: Hazırlanıyor!")


def text_entrance_update(main_string):
    screen_text_entrance.delete(1.0, tk.END)
    screen_text_entrance.insert(1.0, main_string)
    screen_text_label_status.config(text="Sistem Durumu: Hazırlandı!")


make_widgets_visible()

screen_window.mainloop()
