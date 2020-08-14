from server import app
from middleware.post_validate import validate_json_type, validate_json_scheme
from flask import jsonify


@app.route('/1', methods=['GET', 'POST'])
# @validate_json_params
@validate_json_type
def test1():
    """

    :return:
    """
    a = validate_json_scheme("a", "b", "c", "d")
    if a:
        return jsonify("有参数缺失")

    ## 其余业务逻辑
    return "ops"