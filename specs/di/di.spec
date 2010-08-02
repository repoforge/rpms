# $Id$
# Authority: dag
# Upstream: 

Summary: Disk Information Utility
Name: di
Version: 4.26
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.gentoo.com/di/

Source: http://www.gentoo.com/di/di-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
'di' is a disk information utility, displaying everything (and more) that
your 'df' command does. It features the ability to display your disk usage
in whatever format you prefer. It is designed to be portable across many
platforms. Great for heterogenous networks. di Manual Page

%prep
%setup

%build
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__make} install prefix="%{buildroot}%{_prefix}"
%find_lang %{name}

%{__ln_s} -f di.1.gz %{buildroot}%{_mandir}/man1/mi.1.gz

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc LICENSE MANIFEST README
%doc %{_mandir}/man1/di.1*
%doc %{_mandir}/man1/mi.1*
%{_bindir}/di
%{_bindir}/mi

%changelog
* Mon Jul 26 2010 Dag Wieers <dag@wieers.com> - 4.26-1
- Initial package. (using DAR)
