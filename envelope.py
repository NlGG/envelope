#!/usr/bin/python
#-*- encoding: utf-8 -*-
# Quantitative Economics Web: http://quant-econ.net/py/index.html


from __future__ import division
import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def envelope(expression, with_animation=False, **kwargs):

    # 可変長キーワード引数（**kwargs）の初期化処理
    x_list = kwargs.get('x_list', np.arange(0, 100, 0.5))
    parameter_list = kwargs.get('parameter_list', np.arange(0, 10, 0.1))

    title = kwargs.get('title', 'Show Envelope Curve')
    xlabel = kwargs.get('xlabel', False)
    ylabel = kwargs.get('ylabel', False)
    color = kwargs.get('color', 'c')
    legend = kwargs.get('legend', False)
    parameter_name = kwargs.get('parameter_name', 'Parameter')

    xlim = kwargs.get('xlim', [0, 100])
    ylim = kwargs.get('ylim', [0, 30])
    plot_size = kwargs.get('plot_size', 5)
    
    
    # アニメーション関数
    def __run(parameter):
        y_list = expression(x_list, parameter)
        
        min_index = y_list.argmin()
        left_bound = max(min_index - plot_size, 0)
        right_bound = min(min_index + plot_size + 1, len(x_list) - 1)
        x_plot_list = x_list[left_bound : right_bound]
        y_plot_list = y_list[left_bound : right_bound]

        del plt.gca().texts[-1]
        ax.annotate(str(parameter_name)+"="+str(parameter),
            xy=(0.05, 0.9),
            xycoords='axes fraction',
            fontsize=16,
            horizontalalignment='left',
            verticalalignment='bottom'
        )

        ax.plot(x_plot_list, y_plot_list, color=color, linewidth=1)


    # 図の初期化処理
    fig, ax = plt.subplots()
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.annotate(str(parameter_name)+"="+str(parameter_list[0]),
        xy=(0, 0),
        xycoords='axes fraction',
        fontsize=16,
        horizontalalignment='right',
        verticalalignment='top'
    )
    ax.plot(0, 0, color=color, linewidth=1 ,label=str(legend))

    if with_animation:
        # __runの引数にparameter_listから1つずつ値を取りながら、figにグラフを描写する
        animation.FuncAnimation(fig, __run, parameter_list, interval=5, repeat=False)

    else:
        for parameter in parameter_list:
            __run(parameter)

    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)

    if ylabel:
        plt.ylabel(ylabel)

    if legend:
        plt.legend()

    plt.show()


# 長期平均費用曲線を求める
envelope(lambda y, k: 1/8 * (y - 10 * k) ** 2 + 1/3 * k ** 2 - 2 * k + 4,
        plot_size = 5,
        title = 'Show Average Long-Run Cost Curve',
        xlabel = 'Y: Production',
        ylabel = 'C: Cost',
        legend = 'Average Short-Run Cost Curves',
        parameter_name = 'K'
        )


"""
# 長期平均費用曲線を求める（with animation）
envelope(lambda y, k: 1/8 * (y - 10 * k) ** 2 + 1/3 * k ** 2 - 2 * k + 4,
        True,
        plot_size = 5,
        title = 'Show Average Long-Run Cost Curve',
        xlabel = 'Y: Production',
        ylabel = 'C: Cost',
        legend = 'Average Short-Run Cost Curves',
        parameter_name = 'K'
        )
"""


"""
# 長期総費用曲線を求める
envelope(lambda y, k: 1/150*((1/2*y-2*k**3) ** 3+(2*k**3)**3) + 1/10*k*((1/2*y-(5*k**3-5*k**2+k))**2-(5*k**3-5*k**2+k) **2) + (1/(4*k) + 1/25*k**6)*y + 5*k**3-5*k**2+5*k+5,
        plot_size = 200,
        title = 'Show Total Long-Run Cost Curve',
        xlabel = 'Y: Production',
        ylabel = 'C: Cost',
        legend = 'Total Short-Run Cost Curves',
        parameter_name = 'K',
        xlim = [0, 100],
        ylim = [0, 300],
        xlist = np.arange(0, 200, 0.5),
        parameter_list = np.arange(0.05, 5.05, 0.05)
        )
"""



