# $Id$
# Authority: dag

Summary: List or change SCSI disk parameters
Name: sdparm
Version: 1.03
Release: 1%{?dist}
License: BSD
Group: System Environment/Base
URL: http://www.torque.net/sg/sdparm.html

Source: http://www.torque.net/sg/p/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use
the SCSI command set) such as CD/DVD and tape drives may also find
parts of sdparm useful. Requires the linux kernel 2.4 series or later.
In the 2.6 series any device node the understands a SCSI command set
may be used (e.g. /dev/sda). In the 2.4 series SCSI device node may be used.

Fetches Vital Product Data pages. Can send commands to start or stop
the media and load or unload removable media.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
%setup

%build
%configure

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README notes.txt
%doc %{_mandir}/man8/sdparm.8*
%{_bindir}/sdparm

%changelog
* Mon Jun 30 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Tue Oct 09 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Tue Oct 17 2006 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (based on upstream package)
