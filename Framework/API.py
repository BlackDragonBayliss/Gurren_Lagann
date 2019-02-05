from flask import Flask, jsonify, request
from flask_cors import CORS
from Operation_Center import Operation_Center

app = Flask(__name__)
CORS(app)


def __new__(self):
    self.operation_center = Operation_Center()


@app.route('/init_system', methods=['POST'])
def init_system():
    operation_center = Operation_Center()
    operation_center.process_main_process_loop()
    return "initiated"


@app.route('/top_stock', methods=['POST'])
def top_stock():
    content = request.get_json()
    return_value = 'pass'
    for key, value in content.items():
        if key == 'request_type':
            if value == "lookup_top_stocks_phase_internal":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_top_stock_phase1_internal()
                                return_value = 'res'
    # # Assemble TSP DM's
    # for key, value in content.items():
    #     if key == 'request_type':
    #         if value == "lookup_top_stocks_DM_assemble":
    #             for key, value in content.items():
    #                 if key == "payload":
    #                     for key, value in value.items():
    #                         if key == "data":
    #                             operation_center = Operation_Center()
    #                             operation_center.process_async_assemble_top_data_managers()
    #                             return_value = 'res'
    # # Initiate TSP DM's
    # for key, value in content.items():
    #     if key == 'request_type':
    #         if value == "lookup_top_stocks_DM_initiate":
    #             for key, value in content.items():
    #                 if key == "payload":
    #                     for key, value in value.items():
    #                         if key == "data":
    #                             operation_center = Operation_Center()
    #                             operation_center.process_async_initiate_top_data_managers()
    #                             return_value = 'res'

    for key, value in content.items():
        if key == 'request_type':
            if value == "transform_top_stock":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_top_stock_phase1(value)
                                return_value = 'res'

    for key, value in content.items():
        if key == 'request_type':
            if value == "query_stock":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_top_stock_phase2(value)
                                return_value = 'res'
    return return_value


@app.route('/query_stock', methods=['POST'])
def query_stock():
    content = request.get_json()
    print(content.items())
    for key, value in content.items():
        if key == 'request_type':
            if value == "query_stock":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_query_stock_phase1(value)
                                return_value = 'res'

    for key, value in content.items():
        if key == 'request_type':
            if value == "query_symbol":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_query_symbol(value)
                                return_value = 'res'
    return return_value


@app.route('/data_manager_assemble', methods=['POST'])
def dm_assemble():
    content = request.get_json()
    print('hit data_manager_assemble')
    print(content.items())
    for key, value in content.items():
        if key == 'request_type':
            if value == "extended_data_manager":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_assemble_extended_data_manager(value)
                                return_value = 'res'
    content = request.get_json()
    print(content.items())
    for key, value in content.items():
        if key == 'request_type':
            if value == "chosen_data_manager":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_assemble_chosen_data_manager(value)
                                return_value = 'res'
    content = request.get_json()
    print(content.items())
    for key, value in content.items():
        if key == 'request_type':
            if value == "bought_data_manager":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_assemble_bought_data_manager(value)
                                return_value = 'res'
    return return_value


@app.route('/NM_query_stock', methods=['POST'])
def DM_query_stock():
    content = request.get_json()
    print(content.items())
    for key, value in content.items():
        if key == 'request_type':
            if value == "NM_query_stock":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            print('hit')
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_DM_stock_creation(value)
                                return_value = 'res'

    return return_value


@app.route('/query_account', methods=['POST'])
def query_account():
    content = request.get_json()
    print(content.items())
    return_value = ''

    for key, value in content.items():
        if key == 'request_type':
            if value == "phase2":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase2_account(value)
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase3":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase3_account(value)
                                return_value = 'res'
    return return_value


@app.route('/trade_market_buy', methods=['POST'])
def trade_market_buy():
    content = request.get_json()
    # print(content.items())
    return_value = ''
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase1":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase1_market_buy()
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase2":
                print(content.items())
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase2_market_buy(value)
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase3":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase3_market_buy(value)
                                return_value = 'res'
    return return_value


@app.route('/trade_market_sell', methods=['POST'])
def trade_market_sell():
    content = request.get_json()
    print("trade_sell")
    return_value = ''
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase1":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase1_market_sell()
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase2":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase2_market_sell(value)
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "phase3":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_phase3_market_sell(value)
                                return_value = 'res'
    return return_value


@app.route('/case_analytics', methods=['POST'])
def case_analytics():
    content = request.get_json()
    print("case_analytics")
    return_value = ''
    for key, value in content.items():
        if key == 'request_type':
            if value == "case_one":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_case_one()
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "case_two":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_case_two(value)
                                return_value = 'res'
    for key, value in content.items():
        if key == 'request_type':
            if value == "case_three":
                for key, value in content.items():
                    if key == "payload":
                        for key, value in value.items():
                            if key == "data":
                                operation_center = Operation_Center()
                                operation_center.process_async_case_three(value)
                                return_value = 'res'
    return return_value


if __name__ == '__main__':
    app.run(debug=False)
