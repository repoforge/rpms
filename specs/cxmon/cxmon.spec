# $Id$
# Authority: matthias

Summary: Command-line file manipulation tool and disassembler
Name: cxmon
Version: 3.1
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.uni-mainz.de/~bauec002/CXMain.html
Source: http://wwwthep.physik.uni-mainz.de/~cbauer/cxmon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, ncurses-devel, readline-devel

%description
cxmon is an interactive command-driven file manipulation tool that is
inspired by the "Amiga Monitor" by Timo Rossi. It has commands and features
similar to a machine code monitor/debugger, but it lacks any functions for
running/tracing code. There are, however, built-in PowerPC, 680x0, 80x86,
x86-64, 6502 and Z80 disassemblers and special support for disassembling
MacOS code.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/cxmon
%{_mandir}/man1/cxmon.1*


%changelog
* Sat Apr  2 2005 Matthias Saou <http://freshrpms.net/> 3.1-1
- Initial RPM release.

