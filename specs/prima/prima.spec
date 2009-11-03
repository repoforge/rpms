# $Id$

# Authority: dries
# Upstream: Dmitry Karasik <dmitry$karasik,eu,org>
# Screenshot: http://www.prima.eu.org/big-picture/vb_unix_large.gif
# ScreenshotURL: http://www.prima.eu.org/big-picture/

%define perl_sitearch %(eval "`perl -V:installsitearch`"; echo $installsitearch)

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

Summary: Extensible Perl toolkit for multi-platform GUI development
Name: prima
Version: 1.26
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.prima.eu.org/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gdbm-devel, db4-devel, libpng-devel, perl(ExtUtils::Packlist)
BuildRequires: libjpeg-devel, libungif-devel, libtiff-devel
Provides: perl(Prima::Buttons), perl(Prima::Classes), perl(Prima::ExtLists)
Provides: perl(Prima::Grids), perl(Prima::Notebooks), perl(Prima::Outlines)
Provides: perl(Prima::Sliders), perl(Prima::StdDlg)
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
Prima is an extensible Perl toolkit for multi-platform GUI development.
Platforms supported include Linux, Windows NT/9x/2K, OS/2 and UNIX/X11
workstations (FreeBSD, IRIX, SunOS, Solaris and others).

The toolkit contains a rich set of standard widgets and has emphasis on 2D
image processing tasks. A Perl program using PRIMA looks and behaves
identically on X, Win32 and OS/2 PM.

%prep
%setup -n Prima-%{version}

%build
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' Makefile.PL
%{__perl} Makefile.PL PREFIX="%{buildroot}/usr"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Copying HISTORY README
%doc %{perl_sitearch}/man/man?/*
%{perl_sitearch}/Prima.pm
%{perl_sitearch}/Prima/
%exclude %{perl_sitearch}/auto/Prima/.packlist
%{perl_sitearch}/auto/Prima/
%{perl_sitearch}/gencls.pod
%{_bindir}/cfgmaint
%{_bindir}/fmview
%{_bindir}/gencls
%{_bindir}/p-class
%{_bindir}/podview
%{_bindir}/tmlink
%{_bindir}/VB

%changelog
* Sun May  4 2008 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Wed Aug 15 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Tue Nov 21 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1.2
- Rebuild for Fedora Core 5.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-2
- fmview added to files section.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> 1.16-2
- Fix requirements.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.16-1
- Update to release 1.16.

* Wed May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.15-1
- Initial package.
