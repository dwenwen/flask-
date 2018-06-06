from flask import blueprints,render_template


hm = blueprints.Blueprint('hm',__name__)

@hm.route('/index',methods=['GET','POST'])
def index():

    return render_template('index.html')