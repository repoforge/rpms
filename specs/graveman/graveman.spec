# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Graphical front-end for cdrtools
Name: graveman
Version: 0.3.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://graveman.tuxfamily.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/graveman/graveman-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4
BuildRequires: libid3tag-devel, libmad-devel, libogg-devel, libvorbis-devel
Requires: cdrecord, mkisofs, sox

%description
Graveman is a graphical front-end for cdrtools (cdrecord, readcd, mkisofs)
and sox. Graveman allows you to burn audio CDs (from WAV, Ogg, or MP3 files)
and data CDs, and to duplicate CDs.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original             \
	--vendor="%{desktop_vendor}"               \
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
%{_bindir}/graveman
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/graveman/
%{_datadir}/pixmaps/graveman48.png

%changelog
* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Initial package. (using DAR)
