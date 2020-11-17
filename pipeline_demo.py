import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


class MultiplierTransformer(beam.DoFn):
    def __init__(self, multiplier):
        beam.DoFn.__init__(self)
        self.multiplier = multiplier

    def setup(self):
        pass
    
    def process(self, element):
        element["number_col"] = element["number_col"] * self.multiplier
        yield element


class MinNumber(beam.PTransform):
    def __init__(self, field):
      beam.PTransform.__init__(self)
      self.field = field
    
    def expand(self, pcoll):
        return (
            pcoll
            | beam.Map(lambda e: (e[self.field], e["number_col"]))
            | beam.CombinePerKey(min)
        )


def main(argv = None):
    fake_data = [
        {"key_field": "a", "date": "2020-02-05", "number_col": 20},
        {"key_field": "a", "date": "2020-01-05", "number_col": 25},
        {"key_field": "b", "date": "2020-02-05", "number_col": 14},
        {"key_field": "c", "date": "2020-02-05", "number_col": 6}
    ]
    
    pipeline_options = PipelineOptions()
    with beam.Pipeline(options=pipeline_options) as p:
        inputs = (
            p
            | "Create data" >> beam.Create(fake_data)
        )
        
        inputs | "Print inputs" >> beam.Map(print)
                                            
        outputs = (
            inputs
            | "Multiply by 2" >> beam.ParDo(MultiplierTransformer(2))
            | "Get min usage" >> MinNumber("key_field")
        )
        
        outputs | "Print outputs" >> beam.Map(print)
    

if __name__ == "__main__":
	main()
