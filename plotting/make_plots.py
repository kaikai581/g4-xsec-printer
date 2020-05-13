import matplotlib.pyplot as plt
import pandas as pd

def compare_all(df_xsec, desc, fn):
    # ax_tot = df_xsec.plot.scatter(x='E(MeV)', y='Total(b)', alpha=0.4, c='y')
    # ax_el = df_xsec.plot.scatter(x='E(MeV)', y='Elastic(b)', s=2, c='r', alpha=0.7, ax = ax_tot)
    # ax_inel = df_xsec.plot.scatter(x='E(MeV)', y='Inelastic(b)', s=2, c='g', alpha=0.7, ax = ax_tot)
    # ax_cap = df_xsec.plot.scatter(x='E(MeV)', y='Capture(b)', s=2, c='b', alpha=0.7, ax = ax_tot)
    fig, axex = plt.subplots(2, sharex=True)
    axex[0] = df_xsec.plot(x='E(MeV)', y='Total(b)', alpha=0.4, c='magenta', lw=4, ax=axex[0])
    df_xsec.plot(x='E(MeV)', y=['Elastic(b)','Inelastic(b)','Capture(b)'], ax=axex[0])
    axex[0].set_xlabel('neutron kinetic energy (MeV)')
    axex[0].set_ylabel(r'cross section (barn, $10^{-24}$cm$^2$)')
    axex[0].set_title(desc)
    axex[1] = df_xsec.plot(x='E(MeV)', y='Total(b)', alpha=0.4, c='magenta', lw=4, ax=axex[1])
    plt.savefig(fn)

def main():
    nC_xsec = pd.read_csv('nC_FTFP_BERT.csv', sep=' ', skipinitialspace=True)
    nH_xsec = pd.read_csv('nH_FTFP_BERT.csv', sep=' ', skipinitialspace=True)
    compare_all(nH_xsec[nH_xsec['E(MeV)'] >= 10], 'neutron cross section off H', 'nH_xsec.png')


if __name__ == '__main__':
    main()