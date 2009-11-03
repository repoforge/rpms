# $Id$
# Authority: dag

Summary: Display Linux /proc stat (/proc/pid/stat) in human-readable format
Name: procstat
Version: 0.0.20070919
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://brokestream.com/procstat.html

Source: http://brokestream.com/procstat.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Procstat is a small tool to translate cryptic info from /proc/*/stat into
understandable form. Actually, ps shows most of things needed. But this
will show you everything at once in mostly raw format.

%prep
%setup -cT

%{__cp} -v %{SOURCE0} .

%build
%{__cc} %{optflags} -o procstat procstat.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 procstat %{buildroot}%{_bindir}/procstat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/procstat

%changelog
* Tue Dec 23 2008 Dag Wieers <dag@wieers.com> - 0.0.20070919-1
- Initial package. (using DAR)
