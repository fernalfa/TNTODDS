import tkinter as tk
from tkinter import ttk

from functions import (
    clear_console,
    extract_list,
    sorted_list_player_doubles,
    sorted_list_special_props,
    boosted_odds_enter,
    Create_by_Category,
    Merge_Player_with_Odds,
    create_players,
    delete_contenders,
    list_extractor,
    list_extractor_provider,
    missing_players,
    odds_compare,
    linealodds,
    Multi_Banner,
    Multi_Final,
    Multi_Select,
    TEXT_SEARCH,
    start_games,
    start_rot_py,
)


def create_label(parent, text, row, column, columnspan=2, width=None):
    if isinstance(text, list):
        label = tk.Label(parent, text='\n'.join(text), width=width)
    else:
        label = tk.Label(parent, text=text, width=width)
    label.grid(row=row, column=column, columnspan=columnspan)

def create_button(parent, text, row, column, command, padx=10, pady=10):
    button = tk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady)

def create_popup():
    popup = tk.Tk()
    popup.title("Office Tools- Menus and Tabs")

    # Create a menu bar
    menu_bar = tk.Menu(popup)
    popup.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Clear Console", command=clear_console)
    file_menu.add_separator()


    label_width = 15  # Adjust the width as needed

    tab_control = ttk.Notebook(popup)

    # FIRST Tab
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='TNT TOOLS')

    # FIRST Label
    create_label(tab1, "DATA ENTRY", 0, 0, columnspan=1, width=label_width)
    create_button(tab1, "Enter Compared Odds", 1, 0, odds_compare)
    create_button(tab1, "Create by Category", 2, 0, Create_by_Category)
    create_button(tab1, "Create Missing Players", 3, 0, create_players)
    # SECOND Label
    create_label(tab1, ["TEXT EXTRACT"], 0, 1, columnspan=1, width=label_width)
    create_button(tab1, "Extract Data List", 1, 1, list_extractor)
    create_button(tab1, "Extract Provider List", 2, 1, list_extractor_provider)
    create_button(tab1, "Check Missing Players", 3, 1, missing_players)
    # THIRD Label
    create_label(tab1, "EXTRA TOOLS", 0, 2, columnspan=1, width=label_width)
    create_button(tab1, "Delete\nEMPTY Contenders", 1, 2, delete_contenders)
    create_button(tab1, "Merge 2 List\nPlayer with Odds", 2, 2, Merge_Player_with_Odds)


    # SECOND Tab
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='ODDS BOOSTS')
    create_button(tab2, "Extract LIST", 1, 0, extract_list)
    create_button(tab2, "Extract PLAYER DOUBLES (A-Z)", 2, 0, sorted_list_player_doubles)
    create_button(tab2, "Extract PLAYER SPECIALS (A-Z)", 3, 0, sorted_list_special_props)
    create_button(tab2, "Enter Compared Odds", 1, 1, boosted_odds_enter)
    create_button(tab2, "Transform Lineal Odds", 2, 1, linealodds)


    # THIRD Tab
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='EXTRA TOOLS')
    create_label(tab3, "EXTRA TOOLS", 0, 0, columnspan=1, width=label_width)
    # FIRST Label
    create_button(tab3, "Specific Text Search", 1, 0, TEXT_SEARCH)
    create_button(tab3, "ROT Tools", 2, 0, start_rot_py)
    create_button(tab3, "Stop / Start Games", 3, 0, start_games)
    # SECOND Label
    create_button(tab3, "Player Props Banner Create", 1, 1, Multi_Banner)
    # THIRD Label
    create_button(tab3, "Multi Select", 1, 2, Multi_Select)
    create_button(tab3, "Multi Final", 2, 2, Multi_Final)
    tab_control.pack(expand=1, fill="both")

    popup.mainloop()
# Show the pop-up window
create_popup()
