# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:49:45 2016

@author: mayou

Contains the different run-modes for the machine-learning algorithms.
"""
import raredecay.meta_config

#import config as cfg


def run(runmode):
    """select the right runmode from the parameter and run it"""
    #global run_config
    #run_config = 'config'
    _reweight1_comparison()



def reweight(data_to_reweight):
    raredecay.meta_config.run_config = 'raredecay.run_config.reweight_cfg'  # 'run_config.reweight1_cfg'
    from raredecay.analysis import ml_analysis
    import importlib
    cfg = importlib.import_module(raredecay.meta_config.run_config)
    from raredecay.tools import data_tools

    ml_ana = ml_analysis.MachineLearningAnalysis()
    reweighter = ml_ana.reweight_mc_real(meta_cfg=cfg.reweight_meta_cfg,
                                         **cfg.reweight_cfg)
    # reweighter = ''  # load from pickle file
    new_weights = ml_ana.reweight_weights(data_to_reweight, reweighter)
    return data_tools.adv_return(new_weights)


def _reweight1_comparison():
    raredecay.meta_config.run_config = 'raredecay.run_config.reweight1_comparison_cfg'  # 'run_config.reweight1_cfg'
    from raredecay.analysis import ml_analysis
    import importlib
    cfg = importlib.import_module(raredecay.meta_config.run_config)

    from raredecay.tools import dev_tool
    logger = dev_tool.make_logger(__name__)
    logger.debug("config file used: " +
                 str(raredecay.meta_config.run_config))



    print "starting physical module reweight1"
    gb_list = []
    original_list = []
    bins_list = []
    ml_ana = ml_analysis.MachineLearningAnalysis()


    gb_reweighter = ml_ana.reweight_mc_real(meta_cfg=cfg.reweight_meta_cfg, **cfg.reweight_cfg)
    #gb_reweighter = 'gb_reweighter1.pickle'
    gb_weights = ml_ana.reweight_weights(cfg.reweight_cfg.get('reweight_data_mc'), gb_reweighter)
    bins_reweighter = ml_ana.reweight_mc_real(meta_cfg=cfg.reweight_meta_cfg_bins, **cfg.reweight_cfg_bins)
    #bins_reweighter = 'bins_reweighter1.pickle'
    bins_weights = ml_ana.reweight_weights(cfg.reweight_cfg.get('reweight_data_mc'), bins_reweighter)
    print bins_weights
    gb_list.append( ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                        cfg.reweight_cfg.get('reweight_data_real'),
                        weight_original =  gb_weights))
    original_list.append( ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                        cfg.reweight_cfg.get('reweight_data_real')))
    bins_list.append(ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                        cfg.reweight_cfg.get('reweight_data_real'),
                        weight_original =  bins_weights))
    print gb_weights
    print bins_weights
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              labels=['mc', 'real'])
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              weights=[gb_weights, None],
                              labels=['mc gb_reweighter', 'real'])
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              weights=[bins_weights, None],
                              labels=['mc bins_reweighter', 'real'])
    names_list = ['gb', 'original', 'bins']
    print
    for i, lists in enumerate([gb_list, original_list, bins_list]):
        print "ROC AUC mean " + names_list[i] + ": ", lists[0][0]
        print lists[0][1]





def _test2():
    pass


def finalize():
    """Finalize the run: print to console and save output_string to file
    """
    print "function finalize not yet implemented"

# temporary:
if __name__ == '__main__':
    run(1)