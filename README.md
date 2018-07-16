# ImageTranslation
pytorch, pix2pix, CycleGAN, DiscoGAN, BicycleGAN, UNIT, MUNIT

- [Pix2Pix](https://github.com/suhoy901/ImageTranslation/blob/master/Pix2Pix/1.%20Pix2Pix_train.ipynb)
- [CycleGAN](https://github.com/suhoy901/ImageTranslation/blob/master/CycleGAN/2.%20CycleGAN_train.ipynb)
- [DiscoGAN](https://github.com/suhoy901/ImageTranslation/blob/master/DiscoGAN/DiscoGAN.ipynb)
- [BicycleGAN_edges2shoes](https://github.com/suhoy901/ImageTranslation/blob/master/BicycleGAN/2.%20BicycleGAN_edges2shoes_train.ipynb)

## 1. Pix2Pix
- facades

<table>
  <tr>
    <td style="text-align: middle;">Input</td>
    <td style="text-align: middle;">Generated</td>
    <td style="text-align: middle;">Target</td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/a/cmp_b0206.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/result/facades/cmp_b0206.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/b/cmp_b0206.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/a/cmp_b0239.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/result/facades/cmp_b0239.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/b/cmp_b0239.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/a/cmp_b0360.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/result/facades/cmp_b0360.jpg"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/Pix2Pix/dataset/facades/test/b/cmp_b0360.jpg"/>
    </td>
  </tr>
</table>

## 2. CycleGAN
- horse2zebra

<table>
  <tr>
    <td style="text-align: middle;">Loss Function</td>
    <td style="text-align: middle;">Generated<br>(Input, Generated, Reconstructed)</td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_results/Loss_values_epoch_200.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_results/horse2zebra_CycleGAN_epochs_200.gif"/>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td style="text-align: middle;">AtoB<br>(Input, Generated, Reconstructed)</td>
    <td style="text-align: middle;">BtoA<br>(Input, Generated, Reconstructed)</td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/AtoB/Test_result_118.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/BtoA/Test_result_118.png"/>
    </td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/AtoB/Test_result_62.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/BtoA/Test_result_62.png"/>
    </td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/AtoB/Test_result_98.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/CycleGAN/horse2zebra_test_results/BtoA/Test_result_98.png"/>
    </td>
  </tr>
</table>

## 3. DiscoGAN
- edges2shoes

<table>
  <tr>
    <td style="text-align: middle;">real_A, fake_B<br>real_B, fake_A
</td>
  </tr>
  <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/DiscoGAN/results/samples_animation.gif"/>
    </td>
</table>
<table>
   <tr>
    <td style="text-align: middle;">AtoB<br>(Input, Generated, Reconstructed)</td>
    <td style="text-align: middle;">BtoA<br>(Input, Generated, Reconstructed)</td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/DiscoGAN/results/25.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/DiscoGAN/results/51.png"/>
    </td>
  </tr>
  <tr>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/DiscoGAN/results/74.png"/>
    </td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/DiscoGAN/results/97.png"/>
    </td>
  </tr>
</table>

## 4. BicycleGAN
- edges2shoes
- edges2handbags


<table>
  <tr>
    <td style="text-align: middle;">epoch</td>
    <td style="text-align: middle;">edges2shoes</td>
    <td style="text-align: middle;">edges2handbags</td>
  </tr>
  <tr>
    <td>epoch 15</td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/BicycleGAN/result/edges2shoes_gif/BicycleGAN_edges2shoes_epochs_10.gif"/>
    </td>
    <td>
     <img src=""/>
    </td>
  </tr>
  <tr>
    <td>epoch 30</td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/BicycleGAN/result/edges2shoes_gif/BicycleGAN_edges2shoes_epochs_30.gif"/>
    </td>
    <td>
     <img src=""/>
    </td>
  </tr>
  <tr>
    <td>epoch 45</td>
    <td>
     <img src="https://raw.githubusercontent.com/suhoy901/ImageTranslation/master/BicycleGAN/result/edges2shoes_gif/BicycleGAN_edges2shoes_epochs_45.gif"/>
    </td>
    <td>
     <img src=""/>
    </td>
  </tr>
</table>


## 5. UNIT

## 6. MUNIT
