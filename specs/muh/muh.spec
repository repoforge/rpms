# $Id$
# Authority: dag
# Upstream: Sebastian Kienzl <seb$riot,org>

%define real_version 2.1rc1

Summary: IRC bouncer with IPV6-support
Name: muh
Version: 2.2a
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://muh.sourceforge.net/

Source: http://dl.sf.net/muh/muh-%{real_version}.tar.gz
Source1: muhrc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/install-info

%description
muh is a quite versatile irc-bouncer for unix. An irc-bouncer is a program
that acts as a middleman between your irc-client and your irc-server.
If you have no idea what this is good for you probably don't need it.

%prep
%setup -n %{name}-%{real_version}

%{__cp} -apv %{SOURCE1} .

%build
%configure \
    --enable-ipv6
%{__make} %{?_smp_mflags}
%{__mv} src/muh src/muh-ipv6

%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 src/muh-ipv6 %{buildroot}%{_bindir}/muh-ipv6

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL muhrc NEWS README TODO VERSION
%doc %{_infodir}/%{name}.info*
%{_bindir}/muh
%{_bindir}/muh-check
%{_bindir}/muh-ipv6
%{_bindir}/muh-rotatelog
%exclude %{_datadir}/muhrc

%changelog
* Fri Nov 12 2010 Dag Wieers <dag@wieers.com> - 2.2a-1
- Updated to release 2.2a

* Fri Nov 12 2010 Dag Wieers <dag@wieers.com> - 2.2-0.beta1
- Updated to release

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 2.1-0.rc1
- Initial package. (using DAR)
