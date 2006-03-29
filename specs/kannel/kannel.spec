# $Id$
# Authority: matthias

Summary: WAP and SMS gateway
Name: kannel
Version: 1.4.0
Release: 4
License: Kannel
Group: System Environment/Daemons
URL: http://www.kannel.org/
Source0: http://www.kannel.org/download/%{version}/gateway-%{version}.tar.bz2
Source1: kannel.logrotate
Source2: kannel.init
Source3: kannel.conf
Patch0: kannel-1.4.0-depend.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bison, byacc, flex, ImageMagick
BuildRequires: libxml2-devel, openssl-devel, zlib-devel
BuildRequires: pcre-devel
# DB backends
BuildRequires: sqlite2-devel
# For the docs... I think we need transfig too, so disable for now.
#BuildRequires: jadetex, tetex-dvips, docbook-dtds, docbook-style-dsssl

%description
The Kannel Open Source WAP and SMS gateway works as both an SMS gateway, for
implementing keyword based services via GSM text messages, and a WAP gateway,
via UDP. The SMS part is fairly mature, the WAP part is early in its
development. In this release, the GET request for WML pages and WMLScript
files via HTTP works, including compilation for WML and WMLScript to binary
forms. Only the data call bearer (UDP) is supported, not SMS.


%package devel
Summary: Development files for the kannel WAP and SMS gateway
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The Kannel Open Source WAP and SMS gateway works as both an SMS gateway, for
implementing keyword based services via GSM text messages, and a WAP gateway,
via UDP. The SMS part is fairly mature, the WAP part is early in its
development. In this release, the GET request for WML pages and WMLScript
files via HTTP works, including compilation for WML and WMLScript to binary
forms. Only the data call bearer (UDP) is supported, not SMS.

Install this package if you need to develop or recompile applications that
use the kannel WAP and SMS gateway.


%prep
%setup -n gateway-%{version}
%{!?rh73:%patch0 -p0 -b .depend}

%{?el3:%{__perl} -pi.orig -e 's|^(CFLAGS)=|$1=-I/usr/kerberos/include |' Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^(CFLAGS)=|$1=-I/usr/kerberos/include |' Makefile.in}


%build
%configure \
    --enable-start-stop-daemon \
    --enable-pcre \
    --with-sqlite
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Install fakesmsc and fakewap, useful for monitoring
%{__install} -m 0755 test/{fakesmsc,fakewap} %{buildroot}%{_bindir}/
# Logrotate entry
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/kannel
# Init script
%{__install} -D -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/rc.d/init.d/kannel
# Default configuration file
%{__install} -D -m 0640 %{SOURCE3} %{buildroot}%{_sysconfdir}/kannel.conf
# Empty log directory
%{__mkdir_p} %{buildroot}%{_var}/log/kannel/
# Rename start-stop-daemon to start-stop-kannel
%{__mv} %{buildroot}%{_sbindir}/start-stop-daemon \
        %{buildroot}%{_sbindir}/start-stop-kannel


%clean
%{__rm} -rf %{buildroot}


%pre
# Create system account
/usr/sbin/useradd -c "Kannel WAP and SMS gateway" -r -M -s '' \
    -d %{_var}/lib/kannel kannel &>/dev/null || :

%post
/sbin/chkconfig --add kannel

%preun
if [ $1 -eq 0 ]; then
    # Last removal, stop service and remove it
    /sbin/service kannel stop &>/dev/null || :
    /sbin/chkconfig --del kannel
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service kannel condrestart &>/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README STATUS
%attr(0640, kannel, kannel) %config(noreplace) %{_sysconfdir}/kannel.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/kannel
%config %{_sysconfdir}/rc.d/init.d/kannel
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%attr(0750, kannel, kannel) %dir %{_var}/log/kannel/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kannel/
%exclude %{_libdir}/kannel/*.a


%changelog
* Mon Jul  4 2005 Matthias Saou <http://freshrpms.net/> 1.4.0-4
- Include (at last!) user creation, logrotate entry and init script.
- Include default configuration file (do nothing, access only from 127.0.0.1).
- Include empty log directory.
- Include fakesmsc and fakewap programs, useful for monitoring purposes.

* Mon Jan 17 2005 Matthias Saou <http://freshrpms.net/> 1.4.0-3
- Added Stefan Radman's patch for kannel bug #173 to fix .depend problem.

* Fri Dec 10 2004 Matthias Saou <http://freshrpms.net/> 1.4.0-1
- Update to 1.4.0.
- Remove the obsolete OpenSSL workaround.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-4
- Added pcre support, doc building (almost) and sqlite backend...
  it still fails with a corrupt first line of .depend on FC3, though.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-2
- Really comment out all scriplets, they're not yet used.

* Thu Jul 29 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-1
- Don't fix the openssl detection for RHL 7.x.

* Thu Jul 22 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-0
- Update to 1.3.2 development version.
- Added -devel sub-package since there are now headers and a static lib.

* Wed Jul 14 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-0
- Initial RPM release, still need to add an init script I think.

