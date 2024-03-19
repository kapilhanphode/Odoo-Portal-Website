from odoo import http
from odoo.http import request

class MyDashboard(http.Controller):

    @http.route(['/my/dashboard'], type='http', auth="user", website=True)
    def customer_form(self, **post):
        print('++++++++++++')
        return request.render("food_search_application.my_dashboard", {})