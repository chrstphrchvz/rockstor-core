
TCP = 'tcp'
UDP = 'udp'
ONE_GB = 1073741824

openvpn = {u'containers': {u'openvpn': {'image': 'kylemanna/openvpn',
                                        'ports': {'1194':
                                                  {'protocol': 'udp',
                                                   'label': 'Server port',
                                                   'host_default': 1194,
                                                   'description': 'OpenVPN server listening port. You may need to open it on your firewall.',},},
                                        'launch_order': 2,
                                        u'opts': [['--cap-add=NET_ADMIN', ''],
                                                  ['--volumes-from', 'ovpn-data'], ],},
                           u'ovpn-data': {'image': 'busybox',
                                          'opts': [['-v', '/etc/openvpn'], ],
                                          'launch_order': 1,},},

           'custom_config': {'servername':
                             {'label': 'Server address',
                              'description': "Your Rockstor system's public ip address or hostname.",},},

           'description': 'Open Source VPN server',
           'website': 'https://openvpn.net/',
           'icon': 'https://openvpn.net/',
           'more_info': '<h4>Additional steps are required by this Rockon.</h4><p>The following steps require you to execute commands as the <code>root</code> user on your Rockstor system.</p><h4><u>Initialize PKI</u>&nbsp;&nbsp;&nbsp;&nbsp;<i>Do this only once.</i></h4><code>/opt/rockstor/bin/ovpn-initpki</code><h4><u>Generate a client certificate</u>&nbsp;&nbsp;&nbsp;&nbsp;<i>One for every client(without passphrase)</i></h4><code>/opt/rockstor/bin/ovpn-client-gen</code><br><h4><u>Retrieve client configuration</u>&nbsp;&nbsp;&nbsp;&nbsp<i>For any one of your clients. The resulting .ovpn file can be used to connect.</i></h4><code>/opt/rockstor/bin/ovpn-client-print</code><h4><u>Configure firewall</u></h4><p>If your Rockstor system is behind a firewall, you will need to configure it to allow OpenVPN traffic to forward to your Rockstor system.</p>',
           'volume_add_support': False, }

owncloud = {'ui': {'slug': '',
                   'https': True,},

            'containers': {'owncloud': {'image': 'pschmitt/owncloud',
                                        'ports': {'443':
                                                  {'ui': True,
                                                   'host_default': 8080,
                                                   'protocol': 'tcp',
                                                   'label': 'WebUI port',
                                                   'description': 'OwnCloud WebUI port. Since Rockstor WebUI runs on 443, choose a different port or the suggested default.',},},
                                        'volumes': {'/var/www/owncloud/data':
                                                    {'description': 'Choose a dedicated Share for OwnCloud data. Eg: create a Share called owncloud-data for this purpose alone.',
                                                     'min_size': 1073741824,
                                                     'label': 'Data directory',},
                                                    '/var/www/owncloud/config':
                                                    {'description': 'Choose a dedicated Share for OwnCloud configuration. Eg: create a Share called owncloud-config for this purpose alone.',
                                                     'label': 'Config directory',
                                                     'min_size': 1073741824,},},
                                        'launch_order': 2,},
                           'owncloud-postgres': {'image': 'postgres',
                                                 'volumes': {'/var/lib/postgresql/data':
                                                             {'description': 'Choose a dedicated Share for OwnClouds postgresql database. Eg: create a Share called owncloud-db for this purpose alone.',
                                                              'label': 'Database',
                                                              'min_size': 1073741824, }, },
                                                 'launch_order': 1}, },
            'container_links': {'owncloud': [{'source_container': 'owncloud-postgres',
                                              'name': 'db'},]},
            'custom_config': {'db_user':
                              {'label': 'DB User',
                               'description': 'Choose a administrator username for the OwnCloud database.',},
                              'db_pw':
                              {'label': 'DB Password',
                               'description': 'Choose a secure password for the database admin user',},},
            'description': 'Secure file sharing and hosting',
            'website': 'https://owncloud.org/',
            'icon': 'https://owncloud.org/wp-content/themes/owncloudorgnew/assets/img/common/logo_owncloud.svg',
            'more_info': '<p>Default username for your OwnCloud UI is <code>admin</code> and password is <code>changeme</code></p>',
            'volume_add_support': False, }

syncthing = {'ui': {'slug': '',
                    'https': True,},

             'containers': {'syncthing': {'image': 'istepanov/syncthing',
                                          'ports': {'8384':
                                                    {'ui': True,
                                                     'host_default': 8090,
                                                     'protocol': TCP,
                                                     'label': 'WebUI port',
                                                     'description': 'Syncthing WebUI port. Choose the suggested default unless you have a strong reason not to.',},
                                                    '22000':
                                                    {'host_default': 22000,
                                                     'protocol': TCP,
                                                     'label': 'Listening port',
                                                     'description': 'Port for incoming data. You may need to open it on your firewall',},
                                                    '21025':
                                                    {'host_default': 21025,
                                                     'protocol': UDP,
                                                     'label': 'Discovery port',
                                                     'description': 'Port for discovery broadcasts. You may need to open it on your firewall',},},
                                          'volumes': {'/home/syncthing/.config/syncthing':
                                                      {'description': 'Choose a dedicated Share for configuration. Eg: create a Share called syncthing-config for this purpose alone.',
                                                       'min_size': ONE_GB,
                                                       'label': 'Config directory',},
                                                      '/home/syncthing/Sync':
                                                      {'label': 'Data directory',
                                                       'description': 'Choose a dedicated Share for all incoming data. Eg: create a Share called syncthing-data for this purpose alone.',},},
                                          'launch_order': 1,},},
             'description': 'Continuous File Synchronization',
             'website': 'https://syncthing.net/',}

rockons = {'OpenVPN': openvpn,
           'OwnCloud': owncloud,
           'Syncthing': syncthing, }



# rockons = \
#           {

#            u'Plex': {u'app_link': u'web',
#                      u'containers': {u'plex': {u'image': u'timhaak/plex',
#                                                u'opts': {u'net': u'host'},
#                                                u'ports': {u'32400': u'ui'},
#                                                u'volumes': [u'/config', '/data',]}},
#                      u'custom_config': {u'iprange': u'ip range of your network'},
#                      u'description': u'Plex media server',
#                      u'website': u'https://plex.tv/'},
#            'Transmission': {'app_link': '',
#                             'containers': {'transmission': {'image': 'dperson/transmission',
#                                                             'ports': {'9091': 'ui',
#                                                                       '51413': ''},
#                                                             'volumes': ['/var/lib/transmission-daemon/downloads',
#                                                                         '/var/lib/transmission-daemon/incomplete',]}},
#                             'custom_config': {'TRUSER': 'Set the username for your Transmission UI',
#                                               'TRPASSWD': 'Password for the user'},
#                             'description': 'Open Source BitTorrent client',
#                             'website': 'http://www.transmissionbt.com/'},
#            'BTSync': {'app_link': '',
#                       'containers': {'btsync': {'image': 'aostanin/btsync',
#                                                 'ports': {'8888': 'ui'},
#                                                 'volumes': ['/data']}},
#                       'description': 'BitTorrent Sync',
#                       'website': 'https://www.getsync.com/'},

#           }

# help text for Volumes
# It is strongly recommended
