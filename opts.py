from argparse import ArgumentParser


def get_args():
    # training related
    parser = ArgumentParser(description='e-Lab Segmentation Script')
    arg = parser.add_argument
    arg('--bs', type=float, default=8, help='batch size')
    arg('--lr',  type=float, default=5e-4, help='learning rate, default is 5e-4')
    arg('--lrd', type=float, default=1e-7, help='learning rate decay (in # samples)')
    arg('--wd', type=float, default=2e-4, help='L2 penalty on the weights, default is 2e-4')
    arg('-m', '--momentum', type=float, default=.9, help='momentum, default: .9')

    # device related
    arg('--workers', type=int, default=8, help='# of cpu threads for data-loader')
    arg('--maxepoch', type=int, default=300, help='maximum number of training epochs')
    arg('--seed', type=int, default=0, help='seed value for random number generator')
    arg('--plot', type=bool, default=False, help='plot training/testing error')
    arg('--nGPU', type=int, default=4, help='number of GPUs you want to train on')
    arg('--save', type=str, default='media', help='save trained model here')

    # data set related:
    arg('--datapath',  type=str, default='/media/HDD1/Datasets', help='dataset location')
    arg('--dataset',  type=str, default='cs', choices=["cs", "cv"],
        help='dataset type: cs(cityscapes)/cv(CamVid)')
    arg('--imHeight', type=int, default=512, help='image height  (576 cv/512 cs)')
    arg('--imWidth', type=int, default=1024, help='image width  (576 cv/512 cs)')

    # model related
    arg('--model',  type=str, default='linknet', help='linknet')
    arg('--pretrained',  type=str, default='/media/HDD1/Models/pretrained/resnet-18.t7',
        help='pretrained encoder for which you want to train your decoder')

    # Saving/Displaying Information
    arg('--saveTrainConf', type=bool, default=False, help='Save training confusion matrix')
    arg('--saveAll', type=bool, default=False, help='Save all models and confusion matrices')
    arg('--resume', type=bool, default=False, help='Resume from previous checkpoint')

    args = parser.parse_args()
    return args
