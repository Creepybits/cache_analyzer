# Cache Analyzer
Analyzes and shows the cache size of Hugging Face, Triton, Pytorch and pip
___

### Run The Script

Open CMD or Powershell in the same folder your cache_analyzer.py script is located. Type `python cache_analyzer.py`  
**Note**: The script only has reading access and can not alter any files!

___
### Move Cache Location  (Windows)
If you find that, for example, Hugging Face is taking up too much of your system disk, you can move the cache location to a second disk by following these steps.  

* Right-click on your windows icon and choose _system_
* Pick _advanced system settings_
* Open _environment variables_
* Under _system variables_ click on _new_
* In _Variable Name_ type **HF_HOME**
* In _Variable Value_ type **path/to/new_cache**

![Skärmbild 2025-06-28 144018](https://github.com/user-attachments/assets/d1d83209-28a5-4dbe-b9dc-5e4fbb3d186a)

Click _OK_ to save and exit.  

**Optional**: Verify the new location by opening a new Powershell window and type `echo $env:HF_HOME`  
