import numpy as np
from scipy.io import wavfile as wav
from ligotools.utils import whiten, reqshift, write_wavfile


def test_whiten_output():
    fs = 4096
    t = np.arange(0, 1, 1/fs)
    x = np.sin(2*np.pi*100*t)
    psd = np.abs(np.fft.rfft(x))**2
    y = whiten(x, psd, 1/fs)
    assert len(y) == len(x)
    assert np.isfinite(y).all()


def test_reqshift_and_write(tmp_path):
    fs = 4096
    t = np.arange(0, 1, 1/fs)
    x = np.sin(2*np.pi*100*t)
    y = reqshift(x, 300, fs)
    out = tmp_path / "test.wav"
    write_wavfile(str(out), fs, y)
    rate, data = wav.read(out)
    assert rate == fs
    assert data.dtype == np.int16