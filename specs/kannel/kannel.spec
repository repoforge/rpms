# $Id$

Summary: WAP and SMS gateway
Name: kannel
Version: 1.2.1
Release: 0
License: Kannel
Group: System Environment/Daemons
URL: http://www.kannel.org/
Source: http://www.kannel.org/download/%{version}/gateway-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libxml2-devel, openssl-devel

%description
The Kannel Open Source WAP and SMS gateway works as both an SMS gateway, for
implementing keyword based services via GSM text messages, and a WAP gateway,
via UDP. The SMS part is fairly mature, the WAP part is early in its
development. In this release, the GET request for WML pages and WMLScript
files via HTTP works, including compilation for WML and WMLScript to binary
forms. Only the data call bearer (UDP) is supported, not SMS.


%prep
%setup -n gateway-%{version}


%build
# Fix for the openssl THREADS check, which should be OPENSSL_THREADS
%{__perl} -pi.orig -e 's|(defined\()THREADS\)|$1OPENSSL_THREADS)|g' configure
%configure \
    --enable-start-stop-daemon \
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
if [ $1 -eq 1 ]; then
#   /sbin/chkconfig --add foobar
fi
                                                                                
%preun
if [ $1 -eq 0 ]; then
#   /sbin/service foobar stop >/dev/null 2>&1 || :
#   /sbin/chkconfig --del foobar
fi
                                                                                
%postun
if [ $1 -ge 1 ]; then
#   /sbin/service foobar condrestart >/dev/null 2>&1 || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README STATUS TODO
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*


%changelog
* Wed Jul 14 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-0
- Initial RPM release, still need to add an init script I think.

