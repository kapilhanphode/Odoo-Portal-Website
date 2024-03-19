from odoo.tools.translate import _
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class ProdcutDetails(http.Controller):

    @http.route(['/all_product_list_view', '/all_product_list_view/page/<int:page>'], type='http', auth="user",
                website=True)
    def product_list_view(self, page=1, sortby='product_id', search='', search_in='product_id', **post):
        # product_category = request.env['products'].search([('product_category','=','AA')])
        sorted_list = {
            'product_id': {'label': 'ID', 'order': 'product_id Asc'},
            'product_name': {'label': 'Name', 'order': 'product_name'},
            'product_description': {'label': 'Description', 'order': 'product_description'},
            'product_rating': {'label': 'Ratings', 'order': 'product_rating'},
            'product_category': {'label': 'Category', 'order': 'product_category'},
            'veg_non_veg': {'label': 'Type', 'order': 'veg_non_veg'},
        }

        search_list = {
            'product_id': {'label': 'ID', 'input': 'product_id', 'domain': [('product_id', 'ilike', search)]},
            'product_name': {'label': 'Name', 'input': 'product_name', 'domain': [('product_name', 'ilike', search)]},
            'product_description': {'label': 'Description', 'input': 'product_description',
                                    'domain': [('product_description', 'ilike', search)]},
            'product_rating': {'label': 'Ratings', 'input': 'product_rating',
                               'domain': [('product_rating', 'ilike', search)]},
            'product_category': {'label': 'Category', 'input': 'product_category',
                                 'domain': [('product_category', 'ilike', search)]},
            'veg_non_veg': {'label': 'Type', 'input': 'veg_non_veg', 'domain': [('veg_non_veg', 'ilike', search)]},
        }

        search_domain = search_list[search_in]['domain']

        for rec in search_domain:
            print('search domain',rec)

        total_products = request.env['products'].search_count(search_domain)
        page_details = pager(url='/all_product_list_view',
                             total=total_products,
                             page=page,
                             url_args={'sortby': sortby, 'search_in': search_in, 'search': search},
                             step=5
                             )
        default_orderby = sorted_list[sortby]['order']
        print('all product view clicked')
        products = request.env['products'].search(search_domain, limit=5, order=default_orderby,
                                                  offset=page_details['offset'])
        print('products', products)
        return request.render("food_search_application.all_product_list_view",
                              {'products': products, 'page_name': 'product_list_view',
                               'pager': page_details, 'sortby': sortby, 'searchbar_sortings': sorted_list,
                               'search_in': search_in, 'searchbar_inputs': search_list, 'search': search
                               })

    @http.route('/test', type='http', auth="user", website=True)
    def test_view(self, filterby=None, **post):
        filter_list = {
            'all': {'label': _('All'), 'domain': []},
            'product_id': {'label': _('ID'), 'domain': [('product_id', '=', ('1', '4'))]},
            'product_categroy': {'label': _('Category'), 'domain': [('product_category', '=', ('Pizza', 'Burger'))]},
        }

        search_domain = filter_list.get(filterby, {}).get('domain', [])
        print('search_domain', search_domain)

        return request.render("food_search_application.test_view",
                              {'searchbar_filters': filter_list, 'filterby': filterby,
                               })
