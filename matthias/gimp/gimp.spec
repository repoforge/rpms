# $Id: gimp.spec,v 1.16 2004/02/04 18:45:41 dude Exp $

%define majver 2.0

Summary: The GNU Image Manipulation Program
Name: gimp
Version: 2.0.0
Release: 0.4
Epoch: 1
License: GPL, LGPL
Group: Applications/Graphics
Source: ftp://ftp.gimp.org/pub/gimp/v%{majver}/gimp-%{version}.tar.bz2
URL: http://www.gimp.org/
Requires: gtk2 >= 2.2.0, gtkhtml2, libjpeg, libpng, libtiff, libmng
Requires: librsvg2, libgsf, libexif, aalib, fontconfig >= 2.2.0
BuildRequires: gcc-c++, perl, perl-XML-Parser
BuildRequires: gtk2-devel >= 2.2.0, gtkhtml2-devel, pkgconfig, gettext
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel, libmng-devel
BuildRequires: librsvg2-devel, libgsf-devel, libexif-devel, aalib-devel
BuildRequires: fontconfig >= 2.2.0
BuildRoot: %{_tmppath}/%{name}-root

%description
The GIMP (GNU Image Manipulation Program) is a powerful image
composition and editing program, which can be extremely useful for
creating logos and other graphics for Web pages.  The GIMP has many of
the tools and filters you would expect to find in similar commercial
offerings, and some interesting extras as well. The GIMP provides a
large image manipulation toolbox, including channel operations and
layers, effects, sub-pixel imaging and anti-aliasing, and conversions,
all with multi-level undo.

The GIMP includes a scripting facility, but many of the included
scripts rely on fonts that we cannot distribute.  The GIMP FTP site
has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.  Some of
the fonts have unusual licensing requirements; all the licenses are
documented in the package.  Get
ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz and
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz if you are so
inclined.  Alternatively, choose fonts which exist on your system
before running the scripts.


%package devel
Summary: GIMP plugin and extension development kit
Group: Applications/Graphics
Requires: gtk2-devel >= 2.0.0, pkgconfig

%description devel
The gimp-devel package contains the static libraries and header files
for writing GNU Image Manipulation Program (GIMP) plug-ins and
extensions.

Install gimp-devel if you're going to create plug-ins and/or
extensions for the GIMP.


%prep
%setup

%build
%configure \
    --enable-default-binary \
    --disable-print
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install-strip DESTDIR=%{buildroot}

# Strip all libs and plug-ins too
#strip %{buildroot}%{_libdir}/%{name}/%{majver}/{modules/*.so,plug-ins/*}

# We don't want those
find %{buildroot}%{_libdir} -name "*.la" | xargs rm -f

# Execute find_lang for all components and merge the resulting lists
%{__rm} -f global.lang
for what in gimp20 gimp20-libgimp gimp20-std-plug-ins gimp20-script-fu; do
    %find_lang ${what}
    %{__cat} ${what}.lang >> global.lang
done

# Install desktop entry
%{__install} -D -m 644 \
    %{buildroot}%{_datadir}/%{name}/%{majver}/misc/%{name}.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# Remove the default symlinks created
%{__rm} -f %{buildroot}%{_bindir}/{gimp,gimp-remote,gimptool}
%{__rm} -f %{buildroot}%{_mandir}/man1/{gimp,gimp-remote,gimptool}.1*


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files -f global.lang
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING MAINTAINERS NEWS README README.i18n
%doc docs/*.txt
%dir %{_sysconfdir}/%{name}/%{majver}
%config %{_sysconfdir}/%{name}/%{majver}/*
%{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{majver}
%{_libdir}/%{name}/%{majver}/environ
%dir %{_libdir}/%{name}/%{majver}/modules
%{_libdir}/%{name}/%{majver}/modules/*.so
%{_libdir}/%{name}/%{majver}/plug-ins
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%doc %{_datadir}/gtk-doc/html/*
%{_mandir}/man1/*

%files devel
%defattr (-, root, root, 0755)
%doc HACKING PLUGIN_MAINTAINERS
%{_includedir}/*
#{_libdir}/*.a
%{_libdir}/*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{majver}
%dir %{_libdir}/%{name}/%{majver}/modules
#{_libdir}/%{name}/%{majver}/modules/*.a
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_mandir}/man5/*


%changelog
* Fri Mar 26 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.4
- Update to 2.0.0 final.

* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.3.pre3
- Update to 2.0pre3.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.2.pre2
- Update to 2.0pre2.

* Wed Jan  7 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.1.pre1
- Update to 2.0pre1.

* Mon Nov 24 2003 Matthias Saou <http://freshrpms.net/> 1.3.23-1
- Update to 1.3.23.

* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 1.3.22-1
- Update to 1.3.22.

* Tue Oct  7 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.21.
- Added all missing dependencies to build with mach.

* Mon Sep  8 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.20.
- Removed the freedesktop build option, on by default now.
- Install the desktop file as-is to avoid lang@foo problems.
- Remove the default symlinks to avoid conflict with gimp 1.2 packages.

* Thu Sep  4 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.19.

* Mon Aug 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.18.
- Update the lang files from gimp14 to gimp20.

* Fri Jul 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.17.

* Fri Jul 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuild against new libexif.

* Fri Jun 27 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.16.

* Wed Jun 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.15.
- Added Epoch 1 to match existing Red Hat packages.

* Tue Apr 15 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.14.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.13.

* Fri Feb 14 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Reinvented the wheel, but packaged 1.3.11.

* Fri Apr 14 2000 Matt Wilson <msw@redhat.com>
- include subdirs in the help find
- remove gimp-help-files generation
- both gimp and gimp-perl own prefix/lib/gimp/1.1/plug-ins
- both gimp and gimp-devel own prefix/lib/gimp/1.1 and
  prefix/lib/gimp/1.1/modules

* Thu Apr 13 2000 Matt Wilson <msw@redhat.com>
- 1.1.19
- get all .mo files

* Wed Jan 19 2000 Gregory McLean <gregm@comstar.net>
- Version 1.1.15

* Wed Dec 22 1999 Gregory McLean <gregm@comstar.net>
- Version 1.1.14
- Added some auto %files section generation scriptlets


