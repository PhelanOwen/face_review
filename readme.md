You'll need to run the following command to get this to work:

```python -m pip install -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle kivy```
```python -m pip install -y face_recognition tensorflow pil```

Once these are correctly installed, the process should be simple:
* Run the <b>face_review.py</b> script to open the main app. Continue rating people (I'm using about 700 altogether for testing).
* You can check your progress using the <b>result_check.py</b> script at any time.
* Once you are happy with the number of results (the more the merrier, try to fill a reasonable amount for each 1-5), run the <b>categorise.py</b> script to sort the data into folders.

TODO:
Add AI part
