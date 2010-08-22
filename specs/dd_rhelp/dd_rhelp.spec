# $Id$
# Authority: dag

Summary: Helper script for ddrescue
Name: dd_rhelp
Version: 0.1.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.kalysto.org/utilities/dd_rhelp/index.en.html

Source: http://www.kalysto.org/pkg/dd_rhelp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: dd_rescue >= 1.03

%description
dd_rhelp uses ddrescue on your entire disc, and attempts to gather the maximum
valid data before trying for ages on badsectors. If you leave dd_rhelp work
for infinite time, it has a similar effect as a simple dd_rescue. But because
you may not have this infinite time, dd_rhelp jumps over bad sectors and rescue
valid data. In the long run, it parses all your device with dd_rescue.

You can Ctrl-C it whenever you want, and rerun-it at will, dd_rhelp resumes the
job as it depends on the log files dd_rescue creates. In addition, progress
is shown in an ASCII picture of your device being rescued.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dd_rhelp %{buildroot}%{_bindir}/dd_rhelp

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README* THANKS TODO doc/example.txt
%{_bindir}/dd_rhelp

%changelog
* Sat Aug 21 2010 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Updated to release 0.1.2.

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
