# $Id$
# Authority: dag

%define _bindir /bin

Summary: Small POSIX-compliant shell
Name: dash
Version: 0.5.4
Release: 1
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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/dash.1*
%{_bindir}/dash

%post
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --install /etc/alternatives/sh sh /bin/dash 20 --slave /etc/alternatives/sh.1.gz sh.1.gz /usr/share/man/man1/dash.1.gz
fi

%postun
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --remove sh /bin/dash
fi

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (Mikel Ward)
