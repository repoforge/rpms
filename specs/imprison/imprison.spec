# $Id$

# Authority: dag

# Upstream: Balazs Nagy <js@js.hu>
# Soapbox: 1
# Imprison: 1

Summary: Imprisons processes to a jail
Name: imprison
Version: 0.2
Release: 0
Group: System Environment/Base
License: GPL
URL: http://js.hu/package/imprison.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://js.hu/package/imprison/%{name}-%{version}.tar.gz
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
#makeinstall
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -m0755 src/imprison %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc src/CHANGES src/COPYING src/COPYRIGHT package/README doc/*.html doc/imprison/
%{_sbindir}/*

%changelog
* Thu Mar 20 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
