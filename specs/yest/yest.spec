# $Id$
# Authority: dag
# Upstream:  Kimball Hawkins <hawkyns$users,sourceforge,net>

Summary: Date/time manipulation and formatting tool
Name: yest
Version: 2.7.0.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://sourceforge.net/projects/yest/

Source: http://dl.sf.net/yest/yest-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
yest is a command line date/time manipulation and formatting program,
very useful in scripts. You can easily add or subtract days, hours
and/or minutes from a specified date. Supports all date(1) output
formats plus more.

%prep
%setup -c
%{__mv} -f README-%{version} README

%build
#%{__make} %{?_smp_mflags}
%{__cc} %{optflags} -o yest yest-%{version}.c

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 yest %{buildroot}%{_bindir}/yest
%{__install} -Dp -m0644 yest-%{version}.man1 %{buildroot}%{_mandir}/man1/yest.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/yest.1*
%{_bindir}/yest

%changelog
* Mon Oct 16 2006 Dag Wieers <dag@wieers.com> - 2.7.0.3-1
- Initial package. (using DAR)
