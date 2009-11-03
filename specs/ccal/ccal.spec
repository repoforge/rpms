# $Id$
# Authority: dag
# Upstream: Jamie Hillman <ccal@jamiehillman.co.uk>

%define real_version 06

Summary: Curses-based calendar/journal/diary & todo list program
Name: ccal
Version: 0.6
Release: 2.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.jamiehillman.co.uk/ccal/

Source: http://www.jamiehillman.co.uk/ccal/ccal%{real_version}.py
Source1: http://www.jamiehillman.co.uk/ccal/instructions.htm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.3
Requires: python >= 2.3

%description
Ccal is a curses-based calendar/journal/diary & todo list program.

%prep
%setup -c -T -D
%{__cp} -apv %{SOURCE1} instructions.html

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 %{SOURCE0} %{buildroot}%{_bindir}/ccal

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc instructions.html
%{_bindir}/ccal

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-2.2
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 0.6-2
- Fixed Group tag.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Fri Aug 20 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
