# $Id$
# Authority: matthias

%define rname Gabber

Summary: Client for the Jabber instant messaging system.
Name: gabber
Version: 1.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/Communications
URL: http://gabber.jabberstudio.org/

Source: http://www.jabberstudio.org/files/gabber/Gabber-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-libs-devel, libglade-devel, libsigc++-devel, aspell-devel
BuildRequires: gtkmm2-devel, libgnomemm2-devel, gconfmm2-devel, libglademm2-devel
BuildRequires: gal >= 0.7, gal-devel, openssl-devel

%description
Gabber is a Gnome client for the distributed Open Source instant messaging
system called Jabber. Gabber is one of the most complete Jabber clients,
while still remaining one of the easiest to use. Jabber allows communication
with a multitude of other instant messaging systems, such as AIM, ICQ,
Yahoo!, MSN, and even IRC.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
	--localstatedir="%{_localstatedir}/lib" \
	--with-release-libs="%{_libdir}" \
	--disable-dependency-tracking \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
#%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/Gabber/*.{a,la}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README* TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/Gabber/
%{_datadir}/pixmaps/Gabber/
%{_datadir}/pixmaps/gabber.png
%{_datadir}/Gabber/
%{_datadir}/applications/*.desktop
#exclude %{_localstatedir}/scrollkeeper/

%changelog
* Tue Jun 29 2004 Dag Wieers <dag@wieers.com> - 1.9.4-1
- Updated to release 1.9.4.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.9.3-0
- Initial package. (using DAR)
