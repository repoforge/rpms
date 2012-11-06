# $Id$
# Authority: dries
# Upstream: Christian Grothoff <christian$grothoff,org>


Summary: Peer-to-peer framework
Name: gnunet
Version: 0.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gnunet.org/

Source: http://gnunet.org/download/gnunet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gnutls
Requires: libmicrohttpd
Requires: libidn
Requires: libunistring
Requires: sqlite

BuildRequires: curl-devel >= 7.15.4
BuildRequires: gmp-devel
BuildRequires: gnutls-devel
BuildRequires: libextractor-devel
BuildRequires: libgcrypt-devel >= 1.2.0
BuildRequires: libmicrohttpd-devel
BuildRequires: libidn-devel
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libunistring-devel
BuildRequires: mysql-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: sqlite-devel

%description
GNUnet is a peer-to-peer framework with focus on providing security. All 
peer-to-peer messages in the network are confidential and authenticated. 
The framework provides a transport abstraction layer and can currently 
encapsulate the network traffic in UDP (IPv4 and IPv6), TCP (IPv4 and IPv6), 
HTTP, or SMTP messages. GNUnet supports accounting to provide contributing 
nodes with better service. The primary service build on top of the framework 
is anonymous file sharing.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package static
Summary: Static libraries for %{name}.
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
This package contains the static libraries for %{name}. 

