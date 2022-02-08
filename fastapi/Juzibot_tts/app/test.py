import paddle
from paddlespeech.cli import TTSExecutor

tts_executor = TTSExecutor()
wav_file = tts_executor(
    text='今天的天气不错啊',
    output='output.wav',
    am='fastspeech2_csmsc',
    am_config=None,
    am_ckpt=None,
    am_stat=None,
    spk_id=0,
    phones_dict=None,
    tones_dict=None,
    speaker_dict=None,
    voc='pwgan_csmsc',
    voc_config=None,
    voc_ckpt=None,
    voc_stat=None,
    lang='zh',
    device=paddle.get_device())
print('Wave file has been generated: {}'.format(wav_file))