# $Id$

# Authority: dag

%define plugindir %(xmms-config --visualization-plugin-dir)
%define rname goom

Summary: A neat visual plugin for XMMS.
Name: xmms-goom
Version: 1.99.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://goom.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ios.free.fr/goom/devel/goom-%{version}-src.tgz
Patch: goom-1.99.4-gcc3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel, SDL-devel, gtk+-devel

%description
A great visual plugins for XMMS.

%prep
%setup -n %{rname}-%{version}
%patch0

%build
./configure \
	--enable-shared \
	--libdir="%{plugindir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{plugindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING KNOWNBUGS NEWS README
%{plugindir}/*.so
%exclude %{plugindir}/*.la

%changelog
* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.99.4-0
- Initial package. (using DAR)
