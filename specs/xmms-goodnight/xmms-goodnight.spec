# $Id$

# Authority: dag

%define plugindir %(xmms-config --general-plugin-dir)

Summary: An XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given time.
Name: xmms-goodnight
Version: 0.3.2
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://fiktiv.szgtikol.kando.hu/~folti/src/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fiktiv.szgtikol.kando.hu/~folti/src/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel

%description
An XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given time.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{plugindir}
%{__install} -m0755 libgoodnight.so %{buildroot}%{plugindir}

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README TODO
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Initial package. (using DAR)