%prep
%setup -n %{name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/gnunet*.1*
%doc %{_mandir}/man5/gnunet*.5*
%{_bindir}/gnunet-directory
%{_bindir}/gnunet-download
%{_bindir}/gnunet-download-manager.scm
%{_bindir}/gnunet-pseudonym
%{_bindir}/gnunet-search
%{_bindir}/gnunet-unindex
%{_bindir}/gnunet-vpn
%{_bindir}/gnunet-auto-share
%{_bindir}/gnunet-arm
%{_bindir}/gnunet-ats
%{_bindir}/gnunet-config
%{_bindir}/gnunet-core
%{_bindir}/gnunet-dns2gns
%{_bindir}/gnunet-ecc
%{_bindir}/gnunet-fs
%{_bindir}/gnunet-gns
%{_bindir}/gnunet-gns-import.sh
%{_bindir}/gnunet-gns-proxy
%{_bindir}/gnunet-gns-proxy-setup-ca
%{_bindir}/gnunet-namestore
%{_bindir}/gnunet-nat-server
%{_bindir}/gnunet-peerinfo
%{_bindir}/gnunet-publish
%{_bindir}/gnunet-resolver
%{_bindir}/gnunet-rsa
%{_bindir}/gnunet-statistics
%{_bindir}/gnunet-template
%{_bindir}/gnunet-testing
%{_bindir}/gnunet-testing-run-service
%{_bindir}/gnunet-transport
%{_bindir}/gnunet-transport-certificate-creation
%{_bindir}/gnunet-uri
%{_libdir}/gnunet/libexec/gnunet-daemon-exit
%{_libdir}/gnunet/libexec/gnunet-daemon-hostlist
%{_libdir}/gnunet/libexec/gnunet-daemon-pt
%{_libdir}/gnunet/libexec/gnunet-daemon-topology
%{_libdir}/gnunet/libexec/gnunet-gns-fcfsd
%{_libdir}/gnunet/libexec/gnunet-helper-dns
%{_libdir}/gnunet/libexec/gnunet-helper-exit
%{_libdir}/gnunet/libexec/gnunet-helper-fs-publish
%{_libdir}/gnunet/libexec/gnunet-helper-nat-client
%{_libdir}/gnunet/libexec/gnunet-helper-nat-server
%{_libdir}/gnunet/libexec/gnunet-helper-testbed
%{_libdir}/gnunet/libexec/gnunet-helper-transport-wlan
%{_libdir}/gnunet/libexec/gnunet-helper-transport-wlan-dummy
%{_libdir}/gnunet/libexec/gnunet-helper-vpn
%{_libdir}/gnunet/libexec/gnunet-service-arm
%{_libdir}/gnunet/libexec/gnunet-service-ats
%{_libdir}/gnunet/libexec/gnunet-service-core
%{_libdir}/gnunet/libexec/gnunet-service-datastore
%{_libdir}/gnunet/libexec/gnunet-service-dht
%{_libdir}/gnunet/libexec/gnunet-service-dns
%{_libdir}/gnunet/libexec/gnunet-service-fs
%{_libdir}/gnunet/libexec/gnunet-service-gns
%{_libdir}/gnunet/libexec/gnunet-service-lockmanager
%{_libdir}/gnunet/libexec/gnunet-service-mesh
%{_libdir}/gnunet/libexec/gnunet-service-mesh-new
%{_libdir}/gnunet/libexec/gnunet-service-namestore
%{_libdir}/gnunet/libexec/gnunet-service-nse
%{_libdir}/gnunet/libexec/gnunet-service-peerinfo
%{_libdir}/gnunet/libexec/gnunet-service-resolver
%{_libdir}/gnunet/libexec/gnunet-service-statistics
%{_libdir}/gnunet/libexec/gnunet-service-template
%{_libdir}/gnunet/libexec/gnunet-service-testbed
%{_libdir}/gnunet/libexec/gnunet-service-transport
%{_libdir}/gnunet/libexec/gnunet-service-vpn
%{_libdir}/gnunet/libexec/mockup-service
%{_libdir}/gnunet/libgnunet_plugin_block_dht.so
%{_libdir}/gnunet/libgnunet_plugin_block_dns.so
%{_libdir}/gnunet/libgnunet_plugin_block_fs.so
%{_libdir}/gnunet/libgnunet_plugin_block_gns.so
%{_libdir}/gnunet/libgnunet_plugin_block_mesh.so
%{_libdir}/gnunet/libgnunet_plugin_block_template.so
%{_libdir}/gnunet/libgnunet_plugin_block_test.so
%{_libdir}/gnunet/libgnunet_plugin_datacache_mysql.so
%{_libdir}/gnunet/libgnunet_plugin_datacache_sqlite.so
%{_libdir}/gnunet/libgnunet_plugin_datacache_template.so
%{_libdir}/gnunet/libgnunet_plugin_datastore_mysql.so
%{_libdir}/gnunet/libgnunet_plugin_datastore_sqlite.so
%{_libdir}/gnunet/libgnunet_plugin_datastore_template.so
%{_libdir}/gnunet/libgnunet_plugin_namestore_sqlite.so
%{_libdir}/gnunet/libgnunet_plugin_test.so
%{_libdir}/gnunet/libgnunet_plugin_transport_http_client.so
%{_libdir}/gnunet/libgnunet_plugin_transport_http_server.so
%{_libdir}/gnunet/libgnunet_plugin_transport_https_client.so
%{_libdir}/gnunet/libgnunet_plugin_transport_https_server.so
%{_libdir}/gnunet/libgnunet_plugin_transport_tcp.so
%{_libdir}/gnunet/libgnunet_plugin_transport_template.so
%{_libdir}/gnunet/libgnunet_plugin_transport_udp.so
%{_libdir}/gnunet/libgnunet_plugin_transport_unix.so
%{_libdir}/gnunet/libgnunet_plugin_transport_wlan.so
%{_libdir}/libgnunetarm.so
%{_libdir}/libgnunetarm.so.1
%{_libdir}/libgnunetarm.so.1.0.2
%{_libdir}/libgnunetats.so
%{_libdir}/libgnunetats.so.0
%{_libdir}/libgnunetats.so.0.3.0
%{_libdir}/libgnunetblock.so
%{_libdir}/libgnunetblock.so.0
%{_libdir}/libgnunetblock.so.0.0.0
%{_libdir}/libgnunetcore.so
%{_libdir}/libgnunetcore.so.0
%{_libdir}/libgnunetcore.so.0.0.1
%{_libdir}/libgnunetdatacache.so
%{_libdir}/libgnunetdatacache.so.0
%{_libdir}/libgnunetdatacache.so.0.0.1
%{_libdir}/libgnunetdatastore.so
%{_libdir}/libgnunetdatastore.so.1
%{_libdir}/libgnunetdatastore.so.1.0.0
%{_libdir}/libgnunetdht.so
%{_libdir}/libgnunetdht.so.0
%{_libdir}/libgnunetdht.so.0.1.1
%{_libdir}/libgnunetdns.so
%{_libdir}/libgnunetdns.so.0
%{_libdir}/libgnunetdns.so.0.0.0
%{_libdir}/libgnunetdnsparser.so
%{_libdir}/libgnunetdnsparser.so.0
%{_libdir}/libgnunetdnsparser.so.0.0.0
%{_libdir}/libgnunetdnsstub.so
%{_libdir}/libgnunetdnsstub.so.0
%{_libdir}/libgnunetdnsstub.so.0.0.0
%{_libdir}/libgnunetfragmentation.so
%{_libdir}/libgnunetfragmentation.so.2
%{_libdir}/libgnunetfragmentation.so.2.0.0
%{_libdir}/libgnunetfs.so
%{_libdir}/libgnunetfs.so.2
%{_libdir}/libgnunetfs.so.2.0.2
%{_libdir}/libgnunetgns.so
%{_libdir}/libgnunetgns.so.0
%{_libdir}/libgnunetgns.so.0.0.0
%{_libdir}/libgnunetgns_common.so
%{_libdir}/libgnunetgns_common.so.0
%{_libdir}/libgnunetgns_common.so.0.0.0
%{_libdir}/libgnunethello.so
%{_libdir}/libgnunethello.so.0
%{_libdir}/libgnunethello.so.0.0.0
%{_libdir}/libgnunetlockmanager.so
%{_libdir}/libgnunetlockmanager.so.0
%{_libdir}/libgnunetlockmanager.so.0.0.0
%{_libdir}/libgnunetmesh.so
%{_libdir}/libgnunetmesh.so.1
%{_libdir}/libgnunetmesh.so.1.0.0
%{_libdir}/libgnunetmeshblock.so
%{_libdir}/libgnunetmeshblock.so.2
%{_libdir}/libgnunetmeshblock.so.2.0.0
%{_libdir}/libgnunetmysql.so
%{_libdir}/libgnunetmysql.so.0
%{_libdir}/libgnunetmysql.so.0.0.0
%{_libdir}/libgnunetnamestore.so
%{_libdir}/libgnunetnamestore.so.0
%{_libdir}/libgnunetnamestore.so.0.0.1
%{_libdir}/libgnunetnat.so
%{_libdir}/libgnunetnat.so.0
%{_libdir}/libgnunetnat.so.0.0.1
%{_libdir}/libgnunetnse.so
%{_libdir}/libgnunetnse.so.0
%{_libdir}/libgnunetnse.so.0.0.0
%{_libdir}/libgnunetpeerinfo.so
%{_libdir}/libgnunetpeerinfo.so.0
%{_libdir}/libgnunetpeerinfo.so.0.0.0
%{_libdir}/libgnunetregex.so
%{_libdir}/libgnunetregex.so.0
%{_libdir}/libgnunetregex.so.0.0.0
%{_libdir}/libgnunetstatistics.so
%{_libdir}/libgnunetstatistics.so.0
%{_libdir}/libgnunetstatistics.so.0.1.2
%{_libdir}/libgnunetstream.so
%{_libdir}/libgnunetstream.so.0
%{_libdir}/libgnunetstream.so.0.0.0
%{_libdir}/libgnunettestbed.so
%{_libdir}/libgnunettestbed.so.0
%{_libdir}/libgnunettestbed.so.0.0.0
%{_libdir}/libgnunettesting.so
%{_libdir}/libgnunettesting.so.1
%{_libdir}/libgnunettesting.so.1.0.0
%{_libdir}/libgnunettesting_old.so
%{_libdir}/libgnunettesting_old.so.0
%{_libdir}/libgnunettesting_old.so.0.0.1
%{_libdir}/libgnunettransport.so
%{_libdir}/libgnunettransport.so.1
%{_libdir}/libgnunettransport.so.1.0.1
%{_libdir}/libgnunettransporttesting.so
%{_libdir}/libgnunettransporttesting.so.0
%{_libdir}/libgnunettransporttesting.so.0.0.0
%{_libdir}/libgnunettun.so
%{_libdir}/libgnunettun.so.0
%{_libdir}/libgnunettun.so.0.0.0
%{_libdir}/libgnunetutil.so
%{_libdir}/libgnunetutil.so.9
%{_libdir}/libgnunetutil.so.9.0.0
%{_libdir}/libgnunetvpn.so
%{_libdir}/libgnunetvpn.so.0
%{_libdir}/libgnunetvpn.so.0.0.0
%{_libdir}/pkgconfig/gnunetarm.pc
%{_libdir}/pkgconfig/gnunetats.pc
%{_libdir}/pkgconfig/gnunetblock.pc
%{_libdir}/pkgconfig/gnunetcore.pc
%{_libdir}/pkgconfig/gnunetdatacache.pc
%{_libdir}/pkgconfig/gnunetdatastore.pc
%{_libdir}/pkgconfig/gnunetdht.pc
%{_libdir}/pkgconfig/gnunetdns.pc
%{_libdir}/pkgconfig/gnunetdnsparser.pc
%{_libdir}/pkgconfig/gnunetdv.pc
%{_libdir}/pkgconfig/gnunetfragmentation.pc
%{_libdir}/pkgconfig/gnunetfs.pc
%{_libdir}/pkgconfig/gnunetgns.pc
%{_libdir}/pkgconfig/gnunethello.pc
%{_libdir}/pkgconfig/gnunetlockmanager.pc
%{_libdir}/pkgconfig/gnunetmesh.pc
%{_libdir}/pkgconfig/gnunetmysql.pc
%{_libdir}/pkgconfig/gnunetnamestore.pc
%{_libdir}/pkgconfig/gnunetnat.pc
%{_libdir}/pkgconfig/gnunetnse.pc
%{_libdir}/pkgconfig/gnunetpeerinfo.pc
%{_libdir}/pkgconfig/gnunetpostgres.pc
%{_libdir}/pkgconfig/gnunetregex.pc
%{_libdir}/pkgconfig/gnunetstatistics.pc
%{_libdir}/pkgconfig/gnunetstream.pc
%{_libdir}/pkgconfig/gnunettestbed.pc
%{_libdir}/pkgconfig/gnunettesting.pc
%{_libdir}/pkgconfig/gnunettransport.pc
%{_libdir}/pkgconfig/gnunettun.pc
%{_libdir}/pkgconfig/gnunetutil.pc
%{_libdir}/pkgconfig/gnunetvpn.pc
%{_datarootdir}/doc/gnunet/COPYING
%{_datarootdir}/doc/gnunet/README
%{_datarootdir}/doc/gnunet/README.mysql
%{_datarootdir}/doc/gnunet/README.postgres
%{_datarootdir}/gnunet/config.d/arm.conf
%{_datarootdir}/gnunet/config.d/ats.conf
%{_datarootdir}/gnunet/config.d/core.conf
%{_datarootdir}/gnunet/config.d/datacache.conf
%{_datarootdir}/gnunet/config.d/datastore.conf
%{_datarootdir}/gnunet/config.d/dht.conf
%{_datarootdir}/gnunet/config.d/dns.conf
%{_datarootdir}/gnunet/config.d/exit.conf
%{_datarootdir}/gnunet/config.d/fs.conf
%{_datarootdir}/gnunet/config.d/gns.conf
%{_datarootdir}/gnunet/config.d/hostlist.conf
%{_datarootdir}/gnunet/config.d/lockmanager.conf
%{_datarootdir}/gnunet/config.d/mesh.conf
%{_datarootdir}/gnunet/config.d/namestore.conf
%{_datarootdir}/gnunet/config.d/nat.conf
%{_datarootdir}/gnunet/config.d/nse.conf
%{_datarootdir}/gnunet/config.d/peerinfo.conf
%{_datarootdir}/gnunet/config.d/pt.conf
%{_datarootdir}/gnunet/config.d/resolver.conf
%{_datarootdir}/gnunet/config.d/statistics.conf
%{_datarootdir}/gnunet/config.d/template.conf
%{_datarootdir}/gnunet/config.d/testbed.conf
%{_datarootdir}/gnunet/config.d/testing.conf
%{_datarootdir}/gnunet/config.d/testing_old.conf
%{_datarootdir}/gnunet/config.d/topology.conf
%{_datarootdir}/gnunet/config.d/transport.conf
%{_datarootdir}/gnunet/config.d/util.conf
%{_datarootdir}/gnunet/config.d/vpn.conf
%{_datarootdir}/gnunet/gnunet-logo-color.png
%{_datarootdir}/gnunet/hellos/02UK
%{_datarootdir}/gnunet/hellos/1G1M
%{_datarootdir}/gnunet/hellos/7RAV
%{_datarootdir}/gnunet/hellos/8B4T
%{_datarootdir}/gnunet/hellos/94CH
%{_datarootdir}/gnunet/hellos/ATF4
%{_datarootdir}/gnunet/hellos/F1GT
%{_datarootdir}/gnunet/hellos/KD9V
%{_datarootdir}/gnunet/hellos/KUPL
%{_datarootdir}/gnunet/hellos/LJR8
%{_datarootdir}/gnunet/hellos/R69Q
%{_datarootdir}/gnunet/hellos/R6OV
%{_datarootdir}/gnunet/hellos/RL7P
%{_datarootdir}/gnunet/testing_hostkeys.dat



%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gnunet/gettext.h
%{_includedir}/gnunet/gns_protocol.h
%{_includedir}/gnunet/gnunet_applications.h
%{_includedir}/gnunet/gnunet_arm_service.h
%{_includedir}/gnunet/gnunet_ats_service.h
%{_includedir}/gnunet/gnunet_bandwidth_lib.h
%{_includedir}/gnunet/gnunet_bio_lib.h
%{_includedir}/gnunet/gnunet_block_lib.h
%{_includedir}/gnunet/gnunet_block_plugin.h
%{_includedir}/gnunet/gnunet_chat_service.h
%{_includedir}/gnunet/gnunet_client_lib.h
%{_includedir}/gnunet/gnunet_common.h
%{_includedir}/gnunet/gnunet_config.h
%{_includedir}/gnunet/gnunet_configuration_lib.h
%{_includedir}/gnunet/gnunet_connection_lib.h
%{_includedir}/gnunet/gnunet_constants.h
%{_includedir}/gnunet/gnunet_container_lib.h
%{_includedir}/gnunet/gnunet_core_service.h
%{_includedir}/gnunet/gnunet_crypto_lib.h
%{_includedir}/gnunet/gnunet_datacache_lib.h
%{_includedir}/gnunet/gnunet_datacache_plugin.h
%{_includedir}/gnunet/gnunet_datastore_plugin.h
%{_includedir}/gnunet/gnunet_datastore_service.h
%{_includedir}/gnunet/gnunet_dht_service.h
%{_includedir}/gnunet/gnunet_directories.h
%{_includedir}/gnunet/gnunet_disk_lib.h
%{_includedir}/gnunet/gnunet_dns_service.h
%{_includedir}/gnunet/gnunet_dnsparser_lib.h
%{_includedir}/gnunet/gnunet_dnsstub_lib.h
%{_includedir}/gnunet/gnunet_dv_service.h
%{_includedir}/gnunet/gnunet_fragmentation_lib.h
%{_includedir}/gnunet/gnunet_fs_service.h
%{_includedir}/gnunet/gnunet_getopt_lib.h
%{_includedir}/gnunet/gnunet_gns_service.h
%{_includedir}/gnunet/gnunet_hello_lib.h
%{_includedir}/gnunet/gnunet_helper_lib.h
%{_includedir}/gnunet/gnunet_load_lib.h
%{_includedir}/gnunet/gnunet_lockmanager_service.h
%{_includedir}/gnunet/gnunet_mesh_service.h
%{_includedir}/gnunet/gnunet_mysql_lib.h
%{_includedir}/gnunet/gnunet_namestore_plugin.h
%{_includedir}/gnunet/gnunet_namestore_service.h
%{_includedir}/gnunet/gnunet_nat_lib.h
%{_includedir}/gnunet/gnunet_network_lib.h
%{_includedir}/gnunet/gnunet_nse_service.h
%{_includedir}/gnunet/gnunet_os_lib.h
%{_includedir}/gnunet/gnunet_peer_lib.h
%{_includedir}/gnunet/gnunet_peerinfo_service.h
%{_includedir}/gnunet/gnunet_plugin_lib.h
%{_includedir}/gnunet/gnunet_postgres_lib.h
%{_includedir}/gnunet/gnunet_program_lib.h
%{_includedir}/gnunet/gnunet_protocols.h
%{_includedir}/gnunet/gnunet_pseudonym_lib.h
%{_includedir}/gnunet/gnunet_regex_lib.h
%{_includedir}/gnunet/gnunet_resolver_service.h
%{_includedir}/gnunet/gnunet_scheduler_lib.h
%{_includedir}/gnunet/gnunet_server_lib.h
%{_includedir}/gnunet/gnunet_service_lib.h
%{_includedir}/gnunet/gnunet_signal_lib.h
%{_includedir}/gnunet/gnunet_signatures.h
%{_includedir}/gnunet/gnunet_statistics_service.h
%{_includedir}/gnunet/gnunet_stream_lib.h
%{_includedir}/gnunet/gnunet_strings_lib.h
%{_includedir}/gnunet/gnunet_testbed_service.h
%{_includedir}/gnunet/gnunet_testing_lib-new.h
%{_includedir}/gnunet/gnunet_testing_lib.h
%{_includedir}/gnunet/gnunet_time_lib.h
%{_includedir}/gnunet/gnunet_transport_plugin.h
%{_includedir}/gnunet/gnunet_transport_service.h
%{_includedir}/gnunet/gnunet_tun_lib.h
%{_includedir}/gnunet/gnunet_util_lib.h
%{_includedir}/gnunet/gnunet_vpn_service.h
%{_includedir}/gnunet/platform.h
%{_includedir}/gnunet/plibc.h
%{_libdir}/gnunet/libgnunet_plugin_block_dht.la
%{_libdir}/gnunet/libgnunet_plugin_block_dns.la
%{_libdir}/gnunet/libgnunet_plugin_block_fs.la
%{_libdir}/gnunet/libgnunet_plugin_block_gns.la
%{_libdir}/gnunet/libgnunet_plugin_block_mesh.la
%{_libdir}/gnunet/libgnunet_plugin_block_template.la
%{_libdir}/gnunet/libgnunet_plugin_block_test.la
%{_libdir}/gnunet/libgnunet_plugin_datacache_mysql.la
%{_libdir}/gnunet/libgnunet_plugin_datacache_sqlite.la
%{_libdir}/gnunet/libgnunet_plugin_datacache_template.la
%{_libdir}/gnunet/libgnunet_plugin_datastore_mysql.la
%{_libdir}/gnunet/libgnunet_plugin_datastore_sqlite.la
%{_libdir}/gnunet/libgnunet_plugin_datastore_template.la
%{_libdir}/gnunet/libgnunet_plugin_namestore_sqlite.la
%{_libdir}/gnunet/libgnunet_plugin_test.la
%{_libdir}/gnunet/libgnunet_plugin_transport_http_client.la
%{_libdir}/gnunet/libgnunet_plugin_transport_http_server.la
%{_libdir}/gnunet/libgnunet_plugin_transport_https_client.la
%{_libdir}/gnunet/libgnunet_plugin_transport_https_server.la
%{_libdir}/gnunet/libgnunet_plugin_transport_tcp.la
%{_libdir}/gnunet/libgnunet_plugin_transport_template.la
%{_libdir}/gnunet/libgnunet_plugin_transport_udp.la
%{_libdir}/gnunet/libgnunet_plugin_transport_unix.la
%{_libdir}/gnunet/libgnunet_plugin_transport_wlan.la
%{_libdir}/libgnunetarm.la
%{_libdir}/libgnunetats.la
%{_libdir}/libgnunetblock.la
%{_libdir}/libgnunetcore.la
%{_libdir}/libgnunetdatacache.la
%{_libdir}/libgnunetdatastore.la
%{_libdir}/libgnunetdht.la
%{_libdir}/libgnunetdns.la
%{_libdir}/libgnunetdnsparser.la
%{_libdir}/libgnunetdnsstub.la
%{_libdir}/libgnunetfragmentation.la
%{_libdir}/libgnunetfs.la
%{_libdir}/libgnunetgns.la
%{_libdir}/libgnunetgns_common.la
%{_libdir}/libgnunethello.la
%{_libdir}/libgnunetlockmanager.la
%{_libdir}/libgnunetmesh.la
%{_libdir}/libgnunetmeshblock.la
%{_libdir}/libgnunetmysql.la
%{_libdir}/libgnunetnamestore.la
%{_libdir}/libgnunetnat.la
%{_libdir}/libgnunetnse.la
%{_libdir}/libgnunetpeerinfo.la
%{_libdir}/libgnunetregex.la
%{_libdir}/libgnunetstatistics.la
%{_libdir}/libgnunetstream.la
%{_libdir}/libgnunettestbed.la
%{_libdir}/libgnunettesting.la
%{_libdir}/libgnunettesting_old.la
%{_libdir}/libgnunettransport.la
%{_libdir}/libgnunettransporttesting.la
%{_libdir}/libgnunettun.la
%{_libdir}/libgnunetutil.la
%{_libdir}/libgnunetvpn.la

%files static
%defattr(-, root, root, 0755)

%changelog
* Tue Nov 06 2012 Christoph Maser <cmaser@gmx.de> - 0.9.4-1
- Updated to release 0.9.4.

* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.

