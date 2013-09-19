# $Id$
# Authority: cmr
#
# Upstream: The Open Source Kerberos Tooling
# <http://oskt.secure-endpoints.com/knc.html>
#
# ExclusiveDist: el6

Summary: Kerberised Netcat
Name: knc
Version: 1.7.1
Release: 1%{?dist}
License: BSD/MIT
Group: System Environment/Daemons
URL: http://oskt.secure-endpoints.com/knc.html
Source0: http://oskt.secure-endpoints.com/downloads/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: krb5-libs krb5-devel gcc automake autoconf libtool

%description
KNC is Kerberised NetCat. It works in basically the same way as either
netcat or stunnel except that it is uses GSS-API to secure the
communication. You can use it to construct client/server applications
while keeping the Kerberos libraries out of your programs address
space quickly and easily.

%prep
%setup -q

%build
autoreconf -f -i
%{configure}
make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Aug 28 2013 Luis Fernando Muñoz Mejías <lfmunozmejias@gmail.com> -
- Initial build.
