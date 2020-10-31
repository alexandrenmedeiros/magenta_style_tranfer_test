# Fast Style Transfer ( [Magenta](https://github.com/magenta/magenta/tree/master/magenta/models/arbitrary_image_stylization) )

This code load and apply the fast arbitrary style transfer model using the tensorflow hub. I did it to test the model by myself.

This model is a distinc approach to the style transfer models. The [original work](https://arxiv.org/abs/1508.06576) realized the style transfer by continuously iterating over some VGG019 layers, wich was a slow method. [Other models](https://arxiv.org/abs/1610.07629) have done an optimization creating different networks for each style. In that way, you could do real time style transfer, but it was limited by a set of styles. [This method](https://arxiv.org/abs/1705.06830) does arbitrary style transfer in real time. It achieves that by training a network that predict the style in addition to the others networks used in the older methods.
