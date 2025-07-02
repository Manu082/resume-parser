import pandas as pd

class CSVExporter:
    def export_to_csv(self, results, filename):
        df = pd.DataFrame(results)
        df = df.sort_values(by='Score', ascending=False)
        df.to_csv(filename, index=False)
 
