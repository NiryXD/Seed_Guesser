# Brute Force Seed Phrase Guesser 🚀

**WARNING: Not Suitable for Real Cryptography!** ⚠️  
This project is a brute force seed phrase guesser that’s as **efficient as Bogosort** – meaning it’s not efficient at all. With a complexity of **O(n!)**, it ensures your GPU gets a workout while you marvel at the futility of brute-forcing mnemonic seed phrases.

---

## 🚀 Features

- Generates 12- or 24-word **random seed phrases** using the BIP-39 word list.
- A **graphical interface** (GUI) built with `CustomTkinter` for ease of use.
- Absolutely **not practical** for recovering lost crypto wallets.
- Provides a fun and educational demonstration of why cryptographic security works! 🤓

---

## 📚 How It Works

1. Choose between a 12-word or 24-word seed phrase in the GUI.
2. The program generates random words from the BIP-39 word list (2048 entries).
3. Attempts to brute-force the correct combination. *(Just kidding! It simply generates phrases randomly.)*

---

## 💡 Complexity

- The algorithm is comparable to **Bogosort**, where we "randomly shuffle until sorted." 🤪
- **Time complexity**: **O(n!)** for the guessing part *(if implemented seriously, but don’t do that)*.  
  For 24 words:  
  `24! = 6.204 × 10^23`  
  Which means you'd be waiting longer than the age of the universe for results! 🕰️

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/niryxd/seed-phrase-guesser.git
   cd seed-phrase-guesser
2. Download the BIP-39 word list:

https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt.

3. Run the app:
   ```bash
   python seed_phrase_guesser.py

---

## 🖼️ GUI Preview

The intuitive interface lets you choose between a 12-word or 24-word seed phrase with a single click.

---

## 🤝 Acknowledgments

This project was created for fun and educational purposes, with a **little help from AI** (thanks, ChatGPT!). The AI-assisted brainstorming and coding guidance made it much easier to implement this amusing tool.

---

## ⚠️ Disclaimer

This tool is strictly for **educational purposes** and not intended for any real-world cryptographic usage. It does not attempt to recover or guess actual wallets or private keys. **Do not rely on this tool for any serious application.**

---

## 📜 License

MIT License – Do whatever you want, but please don’t use this for malicious purposes. Be kind to your fellow crypto users.

---

Enjoy the irony of brute-forcing one of the most secure systems ever designed!

![Alt text](https://media.giphy.com/media/TamGVAGxDTYDNt3dpn/giphy.gif)



