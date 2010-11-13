# $Id$
# Authority: dag

### EL6 ships with seekwatcher-0.12-4.1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Utility for visualizing block layer IO patterns and performance
Name: seekwatcher
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: Development/System
URL: http://oss.oracle.com/~mason/seekwatcher/

Source: http://oss.oracle.com/~mason/seekwatcher/seekwatcher-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
Requires: blktrace
Requires: python
Requires: python-matplotlib
Requires: theora-tools

%description
Seekwatcher generates graphs from blktrace runs to help visualize IO patterns
and performance. It can plot multiple blktrace runs together, making it easy
to compare the differences between different benchmark runs.

You should install the seekwatcher package if you need to visualize detailed
information about IO patterns.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 seekwatcher %{buildroot}%{_bindir}/seekwatcher

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.html
%{_bindir}/seekwatcher

%changelog
* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
