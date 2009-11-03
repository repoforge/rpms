# $Id$
# Authority: dag
# Upstream:

Summary: Turn backlight and external video output on and off on ATI Radeon Mobility
Name: radeontool
Version: 1.5
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://fdd.com/software/radeon/

Source: http://fdd.com/software/radeon/radeontool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: pciutils
Requires: /sbin/lspci

%description
radeontool is a hack to save some battery on an ATI Radeon Mobility
graphics chip. Radeontool can turn off and on the backlight and
external video output. Radeontool requires lspci.

%prep
%setup

%build
%{__cc} %{optflags} radeontool.c -o radeontool

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 radeontool %{buildroot}%{_bindir}/radeontool

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES lightwatch.pl
%{_bindir}/radeontool

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
