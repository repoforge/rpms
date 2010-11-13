# $Id$
# Authority: dag

### EL6 ships with dash-0.5.5.1-3.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define _bindir /bin

Summary: Small POSIX-compliant shell
Name: dash
Version: 0.5.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://gondor.apana.org.au/~herbert/dash/

Source: http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small
as possible.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --install /etc/alternatives/sh sh %{_bindir}/dash 20 --slave /etc/alternatives/sh.1.gz sh.1.gz %{_mandir}/man1/dash.1.gz
fi

%postun
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --remove sh %{_bindir}/dash
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL
%doc %{_mandir}/man1/dash.1*
%{_bindir}/dash

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (Mikel Ward)
