# $Id$
# Authority: dag
# Upstream: <taviso$sdf,lonestar,org>

Summary: Simple interactive debugging utility
Name: scanmem
Version: 0.07
Release: 1%{?dist}
License: GPL
Group: Development/Debuggers
URL: http://taviso.decsystem.org/scanmem.html

Source: http://taviso.decsystem.org/files/scanmem/scanmem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
scanmem is a simple interactive debugging utility, used to locate the address
of a variable in an executing process. This can be used for the analysis or
modification of a hostile process on a compromised machine, reverse
engineering, or as a "pokefinder" to cheat at video games.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS='%{optflags} -DVERSIONSTRING="\"v$(VERSION)\""' LDFLAGS="-lreadline -lncurses"

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README TODO
%doc %{_mandir}/man1/scanmem.1*
%{_bindir}/scanmem

%changelog
* Tue Jun 05 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Tue Jan 30 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
