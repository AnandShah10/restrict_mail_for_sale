===============
Restrict Mail Module
===============

Description
-----------

The "Restrict Mail" module for Odoo enhances the functionality of the chatter in the sale order by introducing a boolean field called "restrict_mail" to the res.partner model. When this field is set to True for a partner, emails will not be sent to that partner from the sale order chatter, even if the partner is added as a follower.

Task For Followers in Chatter
------------------------------

The module implements the following tasks based on specific conditions:

1. **Send Message Restriction**: If a partner is restricted (i.e., "restrict_mail" field is True), emails will not be sent by using the "Send Message" option in the chatter.

2. **@ Tag Restriction**: Even if the "@" tag is used to mention a restricted partner, emails will not be sent to them when using the "Send Message" option.

3. **Log Note Functionality**: Despite being restricted, the functionality to log notes still works when mentioning a restricted partner using "@".

4. **Follower Addition Restriction**: If a partner is not a follower and is restricted, they should not be automatically added as a follower using "@" in the log note.

Usage
-----

1. Navigate to the partner form view in Odoo.
2. Set the "restrict_mail" field to True for partners who should not receive emails from the sale order chatter.
3. When using the chatter in a sale order:
   - Emails will not be sent to restricted partners when using the "Send Message" option.
   - Restricted partners will not receive emails even if mentioned using "@".
   - Logging notes will still function normally for restricted partners when mentioned using "@".
   - Restricted partners who are not followers will not be automatically added as followers using "@".

Compatibility
-------------

- This module is compatible with Odoo version 17.0.

License
-------

GPl-3

Support
-------

For any questions, issues, or feedback regarding this module, please contact:
- shahanand1072004@gmail.com

Disclaimer
----------

This module is provided as-is, without any warranty, expressed or implied. Use at your own risk.
