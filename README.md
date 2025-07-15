# Valorant Vanguard Control Script

## What is this?

This Python script provides an interactive menu to control Riot Games' Vanguard anti-cheat for Valorant.  
You can start, stop, uninstall Vanguard, and configure its startup behavior directly from this tool.

---

## Important!

- This script is **for troubleshooting only** and **should not be used to bypass** anti-cheat protections.  
- Stopping or uninstalling Vanguard may cause Valorant to stop working.  
- You must run this script with **administrator privileges**.  
- Close Valorant before running the script.  
- Use at your own risk.

---

## Features / Menu options

1. **Start Vanguard services** (`vgk` and `vgc`)  
2. **Stop Vanguard services**  
3. **Uninstall Vanguard completely** (stops services, deletes them, and removes program files)  
4. **Configure Vanguard startup behavior**  
   - Enable Vanguard to start automatically at Windows startup  
   - Disable Vanguard auto-start  
5. Exit the program

---

## How to use?

1. Download `Main.py` from this repository.  
2. Make sure you have Python installed on your Windows system.  
3. Close Valorant completely.  
4. Open **Command Prompt as Administrator**.  
5. Navigate to the folder where `Main.py` is located.  
6. Run the script by typing:

   ```cmd
   python Main.py
   ```

7. Use the menu to choose the desired action.  
8. Follow the on-screen prompts.  
9. When finished, select "Exit" from the menu or close the window.

---

## Notes

- Running uninstall will remove Vanguard files and stop the services. You will need to reboot your PC after uninstalling.  
- Changing startup behavior affects whether Vanguard runs automatically when Windows boots.  
- If services fail to stop or start, ensure you are running the script as Administrator.  
- Vanguard may restart automatically in some cases.

---

## Disclaimer

This script is provided **as-is** for educational and troubleshooting purposes only.  
The author is not responsible for any damage or bans caused by misuse.  
Do **NOT** use this tool to cheat or bypass Valorant’s anti-cheat.

---

## License

MIT License [LICENSE](https://github.com/hjcs-dev/Vanguard-Control/blob/main/LICENSE)

---

## Contact

For questions or issues, please open an issue in this repository.

---

*Thank you for using responsibly!*
