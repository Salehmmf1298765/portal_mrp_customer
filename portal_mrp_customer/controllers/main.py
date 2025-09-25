# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class MRPPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'mrp_mo_count' in counters:
            partner = request.env.user.partner_id
            mo_domain = self._prepare_mo_domain(partner)

            Mrp = request.env['mrp.production'].sudo()
            values['mrp_mo_count'] = Mrp.search_count(mo_domain)
        return values

    def _prepare_mo_domain(self, partner):
        commercial_partner = partner.commercial_partner_id

        return [
            '|',
            ('sale_line_id.order_partner_id', 'child_of', [commercial_partner.id]),
            ('procurement_group_id.sale_id.partner_id', 'child_of', [commercial_partner.id]),
        ]

    def _get_mo_searchbar_sortings(self):
        return {
            'date': {'label': _('Start Date'), 'order': 'date_start desc'},
            'name': {'label': _('Reference'), 'order': 'name desc'},
        }

    @http.route(['/my/mos', '/my/mos/page/<int:page>'], type='http', auth='user', website=True)
    def portal_my_mos(self, page=1, date_begin=None, date_end=None, sortby='date', **kwargs):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id

        MrpProduction = request.env['mrp.production'].sudo()

        domain = self._prepare_mo_domain(partner)

        searchbar_sortings = self._get_mo_searchbar_sortings()
        sortby = sortby or 'date'
        sort_order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        url = '/my/mos'
        url_args = {'date_begin': date_begin, 'date_end': date_end}
        if len(searchbar_sortings) > 1:
            url_args['sortby'] = sortby

        pager_values = portal_pager(
            url=url,
            total=MrpProduction.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args=url_args,
        )
        mos = MrpProduction.search(domain, order=sort_order, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            'page_name': 'mrp_mo',
            'mos': mos.sudo(),
            'pager': pager_values,
            'default_url': url,
        })
        if len(searchbar_sortings) > 1:
            values.update({
                'sortby': sortby,
                'searchbar_sortings': searchbar_sortings,
            })

        return request.render('portal_mrp_customer.portal_my_mos', values)
