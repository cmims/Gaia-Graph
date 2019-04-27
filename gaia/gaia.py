import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from astroquery.utils.tap.core import TapPlus
import warnings

warnings.filterwarnings('ignore')

fig = plt.figure()
ax = plt.axes(projection='3d')


def query_gaia():
    gaia = TapPlus(url='http://gea.esac.esa.int/tap-server/tap')

    job = gaia.launch_job_async('select top 100000 ra, dec, phot_g_mean_mag \
        from gaiadr1.gaia_source order by source_id')

    results = job.get_results()

    results = np.array([result.as_void().view((float, 3)) for result in results])

    x = results[:, 2] * np.cos(results[:, 0]) * np.cos(results[:, 1])
    y = results[:, 2] * np.sin(results[:, 0]) * np.cos(results[:, 1])
    z = results[:, 2] * np.sin(results[:, 1])

    sample_size = 1000
    random_idns = np.random.choice(results.shape[0], sample_size)

    ax.scatter(x[random_idns], y[random_idns], z[random_idns], s=3)

    plt.show()


if __name__ == "__main__":
    query_gaia()
