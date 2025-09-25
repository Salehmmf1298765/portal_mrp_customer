# Portal Manufacturing Orders Module

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-875A7B?style=flat&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-success)

A comprehensive Odoo 18.0 module that extends the customer portal functionality to include Manufacturing Orders (MO) visibility and tracking for end customers. This module bridges the gap between manufacturing operations and customer transparency by providing real-time access to production order information through the customer portal.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Module Structure](#module-structure)
- [Security](#security)
- [Technical Details](#technical-details)
- [API Routes](#api-routes)
- [Screenshots](#screenshots)
- [Author](#author)
- [Support](#support)
- [License](#license)

## 🎯 Overview

**Portal Manufacturing Orders** is an Odoo module that allows customers to track their manufacturing orders directly from the customer portal. When a sales order generates manufacturing orders, customers can monitor the production progress, view manufacturing details, and track the status of their products being manufactured.

### Business Use Case
This module solves a critical business need where:
- Customers want visibility into the manufacturing process of their orders
- Businesses need to provide transparency in production timelines
- Sales teams need to reduce inquiries about production status
- Manufacturing teams want to streamline communication with customers

## ✨ Features

### Core Functionality
- **Portal Integration**: Seamlessly integrates with Odoo's existing customer portal infrastructure
- **Manufacturing Order Visibility**: Customers can view all manufacturing orders linked to their sales
- **Real-time Status Tracking**: Live updates on manufacturing order states (Draft, Confirmed, In Progress, Done, Cancelled)
- **Filtered Access**: Customers only see manufacturing orders related to their own purchases
- **Responsive Design**: Mobile-friendly interface for on-the-go access

### Advanced Features
- **Multi-level Partner Support**: Supports commercial partner hierarchy (child_of relationship)
- **Sortable Lists**: Sort manufacturing orders by date or reference
- **Date Range Filtering**: Filter manufacturing orders by creation date
- **Pagination Support**: Efficiently handle large numbers of manufacturing orders
- **Sales Order Linking**: Direct links from manufacturing orders to originating sales orders

## 📦 Requirements

### System Requirements
- **Odoo Version**: 18.0 or higher
- **Python**: 3.10+
- **Database**: PostgreSQL 12+

### Module Dependencies
The module depends on the following Odoo modules:
- `portal` - Base portal functionality
- `stock` - Inventory management
- `mrp` - Manufacturing management
- `sale_mrp` - Sales and Manufacturing integration
- `sale` - Sales management
- `website` - Website functionality

## 🛠️ Installation

### Method 1: Standard Installation
1. Download the module to your Odoo addons directory:
```bash
cd /path/to/odoo/custom_addons
git clone [repository_url] portal_mrp_customer
```

2. Update the module list:
```bash
./odoo-bin -u all -d [database_name]
```

3. Install the module from Apps menu:
   - Navigate to Apps
   - Search for "Portal Manufacturing Orders"
   - Click Install

### Method 2: Manual Installation
1. Place the module folder in your custom addons path
2. Restart Odoo server with updated addons path:
```bash
./odoo-bin --addons-path=addons,custom_addons
```
3. Update apps list and install from the interface

## ⚙️ Configuration

### Access Rights Configuration
The module automatically configures:
- Read-only access to manufacturing orders for portal users
- Security rules limiting visibility to customer's own orders
- No write, create, or delete permissions for portal users

### Portal Menu Configuration
After installation, the module adds:
- "Your Manufacturing Orders" card in the portal home page
- Manufacturing Orders menu item in portal navigation
- Counter showing total number of manufacturing orders

### Optional Settings
No additional configuration is required. The module works out-of-the-box with default settings.

## 📖 Usage

### For End Users (Customers)

1. **Accessing Manufacturing Orders**:
   - Login to the customer portal
   - Click on "Your Manufacturing Orders" card or navigate to /my/mos
   - View the list of all manufacturing orders related to your purchases

2. **Understanding the Display**:
   - **MO Reference**: Unique manufacturing order number
   - **Product**: Name of the product being manufactured
   - **Quantity**: Ordered quantity with unit of measure
   - **Start Date**: Scheduled production start date
   - **State**: Current production status
   - **Sales Order**: Link to the originating sales order

3. **Filtering and Sorting**:
   - Use date range selector to filter orders
   - Sort by date or reference using the dropdown
   - Navigate through pages for large datasets

### For Administrators

1. **Monitoring Usage**:
   - Track portal access through standard Odoo logging
   - Monitor which customers are viewing their manufacturing orders

2. **Troubleshooting**:
   - Check security rules if customers report missing orders
   - Verify sale_line_id relationships are properly set

## 📁 Module Structure

```
portal_mrp_customer/
├── __init__.py                  # Module initialization
├── __manifest__.py              # Module metadata and configuration
├── controllers/
│   ├── __init__.py             # Controllers initialization
│   └── main.py                 # Portal routes and business logic
├── security/
│   ├── ir.model.access.csv    # Access control list
│   └── mrp_portal_security.xml # Security rules for portal users
├── views/
│   └── mrp_portal_templates.xml # Portal UI templates
└── data/                        # Demo data (optional)
```

## 🔒 Security

### Access Control
- **Portal Users**: Read-only access to their own manufacturing orders
- **Domain Filtering**: Enforced at database level through security rules
- **Commercial Partner Support**: Includes orders from all child partners

### Security Rule Implementation
```xml
Domain: [
    ('sale_line_id.order_partner_id', 'child_of', 
     [user.partner_id.commercial_partner_id.id])
]
```

### Best Practices
- No sensitive manufacturing data exposed
- Cost information is not displayed to portal users
- Internal notes and comments are hidden

## 🔧 Technical Details

### Controller Architecture
The module extends `CustomerPortal` controller with:
- `_prepare_home_portal_values()`: Adds MO counter to portal home
- `_prepare_mo_domain()`: Creates security domain for filtering
- `portal_my_mos()`: Main route handler for MO display

### Database Relationships
- Links through `sale_line_id` to track MO origin
- Alternative linking through `procurement_group_id.sale_id`
- Supports both direct and indirect sales-to-manufacturing relationships

### Performance Considerations
- Implements pagination to handle large datasets
- Uses `search_count()` for efficient counting
- Leverages Odoo's ORM caching mechanisms

## 🌐 API Routes

### Available Routes
- `GET /my/mos` - Display all manufacturing orders
- `GET /my/mos/page/<int:page>` - Paginated MO display

### Query Parameters
- `date_begin`: Filter start date (YYYY-MM-DD)
- `date_end`: Filter end date (YYYY-MM-DD)
- `sortby`: Sort option ('date' or 'name')

### Response Format
Returns rendered HTML template with:
- List of manufacturing orders
- Pagination controls
- Sorting options
- Filtering interface

## 📸 Screenshots

### Portal Home Page
The module adds a dedicated card showing the total count of manufacturing orders accessible to the customer.

### Manufacturing Orders List
A comprehensive table view displaying all relevant manufacturing information with sorting and filtering capabilities.

### Mobile Responsive View
Optimized layout for mobile devices ensuring accessibility on all platforms.

## 👤 Author

**Salah Alhjany**
- 📱 Phone: +967711778764
- 📧 Instagram: [@saleh_alhjany](https://www.instagram.com/saleh_alhjany)
- 🌐 Location: Yemen

## 💬 Support

For support, bug reports, or feature requests:
1. Check the [Issues](https://github.com/[repository]/issues) section
2. Contact the author directly via provided contact information
3. Submit a pull request for contributions

### Common Issues and Solutions

**Issue**: Customers don't see their manufacturing orders
- **Solution**: Verify the commercial partner relationship is correctly set
- **Check**: Sale order partner matches portal user's commercial partner

**Issue**: Performance issues with large datasets
- **Solution**: Ensure proper database indexing on sale_line_id
- **Consider**: Implementing additional caching mechanisms

## 📄 License

This module is licensed under **LGPL-3** (GNU Lesser General Public License v3.0).

### Key Points:
- Free to use in commercial and non-commercial projects
- Modifications must be released under the same license
- Can be integrated with proprietary Odoo modules
- No warranty provided

---

## 🚀 Future Enhancements

Planned features for future versions:
- [ ] Manufacturing progress percentage display
- [ ] Email notifications for status changes
- [ ] Document attachments visibility
- [ ] Production timeline visualization
- [ ] Quality check results display
- [ ] Delivery date predictions
- [ ] Multi-language support
- [ ] Export functionality (PDF/Excel)

## 📝 Changelog

### Version 18.0.1.0.0 (Current)
- Initial release for Odoo 18.0
- Basic manufacturing order visibility
- Portal integration
- Security rules implementation
- Responsive design

---

*Built with ❤️ for the Odoo Community*
