# $Id$

# Authority: dag
# Upstream: Jarl van Katwijk <jarl$xs4all,nl>

Summary: Drip is a DVD-to-DIVX;-) ripping frontend for GNOME
Name: drip
Version: 0.9.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://drip.sourceforge.net/

Source: http://drip.sourceforge.net/files/drip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk+-devel >= 1.2, libdvdcss, libdvdread, a52dec-devel
BuildRequires: gnome-libs-devel
#BuildRequires: avifile-devel >= 0.7.22, mpeg2dec-devel = 0.2.1
#BuildRequires: orbitcpp-devel

%description
You'll need decss for handling of the DVD mpeg2 streams, and avifile for
divx;-) encoding. Dont forget to install the windows dll files for avifile.
A patched version of mpeg2divx is hooked into drip for wrapping libmpeg3
and avifile. Also have DVD support in your OS, like linux 2.4.
Good luck backing up your stuff.

Drip is not yet finished, it has bugs and not all of the features are
implemented. Basic dvd to divx ripping seems to work.

%package libifo
Group: System Environment/Libraries
Summary: LibIFO and a set of tools to handle DVD's

%description libifo
LibIFO and a set of tools to handle DVD's

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/drip
%{_bindir}/dripencoder
%{_bindir}/gnomedrip
%{_datadir}/pixmaps/*

%files libifo
%defattr(-, root, root, 0755)
%{_bindir}/bwifo
%{_bindir}/cmdifo
%{_bindir}/navdump
%{_bindir}/tstifo
%{_libdir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.
- Urls fixed.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com>
- Updated to 0.8.3.2

* Fri Apr 13 2001 Dag Wieers <dag@wieers.com>
- Added drip-encoder and few fixes.

* Sat Mar 24 2001 Dag Wieers <dag@wieers.com>
- Initial spec-file.
