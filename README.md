# 🔢 Random Pulse Generator

এই প্রজেক্টে প্রতি **১০ মিনিটে একটি নতুন এলোমেলো সংখ্যা** তৈরি হয় এবং `data/latest.json` ফাইলে সংরক্ষণ করা হয়।  
এই সংখ্যা এবং সময় **GitHub Pages** ওয়েবসাইটে বাংলায় প্রদর্শিত হয়।

---

## ⚙️ সেটআপ নির্দেশিকা

1. **রিপো ফর্ক করুন অথবা নতুন রিপোতে আপলোড করুন**
2. **GitHub PAT (Personal Access Token) তৈরি করুন**
   - Settings → Developer settings → Tokens → Fine-grained PAT
   - পারমিশন দিন: `repo` → `contents: write`
   - রিপোতে গিয়ে **Settings → Secrets → Actions → New repository secret** এ `GH_PAT` নামে সেভ করুন
3. `.github/workflows/pulse.yml` ফাইলটি আগে থেকেই কনফিগার করা আছে
4. `pulse.py` স্ক্রিপ্ট প্রতি রান-এ একটি সংখ্যা তৈরি করবে
5. GitHub Actions প্রতি **১০ মিনিটে রান** করে `latest.json` আপডেট করবে
6. **GitHub Pages চালু করুন**
   - Settings → Pages → Branch `main` + Folder `/ (root)` সিলেক্ট করুন
   - Save করুন
7. এখন আপনার সাইটের লিংক হবে:
