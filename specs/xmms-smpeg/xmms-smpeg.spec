# $Id$

# Authority: dag

# Dists: rh73
# SourceDists: rh73

%define	rname smpeg-xmms
%define plugindir %(xmms-config --input-plugin-dir)

Summary: XMMS SMPEG Plugin
Name: xmms-smpeg
Version: 0.3.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.xmms.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.lokigames.com/pub/open-source/smpeg/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel, gtk+-devel >= 1.2.7, SDL-devel >= 1.1.5, smpeg-devel >= 0.4.1

%description
An MPEG plugin for XMMS using SDL/smpeg as backend.

%prep
%setup -n %{rname}-%{version}

%build
%configure --libdir="%{plugindir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{plugindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{plugindir}/*.so

%changelog
* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Initial package. (using DAR)
