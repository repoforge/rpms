# $Id$
# Authority: dag


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%{?fc1:%define _without_pcapbpf_h 1}
%{?el3:%define _without_pcapbpf_h 1}
%{?rh9:%define _without_pcapbpf_h 1}
%{?rh7:%define _without_pcapbpf_h 1}
%{?el2:%define _without_pcapbpf_h 1}

%define real_version 0.9b3

Summary: SSLSSLv3/TLS network protocol analyzer
Name: ssldump
Version: 0.9
Release: 0.beta3.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.rtfm.com/ssldump/

Source: http://www.rtfm.com/ssldump/ssldump-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel >= 0.9.6, libpcap >= 0.4, libtool
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When ssldump identifies SSLv3/TLS traffic,
ssldump decodes the records and displays them in a textual form to
stdout.

If provided with the appropriate keying material, ssldump will also
decrypt the connections and display the application data traffic.

%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e 's|^(#include <openssl/x509v3.h>)$|$1\n#include <openssl/md5.h>|' ssl/ssldecode.c

%{!?_without_pcapbpf_h:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h base/*.c}

%{?el3:%{__perl} -pi.orig -e 's|^(CFLAGS) \+= |$1 += -I/usr/kerberos/include |' Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^(CFLAGS) \+= |$1 += -I/usr/kerberos/include |' Makefile.in}

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	BINDIR="%{buildroot}%{_sbindir}" \
	MANDIR="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT CREDITS INSTALL* README* VERSION
%doc %{_mandir}/man1/ssldump.1*
%{_sbindir}/ssldump

%changelog
* Mon Jul 09 2007 Dag Wieers <dag@wieers.com> - 0.9-0.beta3.2
- Added fix for missing md5.h include on RHEL5. (Mark Phillips)

* Sun Apr 10 2005 Dag Wieers <dag@wieers.com> - 0.9-0.beta3.1
- Initial package. (using DAR)
