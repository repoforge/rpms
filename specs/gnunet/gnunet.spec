# $Id$
# Authority: dries
# Upstream: Christian Grothoff <christian$grothoff,org>

%{?el4:%define _without_dht 1}
%{?el4:%define _without_guile18 1}

%define real_name GNUnet

Summary: Peer-to-peer framework
Name: gnunet
Version: 0.8.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gnunet.org/

Source: http://gnunet.org/download/GNUnet-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, curl-devel, libextractor-devel, mysql-devel
BuildRequires: gmp-devel, libtool
BuildRequires: libgcrypt-devel >= 1.2.0
BuildRequires: ncurses-devel
%{!?_without_guile18:BuildRequires: guile-devel >= 1.8.0}
#BuildRequires: libtool-ltdl-devel

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
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/gnunet*.1*
%doc %{_mandir}/man5/gnunet*.5*
#%{!?_without_dht:%{_bindir}/gnunet-dht-query}
%{_bindir}/gnunet-directory
%{_bindir}/gnunet-download
%{_bindir}/gnunet-download-manager.scm
%{_bindir}/gnunet-insert
%{_bindir}/gnunet-peer-info
%{_bindir}/gnunet-pseudonym
%{_bindir}/gnunet-search
%{_bindir}/gnunet-stats
%{_bindir}/gnunet-tbench
#%{_bindir}/gnunet-template
%{_bindir}/gnunet-tracekit
%{_bindir}/gnunet-transport-check
%{_bindir}/gnunet-unindex
%{_bindir}/gnunet-update
%{_bindir}/gnunet-vpn
%{_bindir}/gnunet-auto-share
%{_bindir}/gnunet-chat
%{_bindir}/remotetest
%{!?_without_guile18:%{_bindir}/gnunet-setup}
%{_bindir}/gnunetd
%{_libdir}/GNUnet/
%{_libdir}/libgnunetcollection.so.*
%{_libdir}/libgnunetcore.so.*
%{!?_without_dht:%{_libdir}/libgnunetdht_api.so.*}
%{_libdir}/libgnunetecrs.so.*
%{_libdir}/libgnunetfs.so.*
%{_libdir}/libgnunetfsui.so.*
%{_libdir}/libgnunetgetoption_api.so.*
%{_libdir}/libgnunetidentity_api.so.*
%{_libdir}/libgnunetip.so.*
%{_libdir}/libgnunetrpc_util.so.*
%{!?_without_guile18:%{_libdir}/libgnunetsetup.so.*}
%{_libdir}/libgnunettesting_api.so.*
%{_libdir}/libgnunettraffic_api.so.*
%{_libdir}/libgnunetnamespace.so.*
%{_libdir}/libgnunetstats_api.so.*
%{_libdir}/libgnuneturitrack.so.*
%{_libdir}/libgnunetutil.so.*
#%{_libdir}/libgnunetutil_boot.so.*
#%{_libdir}/libgnunetutil_config.so.*
#%{_libdir}/libgnunetutil_containers.so.*
#%{_libdir}/libgnunetutil_cron.so.*
#%{_libdir}/libgnunetutil_crypto.so.*
#%{_libdir}/libgnunetutil_logging.so.*
#%{_libdir}/libgnunetutil_network_client.so.*
%{_libdir}/libgnunetchat_api.so.*
%{_libdir}/libgnunetecrs_core.so.*
%{_libdir}/libgnunetremote_api.so.*
%{_libdir}/libgnunettracekit_api.so.*
%{_datadir}/GNUnet/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GNUnet/
%{_libdir}/libgnunetcollection.so
%{_libdir}/libgnunetcore.so
%{!?_without_dht:%{_libdir}/libgnunetdht_api.so}
%{_libdir}/libgnunetecrs.so
%{_libdir}/libgnunetfs.so
%{_libdir}/libgnunetfsui.so
%{_libdir}/libgnunetgetoption_api.so
%{_libdir}/libgnunetidentity_api.so
%{_libdir}/libgnunetip.so
%{_libdir}/libgnunetrpc_util.so
%{!?_without_guile18:%{_libdir}/libgnunetsetup.so}
%{_libdir}/libgnunettesting_api.so
%{_libdir}/libgnunettraffic_api.so
%{_libdir}/libgnunetnamespace.so
%{_libdir}/libgnunetstats_api.so
%{_libdir}/libgnuneturitrack.so
%{_libdir}/libgnunetutil.so
#%{_libdir}/libgnunetutil_boot.so
#%{_libdir}/libgnunetutil_config.so
#%{_libdir}/libgnunetutil_containers.so
#%{_libdir}/libgnunetutil_cron.so
#%{_libdir}/libgnunetutil_crypto.so
#%{_libdir}/libgnunetutil_logging.so
#%{_libdir}/libgnunetutil_network_client.so
%{_libdir}/libgnunetchat_api.so
%{_libdir}/libgnunetecrs_core.so
%{_libdir}/libgnunetremote_api.so
%{_libdir}/libgnunettracekit_api.so
%exclude %{_libdir}/*.la

%changelog
* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
