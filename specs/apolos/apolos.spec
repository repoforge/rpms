# $Id$

# Authority: dag
# Upstream: Jonathan Gonzalez V. <jonathan@blueplanet.cl>

Summary: Small cd player for GNOME.
Name: apolos
Version: 0.1.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.nongnu.org/apolos/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/apolos/unstable.pkg/%{version}/apolos-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2 >= 2.0, cdparanoia-devel

%description
Apolos is a small cd player for GNOME.

%prep
%setup

### FIXME: Add /usr/include/cdda to include dirs. (Please fix upstream)
%{__perl} -pi.orig -e 's|^(CFLAGS =)|$1 -I%{_includedir}/cdda|' src/Makefile.in

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/*.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Updated to release 0.1.5.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 0.1.4-0
- Initial package. (using DAR)
