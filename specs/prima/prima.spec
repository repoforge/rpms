# $Id$

# Authority: dries
# Upstream: Dmitry Karasik <dmitry$karasik,eu,org>
# Screenshot: http://www.prima.eu.org/big-picture/vb_unix_large.gif
# ScreenshotURL: http://www.prima.eu.org/big-picture/

%define perl_sitearch %(eval "`perl -V:installsitearch`"; echo $installsitearch)

Summary: Extensible Perl toolkit for multi-platform GUI development
Name: prima
Version: 1.16
Release: 2
License: BSD
Group: System Environment/Libraries
URL: http://www.prima.eu.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, gdbm-devel, db4-devel, libpng-devel
BuildRequires: libjpeg-devel, libungif-devel, libtiff-devel
Provides: perl(Prima::Buttons), perl(Prima::Classes), perl(Prima::ExtLists)
Provides: perl(Prima::Grids), perl(Prima::Notebooks), perl(Prima::Outlines)
Provides: perl(Prima::Sliders), perl(Prima::StdDlg)

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
%{__perl} Makefile.PL PREFIX=%{buildroot}/usr
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Copying HISTORY README 
%{perl_sitearch}/Prima.pm
%{perl_sitearch}/Prima
%exclude %{perl_sitearch}/auto/Prima/.packlist
%{perl_sitearch}/auto/Prima/Prima.so
%{perl_sitearch}/gencls.pod
%{perl_sitearch}/man/man?
%{_bindir}/tmlink
%{_bindir}/VB
%{_bindir}/cfgmaint
%{_bindir}/p-class
%{_bindir}/gencls
%{_bindir}/podview

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> 1.16-2
- Fix requirements.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.16-1
- Update to release 1.16.

* Wed May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.15-1
- Initial package.
