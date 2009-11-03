# $Id$
# Authority: dag
# Upstream: Carson Harding <carson,harding$shaw,ca>

Summary: Automatically restart SSH sessions and tunnels
Name: autossh
Version: 1.4b
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.harding.motd.ca/autossh/

Source: http://www.harding.motd.ca/autossh/autossh-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# configure checks is the ssh client exists
BuildRequires: openssh-clients
Requires: openssh-clients

%description
Autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic. The idea and
the mechanism are from rstunnel (Reliable SSH Tunnel), but implemented
in C. The author's view is that it is not as fiddly as rstunnel to get
to work. Connection monitoring using a loop of port forwardings. Backs
off on rate of connection attempts when experiencing rapid failures
such as connection refused.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 autossh %{buildroot}%{_bindir}/autossh
%{__install} -Dp -m0644 autossh.1 %{buildroot}%{_mandir}/man1/autossh.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc autossh.host CHANGES README rscreen
%doc %{_mandir}/man1/autossh.1*
%{_bindir}/autossh

%changelog
* Sat Apr 12 2008 Dag Wieers <dag@wieers.com> - 1.4b-1
- Updated to release 1.4b.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 1.4a-1
- Updated to release 1.4a.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 1.3-2
- Added openssh-clients dependency. (Adrian Reber)
- Build with %%{optflags}. (Adrian Reber)

* Wed Mar 23 2005 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 1.2-2.g
- Fixed Group tag.

* Thu Dec 09 2004 Dag Wieers <dag@wieers.com> - 1.2-1.g
- Updated to release 1.2g.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.2-1.f
- Initial package. (using DAR)
