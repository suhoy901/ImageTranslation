import torch
from torch.autograd import Variable
import sys
import time

TOTAL_BAR_LENGTH = 80
LAST_T = time.time()
BEGIN_T = LAST_T


def progress_bar(current, total, msg=None):
    global LAST_T, BEGIN_T
    if current == 0:
        BEGIN_T = time.time()  # Reset for new bar.

    current_len = int(TOTAL_BAR_LENGTH * (current + 1) / total)
    rest_len = int(TOTAL_BAR_LENGTH - current_len) - 1

    sys.stdout.write(' %d/%d' % (current + 1, total))
    sys.stdout.write(' [')
    for i in range(current_len):
        sys.stdout.write('=')
    sys.stdout.write('>')
    for i in range(rest_len):
        sys.stdout.write('.')
    sys.stdout.write(']')

    current_time = time.time()
    step_time = current_time - LAST_T
    LAST_T = current_time
    total_time = current_time - BEGIN_T

    time_used = '  Step: %s' % format_time(step_time)
    time_used += ' | Tot: %s' % format_time(total_time)
    if msg:
        time_used += ' | ' + msg

    msg = time_used
    sys.stdout.write(msg)

    if current < total - 1:
        sys.stdout.write('\r')
    else:
        sys.stdout.write('\n')
    sys.stdout.flush()


# return the formatted time
def format_time(seconds):
    days = int(seconds / 3600/24)
    seconds = seconds - days*3600*24
    hours = int(seconds / 3600)
    seconds = seconds - hours*3600
    minutes = int(seconds / 60)
    seconds = seconds - minutes*60
    seconds_final = int(seconds)
    seconds = seconds - seconds_final
    millis = int(seconds*1000)

    output = ''
    time_index = 1
    if days > 0:
        output += str(days) + 'D'
        time_index += 1
    if hours > 0 and time_index <= 2:
        output += str(hours) + 'h'
        time_index += 1
    if minutes > 0 and time_index <= 2:
        output += str(minutes) + 'm'
        time_index += 1
    if seconds_final > 0 and time_index <= 2:
        output += str(seconds_final) + 's'
        time_index += 1
    if millis > 0 and time_index <= 2:
        output += str(millis) + 'ms'
        time_index += 1
    if output == '':
        output = '0ms'
    return output


def var(tensor, requires_grad=True):
    """
    Convert tensor to Variable
    """
    if torch.cuda.is_available():
        dtype = torch.cuda.FloatTensor
    else:
        dtype = torch.FloatTensor

    var = Variable(tensor.type(dtype), requires_grad=requires_grad)

    return var


def make_img(dataloader, generator, z, img_num=5, img_size=128):
    """
        < make_img >
        Generate images

    :param dataloader: Data loader for test data set
    :param generator: generator
    :param z: random_z(size = (N, img_num, z_dim))
    :param img_num: Number of images that you want to generate with one test img
    :param img_size: image resolution size
    :return: image result
    """
    if torch.cuda.is_available():
        dtype = torch.cuda.FloatTensor
    else:
        dtype = torch.FloatTensor

    dataloader = iter(dataloader)
    img, _ = dataloader.next()

    N = img.size(0)
    img = var(img.type(dtype))

    result_img = torch.FloatTensor(N * (img_num + 1), 3, img_size, img_size).type(dtype)

    for i in range(N):
        # original image to the leftmost
        result_img[i * (img_num + 1)] = img[i].data

        # Insert generated images to the next of the original image
        for j in range(img_num):
            img_ = img[i].unsqueeze(dim=0)
            z_ = z[i, j, :].unsqueeze(dim=0)

            out_img = generator(img_, z_)
            result_img[i * (img_num + 1) + j + 1] = out_img.data

    # [-1, 1] -> [0, 1]
    result_img = result_img / 2 + 0.5

    return result_img

def plot_loss(avg_losses, num_epochs, save=False, save_dir='result/', show=False):
    fig, ax = plt.subplots()
    ax.set_xlim(0, num_epochs)
    temp = 0.0
    for i in range(len(avg_losses)):
        temp = max(np.max(avg_losses[i]), temp)
    ax.set_ylim(0, temp*1.1)
    plt.xlabel('# of Epochs')
    plt.ylabel('Loss values')

    plt.plot(avg_losses[0], label='D_loss')
    plt.plot(avg_losses[1], label='G_GAN_loss')
    plt.plot(avg_losses[2], label='KL_div')
    plt.plot(avg_losses[3], label='img_recon_loss')
    plt.plot(avg_losses[4], label='G_alone_loss')
    plt.legend()

    # save figure
    if save:
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        save_fn = save_dir + 'Loss_values_epoch_{:d}'.format(num_epochs) + '.png'
        plt.savefig(save_fn)

    if show:
        plt.show()
    else:
        plt.close()
