# $Id$
# Authority: dag

%define _without_lrmi 1

Summary: Tool for probing and parsing monitor EDID
Name: monitor-edid
Version: 2.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://wiki.mandriva.com/en/Tools/monitor-edid

### See: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/monitor-edid/trunk/
### svn export -r 243231 http://svn.mandriva.com/svn/soft/monitor-edid/trunk monitor-edid-2.1
Source: monitor-edid-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_lrmi:BuildRequires: lrmi-devel}

%description
Monitor-edid is a tool for probing and parsing Extended display 
identification data (EDID) from monitors.

For more information about EDID, see http://en.wikipedia.org/wiki/EDID

%prep
%setup
%{__cp} -v x86emu/LICENSE LICENSE.x86emu

### Disable lrmi requirement for building
%if %{?_without_lrmi:1}0
%{__perl} -pi.orig -e 's|TARGETS \+= monitor-get-edid-using-vbe|HAS_VBE=|' Makefile
%endif

%build
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE.x86emu NEWS README
%{_bindir}/monitor-parse-edid
%{_sbindir}/monitor-edid
%{_sbindir}/monitor-get-edid
%{_sbindir}/monitor-probe
%{_sbindir}/monitor-probe-using-X

%changelog
* Wed Jul 22 2009 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
