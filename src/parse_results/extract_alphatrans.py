import os
import json


def main():

    results_path = 'data/tool_results/alphatrans/raw_results/gpt-4o-2024-11-20/body/0.0'

    results = {}
    for project in os.listdir(results_path):
        for schema_file in os.listdir(f'{results_path}/{project}'):

            if 'src.main' not in schema_file:
                continue

            schema_data = {}
            with open(f'{results_path}/{project}/{schema_file}', 'r') as f:
                schema_data = json.load(f)
            
            formatted_schema_file = schema_file.replace('.json', '')
            
            for class_ in schema_data['classes']:

                if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                    continue
                
                for method_ in schema_data['classes'][class_]['methods']:

                    if schema_data['classes'][class_]['methods'][method_]['is_overload']:
                        continue
                    
                    results.setdefault(project, {})
                    results[project].setdefault(formatted_schema_file, {})
                    results[project][formatted_schema_file].setdefault(class_, {})
                    results[project][formatted_schema_file][class_].setdefault(method_, {})

                    if isinstance(schema_data['classes'][class_]['methods'][method_]['graal_validation'], str):
                        results[project][formatted_schema_file][class_][method_]['graal_validation'] = schema_data['classes'][class_]['methods'][method_]['graal_validation']
                    elif isinstance(schema_data['classes'][class_]['methods'][method_]['graal_validation'], dict):
                        results[project][formatted_schema_file][class_][method_]['graal_validation'] = schema_data['classes'][class_]['methods'][method_]['graal_validation']['outcome']
                    else:
                        raise ValueError(f"Unexpected type for graal_validation: {type(schema_data['classes'][class_]['methods'][method_]['graal_validation'])}")
                    
                    source_code = ''.join(schema_data['classes'][class_]['methods'][method_]['body'])
                    target_code = '\n'.join(schema_data['classes'][class_]['methods'][method_]['translation'])

                    results[project][formatted_schema_file][class_][method_]['source_code'] = source_code.split('\n')
                    results[project][formatted_schema_file][class_][method_]['target_code'] = target_code.split('\n')

    output_path = 'data/tool_results/alphatrans/alphatrans_graal_results'
    os.makedirs(output_path, exist_ok=True)

    for project in results:
        with open(f'{output_path}/{project}.json', 'w') as f:
            json.dump(results[project], f, indent=4)


if __name__ == "__main__":
    main()
