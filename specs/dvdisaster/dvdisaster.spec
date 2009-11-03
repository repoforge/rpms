# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Additional error protection for CD/DVD media
Name: dvdisaster
Version: 0.70.4
Release: 1%{?dist}
License: GPL 
Group: Applications/Archiving
URL: http://www.dvdisaster.com/

Source: http://dl.sf.net/dvdisaster/dvdisaster-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, desktop-file-utils, gtk2-devel
BuildRequires: bzip2-devel, libpng-devel

%description
dvdisaster provides a margin of safety against data loss on CD and DVD media
caused by scratches or aging. It creates error correction data,
which is used to recover unreadable sectors if the disc becomes damaged
at a later time.

%prep
%setup

%build
%configure \
	--localedir="%{_datadir}/locale" \
	--with-nls="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	BINDIR="%{buildroot}%{_bindir}" \
	DOCSUBDIR="$(pwd)/doc-rpm" \
	MANDIR="%{buildroot}%{_mandir}" \
	LOCALEDIR="%{buildroot}%{_datadir}/locale"
%find_lang %{name}

%{__install} -Dp -m0644 contrib/dvdisaster48.png %{buildroot}%{_datadir}/pixmaps/dvdisaster48.png
desktop-file-install --vendor %{desktop_vendor}         \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category AudioVideo \
	--add-category X-Red-Hat-Base \
	contrib/dvdisaster.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_bindir}/*-uninstall.sh

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc-rpm/*
%doc %{_mandir}/man1/dvdisaster.1*
%doc %lang(de) %{_mandir}/de/man1/dvdisaster.1*
%doc %lang(it) %{_mandir}/it/man1/dvdisaster.1*
%doc %lang(cs) %{_mandir}/cs/man1/dvdisaster.1*
%{_bindir}/dvdisaster
%{_datadir}/applications/%{desktop_vendor}-dvdisaster.desktop
%{_datadir}/pixmaps/dvdisaster48.png

%changelog
* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 0.70.4-1
- Updated to release 0.70.4.

* Wed Feb 14 2006 Dag Wieers <dag@wieers.com> - 0.66-1
- Initial package. (using DAR)
