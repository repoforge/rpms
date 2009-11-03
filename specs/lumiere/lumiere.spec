# $Id$

# Authority: dag

# Upstream: Stéphane Konstantaropoulos <stephanek$brutele,be>

Summary: GNOME frontend to mplayer, the great movie player for *nix
Name: lumiere
Version: 0.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://brain.shacknet.nu/lumiere.html

Source: http://brain.shacknet.nu/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: mplayer
BuildRequires: libpostproc

%description
Lumiere is a GNOME frontend to mplayer, the great movie player for *nix.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/dvr/
%{_libdir}/lib/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-0.2
- Rebuild for Fedora Core 5.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Mon Jan 20 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Initial package. (using DAR)
