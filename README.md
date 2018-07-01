# ImageTranslation
pytorch, pix2pix, CycleGAN, DiscoGAN, BicycleGAN, UNIT, MUNIT

- ![Pix2Pix](https://github.com/suhoy901/ImageTranslation/blob/master/Pix2Pix/1.%20Pix2Pix_train.ipynb)
- ![CycleGAN](https://github.com/suhoy901/ImageTranslation/blob/master/CycleGAN/2.%20CycleGAN_train.ipynb)

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

## 4. BicycleGAN

## 5. UNIT

## 6. MUNIT
