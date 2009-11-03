# $Id$
# Authority: matthias

%define _use_internal_dependency_generator 0

Summary: Perl extensions for GTK+ (the Gimp ToolKit)
Name: Gtk-Perl
Version: 0.7008
Release: 37%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gtkperl.org/
# www.gtkperl.org doesn't seem to work anymore
Source: http://search.cpan.org/CPAN/authors/id/L/LU/LUPUS/Gtk-Perl-%{version}.tar.gz
#Source: http://www.gtkperl.org/Gtk-Perl-%{version}.tar.gz
Source10: filter-depends.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, gdk-pixbuf-devel, libglade-devel
BuildRequires: gnome-libs-devel, Mesa-devel
BuildRequires: gtkhtml-devel, gal-devel, perl-XML-Parser

# Internal perl provides not caught by the find-provides
Provides: perl(Gnome::Applet::Types)
Provides: perl(Gtk::GLArea::Types)
Provides: perl(Gtk::Gdk::Pixbuf::Types)
Provides: perl(Gtk::GladeXML::Types)
Provides: perl(Gtk::XmHTML::Types)

%define __find_requires %{SOURCE10}

Obsoletes: gtk+-perl

%description
This package includes Perl extensions for GTK+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and GTK+. If you install this package,
you will need to also have Perl and GTK+ installed.

%prep
%setup
# copied from mandrake srpm
# fix for new MakeMaker (ie new perl 5.8.0)
%{__perl} -pi -e '/CCCMD/ && s|/m;|/mg;|' */Makefile.PL


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
    PREFIX=%{buildroot}%{_prefix} \
    INSTALLDIRS=vendor \
    --without-guessing
%{__make} %{?_smp_mflags}

for dir in GdkImlib GdkPixbuf Glade Gnome GtkXmHTML ; do
    pushd ${dir}
        CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX=%{buildroot}%{_prefix} \
        INSTALLDIRS=vendor
        %{__make} %{?_smp_mflags}
    popd
done

%install
%{__rm} -rf %{buildroot}

%{__make} install \
    VENDORPREFIX=%{buildroot}%{_prefix} \
    INSTALLDIRS=vendor

for dir in GdkImlib GdkPixbuf Glade Gnome GtkXmHTML ; do
    pushd ${dir}
        %{__make} install \
        VENDORPREFIX=%{buildroot}%{_prefix} \
        INSTALLDIRS=vendor
    popd
done

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f `find %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux*/ \
    -name .packlist -o -name '*.bs'`

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog NOTES README VERSIONS
%{_libdir}/perl5/vendor_perl/*/*-linux*/Gnome/
%{_libdir}/perl5/vendor_perl/*/*-linux*/Gtk/
%{_libdir}/perl5/vendor_perl/*/*-linux*/Gtk.pm
%{_libdir}/perl5/vendor_perl/*/*-linux*/Gnome.pm
%{_libdir}/perl5/vendor_perl/*/*-linux*/auto/Gnome/
%{_libdir}/perl5/vendor_perl/*/*-linux*/auto/Gtk/
%{_mandir}/man?/*


%changelog
* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.7008-36
- Take over where Red Hat left off :
  http://www.redhat.com/archives/fedora-devel-list/2004-August/msg00455.html
- Major spec file cleanup.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Chip Turner <cturner@redhat.com> 0.7008-35
- rebuild

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Sat Dec 14 2002 Chip Turner <cturner@redhat.com>
- don't use internal rpm dep generator

* Wed Nov 20 2002 Chip Turner <cturner@redhat.com>
- rebuild

* Thu Aug 15 2002 Chip Turner <cturner@redhat.com>
- fix for perl 5.8.0
- filter out perl(XML::Writer) dependency

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Sat Jan 26 2002 Jeff Johnson <jbj@redhat.com>
- added perl provides.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7008-4
- Don't hardcode 5.6.0

* Thu Aug 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7008-3
- remove *::reference man pages, as we don't ship all the modules
  the package wants do build them (#52851)

* Tue Jul 31 2001 Trond Eivind Glomsrød <teg@redhat.com>
- More BuildRequires

* Mon Jul 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Use %%{_tmppath}
- 0.7008
- Update URL and file location
- s/Copyright/License/
- add more buildrequires (#49784)

* Thu Jul  5 2001 Tim Powers <timp@redhat.com>
- fixed file list so that we own the dirs we need to
- remove perl-temp-files

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- rebuilt against newer gtk+ libs

* Thu Jan 11 2001 Tim Powers <timp@redhat.com>
- excludearched ia64

* Sun Dec 10 2000 Tim Powers <timp@redhat.com>
- built the added modules for bug 22013 since he uses that stuff.

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Fri Nov 10 2000 Tim Powers <timp@redhat.com>
- updated to 0.7004
- added docs

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- added defattr

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon May 22 2000 Tim Powers <timp@redhat.com>
- updated to 0.7
- built for 7.0

* Tue Dec 21 1999 Tim Powers <timp@redhat.com>
- updated to 0.6123
- built for 6.2

* Fri Jun 25 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1
* Mon May 10 1999 Cristian Gafton <gafton@redhat.com>
- version 0.5121

* Tue Dec 02 1998 Michael Maher <mike@redhat.com>
- updated to version 0.4

* Fri Oct 08 1998 Michael Maher <mikee@redhat.com>
- cleaned up spec, built for 5.2 powertools.
- added buildroot

* Tue Jul 14 1998 The Rasterman <raster@redhat.com>
- Made it rebuild on multiple architectures (still linux only tho)
- this NEEDS to be buildrooted. not willign to do that quite yet.

* Fri Jul 10 1998 Jeff Carr <jcarr@linuxppc.org>
- Turned of -O2 on the ppc version
- I'm not sure about the LGPL part
