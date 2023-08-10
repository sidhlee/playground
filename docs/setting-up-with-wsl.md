# Setting up with WSL

Things I did to set up a Django project with WSL

## Get the lastest WSL Ubuntu

I had version 18 of Ubuntu and saw 20.04 from the store.
Initially I tried to follow some article to upgrade existing version, but that didn't work out well, so I just installed version 20 directly from the store.

- I uninstalled the old version (18) not knowing that all the file systems are bound to that specific version. So my old project folder was gone as well. Shouldn't be a problem if you're commiting to the GitHub.
- You need to run the new Ubuntu (20) just like any other windows app so that you can create your project folder inside the linux file system.
- Create project folder inside `/home/sidhlee/` and run `code .` to open up in the VSCode.

## Creating virtual environment

First time I ran `python3 -m vent venv` the following message came up:

```bash
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.8-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

You need to run `sudo apt update` before running `sudo apt install python3.8-venv` because you just installed new Ubuntu.

Now you can create virtual env by `python3 -m venv venv` and activate it.

## Installing Django

Make sure you activated virtual env before installing Django.

```bash
python -m pip install Django
```

After installing Django, you can create requirements file by:

```bash
pip freeze > requirements.txt
```

Lastly, don't forget to create `.gitignore` before `git init`.
