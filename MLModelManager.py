import pandas as pd

# MLModelManager class definition
class MLModelManager(object):

    def __init__(self):
        self.setups = []

    # a setup must be a dictionary with at least 2 nodes: details, eval_metrics
    def save_setup(self, setup):       
            self.setups.append(setup)

    # given a KPI (e.g. F1), get_best_model will iterate over all setups saved previously and return the highest one
    def get_best_model(self,kpi,metrics_node):
        max_kpi_value = 0.0

        for setup in self.setups:
            if kpi in setup[metrics_node]:
                kpi_value = setup[metrics_node][kpi]

                if kpi_value > max_kpi_value:
                    max_kpi_value = kpi_value
                    setup_to_return = setup

        return setup_to_return

    def summarize_by_kpi(self,kpi,metrics_node,name_field):

        algo = []
        kpis = []

        for setup in self.setups:
            algo.append(setup['details'][name_field])
            kpis.append(setup[metrics_node][kpi])

        df = pd.DataFrame({'algorithm' : algo, kpi : kpis})

        return(df)
