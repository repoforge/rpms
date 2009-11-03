# $Id:$
# Authority:  dries

# still work in progress
# Tag: test

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{!?dtag:%define _with_lesstif 1}
%{?el5:%define _with_openmotif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc5:%define _with_openmotif 1}
%{?fc4:%define _with_openmotif 1}
%{?fc3:%define _with_lesstif 1}
%{?el4:%define _with_openmotif 1}
%{?el3:%define _with_openmotif 1}
%{?el2:%define _with_lesstif 1}

Summary: Attractive astronomical ephemeris program for X Windows
Name: xephem
Version: 3.7.2
Release: 2%{?dist}
License: Distributable, see Copyright file for details.  NOT GPL!
Group: Applications/Scientific
URL: http://www.clearskyinstitute.com/xephem/xephem.html

Source0: http://www.clearskyinstitute.com/xephem/xephem-%{version}.tar.gz
Source1: XEphem.desktop
Source2: XEphem.png
Patch0: xephem-3.7.2_fc6_patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: perl(cgi-lib.pl)
Requires: lesstif, libXmu, libXt, libXp
%{!?_without_modxorg:BuildRequires: libXmu-devel, libXt-devel, libXp-devel, libXau-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{?_with_openmotif:BuildRequires: openmotif-devel}
BuildRequires: groff

%description
XEphem is an interactive astronomical ephemeris program for X Windows
systems with OpenMotif. It provides many graphical views as well as
quantitative heliocentric, geocentric and topocentric information for
Earth satellites, solar system and deep-sky objects.  

%prep
%setup
%patch -p1 
# make sure the correct libdir is also added to the ldflags (needed on x86_64)
%{__perl} -pi -e "s|^LDFLAGS = |LDFLAGS = -L%{_libdir} |g;" GUI/xephem/Makefile


%build
cd libastro
%{__make} %{?_smp_mflags}
cd ../libip
%{__make} %{?_smp_mflags}
cd ../liblilxml
%{__make}
cd ../libjpegd
%{__make}
cd ../GUI/xephem
%ifarch x86_64
# todo move to prep
cat Makefile | sed -e "s/lib\/libXm/lib64\/libXm/g" > Makefile.new
mv Makefile.new Makefile
%endif
#xmkmf
%{__make} %{?_smp_mflags}
cd tools/lx200xed
%{__make} %{?_smp_mflags}

%install
XS=GUI/xephem
XL=%{buildroot}/usr/share/xephem

%{__install} -d %{buildroot}%{_bindir} \
  %{buildroot}%{_datadir}/xephem \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_datadir}/X11/app-defaults \
  %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/pixmaps

%{__cp} %{SOURCE1} %{buildroot}%{_datadir}/applications/.
%{__cp} %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/.
# move to data package?
#cp *.edb $XS/catalogs/

%{__install} -s -m 755 $XS/xephem %{buildroot}%{_bindir}/xephem
%{__install} -s -m 755 $XS/tools/lx200xed/lx200xed %{buildroot}%{_bindir}/lx200xed

rm -f $XS/tools/lx200xed/lx200xed
rm -f $XS/tools/lx200xed/*.o

%{__install} -m 644 $XS/xephem.man %{buildroot}/usr/share/man/man1/xephem.1x

%{__install} -d -m 755 $XL/auxil
rm -f $XL/auxil/xephem_skyhist
%{__install} -d -m 755 $XL/catalogs
%{__install} -d -m 755 $XL/fifos
%{__install} -d -m 755 $XL/fits
%{__install} -d -m 755 $XL/tools
%{__install} -d -m 755 $XL/lo
%{__install} -d -m 755 $XL/gallery
%{__install} -d -m 755 $XL/help
%{__install} -m 644 $XS/auxil/*		$XL/auxil
#%{__install} -m 644 $XS/catalogs/*		$XL/catalogs
%{__install} -m 644 $XS/fifos/*		$XL/fifos
%{__install} -m 644 $XS/gallery/*            $XL/gallery
cp -a			 $XS/tools/*		$XL/tools/.
cp -a			 $XS/lo/*		$XL/lo/.
cp -a                    $XS/help/*             $XL/help/.

echo "XEphem.ShareDir: /usr/share/xephem" > %{buildroot}/usr/share/X11/app-defaults/XEphem

%clean
%{__rm} -rf %{buildroot}
# ???
#rm -rf $RPM_BUILD_DIR/%{name}


%files
%defattr(-,root,root)
%doc Copyright INSTALL README
%{_bindir}/xephem
%{_bindir}/lx200xed
%{_mandir}/man1/xephem*
%{_datadir}/xephem/
%{_datadir}/X11/app-defaults/XEphem
%{_datadir}/applications/*
%{_datadir}/pixmaps/XEphem.png

%changelog
* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.2-2
- Small changes for rpmforge.
- Made a Seperate data package.

* Thu Jan 4 2007  Gerald Cox <gbcox@member.fsf.org>
- build under FC6 
- update to 3.7.2

* Mon May 15 2006 tim pickering <tim@mmto.org>
- build under FC 5

* Tue Feb  7 2006 tim pickering <tim@mmto.org>
- update to 3.7.1

* Tue Aug 16 2005 tim pickering <tim@mmto.org>
- update to 3.7

* Wed Jun 22 2005 tim pickering <tim@mmto.org>
- update to 3.6.4

* Sun Feb 20 2005 tim pickering <tim@mmto.org>
- update to 3.6.3

* Wed Oct 20 2004 tim pickering <tim@mmto.org>
- update to 3.6.1; build under FC 3

* Mon Aug 16 2004 tim pickering <tim@mmto.org>
- update to 3.6; build under FC 2

* Fri Jan 23 2004 tim pickering <tim@mmto.org>
- build under FC 1

* Fri Aug 22 2003 tim pickering <tim@mmto.org>
- build under RH 9

* Mon Sep 30 2002 tim pickering <tim@mmto.org>
- build under RH 8.0

* Mon Feb 04 2002 <tim@as.arizona.edu>
- New version 3.5.2

* Sun Oct 21 2001 <ckulesa@as.arizona.edu>
- New version 3.5

* Thu Dec 7 2000 <ckulesa@as.arizona.edu>
- New version 3.4
- Redhat 7.0 and 6.x support
- Built dynamically against OpenMotif 2.1.30 (Redhat 7.0 Powertools)
- Discontinued use of wmconfig in favor of GNOME and KDE desktop links
- New PNG and XPM icons for GNOME and KDE
- Now shares "Astro" desktop folder with Tim Pickering's IRAF packages

* Thu Apr 13 2000 <ckulesa@as.arizona.edu>
- Linked against Lesstif 0.89.9
- Redhat 6.2 version
- Uses wmconfig for automatic desktop entries

* Mon Nov 1 1999 <ckulesa@as.arizona.edu>
- RPM-ification
- Statically linked against Lesstif 0.86
