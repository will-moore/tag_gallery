# tag_gallery
An OMERO.web app for showing a gallery of images.
We use Tags with prefix of 'Gallery-' to mark which
images are in each Gallery.


## Instructions:

Clone this repo.

Add the folder that contains this repo to your $PYTHONPATH,
so that in python you can import the ```tag_gallery``` module.

Add (*append*) this app to your OMERO.web apps.

	$ bin/omero config append omero.web.apps '"tag_gallery"'

Add a ```top_link``` to the gallery home page:

	$ bin/omero config append omero.web.ui.top_links '["Gallery", "tag_gallery_index", {"title": "Open Image Gallery"}]'

Restart OMERO.web to see these settings take effect.

Now you can tag a bunch of Images with tags starting with "Gallery-".
If you follow the Gallery link at the top of the webclient, you will see a list of all the
Galleries.
Clicking on the link will take you to the Gallery, showing you the image thumbnails.
Clicking an image will show you the full viewer.

NB: The Gallery home page will show you ALL the Galleries (tags) that you can access,
across all of your groups. For example, in the screenshot below, "Ben's Gallery" is
in a different group from the other tags that are shown in the webclient.


<img width="727" alt="screen shot 2017-06-04 at 23 09 58" src="https://cloud.githubusercontent.com/assets/900055/26765863/c9dcdd0e-497c-11e7-818a-84bb57b62e82.png">

