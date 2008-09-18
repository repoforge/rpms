# $Id$
# Authority: dag
# Upstream: Robin Miller <Robin,Miller$netapp,com>

Summary: Generic data test program
Name: dt
Version: 15.14
Release: 1
License: GPL
Group: Applications/System
URL: http://home.comcast.net/~scsiguy/SCSI_FAQ/RMiller_Tools/dt.html

Source: http://home.comcast.net/~scsiguy/SCSI_FAQ/RMiller_Tools/ftp/dt/dt-source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
dt is a generic data test program used to verify proper operation of
peripherals, file systems, device drivers, or any data stream supported
by the operating system. In its' simplest mode of operation, dt writes
and then verifys its' default data pattern, then displays performance
statisics and other test parameters before exiting. Since verification
of data is performed, dt can be thought of as a generic diagnostic tool.

%prep
%setup -n %{name}.d-WIP

%build
%{__make} -f Makefile.linux PORG="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dt %{buildroot}%{_bindir}/dt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc dt.examples dt.help LINUX-Notes README.1st ToDoList WhatsNew* *Abstract *.txt logs/
%{_bindir}/dt

%changelog
* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 15.14-1
- Initial package. (using DAR)
