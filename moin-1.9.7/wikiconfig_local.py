from wikiconfig import LocalConfig

class Config(LocalConfig):
    configuration_item_1 = 'value1'
    # Security ----------------------------------------------------------
   # This is checked by some rather critical and potentially harmful actions,
   # like despam or PackageInstaller action:
    superuser = [u"Loki"]
   # IMPORTANT: grant yourself admin rights! replace YourName with
   # your user name. See HelpOnAccessControlLists for more help.
   # All acl_rights_xxx options must use unicode [Unicode]
    acl_rights_before = u"Loki:read,write,delete,revert,admin"
   # User interface ----------------------------------------------------
   # Add your wikis important pages at the end. It is not recommended to
   # remove the default links.  Leave room for user links - don't use
   # more than 6 short items.
   # You MUST use Unicode strings here, but you need not use localized
   # page names for system and help pages, those will be used automatically
   # according to the user selected language. [Unicode]
    navi_bar = [
           # If you want to show your page_front_page here:
           u'Clever Creations',
           u'RecentChanges',
           u'FindPage',
           u'HelpContents',
        ]
    
   
   # The default theme anonymous or new users get
    theme_default = 'valhalla'
   
   
   # Language options --------------------------------------------------
   
   # See http://moinmo.in/ConfigMarket for configuration in
   # YOUR language that other people contributed.
   
   # The main wiki language, set the direction of the wiki pages
    language_default = 'en'
   
   # the following regexes should match the complete name when used in free text
   # the group 'all' shall match all, while the group 'key' shall match the key only
   # e.g. CategoryFoo -> group 'all' ==  CategoryFoo, group 'key' == Foo
   # moin's code will add ^ / $ at beginning / end when needed
   # You must use Unicode strings here [Unicode]
    page_category_regex = ur'(?P<all>Category(?P<key>(?!Template)\S+))'
    page_dict_regex = ur'(?P<all>(?P<key>\S+)Dict)'
    page_group_regex = ur'(?P<all>(?P<key>\S+)Group)'
    page_template_regex = ur'(?P<all>(?P<key>\S+)Template)'
   
   # Content options ---------------------------------------------------
   
   # Show users hostnames in RecentChanges
    show_hosts = 1
   
   # Enable graphical charts, requires gdchart.
   #chart_options = {'width': 600, 'height': 300}

