# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Graphical front-end for cdrtools
Name: graveman
Version: 0.3.12
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://graveman.tuxfamily.org/

#Source: http://savannah.nongnu.org/download/graveman/graveman-%{version}.tar.bz2
Source: http://graveman.tuxfamily.org/graveman-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4, libglade2-devel >= 2.4
BuildRequires: libid3tag-devel, libmad-devel, libogg-devel, libvorbis-devel
Requires: cdrecord, mkisofs, sox

%description
Graveman is a graphical front-end for cdrtools (cdrecord, readcd, mkisofs)
and sox. Graveman allows you to burn audio CDs (from WAV, Ogg, or MP3 files)
and data CDs, and to duplicate CDs.

%prep
%setup

%{__perl} -pi.orig -e 's|^(Applicationman)\s*=.*|$1 = \$(DESTDIR)\$(mandir)|' man/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}{,/fr}/man1/
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original             \
	--vendor "%{desktop_vendor}"               \
	--remove-category Utility                  \
	--add-category X-Red-Hat-Base              \
	--add-category AudioVideo                  \
	--add-category DiscBurning                 \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/graveman.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/graveman.1*
%doc %{_mandir}/fr/man1/graveman.1*
%doc %{_mandir}/nl/man1/graveman.1*
%{_bindir}/graveman
%{_datadir}/applications/%{desktop_vendor}-graveman.desktop
%{_datadir}/graveman/
%{_datadir}/pixmaps/graveman48.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.12-1.2
- Rebuild for Fedora Core 5.

* Tue May 17 2005 Dag Wieers <dag@wieers.com> - 0.3.12-1
- Updated to release 0.3.12.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.3.10-1
- Updated to release 0.3.10.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Initial package. (using DAR)
