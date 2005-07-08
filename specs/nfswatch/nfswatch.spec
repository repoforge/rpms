# $Id$
# Authority: dag

Summary: Command line tool to monitor NFS traffic
Name: nfswatch
Version: 4.99.0
Release: 1
License: BSD
Group: Applications/Internet
URL: http://nfswatch.sourceforge.net/

Source: http://dl.sf.net/nfswatch/nfswatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
nfswatch is a command-line tool for monitoring NFS traffic. nfswatch
can capture and analyze the NFS packets on a particular network
interface or on all interfaces.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	LINUXCFLAGS="-DLINUX %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nfslogsum %{buildroot}%{_sbindir}/nfslogsum
%{__install} -Dp -m0755 nfswatch %{buildroot}%{_sbindir}/nfswatch
%{__install} -Dp -m0644 nfslogsum.8 %{buildroot}%{_mandir}/man8/nfslogsum.8
%{__install} -Dp -m0644 nfswatch.8 %{buildroot}%{_mandir}/man8/nfswatch.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man8/nfslogsum.8*
%doc %{_mandir}/man8/nfswatch.8*
%{_sbindir}/nfslogsum
%{_sbindir}/nfswatch

%changelog
* Mon Feb 14 2005 Dag Wieers <dag@wieers.com> - 4.99.0-1
- Initial package. (using DAR)
