import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, get_window, hilbert
from scipy.io.wavfile import write as wavwrite


def whiten(strain, psd, dt):
    n = len(strain)
    hf = np.fft.rfft(strain)
    norm = np.sqrt(psd / (dt / 2.0))
    norm = np.where(norm == 0, np.inf, norm)
    white_hf = hf / norm[:len(hf)]
    white = np.fft.irfft(white_hf, n)
    return white


def write_wavfile(path, fs, data):
    x = np.asarray(data, dtype=float)
    x = x / (np.max(np.abs(x)) + 1e-12)
    wavwrite(path, fs, (x * 32767).astype(np.int16))


def reqshift(x, fshift, fs):
    t = np.arange(len(x)) / float(fs)
    analytic = hilbert(x)
    y = analytic * np.exp(2j * np.pi * fshift * t)
    return np.real(y)


def plot_psd(strain, fs, seg_seconds=4, overlap_seconds=2, window="hann", outpath=None):
    nperseg = int(seg_seconds * fs)
    noverlap = int(overlap_seconds * fs)
    win = get_window(window, nperseg, fftbins=True)
    freqs, psd = welch(
        strain, fs=fs, window=win, nperseg=nperseg,
        noverlap=noverlap, detrend="constant",
        return_onesided=True, scaling="density"
    )
    plt.figure(figsize=(6, 4))
    plt.loglog(freqs, psd)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("PSD [strain²/Hz]")
    if outpath:
        plt.savefig(outpath)
        plt.close()
    return freqs, psd