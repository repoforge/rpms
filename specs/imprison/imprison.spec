# $Id$
# Authority: dag
# Upstream: Balazs Nagy <js$js,hu>

# Soapbox: 1
# Imprison: 1

Summary: Imprisons processes to a jail
Name: imprison
Version: 0.2
Release: 0.2%{?dist}
Group: System Environment/Base
License: GPL
URL: http://js.hu/package/imprison.html

Source: http://js.hu/package/imprison/imprison-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libcap-devel

%description
Imprison imprisons processes to a jail. It can change root dir,
capabilities, userid, and groups.

%prep
%setup -n admin/%{name}-%{version}

%build
%{__make} %{?_smp_mflags} -C src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/imprison %{buildroot}%{_sbindir}/imprison

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.html doc/imprison/ package/README src/CHANGES src/COPYING src/COPYRIGHT
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-0.2
- Rebuild for Fedora Core 5.

* Thu Mar 20 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
