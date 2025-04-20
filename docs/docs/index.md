# Documentation

---

## **Description**

Implemented a deep **learning-based image** compression system using **discretized Gaussian Mixture Models** for precise entropy estimation and **attention modules** to improve visual quality. Achieves **state-of-the-art** compression performance with fewer bits and better image reconstruction, matching or outperforming standards like `JPEG`, `JPEG2000`, `HEVC`, and even `VVC` in `PSNR` and `MS-SSIM`.

## **Commands**

All common tasks for this project are exposed via the Makefile. To see a complete list of available targets and their descriptions, run:

```bash
make help
```

## **Citation**

Please cite the following paper if you use this work:

```bibtex
@inproceedings{cheng2020image,
    title     = {Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules},
    author    = {Cheng, Zhengxue and Sun, Heming and Takeuchi, Masaru and Katto, Jiro},
    booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    year      = {2020}
}
```

## **License**

The license for this project can be found here: [MIT](./LICENSE)
