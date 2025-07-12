# cag  

`cag` is a small Python library inspired by this [research](https://arxiv.org/html/2412.15605v1) and [repo](https://github.com/hhhuang/CAG). `cag` is used by [cag_cli](https://github.com/panalexeu/cag_cli.git).

The idea is simple: to define various data loaders for different file formats to ingest new information into a model's context window in a stable and unified format. 

As a unified format, XML was chosen because of its ability to represent text structure with attributes and boundaries. However, in the proposed unified format, only two tags are available:

* `<Context/>` - represents a context root, e.g., a whole file;
* `<ContextUnit/>` - represents some units inside of a file, e.g., pages in a PDF;

Any useful attributes, such as filenames, page numbers, etc., are defined inside the tags above, so the model's understanding is enriched more, providing the possibility to navigate in the context, cite, and quote it.

Currently supported data source loaders are: `img_openai`, `pdf`, `text`.

## Example  

For better understanding, consider this example. For instance, I would like to cache and save in a context window an image of my cat Murchik.

![murchik](./imgs/murchik.jpeg)

To do so, I process the image with the `img_openai` data loader and store the resulting `Context` with a `XMLCtxFormatter`. The resulting `xml` file will look something like this:

```xml
<?xml version="1.0" ?>
<Context name="murchik.jpeg">
	<ContextUnit>The image shows a black cat sitting on top of a red container. The cat has striking yellow eyes and is looking towards the right side of the image. In the background, there are a couple of plant pots, one green and beige with some small green plants growing in it, and another larger red pot containing other plants. The setting appears to be outdoors, possibly in a garden or balcony area, with sunlight casting shadows on the wall behind. The overall scene has a warm and calm atmosphere.</ContextUnit>
</Context>
```

Then this file could be directly provided for a model and parameters cached.

## Installation  

To install the package, run:

```bash
pip install "git+https://github.com/panalexeu/cag.git"
```
